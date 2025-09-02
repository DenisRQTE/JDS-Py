import random
from time import sleep
from players import User, Dealer
from helpers import calc_score, SUITS, RANKS
#define cards
# define card values array dictionnary
# deal cards arrray
# hit stand option / fucntion
#  optinal : split option function
# bankers turn 
# A= 1-11
# Anouncing winner
# banking system
 
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

player.show_hand()
            
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
            player.show_hand()
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
