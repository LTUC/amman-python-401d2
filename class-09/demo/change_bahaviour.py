import builtins
from game_of_greed.game import Game

old_print = print

def mock_print(*args):
    old_print('New way of printing: '+args[0].upper()+'!!!!')

def change(str):
    builtins.print = mock_print # overwrite the normal print to be mock_print
    print(str)
    game = Game()
    game.play()
    builtins.print = old_print


if __name__ == "__main__":
    change('hello class')
    print('hi')
