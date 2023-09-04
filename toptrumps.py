import math
import random
import time

def main():
    

	class Character:
		def __init__(self,name,attack,defence,physical,stamina,speed,technique):
			self.name = name
			self.attack = attack
			self.defence = defence
			self.physical = physical
			self.stamina = stamina
			self.speed = speed
			self.technique = technique


	cards = []
	cards.append(Character('Lionel Messi - Barcelona (SS)',79,49,81,80,87,85))
	cards.append(Character('Cristiano Ronaldo - Manchester United (WF)',78,44,81,82,88,91))
	cards.append(Character('Kaka - AC Milan (AMF)',87,54,83,86,89,93))
	cards.append(Character('Didier Drogba - Chelsea (CF)',87,50,91,86,86,88))
	cards.append(Character('David Beckham - Real Madrid (SMF)',80,60,75,88,74,88))
	cards.append(Character('Steven Gerrard - Liverpool (CMF)',84,70,88,85,84,83))
	cards.append(Character('Zlatan Ibrahimovic - Inter Milan (CF)',90,38,97,86,84,95))
	cards.append(Character('Fabio Cannavaro - Real Madrid (CB)',60,97,86,85,79,76))
	cards.append(Character('Gianluigi Buffon - Juventus (GK)',35,97,88,65,79,56))
	cards.append(Character('Thierry Henry - Arsenal (CF)',97,33,82,80,94,96))
	cards.append(Character('John Terry - Chelsea (CB)',63,94,90,83,75,76))
	cards.append(Character('Frank Lampard - Chelsea (CMF)',84,65,82,97,77,85))
	cards.append(Character('Rio Ferdinand - Manchester United (CB)',66,95,89,83,81,83))
	cards.append(Character('Wayne Rooney - Manchester United (CF)',85,50,90,90,88,90))
	cards.append(Character('Jens Lehmann - Arsenal (GK)',35,89,87,60,64,40))
	cards.append(Character('Iker Casillas - Real Madrid (GK)',30,92,80,65,68,43))
	cards.append(Character('Carles Puyol - Barcelona (CB)',64,93,87,93,85,76))
	cards.append(Character('Ronaldinho - Barcelona (SS)',94,43,86,84,88,98))
	cards.append(Character('Andrea Pirlo - AC Milan (CMF)',81,63,74,84,74,95))
	cards.append(Character('Alessandro Nesta - AC Milan (CB)',62,95,84,84,80,77))
	cards.append(Character('Gennaro Gattuso - AC Milan (DMF)',66,82,83,95,81,73))
	cards.append(Character('Adriano - Inter Milan (CF)',91,36,97,84,88,88))
	cards.append(Character('Javier Zanetti - Inter Milan (SB)',74,66,86,93,84,80))
	cards.append(Character('Francesco Totti - AS Roma (SS)',92,35,84,80,77,94))
	cards.append(Character('Bastian Schweinsteiger - Bayern Munchen (AMF)',78,52,80,82,79,86))
	cards.append(Character('Philipp Lahm - Bayern Munchen (SB)',74,61,72,85,84,78))
	cards.append(Character('Roberto Carlos - Real Madrid (SB)',79,65,75,93,87,89))
	cards.append(Character('Kolo Toure - Arsenal (CB)',66,78,90,87,85,70))
	cards.append(Character('Juan Roman Riquelme - Villarreal (AMF)',83,52,82,77,73,93))
	cards.append(Character('Rafael van der Vaart - Hamburger SV (AMF)',85,53,77,80,75,90))
	cards.append(Character('Fernando Torres - Atletico Madrid (CF)',87,43,83,78,84,90))
	cards.append(Character('Pavel Nedved - Juventus (AMF)',85,60,76,95,83,87))
	cards.append(Character('Tomas Rosicky - Arsenal (AMF)',82,59,76,82,85,92))
	cards.append(Character('Samuel Eto*o - Barcelona (CF)',93,47,84,90,96,84))
	cards.append(Character('Roberto Ayala - Valencia (CB)',62,93,81,81,78,75))
	cards.append(Character('David Villa - Valencia (CF)',88,39,77,85,88,83))
	cards.append(Character('Juninho Permabucrano - Olympique Lyon (AMF)',85,63,75,86,75,89))
	cards.append(Character('Franck Ribery - Olympique Marseille (SMF)',75,45,74,86,87,83))
	cards.append(Character('Daniele de Rossi - AS Roma (CMF)',76,62,82,85,72,83))
	cards.append(Character('Luca Toni - Fiorentina (CF)',91,41,92,82,74,86))
	cards.append(Character('Deco - Barcelona (CMF)',80,74,80,92,76,92))
	cards.append(Character('Ricardo Carvalho - Chelsea (CB)',65,93,81,84,75,75))
	cards.append(Character('Xabi Alonso - Liverpool (DMF)',72,75,81,89,75,85))
	cards.append(Character('Sami Hyypia - Liverpool (CB)',58,88,90,77,71,72))
	cards.append(Character('Gareth Barry - Aston Villa (SMF)',73,66,80,84,80,75))
	cards.append(Character('Martin Laursen - Aston Villa (CB)',56,84,85,78,76,62))
	cards.append(Character('Olaf Mellberg - Aston Villa (CB)',62,86,86,85,78,78))
	cards.append(Character('Gabby Agbonlahor - Aston Villa (CF)',70,42,70,79,93,79))
	cards.append(Character('Benni McCarthy - Blackburn Rovers (CF)',84,45,78,79,85,84))
	cards.append(Character('Tugay - Blackburn Rovers (DMF)',71,76,72,82,73,87))
	cards.append(Character('Brad Friedel - Blackburn Rovers (GK)',40,90,88,60,64,55))
	cards.append(Character('Robbie Savage - Blackburn Rovers (DMF)',68,72,71,90,74,77))
	cards.append(Character('Nicolas Anelka - Bolton Wanderers (CF)',85,35,84,81,88,88))
	cards.append(Character('Kevin Davies - Bolton Wanderers (CF)',77,58,87,82,75,75))
	cards.append(Character('Gary Speed - Bolton Wanderers (CMF)',70,69,84,80,74,76))
	cards.append(Character('Ivan Campo - Bolton Wanderers (DMF)',63,75,84,82,70,75))
	cards.append(Character('Darren Bent - Charlton Athletic (CF)',84,38,85,86,85,79))
	cards.append(Character('Matt Holland - Charlton Athletic (CMF)',69,73,79,85,74,77))
	cards.append(Character('Lee Carsley - Everton (CMF)',67,70,82,85,70,70))
	cards.append(Character('Tim Cahill - Everton (CMF)',78,67,75,86,77,76))
	cards.append(Character('Tony Hibbert - Everton (SB)',60,75,76,84,81,75))
	cards.append(Character('Tim Howard - Everton (GK)',30,84,88,60,62,48))
	cards.append(Character('Cesc Fabregas - Arsenal (CMF)',75,58,69,82,77,87))
	cards.append(Character('Robin van Persie - Arsenal (CF)',76,37,81,82,84,88))
	cards.append(Character('Arjen Robben - Chelsea (WF)',81,53,79,78,88,87))
	cards.append(Character('Claude Makelele - Chelsea (DMF)',64,85,74,93,83,82))
	cards.append(Character('Papa Bouba Diop - Fulham (CMF)',75,67,91,82,75,75))
	cards.append(Character('Jimmy Bullard - Fulham (CMF)',70,67,83,83,78,76))
	cards.append(Character('Peter Crouch - Liverpool (CF)',80,38,81,77,75,77))
	cards.append(Character('Jamie Carragher - Liverpool (CB)',63,88,86,83,77,70))
	cards.append(Character('Javier Mascherano - Liverpool (DMF)',70,78,77,86,80,80))
	cards.append(Character('Joey Barton - Manchester City (CMF)',74,76,81,88,76,76))
	cards.append(Character('Micah Richards - Manchester City (SB)',68,68,83,79,82,75))
	cards.append(Character('Paul Scholes - Manchester United (CMF)',80,63,77,87,76,86))
	cards.append(Character('Nemanja Vidic - Manchester United (CB)',48,82,88,79,75,69))
	cards.append(Character('Patrice Evra - Manchester United (SB)',80,69,80,88,87,83))
	cards.append(Character('Edwin van der Sar - Manchester United (GK)',30,95,82,65,68,63))
	cards.append(Character('Yakubu - Middlesbrough (CF)',84,32,85,82,86,81))
	cards.append(Character('Stewart Downing - Middlesbrough (SMF)',78,52,72,73,85,79))
	cards.append(Character('Mark Viduka - Middlesbrough (CF)',87,40,93,75,77,85))
	cards.append(Character('Jonathan Woodgate - Middlesbrough (CB)',53,83,82,79,76,72))
	cards.append(Character('Damien Duff - Newcastle United (WF)',83,59,73,90,88,86))
	cards.append(Character('Obafemi Martins - Newcastle United (CF)',78,40,82,85,99,80))
	cards.append(Character('Nolberto Solano - Newcastle United (SMF)',78,59,69,91,82,86))
	cards.append(Character('Stephen Carr - Newcastle United (SB)',75,72,80,88,83,78))
	cards.append(Character('Michael Owen - Newcastle United (CF)',91,35,82,80,90,85))
	cards.append(Character('Mwaruwari Benjani - Portsmouth (CF)',84,44,87,84,83,75))
	cards.append(Character('Nwankwo Kanu - Portsmouth (SS)',83,45,85,74,73,92))
	cards.append(Character('Sol Campbell - Portsmouth (CB)',60,90,95,79,76,77))
	cards.append(Character('David James - Portsmouth (GK)',30,84,90,60,65,46))
	cards.append(Character('Kevin Doyle - Reading (CF)',78,34,80,78,83,76))
	cards.append(Character('Phil Jagielka - Sheffield United (CB)',63,73,83,83,75,75))
	cards.append(Character('Dimitar Berbatov - Tottenham Hotspur (CF)',86,43,85,82,84,87))
	cards.append(Character('Robbie Keane - Tottenham Hotspur (CF)',87,33,76,82,88,82))
	cards.append(Character('Jermaine Defoe - Tottenham Hotspur (CF)',85,43,75,82,87,84))
	cards.append(Character('Ledley King - Tottenham Hotspur (CB)',57,85,89,86,79,71))
	cards.append(Character('Paul Robinson - Tottenham Hotspur (GK)',30,84,89,63,66,66))
	cards.append(Character('Danny Shittu - Watford (CB)',43,77,81,75,71,59))
	cards.append(Character('Carlos Tevez - West Ham United (SS)',84,43,89,85,83,87))
	cards.append(Character('Bobby Zamora - West Ham United (CF)',77,39,80,75,80,75))
	cards.append(Character('Paul Konchesky - West Ham United (SB)',70,70,74,82,82,81))
	cards.append(Character('Emile Heskey - Wigan Athletic (CF)',83,56,88,84,84,81))
	cards.append(Character('Antonio Valencia - Wigan Athletic (AMF)',73,45,78,80,81,80))


    
	print("SOCCER STARS TOP TRUMPS 06/07")
	print("----------------------------")
	time.sleep(2)
	print("""
    Welcome to Soccer Stars Top Trumps 06/07! Here is a little game based on the popular card game Top Trumps,
    where players compete over cards with various statistics. I have always had a fascination with 2000s era
    football, as for me it was the best period in terms of competitive teams, and the period where the some of
    the best players of all time played in. I was also inspired by the game PES6, widely believed by many to be
    the greatest football simulation video game ever made, so thought I would base the players and statistics off
    the 2006/07 season, looking back there were a lot of great teams from that period: Ferguson's United, Mourinho's
    Chelsea, Ancelotti's AC Milan, Rijkaard's Barcelona, and even some great underdog sides like Portsmouth, Aston
    Villa and Middlesbrough from this time.
    
    Each player, or card in this simulation, has six stats: Attack, Defence, Physical, Stamina, Speed and Technique.
    I have tried to go for a healthy balance of goalkeepers, defenders, midfielders and forwards so there is a balance
    in stats. I've tried to go for a balance as well between all the superstar names as well as the more 'cult heroes'
    of the era, that should make the games more exciting I think. Hopefully you will enjoy this program and relive the 
    golden era of 00s European Football!""")
	time.sleep(3)
	input("\n Press any key to begin the simulation: ")
	print("\n")
	time.sleep(2)

	random.shuffle(cards)

	playerDeck = []
	computerDeck = []

	playernowins = 0
	computernowins = 0


	# deal the cards
	while len(cards) > 0 and len(playerDeck) < 10 and len(computerDeck) < 10:
		playerDeck.append(cards.pop(0))
		computerDeck.append(cards.pop(0))

	playerTurn = True
	allowedResponses = ["1","2","3","4","5","6"]

	print(f"Player has {len(playerDeck)} cards")
	print(f"Computer has {len(computerDeck)} cards")

	while len(playerDeck) > 0 and len(computerDeck) > 0:

		time.sleep(2)

		playerCard = playerDeck.pop(0)
		computerCard = computerDeck.pop(0)

		print("\nYour card:")
		print("Name:",playerCard.name)
		print("1. Attack:",playerCard.attack)
		print("2. Defence:",playerCard.defence)
		print("3. Physical:",playerCard.physical)
		print("4. Stamina:",playerCard.stamina)
		print("5. Speed:",playerCard.speed)
		print("6. Technique:",playerCard.technique)

		time.sleep(2)

		if playerTurn == True:
			answer = input("Which skill do you choose?: ")
			while allowedResponses.count(answer) == 0:
				answer = input("That isn't a valid answer, please try again: ")
		else:
			answer = random.choice(allowedResponses)
			print("Computer chooses", answer)

		print("\nCOMPUTER CARD")
		print("Name:", computerCard.name)

		playerWins = False

		if answer == "1":
			print("Attack:", computerCard.attack)
			isDraw = (playerCard.attack == computerCard.attack)
			playerWins = (playerCard.attack > computerCard.attack)
			playerLoses = (playerCard.attack < computerCard.attack)
		elif answer == "2":
			print("Defence:", computerCard.defence)
			isDraw = (playerCard.defence == computerCard.defence)
			playerWins = (playerCard.defence > computerCard.defence)
			playerLoses = (playerCard.defence < computerCard.defence)
		elif answer == "3":
			print("Physical:", computerCard.physical)
			isDraw = (playerCard.physical == computerCard.physical)
			playerWins = (playerCard.physical > computerCard.physical)
			playerLoses = (playerCard.physical < computerCard.physical)
		elif answer == "4":
			print("Stamina:", computerCard.stamina)
			isDraw = (playerCard.stamina == computerCard.stamina)
			playerWins = (playerCard.stamina > computerCard.stamina)
			playerLoses = (playerCard.stamina < computerCard.stamina)
		elif answer == "5":
			print("Speed:", computerCard.speed)
			isDraw = (playerCard.speed == computerCard.speed)
			playerWins = (playerCard.speed > computerCard.speed)
			playerLoses = (playerCard.speed < computerCard.speed)
		elif answer == "6":
			print("Technique:", computerCard.technique)
			isDraw = (playerCard.technique == computerCard.technique)
			playerWins = (playerCard.technique > computerCard.technique)
			playerLoses = (playerCard.technique < playerCard.technique)

		time.sleep(2)

		if isDraw:
			print("\nIt's a tie!")
			playerDeck.append(playerCard)
			computerDeck.append(computerCard)
		elif playerWins:
			print("\nYou win this hand!")
			playerDeck.append(playerCard)
			playerDeck.append(computerCard)
			print(f"Player has {len(playerDeck)} cards remaining")
			print(f"Computer has {len(computerDeck)} cards remaining")
			playerTurn = True
		else:
			print("\nYou lose this hand!")
			computerDeck.append(computerCard)
			computerDeck.append(playerCard)
			print(f"Player has {len(playerDeck)} cards remaining")
			print(f"Computer has {len(computerDeck)} cards remaining")
			playerTurn = False

	time.sleep(2)

	if len(playerDeck) == 0:
	    print("YOU LOSE!")
	    computernowins += 1
	    print(f"Player has {playernowins}")
	    print(f"Computer has {computernowins}")
	else:
	    print("YOU WIN!")
	    playernowins += 1
	    print(f"\nPlayer has {playernowins} wins")
	    print(f"Computer has {computernowins} wins")

	print("\n")
	print("Thanks for playing!")
	while True:
		play_again = input("Would you like to play again? Type Y or N: ")
		if play_again.lower() == 'y':
			print("\n")
			main()
		elif play_again.lower() == 'n':
			print("No problem, enjoy the rest of your day!")
			time.sleep(3)
			break
		else:
			print("Type Y or N: ")

if __name__ == "__main__":
	main()


                                 	
