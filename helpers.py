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