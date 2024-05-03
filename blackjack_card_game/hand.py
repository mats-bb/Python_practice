class Hand:
    def __init__(self, cards):
        self.cards = cards

    def get_value(self):
        value = 0
        aces = 0
        
        for card in self.cards:
            card_val = card.value
            if card_val == 1:
                aces += 1
            else:
                value += min(card_val, 10)

        if aces == 0:
            return value

        if value + 11 > 21:
            return value + aces
        
        elif aces == 1:
            return value + 11
        
        elif value + 11 + (aces - 1) <= 21:
            return value + 11 + (aces - 1)
        
        else:
            return value + aces
            
            
    def add_to_hand(self, card):
        self.cards.append(card)

    def __str__(self):
        string_cards = [str(card) for card in self.cards]
        return ", ".join(string_cards)
    


