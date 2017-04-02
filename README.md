# Telegram-template-bot

This project is a simple but fully configured telegram bot, which is ready for deploy to heroku. You can use it as a starter template for your own projects.

## Instructions

Firstly, clone this repo:
```bash
$ git clone https://github.com/ValentunSergeev/telegram-template-bot.git
$ cd telegram-template-bot
```
Then, setup heroku project:
```bash
$ heroku create
$ heroku config:set TOKEN= YOUR_BOT_TOKEN #paste your bot token here
$ git push heroku master
```
So, thats all! Now you have a working bot hosted in heroku
