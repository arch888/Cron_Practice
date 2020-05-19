

def Cron_Practice_help():
	helpHand = """Hey There

	Some useful commands - 
	fab - To Favorite Questios for Today
	tasks - To see the questions that are scheduled for today
	compile - To compile the tasks into a CSV File"""

	print(helpHand)

def Cron_Practice_invalid():
	print("Sorry Invalid Command !")
	Cron_Practice_help()