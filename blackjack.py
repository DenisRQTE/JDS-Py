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


SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11  
}

deck = [{"suit": suit, 
         "rank": rank, 
         "text":"| " + rank + " of " + suit + " |" } 
         for suit in SUITS for rank in RANKS]

random.shuffle(deck)

def deal():
    return deck.pop() 

current_hand = []
current_hand.append(deal())
current_hand.append(deal())
score = 0
for card in current_hand:
    print(card["text"], end=" ")
print()

for card in current_hand:
    rank=card["rank"]
    value=CARD_VALUES[rank]
    if rank == "A":
        flex_score=score
        flex_score+=value
        if flex_score > 21:
            score+=1
        else:
            score=flex_score
    else:
        score+=value
            
print(f"Current score: {score}")

hit = input("do you want to hit or stay : ")

"""
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

"""
