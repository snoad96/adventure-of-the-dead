def intro():
    """ 
    This will introduce the game to the player.
    """
    print("Welcome to the Adventure of the Dead, A story based walkthrough") 
    print("Inspired by the Classic Movie: Shaun of the Dead")
    print("Will you join us on this adventure? (yes/no)")
    answer = input("").lower().strip()
    while answer not in [YES, NO]:
        print("That doesn't work... Try again")
        answer = input("").lower().strip()
    if answer in YES:
        print("We may have to kill my Stepdad")


intro()


def start_game():
    """ 
    This is the beginning of the Game, giving the player an option of 
    how they would like to start.
    """


def play_again():
    """ 
    Option to play the game again.
    """
