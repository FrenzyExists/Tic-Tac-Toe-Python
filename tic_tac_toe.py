from random import randint, choice

class TicTacToe:
    def __init__(self):
        self.grid = [[" " for i in range(3)] for j in range(3)]

    def get_grid(self):
        return self.grid

    def reset_grid(self):
        self.grid = [[" " for i in range(3)] for j in range(3)]

    def replace(self, num, symbol):
        if num == "1":
            self.grid[0][0] = symbol
        elif num == "2":
            self.grid[0][1] = symbol
        elif num == "3":
            self.grid[0][2] = symbol
        elif num == "4":
            self.grid[1][0] = symbol
        elif num == "5":
            self.grid[1][1] = symbol
        elif num == "6":
            self.grid[1][2] = symbol
        elif num == "7":
            self.grid[2][0] = symbol
        elif num == "8":
            self.grid[2][1] = symbol
        elif num == "9":
            self.grid[2][2] = symbol

    def draw_grid(self):
        a = 3 * [' ' * 5]
        b = 3 * ['_' * 5]
        c = ['  ' + i + '  ' for i in self.grid[0]]
        d = ['  ' + i + '  ' for i in self.grid[1]]
        e = ['  ' + i + '  ' for i in self.grid[2]]
        print("\n".join(map("|".join, (a, c, b, a, d, b, a, e, a))))


# This snipped is made by Boris
# https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
def _lines(board):
    yield from board  # the rows
    yield [board[i][i] for i in range(len(board))]  # one of the diagonals

def lines(board):
    yield from _lines(board)
    # rotate the board 90 degrees to get the columns and the other diagonal
    yield from _lines(list(zip(*reversed(board))))

def who_won(board):
    for line in lines(board):
        if len(set(line)) == 1 and line[0] is not None:
            return line[0]
    return None  # if we got this far, there's no winner

class Player:
    def __init__(self, name):
        self.name = name
        self.coin = ""
        self.positions = []

def main():
    Game = TicTacToe()
    game_bool = True
    while True:
        print("Welcome to my version of tic tac toe. This version runs in the console. You know the rules, you'll play against a dumb "
              "cpu, and the default size of the grid is 3x3.")

        P1 = Player(input("Player 1, what's your name? "))
        P1.coin = choice(["X", "O"])
        P2 = Player("CPU")
        P2.coin = "X" if P1.coin == "O" else "O"
        while game_bool:

            print("Good! Lets start. " + P1.name + " your coin is " + P1.coin + ", and " + P2.name + " your coin is " + P2.coin)
            pos = input(P1.name + " Enter your position (1-9) ")
            
            valid  = False
            while not valid:
                print("YEEES")
                try:
                    type(int(pos))
                    if (int(pos) > 9) or (int(pos) < 1):
                      raise Exception                      
                    valid = True
                except:
                    print("Um yeah, try something else")
                    pos = input(P1.name + " Enter your position (1-9) ")
            
            # print(pos, "pos")
            print(P2.positions, "P2 pos")
            while pos in P2.positions or pos in P1.positions:
                pos = input("Position taken! Enter another position ")
            P1.positions.append(pos)
            Game.replace(pos, P1.coin)

            pos = str(randint(1, 9+1))
            while pos in P1.positions or pos in P2.positions:
                print("Position taken! Enter another position ")
                pos = str(randint(1, 9+1))
            P2.positions.append(pos)
            Game.replace(pos, P2.coin)

            Game.draw_grid()

            winner = who_won(Game.get_grid())
            if winner == P1.coin:
                game_bool = False
                print(P1.name + " you won!!!")
            elif winner == P2.coin:
                print("Well... you tried")
                game_bool = False
        repeat = input("Do you want to play again? (Yes, No)")
        if repeat.lower() == "yes":
            # Clear Game
            game_bool = True
            Game.reset_grid()         
            P1.positions.clear()
            P2.positions.clear()
            continue
        elif repeat.lower() == "no":
            break
        else:
            print("Welp, I didn't get that so, I will simply assume you want to finish. Bye!")
            break


if __name__ == "__main__":
    main()
    
