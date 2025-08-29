class Player:
    playerNum = 0

    def __init__(self, score=0, hand = None):
        if hand is None:
            hand = []
        self.hand = hand
        self.score = score
        self.playerNum = Player.playerNum
        Player.playerNum += 1

class Dealer(Player):
    def __init__(self, score=0, hand = None):
        super().__init__(score, hand)

    def deal(self, deck):
        return deck.pop() 
        
class User(Player):
    def __init__(self, score=0, hand = None):
        super().__init__(score, hand)