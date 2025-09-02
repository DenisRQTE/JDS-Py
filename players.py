class Player:
    playerNum = 0

    def __init__(self, score=0, hand = None):
        if hand is None:
            hand = []
        self.hand = hand
        self.score = score
        self.playerNum = Player.playerNum
        Player.playerNum += 1
        
    def show_hand(self):
        for card in self.hand:
            print(card["text"], end=" ")
        print()
        return

class Dealer(Player):
    def __init__(self, score=0, hand = None):
        super().__init__(score, hand)

    def deal(self, deck):
        return deck.pop() 
        
class User(Player):
    def __init__(self, score=0, hand = None):
        super().__init__(score, hand)

    def play(self):
        hit_opts = ["h", "hit"]
        stand_opts = ["s", "stand", "stay"]
        user_play = input("do you want to hit or stand : ").lower()
        if user_play in hit_opts:
            play = "hit"
        elif user_play in stand_opts:
            play = "stand"
        return play