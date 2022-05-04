from classes.deck import Deck
import random

bicycle = Deck()

#bicycle.show_cards()
##game rules
#rules for WAR
# player A and player B
#
#deck is divided into two between players 26 cards each
# each player turns up a card at the same time
# player with higher card, takes both cards then adds them to their deck
# 
#if cards are same rank, refer to rules and implement later

##start the game by dealing our deck in half to player A and player b
#generate two different arrays which will be player A's half, and player B's half

#player_1_deck = random.choice()
player_1_pile = []##for keeping cards during rounds
player_2_pile = []


# make players draw and compare in each round
# winner adds cards to their respective points pile

class Player:
    def __init__(self):
        self.deck = []
        self.point_pile = []
        self.card = "temp-card"
    def draw(self):
        self.card = random.choice(self.deck)
        self.deck.remove(self.card)
        return self.card
    def win(self, card1, card2):
        self.point_pile.append(card1)
        self.point_pile.append(card2)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.card1 = "temp-card"
        self.card2 = "temp-card"

    def start_game(self,p1,p2):##deals the deck to p1 and p2
        [p1.deck, p2.deck ] = self.deck.split_deck()

    def game_round(self,p1,p2):
        #players touch and remove the cards from their deck
        self.card1 = p1.draw()
        self.card2 = p2.draw()
        #players compare
        if self.card1.point_val > self.card2.point_val:
            print(f"Player 1 wins this round by beating a {self.card2.string_val} with a {self.card1.string_val}")
            p1.win(self.card1,self.card2)  
        else:
            print(f"Player 2 wins this round by beating a {self.card1.string_val} with a {self.card2.string_val}")
            p2.win(self.card1,self.card2)
    
    def play_game(self,p1,p2):
        while p1.deck and p2.deck:
            self.game_round(p1,p2) 
        print(f"player 1 has {len(p1.point_pile)} amount of cards and player 2 has {len(p2.point_pile)} amount of cards")

#we created two players
thing1 = Player()
thing2 = Player()
#create our game, war
war = Game()
#start the game
war.start_game(thing1,thing2)
#play game until completion
war.play_game(thing1,thing2)

