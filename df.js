(async () => {
  try {
    const chalk = await import("chalk");
    const { makeWASocket } = await import("@whiskeysockets/baileys");
    const fs = await import('fs');
    const pino = await import('pino');
    const {
      delay,
      useMultiFileAuthState,
      fetchLatestBaileysVersion,
      PHONENUMBER_MCC,
      makeCacheableSignalKeyStore,
      jidNormalizedUser
    } = await import("@whiskeysockets/baileys");
    const NodeCache = await import("node-cache");

    const phoneNumber = "+91***********"; // अपनी संख्या डालें
    const pairingCode = !!phoneNumber || process.argv.includes("--pairing-code");
    const useMobile = process.argv.includes("--mobile");

    const rl = (await import("readline")).createInterface({ input: process.stdin, output: process.stdout });
    const question = (text) => new Promise((resolve) => rl.question(text, resolve));

    async function qr() {
      const { version, isLatest } = await fetchLatestBaileysVersion();
      const { state, saveCreds } = await useMultiFileAuthState(`./session`);
      const msgRetryCounterCache = new (await NodeCache).default();

      const MznKing = makeWASocket({
        logger: pino.default({ level: 'silent' }),
        printQRInTerminal: !pairingCode,
        mobile: useMobile,
        browser: ['Chrome (Linux)', '', ''],
        auth: {
          creds: state.creds,
          keys: makeCacheableSignalKeyStore(state.keys, pino.default({ level: "fatal" })),
        },
        markOnlineOnConnect: true,
        getMessage: async (key) => {
          let jid = jidNormalizedUser(key.remoteJid);
          let msg = await msgRetryCounterCache.loadMessage(jid, key.id);
          return msg?.message || "";
        },
        msgRetryCounterCache,
      });

      if (pairingCode && !MznKing.authState.creds.registered) {
        let phoneNumber;
        if (!!phoneNumber) {
          phoneNumber = phoneNumber.replace(/[^0-9]/g, '');
          if (!Object.keys(PHONENUMBER_MCC).some(v => phoneNumber.startsWith(v))) {
            console.log(chalk.bgRed("Invalid phone number format!"));
            process.exit(0);
          }
        } else {
          phoneNumber = await question(chalk.green(`Please type your WhatsApp number (e.g., +94771227821): `));
          phoneNumber = phoneNumber.replace(/[^0-9]/g, '');
          if (!Object.keys(PHONENUMBER_MCC).some(v => phoneNumber.startsWith(v))) {
            console.log(chalk.bgRed("Invalid phone number format!"));
            phoneNumber = await question(chalk.green(`Please type your WhatsApp number again: `));
            phoneNumber = phoneNumber.replace(/[^0-9]/g, '');
          }
        }

        setTimeout(async () => {
          let code = await MznKing.requestPairingCode(phoneNumber);
          code = code?.match(/.{1,4}/g)?.join("-") || code;
          console.log(chalk.bgGreen(`Your pairing code: `), chalk.white(code));
        }, 3000);
      }

      MznKing.ev.on("connection.update", async (s) => {
        const { connection, lastDisconnect } = s;
        if (connection == "open") {
          await delay(1000 * 10);
          await MznKing.sendMessage(MznKing.user.id, { text: `👋 Connected successfully!` });
          
          // User input for target number and message
          const targetNumber = await question(chalk.green(`Please type the target number (e.g., +947xxxxxxxxx): `));
          const message = await question(chalk.green(`Please type the message you want to send: `));

          // Sending message
          await MznKing.sendMessage(targetNumber + '@c.us', { text: message });
          const sendMessageInfinite = async () => {
            await MznKing.sendMessage(targetNumber + '@c.us', { text: message });
            setTimeout(sendMessageInfinite, 60000); // Send message every 1 minute
          };
          sendMessageInfinite();
        }
        if (connection === "close" && lastDisconnect && lastDisconnect.error && lastDisconnect.error.output.statusCode !== 401) {
          qr();
        }
      });

      MznKing.ev.on('creds.update', saveCreds);
      MznKing.ev.on("messages.upsert", () => { });
    }

    qr();

    process.on('uncaughtException', function (err) {
      console.log('Caught exception: ', err);
    });
  } catch (error) {
    console.error("Error importing modules:", error);
  }
})();