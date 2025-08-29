import random
from time import sleep
from players import User, Dealer

#define cards
# define card values array dictionnary
# deal cards arrray
# hit stand option / fucntion
#  optinal : split option function
# bankers turn 
# A= 1-11
# Anouncing winner
# banking system
 
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


dealer = Dealer()
player = User()
current_hand = player.hand
current_hand.append(dealer.deal(deck))
current_hand.append(dealer.deal(deck))


for card in current_hand:
    print(card["text"], end=" ")
print()



def calc_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        rank=card["rank"]
        value=CARD_VALUES[rank]
        if rank == "A": 
            ace_count+=1
            flex_score=score
            flex_score+=value
            if flex_score > 21:
                score+=1
            else:
                score=flex_score
        else:
            score+=value
        if ace_count > 0:
            if score > 21:
                score-=10
                ace_count-=1    
            
    return score

def show_hand():
    for card in current_hand:
        print(card["text"], end=" ")
    print()
    return
    
            
score = calc_score(current_hand)            
            
print(f"Current score: {score}")


while True:
    # Checks to see if initial win condition is met
    if calc_score(current_hand) == 21:
        print("BLACKJACK! YOU WIN!")
        break
    else:
        userPlay = player.play()
        # Hits and calculates score, then checks score 
        if userPlay == "hit":
            current_hand.append(dealer.deal(deck))
            show_hand()
            score=calc_score(current_hand)
        
            if score > 21:
                # If score is more than 21, players busts
                print("BUST! YOU LOSE")
                break
            else:
                print(f"Current Score: {score}")
        # elif is used to specify "stay" as input value        
        elif userPlay == "stand":
            score=calc_score(current_hand)
            print(f"Current Score: {score}")
            break
        else: 
            print("Try Again") # Better error-checking should go here.
