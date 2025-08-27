class Bank:
    def __init__(self, starting_balance):
        self.balance = starting_balance
        self.current_bet = 0

    def place_bet(self, amount):
        print(f"Confirm that you want to spend {amount} ")
        if amount > self.balance:
            print("Insufficient funds, make a deposit through the banker to place further bets.")
        else:
            self.balance -= amount
            self.current_bet = amount
    def win(self):
        self.balance += self.current_bet
        return f"You've won {self.current_bet}" 
    def lose(self):
        return f"You've lost {self.current_bet}"
    def stand_off(self,):
        return f"Stand-off, no payout"
    def blackjack(self,):