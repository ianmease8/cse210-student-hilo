import random
class Player:
    def __init__(self):
        """Class constructor
        Args: Self Player an instance of player
        """
        self.guess = None
        self.again = 0

    def user_guess(self):
        """Gets input from user as to their guess
        Args: self Player 
        """
        self.guess = input("higher or lower? [H/L]: ").lower()

    def contituation(self):
        """Gets input from user as to playing another round
        Args: self Player
        """
        self.again = input("another round? [Y/N]: ").lower()


