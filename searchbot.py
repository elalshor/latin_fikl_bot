import telebot
import requests
from telebot import types

bot = telebot.TeleBot('6725473706:AAHeymN9rL2t2YGLwNTfxDQa6f8NI6AKzqA')
bot.remove_webhook()


@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    pressStartButton = 'Кнопка старт'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    latinButton = types.KeyboardButton('ЛАТЫНЬ')
    markup.add(latinButton)

    bot.send_message(message.chat.id, "Напишите своё предложение на латыни!",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'ЛАТЫНЬ':
            bot.send_message(message.chat.id, 'Можете написать слово, словосочетание или предложение на латыни, а мы постараемся его перевести.')
        else:
            user_id = message.from_user.id
            searchQuery = message.text
            url = f"https://www.latin-is-simple.com/en/vocabulary/search/?q={searchQuery}"
            responce = requests.get(url)
            if not responce.json():
                bot.send_message(message.chat.id, 'Я ничего не нашел по вашему запросу')
            for SearchResult in responce.json():
                title = SearchResult['title']
                completeMessage = f"{title['rendered']} {SearchResult['link']}"
                bot.send_message(message.chat.id, completeMessage)


bot.polling(none_stop=True)
