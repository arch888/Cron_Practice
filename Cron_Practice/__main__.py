import sys
from Cron_Practice.help import Cron_Practice_help, Cron_Practice_invalid
from Cron_Practice.models import favoriteQuestion, tasksToday, compileTasks, initial, updateFileName

def main():
	args = sys.argv[1:]
	orders = {
		"fab": favoriteQuestion, 
		"tasks": tasksToday, 
		"compile": compileTasks,
		"build": initial,
		"update": updateFileName
	}
	if len(args):
		cur = args[0]
		if cur in orders:
			orders[cur](args[1:])
		else:
			Cron_Practice_invalid()
	else:
		Cron_Practice_help()