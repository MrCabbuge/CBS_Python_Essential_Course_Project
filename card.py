class Card:
    def __init__(self, value, suit):
        self.point = value
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][value - 1]  # list of values
        self.suit = "♥♦♣♠"[suit]  # list of suits using emojis

    # printing a card image by ASCII
    def visual_card(self):
        print("┌───────┐")
        print(f"| {self.value:<2}    |")
        print("|       |")
        print(f"|  {self.suit}   |")
        print("|       |")
        print(f"|    {self.value:>2} |")
        print("└───────┘")

    # function to get value of the card
    def point_price(self):
        if self.point >= 10:  # J, Q, K - return price of 10
            return 10
        elif self.point == 1:  # A - return 1 if Ace
            return 11
        return self.point  # return price corresponding to value of the card
