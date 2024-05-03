from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()


    def confirm_start(self):
       play = input(f"You are starting with ${self.player.balance}. Would you like to play a hand? ").lower().strip()
       return play in ["yes", "y", "start"]


    def place_bet(self):
        while True:
            try:
                bet = float(input("Place your bet: "))
            except ValueError:
                print("Enter a valid number.")
                continue
            else:
                if bet > self.player.balance:
                    print("You don't have sufficient funds.")
                elif bet < Game.MINIMUM_BET:
                    print("The minimum bet is ${Game.MINIMUM_BET}!")
                else:
                    self.bet = bet
                    break
                

    def deal_initial_hands(self):
        self.player.hand = Hand(self.deck.deal(2))
        self.dealer.hand = Hand(self.deck.deal(2))
        self.dealer.hand.cards[1].hidden = True
        print(f"You are dealt: {self.player.get_str_hand()}")
        print(f"Dealer is dealt: {self.dealer.get_str_hand()}")


    def handle_blackjack(self):
        player_hand_val = self.player.hand.get_value()
        dealer_hand_val = self.dealer.hand.get_value()

        if player_hand_val != 21:
            return False
        
        if dealer_hand_val == 21:
            return True
        
        print(f"Blackjack! You win ${self.bet * 1.5}")
        self.player.balance += self.bet * 1.5
        return True
    

    def determine_winner(self):
        player_hand_val = self.player.hand.get_value()
        dealer_hand_val = self.dealer.hand.get_value()

        if player_hand_val > dealer_hand_val:
            self.player.balance += self.bet
            print(f"You win ${self.bet}!")
        
        elif player_hand_val < dealer_hand_val:
            self.player.balance -= self.bet
            print(f"The dealer wins, you lose ${self.bet}!")

        elif player_hand_val == dealer_hand_val:
            print("You tie!")
            
        
    def start_round(self):
        self.deck.shuffle()
        self.place_bet()
        self.deal_initial_hands()

        if self.handle_blackjack():
            return

        player_lost = self.player_turn()
        if player_lost:
            self.player.balance -= self.bet
            print(f"You bust, you lose ${self.bet}!")
            return
  
        dealer_lost = self.dealer_turn()
        if dealer_lost:
            self.player.balance += self.bet
            print(f"The dealer busts, you win ${self.bet}!")
            return
        
        self.determine_winner()
        self.reset_round()


    def start_game(self):
        while self.player.balance > 0:
            if not self.confirm_start():
                print(f"You've left the game with ${self.player.balance}.")
                break

            self.start_round()

        else:

            print("You're out of money, restart program to play again.")


    def get_hit_or_stay(self):
        while True:
            hit_or_stay = input("Would you like to hit or stay? ").lower().strip()

            if  hit_or_stay in ["hit", "stay"]:
                break

            print("Please enter 'hit' or 'stay'.")
            
        return hit_or_stay == "hit"


    def player_turn(self):
        while True:
            hit = self.get_hit_or_stay()
            if not hit:
                break
            
            new_card = self.deck.deal(1)[0]
            self.player.hand.add_to_hand(new_card)

            print(f"You've been dealt {new_card}")
            print(f"You now have {self.player.get_str_hand()}")

            hand_value = self.player.hand.get_value()
            if hand_value > 21:
                return True

        return False
                

    def dealer_turn(self):
        self.dealer.hand.cards[1].hidden = False
        while True:
            print(f"The dealer has {self.dealer.get_str_hand()}")

            hand_value = self.dealer.hand.get_value()
            if hand_value >= 17 and not hand_value >= 21:
                print("The dealer stays.")
                break

            elif hand_value <= 16:
                new_card = self.deck.deal(1)[0]
                self.dealer.hand.add_to_hand(new_card)
                print(f"The dealer hits and is dealt: {new_card} ")

            elif hand_value == 21:
                return False
            
            else:
                return True

    def reset_round(self):
        self.deck.shuffle()
        self.player.hand = None
        self.dealer.hand = None
        self.bet = 0