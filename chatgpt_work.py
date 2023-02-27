import telebot
import openai
import os

from dotenv import load_dotenv
load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))
openai.api_key = (os.getenv("CHATGPT_API_KEY"))

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, я бот для работы с OpenAI! Что ты хочешь сделать?')

@bot.message_handler(content_types=['text'])
def send_text(message):
    response = openai.Completion.create(engine="text-davinci-003", prompt=message.text, max_tokens=1024)
    bot.send_message(message.chat.id, response['choices'][0]['text'])

bot.polling()

