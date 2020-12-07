class Game:
    def __init__(self, roller=None):
        self.roller = roller

    # @staticmethod
    # def print_roll(roll):
    #     print(','.join([str(i) for i in roll]))

    def play(self):
        print('Welcome to Game of Greed')
        res = input('Wanna play?')
        if res == 'n':
            print('OK. Maybe another time')
        elif res == 'y':
            round = 1
            remaining_dice = 6
            score = 0
            print(f'Starting round {round}')
            print(f'Rolling {remaining_dice} dice...')
            roll = self.roller(remaining_dice)
            # Game.print_roll(roll)
            print(','.join([str(i) for i in roll]))
            dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
            if dice_to_keep == 'q':
                print(f'Total score is {score} points')
                print(f'Thanks for playing. You earned {score} points')

if __name__ == '__main__':
    game = Game()
    game.play()
