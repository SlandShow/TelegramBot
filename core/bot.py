import telebot
import config

bot = telebot.TeleBot(config.token)


# создаем handler (обработчик событий)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text[::-1]) # переворачивает сообщение и отправляет пользователю

# бесконечный цикл
if __name__ == '__main__':
    bot.polling(none_stop=True)