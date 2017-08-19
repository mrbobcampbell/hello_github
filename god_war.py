import numpy as np
from matplotlib import pyplot as plt
import statistics


# Dictionary containing all 52 cards
full_deck = {"Ace of Hearts": 1, "Two of Hearts": 2,
             "Three of Hearts": 3, "Four of Hearts": 4,
             "Five of Hearts": 5, "Six of Hearts": 6, "Seven of Hearts": 7,
             "Eight of Hearts": 8, "Nine of Hearts": 9, "Ten of Hearts": 10,
             "Jack of Hearts": 11, "Queen of Hearts": 11, "King of Hearts": 11,
             "Ace of Spades": 1, "Two of Spades": 2, "Three of Spades": 3,
             "Four of Spades": 4, "Five of Spades": 5, "Six of Spades": 6,
             "Seven of Spades": 7, "Eight of Spades": 8, "Nine of Spades": 9,
             "Ten of Spades": 10, "Jack of Spades": 11, "Queen of Spades": 11,
             "King of Spades": 11, "Ace of Diamonds": 1, "Two of Diamonds": 2,
             "Three of Diamonds": 3, "Four of Diamonds": 4,
             "Five of Diamonds": 5, "Six of Diamonds": 6,
             "Seven of Diamonds": 7, "Eight of Diamonds": 8,
             "Nine of Diamonds": 9, "Ten of Diamonds": 10,
             "Jack of Diamonds": 11, "Queen of Diamonds": 11,
             "King of Diamonds": 11, "Ace of Clubs": 1,
             "Two of Clubs": 2, "Three of Clubs": 3, "Four of Clubs": 4,
             "Five of Clubs": 5, "Six of Clubs": 6, "Seven of Clubs": 7,
             "Eight of Clubs": 8, "Nine of Clubs": 9, "Ten of Clubs": 10,
             "Jack of Clubs": 11, "Queen of Clubs": 11, "King of Clubs": 11}

# load available_deck from dictionary
available_deck = []
for cards in full_deck:
    available_deck.append(cards)

# automatically draw two cards from available deck until deck is depleted
# print(len(available_deck))
match_list = []
game_list = []

god_counter = 0
player1_god = 0
player2_god = 0
tie_god = 0
match_counter = 0
player1_match = 0
player2_match = 0
tie_match = 0
availabe_counter = len(available_deck)
player1_score = 0
player2_score = 0
tie_score = 0

while god_counter < 1000:
    while match_counter < 1000:
        while availabe_counter > 1:
            player1_card = available_deck[np.random.randint(len(available_deck))]
            available_deck.remove(player1_card)
            # print("Player 1's card: ",player1_card, full_deck[player1_card])
            availabe_counter -= 1
            player2_card = available_deck[np.random.randint(len(available_deck))]
            # print("Player 2's card: ", player2_card, full_deck[player2_card])
            available_deck.remove(player2_card)
            availabe_counter -= 1
            if full_deck[player1_card] > full_deck[player2_card]:
                player1_score += 1
                # print("Player 1 wins!")
            elif full_deck[player1_card] == full_deck[player2_card]:
                tie_score += 1
            else:
                player2_score += 1
                # print("Player 2 wins!")
        if player1_score > player2_score:
            player1_match += 1
        elif player1_score == player2_score:
            tie_match += 1
            # print("Tie Game!")
        else:
            player2_match += 1
        match_counter += 1
        game_list.append(player1_score)
        game_list.append(player2_score)
        available_deck = []
        for cards in full_deck:
            available_deck.append(cards)
        availabe_counter = len(available_deck)
        player1_score = 0
        player2_score = 0
        tie_score = 0

    if player1_match > player2_match:
        player1_god += 1
    elif player1_match == player2_match:
        tie_god += 1
    else:
        player2_god += 1

    match_counter = 0
    god_counter += 1
    match_list.append(player1_match)
    match_list.append(player2_match)
    print("Meta game number: ", god_counter)
    print("Player 1 Match Wins: ", player1_match)
    print("Player 2 Match Wins: ", player2_match)
    print("Player 1 god wins: ", player1_god)
    print("Player 2 god wins: ", player2_god)
    print("God Ties: ", tie_god)
    print("\n\n")
    player1_match = 0
    player2_match = 0
    tie_match = 0

print(match_list)
print("Match Recap:")
print('Mean: ', statistics.mean(match_list))
print('Std_dev: ', statistics.stdev(match_list))
print('Variance: ', statistics.variance(match_list))
print('Var2: ', statistics.stdev(match_list)**2)
print("Match Count: ", len(match_list))


# print(game_list)
print("Game Recap: ")
print('Mean: ', statistics.mean(game_list))
print("Game probability: ", statistics.mean(game_list) / 26)
print('Std_dev: ', statistics.stdev(game_list))
print('Variance: ', statistics.variance(game_list))
print('Var2: ', statistics.stdev(game_list)**2)
print("Game count: ", len(game_list))

# plt.figure(100)
# num_bins = 300
# n, bins, patches = plt.hist(match_list, num_bins, facecolor='blue')

# plt.figure(2)
# num_bins = 300
# n, bins, patches = plt.hist(game_list, num_bins, facecolor='blue')
# plt.show()

print((statistics.mean(match_list) / len(match_list)))
x1 = statistics.mean(match_list)
x2 = (statistics.mean(game_list) / 26) * 100
print(x1)
print(x2, "\n")
print(x1 - x2, "game over")
