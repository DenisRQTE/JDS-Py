import pytest
from buyside import Bank

class TestBank:
    def test_init(self):
        """Test bank initialization with starting balance"""
        bank = Bank(1000)
        assert bank.balance == 1000
        assert bank.current_bet == 0
    
    def test_place_bet_sufficient_funds(self):
        """Test placing a bet when there are sufficient funds"""
        bank = Bank(1000)
        bank.place_bet(100)
        assert bank.balance == 900
        assert bank.current_bet == 100
    
    def test_place_bet_insufficient_funds(self):
        """Test placing a bet when there are insufficient funds"""
        bank = Bank(50)
        bank.place_bet(100)
        # Balance should remain unchanged
        assert bank.balance == 50
        # Current bet should remain unchanged (0)
        assert bank.current_bet == 0
    
    def test_place_bet_exact_balance(self):
        """Test placing a bet equal to the current balance"""
        bank = Bank(100)
        bank.place_bet(100)
        assert bank.balance == 0
        assert bank.current_bet == 100
    
    def test_win(self):
        """Test winning a bet (doubles the bet amount)"""
        bank = Bank(1000)
        bank.place_bet(100)
        result = bank.win()
        
        # Balance should increase by 2x the bet (original 900 + 200 = 1100)
        assert bank.balance == 1100
        assert result == "You've won 100"
    
    def test_lose(self):
        """Test losing a bet"""
        bank = Bank(1000)
        bank.place_bet(100)
        result = bank.lose()
        
        # Balance should remain at 900 (bet was already deducted)
        assert bank.balance == 900
        assert result == "You've lost 100"
    
    def test_stand_off(self):
        """Test a stand-off (bet amount returned)"""
        bank = Bank(1000)
        bank.place_bet(100)
        result = bank.stand_off()
        
        # Balance should return to original (bet returned)
        assert bank.balance == 1000
        assert bank.current_bet == 0
        assert result == "Stand-off, no payout"
    
    def test_blackjack(self):
        """Test blackjack win (2.5x the bet amount)"""
        bank = Bank(1000)
        bank.place_bet(100)
        bank.blackjack()
        
        # Balance should increase by 2.5x the bet (original 900 + 250 = 1150)
        assert bank.balance == 1150
        assert bank.current_bet == 0
    
    def test_multiple_bets(self):
        """Test multiple betting scenarios"""
        bank = Bank(1000)
        
        # First bet and win
        bank.place_bet(100)
        bank.win()
        assert bank.balance == 1100
        
        # Second bet and lose
        bank.place_bet(200)
        bank.lose()
        assert bank.balance == 900
        
        # Third bet and stand-off
        bank.place_bet(150)
        bank.stand_off()
        assert bank.balance == 900
        
        # Fourth bet and blackjack
        bank.place_bet(100)
        bank.blackjack()
        assert bank.balance == 1050
    
    def test_zero_balance_scenarios(self):
        """Test edge cases with zero or low balance"""
        bank = Bank(0)
        bank.place_bet(10)
        
        # Should not be able to place bet with zero balance
        assert bank.balance == 0
        assert bank.current_bet == 0


if __name__ == "__main__":
    pytest.main([__file__])
