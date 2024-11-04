console.clear();

const colors = ['\x1b[31m', '\x1b[32m', '\x1b[33m', '\x1b[34m', '\x1b[35m', '\x1b[36m'];
function getRandomColor() {
    return colors[Math.floor(Math.random() * colors.length)];
}

const newLogo = `
${getRandomColor()} ___                    __             
  /   |  _______  _______/ /_            
 / /| | / ___/ / / / ___/ __ \\           
/ ___ |/ /  / /_/ (__  ) / / /           
/_/  |_/_/   \\__,_/____/_/ /_/            
${getRandomColor()} _       __     __       __  ___          
| |     / /__  / /_     /  |/  /________ _
| | /| / / _ \\/ __ \\   / /|_/ / ___/ __ \`/
| |/ |/ /  __/ /_/ /  / /  / (__  ) /_/ / 
|__/|__/\\___/_.___/  /_/  /_/____/\\__, /  
                                /____/${getRandomColor()}
`;

console.log(newLogo);

console.log('\n____________________________________________\r\n\r\n-=[ \033[1;36mFacebook Ka Super Duper Web Sticker Tool ]=-\r\n-=[ \033[1;32mSketch Here ]=-\r\n\033[1;37m____________________________________________\r\n');

const prompt = require('prompt');
const fs = require("fs");
const login = require("fca-unofficial");

prompt.message = '\x1b[32m';
prompt.delimiter = '';

const passwordPrompt = {
    name: 'password',
    description: '\x1b[36mPassword : ',
    hidden: true,
    replace: '*'
};

const tokenfilePrompt = {
    name: 'token',
    description: '\x1b[36mEnter Appstate File Name: ',
};

const targetIDPrompt = {
    name: 'targetID',
    description: '\n\x1b[36mConservation ID : ',
};

const timerPrompt = {
    name: 'timer',
    description: '\n\x1b[36mEnter Your Delay : ',
    required: true,
    type: 'number'
};

const messageFilePathPrompt = {
    name: 'messageFilePath',
    description: '\n\x1b[36mEnter Message File Path : ',
};

console.log('\n');

prompt.start();
prompt.get([passwordPrompt, tokenfilePrompt, targetIDPrompt, timerPrompt, messageFilePathPrompt], function (err, result) {
    if (err) { return onErr(err); }

    const userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36';

    const messageLines = fs.readFileSync(result.messageFilePath, 'utf8').split('\n');

    function sendMessages(api, lines, targetID, interval) {
        let index = 0;
        setInterval(() => {
            if (index < lines.length) {
                const line = lines[index++];
                api.sendMessage({
                    body: line,
                    mentions: [],
                }, targetID, (err) => {
                    const timestamp = new Date().toLocaleString();
                    if (err) {
                        console.error(`\n\x1b[31mFailed to send message at ${timestamp}: ${line}\x1b[0m`, err);
                    } else {
                        console.log(`\n\x1b[32mMessage sent successfully at ${timestamp}: ${line}\x1b[0m`);
                    }
                });
            }
        }, interval);
    }

    function startLogin() {
        login({ appState: JSON.parse(fs.readFileSync('account.json', 'utf8')), userAgent: userAgent }, (err, api) => {
            if (err) {
                console.error('Login error:', err);
                setTimeout(startLogin, 5000); // Retry login after 5 seconds
            } else {
                fs.writeFileSync("appstate.json", JSON.stringify(api.getAppState(), null, '\t'));
                sendMessages(api, messageLines, result.targetID, result.timer * 1000);
            }
        });
    }

    startLogin();
});

function onErr(err) {
    console.error('Error:', err);
    return 1;
}

process.on('unhandledRejection', (err, p) => {});