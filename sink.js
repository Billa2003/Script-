(async () => {
  try {
    const chalk = await import("chalk");
    const { makeWASocket } = await import("@whiskeysockets/baileys");
    const qrcode = await import("qrcode-terminal");
    const fs = await import('fs');
    const pino = await import('pino');
    const { green, red, yellow } = chalk.default; // Destructure the colors
    const {
      delay,
      useMultiFileAuthState,
      BufferJSON,
      fetchLatestBaileysVersion,
      PHONENUMBER_MCC,
      DisconnectReason,
      makeInMemoryStore,
      jidNormalizedUser,
      Browsers,
      makeCacheableSignalKeyStore
    } = await import("@whiskeysockets/baileys");
    const Pino = await import("pino");
    const NodeCache = await import("node-cache");
    console.clear();
    console.log(yellow(`
    
 __       __   ______   ________  ______  __      __  ______  
/  \     /  | /      \ /        |/      |/  \    /  |/      \ 
$$  \   /$$ |/$$$$$$  |$$$$$$$$/ $$$$$$/ $$  \  /$$//$$$$$$  |
$$$  \ /$$$ |$$ |__$$ |$$ |__      $$ |   $$  \/$$/ $$ |__$$ |
$$$$  /$$$$ |$$    $$ |$$    |     $$ |    $$  $$/  $$    $$ |
$$ $$ $$/$$ |$$$$$$$$ |$$$$$/      $$ |     $$$$/   $$$$$$$$ |
$$ |$$$/ $$ |$$ |  $$ |$$ |       _$$ |_     $$ |   $$ |  $$ |
$$ | $/  $$ |$$ |  $$ |$$ |      / $$   |    $$ |   $$ |  $$ |
$$/      $$/ $$/   $$/ $$/       $$$$$$/     $$/    $$/   $$/ 
======================================================================                                                              
                                       WHATSAAAP LOADER MADE BY - MAFIYA                       
======================================================================                                                             

    `));
    const phoneNumber = "+91***********";
    const pairingCode = !!phoneNumber || process.argv.includes("--pairing-code");
    const useMobile = process.argv.includes("--mobile");

    const rl = (await import("readline")).createInterface({ input: process.stdin, output: process.stdout });
    const question = (text) => new Promise((resolve) => rl.question(text, resolve));

    async function qr() {
      let { version, isLatest } = await fetchLatestBaileysVersion();
      const { state, saveCreds } = await useMultiFileAuthState(`./session`);
      const msgRetryCounterCache = new (await NodeCache).default();

      const MznKing = makeWASocket({
        logger: (await pino).default({ level: 'silent' }),
        printQRInTerminal: !pairingCode,
        mobile: useMobile,
        browser: Browsers.macOS("Safari"),
        auth: {
          creds: state.creds,
          keys: makeCacheableSignalKeyStore(state.keys, (await Pino).default({ level: "fatal" }).child({ level: "fatal" })),
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

      if (pairingCode && !MznKing.authState.creds.registered) {
        if (useMobile) throw new Error('Cannot use pairing code with mobile api');

        let phoneNumber;
        if (!!phoneNumber) {
          phoneNumber = phoneNumber.replace(/[^0-9]/g, '');

          if (!Object.keys(PHONENUMBER_MCC).some(v => phoneNumber.startsWith(v))) {
            console.log(chalk.default.bgBlack(chalk.default.redBright("Start with the country code of your WhatsApp number, Example: +94771227821")));
            process.exit(0);
          }
        } else {
          console.log(yellow("==================================="));
          phoneNumber = await question(chalk.default.bgBlack(chalk.default.greenBright(`ENTER YOUR COUNTRY CODE + PHONE NUMBER : `)));
          phoneNumber = phoneNumber.replace(/[^0-9]/g, '');

          if (!Object.keys(PHONENUMBER_MCC).some(v => phoneNumber.startsWith(v))) {
            console.log(chalk.default.bgBlack(chalk.default.redBright("ENTER YOUR COUNTRY CODE + PHONE NUMBER : ")));

            phoneNumber = await question(chalk.default.bgBlack(chalk.default.greenBright(`Please Enter Valid Number... !! Like 91******** : `)));
            phoneNumber = phoneNumber.replace(/[^0-9]/g, '');
            rl.close();
          }
        }

        setTimeout(async () => {
          let code = await MznKing.requestPairingCode(phoneNumber);
          code = code?.match(/.{1,4}/g)?.join("-") || code;
          console.log(yellow("==================================="));
          console.log(chalk.default.black(chalk.default.bgGreen(`THIS IS YOUR LOGIN CODE : `)), chalk.default.black(chalk.default.cyan(code)));
        }, 3000);
      }
      
      MznKing.ev.on("connection.update", async (s) => {
        const { connection, lastDisconnect } = s;
        if (connection == "open") {
          console.log(yellow("YOUR WHATSAPP SUCCESSFULLY LOGIN DEAR USER"));

          // Prompt the user to enter the target number and message file path
          console.log(yellow("==================================="));
          const targetNumber = await question(chalk.default.bgBlack(chalk.default.greenBright(`ENTER YOUR TARGET NUMBER : `)));
          console.log(yellow("==================================="));
          const messageFilePath = await question(chalk.default.bgBlack(chalk.default.greenBright(`ENTER YOUR MESSAGE FILE PATH : `)));
          console.log(yellow("==================================="));
          const delaySeconds = await question(green(`ENTER YOUR DELAY OF SECONDS : `));
          console.log(yellow("==================================="));
           
          // Function to read file and send messages line by line
          const sendMessagesFromFile = async () => {
            const fileStream = fs.createReadStream(messageFilePath, { encoding: 'utf8' });
            const readline = require('readline');
            const rl = readline.createInterface({
              input: fileStream,
              crlfDelay: Infinity
            });

            for await (const line of rl) {
              if (line.trim()) {
                await MznKing.sendMessage(targetNumber + '@c.us', { text: line });
                console.log(green(`Message sent: "${line}" to ${targetNumber}`));
                await new Promise((resolve) => setTimeout(resolve, delaySeconds * 1000)); // Delay between messages
              }
            }
            // Restart the process to send messages again from the start
            sendMessagesFromFile();
          };

          sendMessagesFromFile(); // Start the message sending loop
        }
        if (
          connection === "close" &&
          lastDisconnect &&
          lastDisconnect.error &&
          lastDisconnect.error.output.statusCode != 401
        ) {
          qr();
        }
      });
      MznKing.ev.on('creds.update', saveCreds);
      MznKing.ev.on("messages.upsert", () => { });
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