from helpers import calc_score, underline, CARD_VALUES

class Player:
    playerNum = 0

    def __init__(self, score=0, hand = None):
        if hand is None:
            hand = []
        self.hand = hand
        self.playerNum = Player.playerNum
        Player.playerNum += 1
    
    @property
    def score(self):
        return calc_score(self.hand)
    
    def play(self, hit=None):
        if hit is None:
            hit_opts = ["h", "hit"]
            stand_opts = ["s", "stand", "stay"]
            user_play = input("do you want to hit or stand : ").lower()
            if user_play in hit_opts:
                return "hit"
            elif user_play in stand_opts:
                return "stand"
            else:
                return self.play()
        elif hit == True:
            return "hit"
        elif hit == False:
            return "stand"

class Dealer(Player):
    def __init__(self, score=0, hand = None):
        super().__init__(score, hand)

    def deal(self, deck):
        return deck.pop() 
        
class User(Player):
    def __init__(self, score=0, hand = None):
        super().__init__(score, hand)

