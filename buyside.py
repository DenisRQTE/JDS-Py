class Bank:
    def __init__(self, starting_balance):
        self.balance = starting_balance
        self.current_bet = 0

    def place_bet(self, amount):
        print(f"Confirm that you want to spend {amount} ")
        if amount > starting_balance:
            print("Insufficient funds, make a deposit in order to place further bets.")
        else:
            self.balance -= amount
            self.current_bet = amount
    def win()

    def lose()

    def moneyback()

    def blackjack()