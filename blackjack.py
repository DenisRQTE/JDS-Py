import random
from time import sleep
from players import User, Dealer
from helpers import SUITS, RANKS, clear_terminal, show_table
#define cards
# define card values array dictionnary
# deal cards arrray
# hit stand option / fucntion
#  optinal : split option function
# bankers turn 
# A= 1-11
# Anouncing winner
# banking system
clear_terminal()

dealer = Dealer()
user = User()
table = [dealer, user]
 
deck = [{"suit": suit, 
         "rank": rank, 
         "text":"| " + rank + " of " + suit + " |" } 
         for suit in SUITS for rank in RANKS]

random.shuffle(deck)

for i in range(2):
    for player in table:
        player.hand.append(dealer.deal(deck))

# Scores are computed dynamically via Player.score property
if dealer.score == 21:
    show_table(dealer, [user], reveal_dealer=True)
    print("DEALER HAS BLACKJACK! YOU LOSE")
    exit()
elif user.score == 21:
    show_table(dealer, [user], reveal_dealer=True)
    print("LUCKY YOU, you hit BlackJack! Drinks on Mark")
    exit()
else:
    print("Let's play!")

while True:
    show_table(dealer, [user], reveal_dealer=False)
    # Checks to see if initial win condition is met

    userPlay = user.play()
    # Hits and calculates score, then checks score 
    if userPlay == "hit":
        user.hand.append(dealer.deal(deck))
        show_table(dealer, [user], reveal_dealer=False)
    
        if user.score > 21:
            # If score is more than 21, players busts
            print("BUST! YOU LOSE")
            exit()
        else:
            print(f"Current Score: {user.score}")
    # elif is used to specify "stay" as input value        
    elif userPlay == "stand":
        print(f"Current Score: {user.score}")
        break
    else: 
        print("Try Again") # Better err
    
if user.score <= 21:
    # Dealer's turn
    sleep(1)
    show_table(dealer, [user], reveal_dealer=True)
    sleep(1)

    while dealer.score < 17:
        dealer.hand.append(dealer.deal(deck))
        show_table(dealer, [user], reveal_dealer=True)

        if dealer.score > 21:
            print("DEALER BUST! YOU WIN")
            break
        else:
            print(f"Current Score: {dealer.score}")
        sleep(1)

if dealer.score > user.score:
    print("DEALER WINS")
elif dealer.score < user.score:
    print("YOU WIN")
else:
    print("IT'S A TIE")

print("GAME OVER")