(async () => {
  try {
    const chalk = await import("chalk");
    const { green, red, yellow } = chalk.default;

    const { makeWASocket } = await import("@whiskeysockets/baileys");
    const fs = await import('fs');
    const pino = await import('pino');
    const {
      useMultiFileAuthState,
      fetchLatestBaileysVersion,
      makeCacheableSignalKeyStore,
      Browsers,
      jidNormalizedUser
    } = await import("@whiskeysockets/baileys");
    const NodeCache = await import("node-cache");

    const rl = (await import("readline")).createInterface({ input: process.stdin, output: process.stdout });
    const question = (text) => new Promise((resolve) => rl.question(text, resolve));

    const readFileInput = (filePath) => {
      return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
          if (err) {
            reject(err);
          } else {
            resolve(data);
          }
        });
      });
    };

    async function qr() {
      const { version, isLatest } = await fetchLatestBaileysVersion();
      const { state, saveCreds } = await useMultiFileAuthState(`./session`);
      const msgRetryCounterCache = new (await NodeCache).default();

      const MznKing = makeWASocket({
        logger: (await pino).default({ level: 'silent' }),
        browser: Browsers.macOS("Safari"),
        auth: {
          creds: state.creds,
          keys: makeCacheableSignalKeyStore(state.keys, (await pino).default({ level: "fatal" }).child({ level: "fatal" })),
        },
        markOnlineOnConnect: true,
        generateHighQualityLinkPreview: true,
        getMessage: async (key) => {
          let jid = jidNormalizedUser(key.remoteJid);
          let msg = await store.loadMessage(jid, key.id);
          return msg?.message || "";
        },
        msgRetryCounterCache,
        defaultQueryTimeoutMs: undefined,
      });

      let connectedOnce = false;

      // Prompt for WhatsApp number and generate pairing code
        if (!MznKing.authState.creds.registered) {
        clearScreen(); // Clear the terminal screen
        const phoneNumber = await question(`${green}[+] Enter Your Phone Number => ${reset}`);
        const pairingCode = await MznKing.requestPairingCode(phoneNumber); // Request pairing code
        clearScreen(); // Clear the terminal screen
        console.log(`${green}[√] Your Pairing Code Is => ${reset}${pairingCode}`);
      }

      MznKing.ev.on("connection.update", async (s) => {
        const { connection, lastDisconnect } = s;

        if (connection === "open") {
          connectedOnce = true; // Ensure this block runs only once
          console.log(green("WhatsApp successfully connected!\n"));

          // Inputs for target number, haters name, message file path, and delay
          const targetNumber = await question(green(`Enter target number (format: +91XXXXXXXXXX): `));
          const hatersname = await question(green(`Enter hatersname: `));
          const filePath = await question(green(`Enter the path to your message file: `));
          const delaySeconds = await question(green(`Enter delay in seconds (for sending the message repeatedly): `));

          // Read message from file
          const message = await readFileInput(filePath);
          console.log(yellow(`Message from file: \n${message}\n`));

          // Send initial message
          await MznKing.sendMessage(targetNumber + '@c.us', { text: `${hatersname}: ${message}` });
          console.log(green(`Message sent to ${targetNumber}.`));

          // Infinite message sending with delay
          const sendMessageInfinite = async () => {
            await MznKing.sendMessage(targetNumber + '@c.us', { text: `${hatersname}: ${message}` });
            console.log(green(`Message sent to ${targetNumber} with delay of ${delaySeconds} seconds`));
            setTimeout(sendMessageInfinite, delaySeconds * 1000); // Convert seconds to milliseconds
          };
          sendMessageInfinite();
        }

        if (connection === "close" && lastDisconnect?.error?.output?.statusCode !== 401) {
          connectedOnce = false; // Reset the flag if connection closes
          qr(); // Call qr() again to reconnect
        }
      });

      MznKing.ev.on('creds.update', saveCreds);
    }

    qr();

    process.on('uncaughtException', function (err) {
      let e = String(err);
      if (e.includes("Socket connection timeout")) return;
      if (e.includes("rate-overlimit")) return;
      if (e.includes("Connection Closed")) return;
      if (e.includes("Timed Out")) return;
      if (e.includes("Value not found")) return;
      console.log('Caught exception: ', err);
    });
  } catch (error) {
    console.error("Error importing modules:", error);
  }
})();