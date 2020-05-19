import sqlite3
from Cron_Practice.help import Cron_Practice_invalid
import datetime, csv, os

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()


def initial():
	c.execute('''CREATE TABLE practice (question_name text, question_link text, question_date text)''')
	conn.commit()

# initial()

# Change this iterations accordingly as 
# per your convinience anytime in future
iterations = [3, 7, 12, 16, 20, 25, 30, 40, 45, 60]
# iterations = [0]

def favoriteQuestion(args):
	questions_name = args[0]
	question_link = args[1]
	question_date = str(datetime.date.today())
	m = (questions_name, question_link, question_date,)
	c.execute('''INSERT INTO practice VALUES (?,?,?)''',m)
	conn.commit()
	print("Awesome Done!")

def tasksToday(args):
	out = []
	for prev in iterations:
		prevDate = (datetime.date.today() - datetime.timedelta(days = prev), )
		c.execute('''SELECT * FROM practice WHERE question_date = ?''', prevDate)
		out += list(c.fetchall())
	for i in out:
		print(' '.join(i))
	if not out:
		print("Wohhooo you are free !")
	return out


def formCSV(out):
	today = 'today_'+str(datetime.date.today())+'.csv'
	with open(today, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["Question Name", "Question Link", "First Day", "Solution Link"])
		for row in out:
			writer.writerow(list(row))
	today = "/home/archit/Projects/Cron_Practice/" + today
	base = today[:-4]
	# base = os.path.splittext(today)[0]
	os.rename(today, base + '.xlsx')

def compileTasks(args):
	out = tasksToday(args)
	formCSV(out)
	print(len(out))