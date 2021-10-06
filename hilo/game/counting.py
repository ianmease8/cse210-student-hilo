from game.cards import Cards

class Counting:
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.cards = Cards()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
        """
        self.thrower.throw_dice()
    
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        points = self.cards.pointss()
        self.score += points
    
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.
        Args:
            self (Director): An instance of Director.
        """
        print(f"\n next card was: {self.thrower.dice}")
        print(f"Your score is: {self.score}")
        if self.thrower.can_throw():
            choice = input("keep playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False