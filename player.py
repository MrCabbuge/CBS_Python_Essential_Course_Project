class Player:
    def __init__(self, is_dealer, deck):  # initializing a player with no cards
        self.cards = []
        self.is_dealer = is_dealer  # if the player is a dealer or not
        self.deck = deck  # give player access to the deck
        self.score = 0  # give initial score of 0

    # function that allows player to draw a card from deck and check the score of the drawn card
    def hit(self):
        self.cards.extend(self.deck.draw_card(1))
        self.check_score()
        if self.score > 21:  # check for potential blackjack
            return 1
        return 0

    # function to draw 2 cards and check for blackjack
    def deal(self):
        self.cards.extend(self.deck.draw_card(2))
        self.check_score()
        if self.score == 21:  # check for potential blackjack
            return 1
        return 0

    # adds scores of all cards and checks aces
    def check_score(self):
        aces_counter = 0
        self.score = 0
        for card in self.cards:
            if card.point_price() == 11:  # Ace default score of 11
                aces_counter += 1  # add +1 if ace is present in hand
            self.score += card.point_price()
        # if the total score of player is bigger than 21, we simulate Aces as 1
        while aces_counter != 0 and self.score > 21:
            aces_counter -= 1
            self.score -= 10  # subtract 10 from total points to simulate Aces as 1
        return self.score

    # shows cards and score of the player or dealer
    def show(self):
        if self.is_dealer:
            print("Dealer's Cards")
        else:
            print("Player's Cards")

        for i in self.cards:
            i.visual_card()

        print("Score: " + str(self.score))
