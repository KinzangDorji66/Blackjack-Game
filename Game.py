import random

class Card:

    def __init__(self, suit, rank, value, face_up=False):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.face_up = face_up

    def __str__(self):
        result = ""
        if self.face_up:
            result = f"{self.rank} of {self.suit}"
        else:
            result = "***Not Shown***"

        return result



class Deck:

    def __init__(self):
        self.suits = ["Diamond", "Hearts", "Club", "Spade"]
        self.cards = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}
        self.card_list = []
        
        for suit in self.suits:
            for crank, cvalue in self.cards.items():
                card = Card(suit, crank, cvalue)
                self.card_list.append(card)

    def deal(self, face_up):
        card = self.card_list[0]
        self.card_list.remove(card)
        card.face_up = face_up
        return card

    def shuffle(self):
        random.shuffle(self.card_list)

    def __str__(self):
        return f"Deck has {len(self.card_list)} cards"


class Hand:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)

    def get_score(self):
        for card in self.cards:
            if card.face_up:
                self.value += card.value
        return self.value

    def show(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        return f"{self.name}"


class Chips:

    def __init__(self):
        self.chips = 0

    def add(self, chip):
        self.chips += chip

    def __str__(self):
        return f"Total Chips:{self.chips}"
    

class Table:

    def __init__(self, deck, dealer, player):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.bets = 0


    def place_bet(self, bet):
        self.bets += bet * 2


    def player_hit(self):
        card = self.deck.deal(face_up=True)
        self.player.add_card(card)


    def dealer_hit(self):
        card = self.deck.deal(face_up=True)
        self.dealer.add_card(card)


    def deal_cards(self):
        self.deck.shuffle()

        for i in range(2):
            card = self.deck.deal(face_up=True)
            self.player.add_card(card)

        card = self.deck.deal(face_up=True)
        self.dealer.add_card(card)

        card = self.deck.deal(face_up=False)
        self.dealer.add_card(card)


    def player_bust(self):
        if self.player.get_score() > 21: 
            return True

    def dealer_bust(self):
        if self.dealer.get_score() > 21:
            return True

    def __str__(self):
        return f"Total Bets:{self.bets}"

deck = Deck()
player = Hand("Kinzang")
dealer = Hand("Computer")
table = Table(deck, dealer, player)
table.place_bet(100)
table.deal_cards()

print("\n###{}###".format(dealer))
print("Score:{}".format(dealer.get_score()))
print("Cards:")
dealer.show()
print("\n###{}###".format(player))
print("Score:{}".format(player.get_score()))
print("Cards:")
player.show()