"""
This file will be the main file that will run the main program for the
risk ai
"""

import board as b

def main():
    game = b.board(player = ["red", "yellow", "blue", "green", "purple", "orange"])
    game.create_board()
    for i in game.find_best_areas():
        print(i)
        print("\n")


if __name__ == "__main__":
    main()