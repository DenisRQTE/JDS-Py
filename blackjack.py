import random

#define cards
# define card values array dictionnary
# deal cards arrray
# hit stand option / fucntion
#  optinal : split option function
# bankers turn 
# A= 1-11
# Anouncing winner
# banking system


stand = "stand"


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11  
}

deck = [rank + " of " + suit for suit in suits for rank in ranks]

random.shuffle(deck)  



current_hand = deck[:2]
sum_of_cards = sum(card_values[card.split(" ")[0]] for card in current_hand)

print(deck[:2])


count = 2

while sum_of_cards <= 21:
    hit_or_stand = input("would you like to hit or stand : ")
    if hit_or_stand == "hit":
        count += 1
        next_card = deck[count]
        print(next_card)
        value_of_next_card = card_values[next_card.split(" ")[0]]
        sum_of_cards = sum_of_cards + value_of_next_card
        print(sum_of_cards)
    elif hit_or_stand == "stand":
        print(f"you've chosen to stand your final score is : {sum_of_cards=} ")
        break


    else:  
        print("input not recognized")
    
    if sum_of_cards == 21:
        print("LUCKY YOU, you hit blackjack ! Drinks on mark")
        


