"""
AUTOMATED CARD GAME UNO

Description = "Automated version of the card game Uno. 
Note = Using this as a chance to work with classes"
Name = uno.py
Author = Tola Shobande (tolajs)
"""

import random
import time
from collections import Counter

suits = ("Red", "Green", "Yellow", "Blue")
ranks = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
actions = ("Reverse", "Draw 2", "Skip", "Wild Card", "Wild Draw 4")


class Card:
    """
    Card class for creating an instance of an UNO card having a
    suit, rank and an action.
    
    * Suit - The colour of the card (R,G,B,Y)
    * Rank - The rank of the card (0-9)
    * Action cards - The card's action
    """
    def __init__(self, suit=None, rank=None, action=None):
        self.suit = suit
        self.rank = rank
        self.action = action

    def __str__(self):
        if self.rank == None and self.suit in suits:
            return self.action + " " + self.suit
        elif self.rank == None and self.suit == None:
            return self.action
        return self.rank + " " + self.suit


class Deck:
    """
    Creates an instance of a card deck. This deck has 60 cards; 40 ranked card
    and 20 action cards
    * Ranked cards - 40
    * Draw 2 cards - 4
    * Reverse cards - 4
    * Skip cards - 4
    * Wild cards - 4
    * Wild draw 4 cards - 4
    """
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit=suit, rank=rank)
                self.all_cards.append(created_card)

            for actn in actions[:3]:
                created_card = Card(suit=suit, action=actn)
                self.all_cards.append(created_card)

            for actn in actions[3:]:
                created_card = Card(action=actn)
                self.all_cards.append(created_card)

    def shuffle(self):
        """ Implementing the random module to shuffle deck """
        random.shuffle(self.all_cards)

    def deal_card(self):
        """ Deal one card from deck """
        return self.all_cards.pop()

    def refill(self,cards):
        """Refills the deck when empty"""
        self.all_cards = cards
        self.shuffle()

class Player:
    """
    Player class hold defines the player's name and cards in hand.
    Allows player to add and remove cards from the hand.
    """
    def __init__(self, name):
        self.name = name
        self.uno = False
        self.all_cards = []

    def remove_card(self, index):
        """Removes card at specified index """
        return self.all_cards.pop(index)

    def add_card(self, new_card):
        """Adds a new card to player's hand"""
        self.all_cards.append(new_card)
        
    def call_uno(self, logic):
        self.uno = logic

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} card(s)."


class Table:
    """
    Table class holds a list of cards that have been played.
    Cards are added to the table and the details (suit, rank and action)
    of the last card is stored in the class's attribute.
    """
    def __init__(self):
        self.played_cards = []
        self.suit = None
        self.rank = None
        self.action = None

    def add_card(self, new_cards):
        """Adds card to the end of played cards list"""
        self.played_cards.append(new_cards)
        self.suit = self.played_cards[-1].suit
        self.rank = self.played_cards[-1].rank
        self.action = self.played_cards[-1].action

    def top_card(self):
        """Returns the last card played on table"""
        return self.played_cards[-1]

    def change_suit(self, new_suit):
        """Changes the class's suit attribute"""
        self.suit = new_suit
    
    def clear(self):
        """
        Empty the table leaving only the last cards in list.
        Returns a list of played cards excluding the last card played.
        """
        temp_lst = self.played_cards[:-1]
        self.played_cards = [self.played_cards[-1]]
        return temp_lst

    # TODO Might remove this
    def __str__(self):
        top = self.played_cards[-1]

        if top.rank == None and (top.suit in suits):
            return f"The card in play is {top.action} {top.suit}"
        elif top.rank == None and top.suit == None:
            return f"The card in play is {top.action}"
        return f"The card in play is {top.rank} {top.suit}"


class Game:
    """
    * Game class hold the UNO game logic and defines the ability to use action cards
    and direct the flow of the game.
    * Each player is dealt 7 cards at the start of the game, followed by dealing a card
    to the table.
    * Player One starts the game by playing a card or is sanction depending on the card on 
    the table, while the other players follow suit.
    * First player to play all cards in hand wins the game.
        
    >>> self.run() Starts the game loop
    >>> self.next_turn() Controls the game flow
    >>> self.wild() Controls Wild Cards
    >>> self.check_top_card() Controls other action cards
    """
    
    def __init__(self):
        self.direction = 1
        self.turn = 0

        self.deck = Deck()
        self.table = Table()
        self.p1 = Player("One")
        self.p2 = Player("Two")
        self.p3 = Player("Three")
        self.deck.shuffle()

        for _ in range(7):
            self.p1.add_card(self.deck.deal_card())
            self.p2.add_card(self.deck.deal_card())
            self.p3.add_card(self.deck.deal_card())
        print(f"\nPlayers {self.p1.name}, {self.p2.name} and {self.p3.name} have been dealt 7 cards each")

        self.players = [self.p1, self.p2, self.p3]

    def draw_card(self, turn):
        """Deal A player one card"""
        self.players[turn].add_card(self.deck.deal_card())      

    def deal_table(self):
        """Deals a card to the table given the card is not a wild card"""
        top = self.deck.all_cards[-1].action

        if top == "Wild Card" or top == "Wild Draw 4":
            self.deck.shuffle()
            self.deal_table()
        else:
            self.table.add_card(self.deck.deal_card())

    def next_turn(self):
        """Changes the player's turn and keeps self.turn attribute in bounds"""
        self.turn += self.direction

        if self.turn >= (len(self.players)):
            self.turn = 0
        elif self.turn < (-len(self.players)):
            self.turn = -1

    def check_top_card(self):
        """
        Responds to when an action that is not a wild card is played.
        * Skips one turn for Skip cards
        * Reverses the play direction for Reverse cards
        * Deals two cards when a Draw 2 card is played
        """
        if self.table.action == "Skip":
            self.next_turn()
            
        if self.table.action == "Reverse":
            self.direction *= -1
            self.next_turn()
            
        if self.table.action == "Draw 2":
            self.draw_card(self.turn)
            self.draw_card(self.turn)
            print(f"Player {self.players[self.turn].name} has drawn 2 cards!\n")
            self.next_turn()

    def wild(self):
        """Control logic for Wild cards and Wild Draw 4 cards"""
        new_suit = ""
        max = 0
        rank_lst = []

        # Get the suits of cards in player's hand
        for i in self.players[self.turn].all_cards:
            rank_lst.append(i.suit)

        count = Counter(rank_lst)

        # If user only has wild cards or has played their last card
        if set(rank_lst) == {None} or rank_lst==[]:
            new_suit = random.choice(suits)
        else:
            # Get the most occurring suit in player's hand
            for suit, amount in count.items():
                if amount > max and suit != None:
                    new_suit = suit
                    max = amount

        # Update the table suit to the most occurring suit in player's hand
        self.table.change_suit(new_suit)
        print(f"Player {self.players[self.turn].name} requests {new_suit}\n")
        self.next_turn()

        # Draw 4 cards if action is 'Wild Draw 4'
        if self.table.action == "Wild Draw 4":
            for _ in range(4):
                self.draw_card(self.turn)
            print(f"Player {self.players[self.turn].name} has drawn 4 cards!\n")
            self.next_turn()

    def run(self):
        """Main game loop"""
        
        running = True
        # Pre-requirements
        self.deal_table()
        print(f"Card on table is {self.table.top_card()}\n")
        self.check_top_card()

        while running:
            # Check if someone has won
            for player in self.players:
                if len(player.all_cards) == 0:
                    print(f"Player {player.name} wins!!!")
                    running = False
                    break
            if not running:
                break

            # Call UNO if player has one card left
            for player in self.players:
                if len(player.all_cards) == 1 and player.uno == False:
                    player.call_uno(True)
                    print(f"Player {player.name} calls UNO!!\n")
                if len(player.all_cards) != 1:
                    player.call_uno(False)

            # Refill deck if deck is empty
            if self.deck.all_cards == []:
                self.deck.refill(self.table.clear())

            # Start new round
            for index, card in enumerate(self.players[self.turn].all_cards):
                # Check if similar suit is the available
                if card.suit == self.table.suit:
                    print(f"Player {self.players[self.turn].name} has played {card}\n")
                    self.table.add_card(self.players[self.turn].remove_card(index))

                    if card.action == "Reverse":
                        self.check_top_card()
                        break
                    if card.action == "Skip":
                        self.check_top_card()
                        self.next_turn()
                        break
                    if card.action == "Draw 2":
                        self.next_turn()
                        self.check_top_card()
                        break
                    else:
                        self.next_turn()
                        break
            else:
                for index, card in enumerate(self.players[self.turn].all_cards):
                    # Check if similar rank is available
                    if self.table.action == None: # Skips action cards with suits
                        if card.rank == self.table.rank:
                            print(
                                f"Player {self.players[self.turn].name} has played {card}\n"
                            )
                            self.table.add_card(
                                self.players[self.turn].remove_card(index)
                            )
                            self.next_turn()
                            break
                else:
                    for index, card in enumerate(self.players[self.turn].all_cards):
                        # Check if wild cards are available
                        if card.action in ["Wild Card", "Wild Draw 4"]:

                            print(
                                f"Player {self.players[self.turn].name} has played {card}"
                            )
                            self.table.add_card(
                                self.players[self.turn].remove_card(index)
                            )
                            self.wild()
                            break
                    else:
                        # Draw card from deck
                        print(
                            f"Player {self.players[self.turn].name} has drawn card from deck \n"
                        )
                        self.draw_card(self.turn)
                        self.next_turn()

            #time.sleep(2)


if __name__ == "__main__":
    game = Game()
    game.run()
