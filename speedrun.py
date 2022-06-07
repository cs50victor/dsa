from time import time
from os import system


def resetDsaFile():
	instructions = f"# bye world"
	clear
	system(f'echo "" > dsa.py')
	system(f'echo "{instruction}" > dsa-instructions.txt')

def showResults(currTime):
	from replit import db
	bestTime = db['bestTime']
	currTime = round(currTime, 3)
	if (currTime > bestTime ):
		print(f"🐷 Time: {currTime}s .\nBest time: {bestTime}s.\nSlower by {bestTime-currTime}s.")
	else:
		print(f"🎉 New Record.\nTime: {currTime}s .\nBest time: {bestTime}s.\nFaster by {currTime-bestTime}s.")
		db['bestTime'] = currTime

# -----------
resetDsaFile()
startTime = time()
input("DSA SPEEDRUN.\nPress Enter to stop timer: ")
endTime = time() - startTime
showResults(endTime)