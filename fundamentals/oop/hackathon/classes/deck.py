from . import card
import random
class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def split_deck(self):
        #get a random half of the deck
        yours = random.sample(self.cards, 26)#random sample gives us a list of same item type we give it
        opp = [] # populate with loop that does check to make sure deck halves are different
        for card in self.cards: #going through the deck 
            if(card not in yours):
                opp.append(card) #add the card to the other half
        return yours, opp
    def show_cards(self):
        for card in self.cards:
            card.card_info()

