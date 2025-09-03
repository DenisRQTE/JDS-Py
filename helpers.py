import os

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11  
}

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

def underline(text):
    return text + "\n" + "-" * len(text)

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def show_table(dealer, players, reveal_dealer=False):
    clear_terminal()
    print(underline("Dealer Hand"))
    if reveal_dealer:
        for card in dealer.hand:
            print(card["text"], end=" ")
        print()
        print(f"Score: {calc_score(dealer.hand)}")
    else:
        if dealer.hand:
            first_card = dealer.hand[0]
            value = CARD_VALUES[first_card["rank"]]
            print(first_card["text"], end=" ")
            print("| Hidden |", end=" ")
            print()
            print(f"Score: {value}")
        else:
            print("(no cards)")
            print("Score: 0")
    print()
    for p in players:
        header = f"Player {p.playerNum} hand: "
        print(underline(header))
        for card in p.hand:
            print(card["text"], end=" ")
        print()
        print(f"Score: {calc_score(p.hand)}")
        print()