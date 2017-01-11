import telebot
import time

import config


bot = telebot.TeleBot(config.token)
timeQuestions = ["который сейчас час?", "который час?", "скажи время?", "сколько сейчас часов?"]
timeArray = ["время", "час", "мин", "сек"]




def checkTime(message):
    strMessage = message.text
    for i in timeArray:

        if i in strMessage.lower():
            bot.send_message(message.chat.id,
            "Вот вся информация, которая вас интересует: " + str(time.ctime()))

def checkGreeting(message):
    # если это не вопрос, а обращение
    strMessage = message.text

    if "arty" in strMessage.lower() and not "?" in message.text:
        bot.send_message(message.chat.id, "Да, слушаю вас?")
    else:
        checkTime(message)


# создаем handler (обработчик событий)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    print(message.text)
    checkGreeting(message)

# Цикл
if __name__ == '__main__':
     bot.polling(none_stop=True)