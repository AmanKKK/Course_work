from tg_token import tg_token
import telebot
import psycopg2

bot = telebot.TeleBot(tg_token,parse_mode = None)


@bot.message_handler(commands=['start'])
def reply_to_user(message):
	bot.send_message(message.chat.id,
	"Hello!\n" + 
	"My name is Habit changer\n" +
	"/set_habit is the command to set a new habit, that you want to follow on daily bases\n" +
	"/give_up_habbit is the command to give up a bad habit, that you have, and you want to stop do it\n"
	"/help is the command to see more commands that I have, and see how exactly to use /set_habit and /give_up_habit commands"
	)



@bot.message_handler(commands=['view'])
def view_chat_info(message):
	print(message.chat.id)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)






bot.infinity_polling()


