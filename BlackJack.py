###Final Product
import random

class Card:

    def __init__(self, suit, rank):
        card_vals = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 
                 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 
                 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.suit = suit
        self.rank = rank
        self.value = card_vals[rank]

    def __str__(self):
        return f'{self.value} of {self.suit}'

######################################################

class Deck:

    def __init__(self):
        self.deck = []
        self.ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 
                 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 
                 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n' +card.__str__()
            #print(card)
        return f'The deck has :' + deck_composition

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def get_card(self):
        top_card = self.deck.pop()
        return top_card
        #return self.deck.pop()

###################################################### 
deck = Deck()
deck.shuffle()
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 
                 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 
                 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Hand:
    
    '''Class that stores the cards a player is holding'''
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def add_card(self,new_card):
        #self.cards.append(card_deck.get_card())
        new_card = str(new_card)
        self.cards.append(new_card)
        return self.cards
        

    def get_tally(self, cards):
        result = []
        count = 0
        for card in self.cards: #self.cards is a card list
            #print(cards[count].split()[0])
            temp = int(cards[count].split()[0])
            result.append(temp)
            count += 1   
        return sum(result)

    def __str__(self):
        returned = ''
        for card in self.cards:
            returned += card + '\n'
        return returned

######################################################
player_hand = Hand()
comp_hand = Hand()
 #create a deck object 
deck = Deck()
#shuffle the deck
deck.shuffle()
#initialize a player_sum and comp_sum to zero
player_tally=0
comp_tally=0  
######################################################

class Blackjack:
        
    def player_deal(self, cards, tally):
        '''deals a single card and returns the new tally of all that player/'s cards'''
        player_hand.add_card(deck.get_card())
        #hand.add_card('4 of Spades')
        player_card_value = player_hand.get_tally(player_hand.cards)
        return player_card_value
    
    def comp_deal(self, cards, tally):
        comp_hand.add_card(deck.get_card())
        comp_card_value = comp_hand.get_tally(comp_hand.cards)
        return comp_card_value

    def check_bust(self, tally):
        '''returns True or False based on whether the tally is greater than 21'''
        pass
        if tally > 21:
            #print('Bust!')
            return False
        else:
            return True
        
    def check_blackjack(self, tally):
        '''returns True or False based on whether the tally is equal to 21'''
        pass
        if tally == 21:
            print('You have 21 points!')
            return False
        else:
            return True

    def player_turn(self, player_cards, player_tally):
        '''Continues to ask the user if they want to choose a new card (and then chooses a card)
        until the player busts or chooses to stop receiving more cards. It then returns the player_sum.'''
        pass
        continues = True
        while continues == True:   
            print(player_hand.cards)
            choose = input('Do you want Hit or Stand?')
            choose = choose.lower()[0]
            if choose == 'h':
                player_hand.add_card(deck.get_card())
            elif choose == 's':
                print('You stop calling for card.')
                continues = False
            self.player_tally = player_hand.get_tally(player_hand.cards)
        return self.player_tally

    def computer_turn(self, cards, comp_tally):
        '''Continues to choose a new card
        until the computer busts or the comp_sum becomes 17 or higher. It then returns the comp_sum.'''
        pass
        continues = True
        self.comp_tally = comp_tally
        while continues == True:
            #comp_hand.add_card(deck.get_card())
            #self.comp_tally = comp_hand.get_tally(comp_hand.cards)
            if self.comp_tally < 17:
                comp_hand.add_card(deck.get_card())
                self.comp_tally = comp_hand.get_tally(comp_hand.cards)
            elif self.comp_tally >= 17:
                    continues = False
                    return self.comp_tally
    
    def find_winner(self, player_tally, comp_tally):
        '''Prints Player Wins!, Computer Wins!, or Tie! based on a comparison of player_sum and comp_sum.'''
        pass
        if player_tally > 21:
            print(f'Player BUST!!! {player_tally}')
            print('Dealer Wins!')
        elif comp_tally > 21:
            print(f'Dealer BUST!!! {comp_tally}')
            print('Player Wins!')
        elif player_tally == comp_tally:
            print('Tie!!')
        elif player_tally > comp_tally:
            print('Player Wins!')
        elif player_tally < comp_tally:
            print('Computer Wins!')

######################################################
#game = Blackjack()
#print(comp_hand.cards)
#comp_hand.add_card(deck.get_card())
#print(comp_hand.cards)
#print()
######################################################
#print(player_hand.cards)
#player_hand.add_card(deck.get_card())
#print(player_hand.cards)
#print()
######################################################
#print(game.player_deal(player_hand.cards,0))
#print(player_hand.cards)
#print()
######################################################
#game.player_turn(player_hand.cards, game.player_deal)
#score_h = game.player_turn(player_hand.cards, game.player_deal)
#print(score)
#print(game.check_bust(score))
######################################################
#print(comp_hand.cards)
#score_c = game.computer_turn(comp_hand.cards, game.comp_deal)
#print(score_c)
#print(game.check_bust(score_c))
######################################################
continues = True
while continues == True:
    deck = Deck()
    deck.shuffle()
    game = Blackjack()
    

    player_hand = Hand()
    player_hand.add_card(deck.get_card())
    player_hand.add_card(deck.get_card())

    comp_hand = Hand()
    comp_hand.add_card(deck.get_card())
    comp_hand.add_card(deck.get_card())
    comp_val = comp_hand.get_tally(comp_hand.cards)

    print(f"This are Dealer's card: {comp_hand.cards} ")
    score_h = game.player_turn(player_hand.cards, game.player_deal)
    continues = game.check_bust(score_h)
    continues = game.check_blackjack(score_h)

    score_c = game.computer_turn(comp_hand.cards, comp_val)
    continues = game.check_bust(score_c)
    continues = game.check_bust(score_c)

    print(game.find_winner(score_h, score_c))
    continues = input('Will you want to start the game again? Y or N')
    if continues.lower()[0] == 'y':
        continues = True
    else:
        print('Game Ends!')
        break