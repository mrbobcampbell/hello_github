import numpy as np

#Dictionary containing all 52 cards
print("Section 1")
full_deck = {"One of Hearts" : 1, "Two of Hearts" : 2, "Three of Hearts" : 3, "Four of Hearts" : 4, "Five of Hearts" : 5, "Six of Hearts" : 6, "Seven of Hearts" : 7, "Eight of Hearts" : 8, "Nine of Hearts" : 9, "Ten of Hearts" : 10}
print(full_deck,"\n")

#Checking to see if a card is in the dictionary
print("Section 2")
print("Is the One of Hearts in the deck?",'One of Hearts' in full_deck,"\n")

#Checking to see if the dictionary lookup is a number... it is.
print("Section 3")
print(full_deck['One of Hearts'],' > ', full_deck['Two of Hearts'],"?")
if full_deck["One of Hearts"] > full_deck["Two of Hearts"]:
	print("True\n\n")
else:
	print("False\n\n")


#load available_deck from dictionary
print("Section 4")
available_deck = []
for cards in full_deck:
	available_deck.append(cards)
	
print(available_deck,"\n\n")


#randomly pick a card from the available_deck
print("Section 5")
print(available_deck[np.random.randint(3)],"\n\n")


#remove a card from the deck
print("Section 6")
print(available_deck)
available_deck.remove('One of Hearts')
print(available_deck,"")
#add it back
available_deck.append('One of Hearts')
print(available_deck,"\n\n")


#randomly remove cards from available_deck until there are none left
print("Section 7")

availabe_counter = len(available_deck)

while availabe_counter > 0:
	available_deck.remove(available_deck[np.random.randint(availabe_counter)])
	print(available_deck)
	availabe_counter -= 1
	
print("\n\n")


#reload available_deck
available_deck = []
for cards in full_deck:
	available_deck.append(cards)
	
	
#draw two cards the available_deck and see who wins
print("Section 8")
player1_card = available_deck[np.random.randint(len(available_deck))]
available_deck.remove(player1_card)
print("Player 1's card: ",player1_card, full_deck[player1_card])
player2_card = available_deck[np.random.randint(len(available_deck))]
print("Player 2's card: ", player2_card, full_deck[player2_card])
if full_deck[player1_card] > full_deck[player2_card]:
	print("Player 1 wins!")
else:
	print("Player 2 wins!")

print("\n\n")


#reload available_deck
available_deck = []
for cards in full_deck:
	available_deck.append(cards)
	

#automatically draw two cards from available deck until deck is depleted
print("Section 9")
availabe_counter = len(available_deck)
player1_score = 0
player2_score = 0

while availabe_counter > 0:
	player1_card = available_deck[np.random.randint(len(available_deck))]
	available_deck.remove(player1_card)
	print("Player 1's card: ",player1_card, full_deck[player1_card])
	availabe_counter -= 1
	player2_card = available_deck[np.random.randint(len(available_deck))]
	print("Player 2's card: ", player2_card, full_deck[player2_card])
	available_deck.remove(player2_card)
	availabe_counter -= 1
	if full_deck[player1_card] > full_deck[player2_card]:
		player1_score += 1
		print("Player 1 wins!")
	else:
		player2_score += 1
		print("Player 2 wins!")
		
if player1_score > player2_score:
	print("Player 1 wins the match", player1_score, "to", player2_score, "!!!")	
else:
	print("Player 2 wins the match", player2_score, "to", player1_score, "!!!")	

