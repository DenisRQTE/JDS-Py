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

print(deck[:2])

current_hand = deck[:-1]
value = sum(card_values[card.split(" ")[0]] for card in current_hand)


hit = input("do you want to hit or stay : ")

def hit_stay(hit):
    
    
    if hit == "hit":
        print(": ", deck[:3])
        hit = input("do you want to hit or stay : ")

        if hit == "hit":
            print(": ", deck[:4])
            hit = input("do you want to hit or stay : ")

            if hit == "hit":
                print(": ", deck[:5])
                print(value)
                return
            
            elif stand:
                print(value)
                print(deck[:4])                
                return 
            
        elif stand:
            print(value)
            print(deck[:3])
            return 
        
    elif stand:
        print(deck[:2])
        print(value)
        return 

hit_stay(hit)




