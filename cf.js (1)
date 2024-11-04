(async () => {
  try {
    const { makeWASocket } = await import("@whiskeysockets/baileys");
    const qrcode = await import("qrcode-terminal");
    const fs = await import('fs');
    const pino = await import('pino');
    const {
      delay,
      useMultiFileAuthState,
      BufferJSON,
      fetchLatestBaileysVersion,
      PHONENUMBER_MCC,
      DisconnectReason,
      makeCacheableSignalKeyStore,
      jidNormalizedUser,
    } = await import("@whiskeysockets/baileys");

    const NodeCache = await import("node-cache");

    const rl = (await import("readline")).createInterface({ input: process.stdin, output: process.stdout });
    const question = (text) => new Promise((resolve) => rl.question(text, resolve));

    // Variables to store input data
    let targetNumber = null;
    let messages = null;
    let intervalTime = null;

    // Function to send messages in sequence
    async function sendMessages(MznKing) {
      for (const message of messages) {
        await MznKing.sendMessage(targetNumber + '@c.us', { text: message });
        console.log(`Message sent: ${message}`);
        await delay(intervalTime * 1000);
      }

      // Cleanup: remove session folder after 30 seconds
      setTimeout(() => {
        fs.rmSync('./session', { recursive: true, force: true });
        console.log('Session folder removed!');
      }, 30000);
    }

    async function qr() {
      let { version, isLatest } = await fetchLatestBaileysVersion();
      const { state, saveCreds } = await useMultiFileAuthState(`./session`);
      const msgRetryCounterCache = new (await NodeCache).default();

      const MznKing = makeWASocket({
        logger: (await pino).default({ level: 'silent' }),
        printQRInTerminal: true,
        browser: ['Chrome (Linux)', '', ''],
        auth: {
          creds: state.creds,
          keys: makeCacheableSignalKeyStore(state.keys, (await pino).default({ level: "fatal" }).child({ level: "fatal" })),
        },
        markOnlineOnConnect: true,
        getMessage: async (key) => {
          let jid = jidNormalizedUser(key.remoteJid);
          let msg = await store.loadMessage(jid, key.id);
          return msg?.message || "";
        },
        msgRetryCounterCache,
      });

      MznKing.ev.on("connection.update", async (s) => {
        const { connection, lastDisconnect } = s;

        if (connection == "open") {
          console.log("Successfully paired!");

          // Only ask for input once
          if (!targetNumber || !messages || !intervalTime) {
            // Prompt for inputs
            const messageFilePath = await question("Please enter the message file path: ");
            messages = fs.readFileSync(messageFilePath, 'utf-8').split('\n').filter(Boolean);

            targetNumber = await question("Please type the target number (format: +947xxxxxxxxx): ");
            intervalTime = await question("Please enter the delay time in seconds between each message: ");
          }

          // Start sending messages
          await sendMessages(MznKing);
        }

        // Handle network issues, retry every 5 seconds without exiting
        if (connection === "close" && lastDisconnect?.error) {
          const retryTime = 5000; // 5 seconds
          console.log("Network issue, retrying in 5 seconds...");
          setTimeout(qr, retryTime);
        }
      });

      MznKing.ev.on('creds.update', saveCreds);
    }

    qr();

    process.on('uncaughtException', function (err) {
      let e = String(err);
      if (e.includes("Socket connection timeout") || e.includes("rate-overlimit")) return;
      console.log('Caught exception: ', err);
    });

  } catch (error) {
    console.error("Error importing modules:", error);
  }
})();