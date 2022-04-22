from asyncio.windows_events import NULL
from pickle import TRUE
from tg_token import tg_token
import telebot
import database_connection
from database_connection import cursor
from database_connection import conn
import re


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
	user_id = str(message.from_user.id)
	cursor.execute('INSERT INTO tg_users_data(user_name,tg_user_id) ' + 
	              'VALUES(' + '\'' + message.from_user.first_name + '\'' + ',' + user_id +');')
	conn.commit()
#не рабочая функция, от слова совсем
@bot.message_handler(commands=['set_habit'])
def set_habit_reply(message):
	bot.send_message(message.chat.id,
	"Set new habit\n"
	)
	@bot.message_handler(regexp="POS")
	def insert_habit(message):
		print('passed')
		user_id = str(message.from_user.id)
		data_to_insert = {
			'habit_name': NULL,
			'tg_habit_type': NULL,
			'period_time': NULL,
			'notif_time': NULL
		}
		print(message.text + '\n')
		message_parse = message.text.split()
		data_to_insert['habit_name'] = message_parse[0]
		data_to_insert['tg_habit_type'] = message_parse[1]
		data_to_insert['period_time'] = message_parse[2]
		data_to_insert['notif_time'] = message_parse[3]
		habit_id = message.from_user.id + 1
		str_habit_id = str(habit_id)
		cursor.execute(
		        'INSERT INTO habits_list(tg_user_id,habit_name,tg_habit_type,period_time,notif_time,habit_id)' +
				' VALUES('  + user_id + 
		        ',' + '\'' + data_to_insert['habit_name'] + '\'' + 
				',' + '\'' + data_to_insert['tg_habit_type'] + '\'' + 
			    ',' + data_to_insert['period_time'] + 
			    ',' + '\'' + data_to_insert['notif_time'] + '\'' + 
				',' + str_habit_id +
			    ');'
		)
		conn.commit()
@bot.message_handler(commands=['give_up_habit'])
def give_up_habit_reply(message):
	bot.send_message(message.chat.id,
	"Set a habit,that you want to give up!")
	@bot.message_handler(regexp="NEG")
	def give_up_habit(message):
		user_id = str(message.from_user.id)
		data_to_insert = {
			'habit_name': NULL,
			'tg_habit_type': NULL,
			'period_time': NULL,
			'notif_time': NULL
		}
		message_parse = message.text.split()
		data_to_insert['habit_name'] = message_parse[0]
		data_to_insert['tg_habit_type'] = message_parse[1]
		data_to_insert['period_time'] = message_parse[2]
		data_to_insert['notif_time'] = message_parse[3]
		habit_id = message.from_user.id + 1
		str_habit_id = str(habit_id)
		cursor.execute(
		        'INSERT INTO habits_list(tg_user_id,habit_name,tg_habit_type,period_time,notif_time,habit_id)' +
				' VALUES('  + user_id + 
		        ',' + '\'' + data_to_insert['habit_name'] + '\'' + 
				',' + '\'' + data_to_insert['tg_habit_type'] + '\'' + 
			    ',' + data_to_insert['period_time'] + 
			    ',' + '\'' + data_to_insert['notif_time'] + '\'' + 
				',' + str_habit_id +
			    ');'
		)
		conn.commit()

	
	




		




		







bot.infinity_polling()


