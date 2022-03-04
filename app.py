import telebot
from config import keys, TOKEN
from extensions import ConvertExeption, CryptoConverter
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    text = 'Чтобы начать работу введите комманду боту в следующием формате:\n<имя валюты>' \
           '<в какую валюту перевести>' \
           '<количество переводимой валюты>\nУвидеть список всех доступных валют: /value'
    bot.reply_to(message, text)

@bot.message_handler(commands=['value'])
def values(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertExeption('Неверно введены данные.')
        currency0, currency1, quantity = values
        total = CryptoConverter.convert(currency0, currency1, quantity)
    except ConvertExeption as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'Цена: {quantity} {currency1}  - {total} {currency0}'
        bot.send_message(message.chat.id, text)

bot.polling()