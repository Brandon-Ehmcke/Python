import random

##card values##
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

##Sets game to playing for while loop in logic section##
playing = True

##Class that creates the card(s)##
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit
    
##Class that creates the deck at the start of each game. Contains functions shuffle deck and append when hitting##  
class Deck:

    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)

                self.deck.append(created_card)

    def __str__(self):

        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+deck_comp

    def shuffle(self):

        random.shuffle(self.deck)

    def deal(self):

        single_card = self.deck.pop()
        return single_card

##Creates hand for dealer and player. Contains function to check for ace(1,11)##
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    ##If player hand value is greater than 21, change the ACES default of 11 to 1##
    def adjust_for_aces(self):

        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

##creates chip total(default of 100) to bet at start of game. Append or reduces chip count accordingly at loss or win##
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

#### Functions for game run####     
def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips are you betting? "))
        except:
                print('Sorry please provide a number')
        else:
            if chips.bet > chips.total:
                    print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()

def hit_or_stay(deck,hand):
    global playing ##control for the while loop in logic##

    while True:
        x = input('hit or Stay? Enter h or s: ')

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print('Player stays, Dealers turn!')
            playing = False

        else:
            print('Sorry, i did not understand that. Please enter h or s only!')
            continue
        break

def show_some(player,dealer):
    ##Show only one of the dealers cards[1]##
    print("\n Dealer's Hand: ")
    print("First card is hidden!")
    print(dealer.cards[1])

    ##Show both player cards##
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    ##show all dealer cards for end game value##
    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)

    ##show Dealers card value##
    print(f"Value of Dealer's hand is: {dealer.value}")
    
    ##show all Player cards for end game value##
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)

    ##show Players card value##
    print(f"Value of Player's hand is: {player.value}")

def player_busts(player,dealer,chips):
    print("PLAYER BUSTS!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER HAS WON!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("DEALER BUSTS, PLAYER HAS WON!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER HAS WON!")
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and player tie! PUSH')

    
####GAME LOGIC BELOW####
while True:    

    print("Welcome to Blackjack!")

    ##Create the game deck, shuffle that deck, and deal two cards to the player and dealer##
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    Dealer_hand = Hand()
    Dealer_hand.add_card(deck.deal())
    Dealer_hand.add_card(deck.deal())

    ##Player chips##
    player_chips = Chips()

    ##Prompt for bet##
    take_bet(player_chips)

    ##Show cards. Keeps one dealer card hidden##
    show_some(player_hand,Dealer_hand)

    ##logic loop##

    while playing:
        hit_or_stay(deck,player_hand)

        show_some(player_hand,Dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,Dealer_hand,player_chips)

        break

    if player_hand.value <= 21:

        while Dealer_hand.value < player_hand.value:
            hit(deck,Dealer_hand)

        if Dealer_hand.value > 21:
            dealer_busts(player_hand,Dealer_hand,player_chips)
        elif Dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,Dealer_hand,player_chips)
        elif Dealer_hand.value < player_hand.value:
            player_wins(player_hand,Dealer_hand,player_chips)
        else:
            push(player_hand,Dealer_hand)

    print(f'\n Player total chip value is currently: {player_chips.total}')
    new_game = input('Would you like to play again?: y/n')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else: 
        print('Thank you for playing!')
        break



#test_deck = Deck()
#test_deck.shuffle()