from game.cards import Player
import random

class Dealer:
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.keep_playing = True
        self.score = 300
        self.player = Player()
        self.card1 = 0
        self.card2 = 0
        

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.keep_playing:
            self.cardsobtain()
            print(f"the first card is: {self.card_name(self.card1)}")
            self.compare_guess()
            self.display_points()
            self.can_play_again()
    
    
    def cardsobtain(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.card1 = random.randint(1, 13)
        self.card2 = random.randint(1, 13)
        while self.card1 == self.card2:
            self.card2 = random.randint(1, 13)
   
    def compare_guess(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Dealer): An instance of Dealer.
        """

        self.player.user_guess()
        print(f"Next card was: {self.card_name(self.card2)}")
        if (self.card1 > self.card2 and self.player.guess == "l") or (self.card1 < self.card2 and self.player.guess == "h"):
            self.score += 100
        else:
            self.score += -75

    def card_name(self, card):
        """ Changes card from value to its face card initial
        args: card  """

        if (card < 11):
            return(str(card))
        elif(card == 11):
            return("J")
        elif(card == 11):
            return("Q")
        elif(card == 13):
            return("K")
                
            
    def display_points(self):
        """Prints the score
        """
        print(f"Score: {self.score}")

    def can_play_again(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the final score of the game
        Args:
            self (Dealer): An instance of Dealer.
        """
        if self.score <= 0:
            self.keep_playing = False
            print(f"Game over you lose and are bad at this game!")

        else:
            self.player.contituation()
        if self.player.again == "n":
            print(f"final score is {self.score}")
            self.keep_playing = False
