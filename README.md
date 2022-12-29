# ChatGPT discord bot


---
## Features

- Type anything into channel and will respond according using chatGPT
- Uses [ChatGPT unoffical API](https://dillinger.io/)

---
## Install
- Start by cloning the repo:
```sh
git clone https://github.com/GSstarGamer/Chat-GPT-bot
```

- Then install the required packages by doing:
```
pip install -r req-pac.txt
```

- Fill in your details in `config.json`
-- To get ChatGPT auth token go [here](https://github.com/acheong08/ChatGPT/wiki/Setup) and follow steps to get `Session Token Authentication
`. That long string will be placed here `"auth_token": "CHATGPT_AUTH_TOKEN"` instead of CHATGPT_AUTH_TOKEN
-- To get Discord token go follow [this](https://www.writebots.com/discord-bot-token/) and put it here `"bot_token": "YOUR_BOT_TOKEN"` instead of YOUR_BOT_TOKEN.
-- Put in the channelID so the bot can read which channel to respond to.

- After all that now to start the bot do:
```sh
py bot.py
```
or
```sh
python3 bot.py
```
---
Other that than everything should work. If any ideas tell me and you can freely use it for your use and learn how it works. 
Happy coding.