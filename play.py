from collections import Counter
from threading import Thread
from random import randint
from game import *
import time, os

place=0
players_in_game=[]
deck = Deck()
deck.shuffleDeck()
deck.shuffleDeck()
banner = '''
 ____                 ____                   
|  _ \ __ _ ___ ___  |  _ \ ___  _   _ _ __  
| |_) / _` / __/ __| | |_) / _ \| | | | '_ \ 
|  __/ (_| \__ \__ \ |  _ < (_) | |_| | | | |
|_|   \__,_|___/___/ |_| \_\___/ \__,_|_| |_|
                                             
 ____              _              
|  _ \  ___  _ __ | | _____ _   _ 
| | | |/ _ \| '_ \| |/ / _ \ | | |
| |_| | (_) | | | |   <  __/ |_| |
|____/ \___/|_| |_|_|\_\___|\__, |
                            |___/ v1.0
'''
def declareWinner(Player,arr,delay,yourHand):
	global place
	time.sleep(delay)
	print("WE HAVE A WINNER!!")
	place+=1
	if place == 1:
		print("FIRST PLACE WINNER:",Player)
		print(arr)
	elif place == 2:
		print("SECOND PLACE WINNER:",Player)
		print(arr)
	elif place == 3:
		print("THIRD PLACE WINNER:",Player)
		print(arr)
	elif place == 4:
		print("LAST PLACE WINNER:",Player)
		print(arr)
	print("\n\nYour Hand: ",yourHand)

print(banner)
yourName = input("Enter Your Name: ")
you = Player(yourName)
players_in_game.append(you)
createNames=input("Would you like to give each challenger a name? (y or n)\n> ")
createNames.lower()
if createNames == 'y':
	for i in range(1,4):
		player_name = input("Enter player's %s name: "%(i+1))
		players_in_game.append(player_name) 
		players_in_game[i]=Player(players_in_game[i])
elif createNames == 'n':
	for i in range(1,4):
		players_in_game.append("Player %s"%(i+1)) 
		players_in_game[i]=Player(players_in_game[i])

print("Handing out cards...")
for i in range(1,5):
	for player in players_in_game:
		print(player.name+" Got %d card\n"%(i))
		player.drawCard(deck)
		time.sleep(1)
		os.system("clear")
		print(banner)
		print("Handing out cards...")

a = players_in_game[0].getHand()
b = players_in_game[1].getHand()
c = players_in_game[2].getHand()
d = players_in_game[3].getHand()


player1 = Counter(b).most_common(1)
player2 = Counter(c).most_common(1)
player3 = Counter(d).most_common(1)

commonB = player1[0][0]
commonC = player2[0][0]
commonD = player3[0][0]

def main():
	commonYou=0
	commonplayer1=0
	commonplayer2=0
	commonplayer3=0
	win = False
	os.system("clear")
	print(banner)
	while 1:
		while 1:
			try:
				print("Your Hand:")
				print(a)
				print("\nIndexes +++++ Cards")
				for i in range(0,len(a)):
					print("   %d -------> %s"%(i, a[i]))

				print("\nChoose the index of the card you wish to give",players_in_game[1].name)
				index=int(input("> "))
				if index < 0 or index > len(a)-1:
					print("Invalid Index.... Try Again!")
				else:
					print("You gave a %s to %s"%(a[index],players_in_game[1].name))
					b.append(a[index])
					del a[index]
					You = Counter(a).most_common(1)
					commonYou = You[0][1]
					if commonYou == 4 and len(a) == 4:
						print("You Have a winning hand!, let's wait until all players have four cards")
					break
			except:
				pass

		for i in range(0,len(b)):
			try:
				if b[i] != commonB:
					print("\n%s gave a card to %s"%(players_in_game[1].name,players_in_game[2].name))
					c.append(b[i])
					del b[i]
					player1 = Counter(b).most_common(1)
					commonplayer1 = player1[0][1]
					#print("%s: %s"%(players_in_game[1].name,b))
					break

			except:
				pass
		
		for i in range(0,len(c)):
			try:
				if c[i] != commonC:
					print("\n%s gave a card to %s"%(players_in_game[2].name,players_in_game[3].name))
					d.append(c[i])
					del c[i]
					player2 = Counter(c).most_common(1)
					commonplayer2 = player2[0][1]
					#print("%s: %s"%(players_in_game[2].name,c))
					
					break
			except:
				pass

		for i in range(0,len(d)):
			try:
				if d[i] != commonD:
					print("\n%s gave a %s to you"%(players_in_game[3].name,d[i]))
					a.append(d[i])
					del d[i]
					player3 = Counter(d).most_common(1)
					commonplayer3 = player3[0][1]
					#print("%s: %s"%(players_in_game[3].name,d))
					#print("%s: %s"%(players_in_game[0].name,a))
					while 1:
						con = input("\nReady? (y or n)\n> ")
						con.lower()
						if con == 'y':
							break
						elif con == 'n':
							break
							return None
						else:
							print("Select y for Yes or n for No!\n")
					break
			except:
				pass
		if commonYou == 4 and len(a) == 4:
			win=True
			t1 = Thread(target=declareWinner, args=(players_in_game[0].name, a, randint(0,5), a))
			t1.start()
		if commonplayer1 == 4 and len(b) == 4:
			win=True
			t2 = Thread(target=declareWinner, args=(players_in_game[1].name, b, randint(0,5), a))
			t2.start()
		if commonplayer2 == 4 and len(c) == 4:
			win=True
			t3 = Thread(target=declareWinner, args=(players_in_game[2].name, c, randint(0,5), a))
			t3.start()
		if commonplayer3 == 4 and len(d) == 4:
			win=True
			t4 = Thread(target=declareWinner, args=(players_in_game[3].name, d, randint(0,5), a))
			t4.start()

		if win:
			pass
		else:
			os.system("clear")
			print(banner)
		if win:
			break
		else:
			pass
				
main()