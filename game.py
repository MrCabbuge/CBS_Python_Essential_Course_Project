from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()  # initiate deck
        self.deck.generate_deck()  # fill deck with cards
        self.player = Player(False, self.deck)  # initiate player with access to the deck
        self.dealer = Player(True, self.deck)  # initiate dealer with access to the deck

    def start_game(self):
        # dealing cards to the player and the dealer
        player_status = self.player.deal()
        dealer_status = self.dealer.deal()

        self.player.show()  # print cards of the player

        if player_status == 1:  # check if player has blackjack
            print("Player got Game! Congrats!")
            if dealer_status == 1:  # if player has blackjack, check if dealer has blackjack too and call a tie
                print("Dealer and Player got Game! It's a push. (Tie)")
            return 1

        command = ""  # if player has no blackjack, give option to take more cards or stop drawing
        while command != "stand":
            bust = 0
            command = input("Hit or Stand? ").lower()  # ask for input to hit or stand (using lowercase to user-proof)

            if command == "hit":
                bust = self.player.hit()
                self.player.show()
            if bust == 1:  # if score is >21 bust the player
                print("Player busted. Good Game!")
                return 1
        print("\n")
        self.dealer.show()  # show dealer's cards
        if dealer_status == 1:  # if dealer has 21, call blackjack
            print("Dealer got Game! Better luck next time!")
            return 1
        # dealer hits until his total is 17 or over
        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:  # if dealer is >21 bust the dealer
                self.dealer.show()
                print("Dealer busted. Congrats!")
                return 1
            self.dealer.show()
        # compare the scores of player and dealer and score the game
        if self.dealer.check_score() == self.player.check_score():
            print("It's a Push (Tie). Better luck next time!")
        elif self.dealer.check_score() > self.player.check_score():
            print("Dealer wins. Good Game!")
        elif self.dealer.check_score() < self.player.check_score():
            print("Player wins. Congratulations!")


blackjack = Game()
blackjack.start_game()
