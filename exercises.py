
# TicTacToe Game 

class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"{self.name} ({self.mark})"

    def get_mark(self):
        return self.mark

    def get_name(self):
        return self.name


class Board:
    def __init__(self):
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
              A   B   C
          1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
              ----------
          2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
              ----------
          3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def get_board(self):
        return self.board

    def update_board(self, position, mark):
        self.board[position] = mark

    def check_winner(self):
        b = self.board
        # Check rows
        for row in ['a', 'b', 'c']:
            if b[f'{row}1'] and (b[f'{row}1'] == b[f'{row}2'] == b[f'{row}3']):
                return b[f'{row}1']
        # Check columns
        for col in ['1', '2', '3']:
            if b[f'a{col}'] and (b[f'a{col}'] == b[f'b{col}'] == b[f'c{col}']):
                return b[f'a{col}']
        # Check diagonals
        if b['a1'] and (b['a1'] == b['b2'] == b['c3']):
            return b['a1']
        if b['a3'] and (b['a3'] == b['b2'] == b['c1']):
            return b['a3']
        return None


class Game:
    def __init__(self):
        self.players = [Player("Player 1", 'X'), Player("Player 2", 'O')]
        self.current_player_index = 0
        self.board = Board()
        self.tie = False
        self.winner = None

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while True:
            self.reset_game()
            while not self.winner and not self.tie:
                self.render()
                self.get_move()
                self.check_for_winner()
                self.check_for_tie()
                self.switch_turn()
            self.render()
            self.print_final_message()

            if not self.play_again():
                print("Thanks for playing!")
                break

    def reset_game(self):
        self.board = Board()
        self.tie = False
        self.winner = None
        self.current_player_index = 0  # Reset to Player 1

    def render(self):
        self.board.print_board()
        if self.winner:
            print(f"{self.winner.get_name()} wins the game!")
        elif self.tie:
            print("Tie game!")
        else:
            print(f"It's {self.current_player().get_name()}'s turn!")

    def current_player(self):
        return self.players[self.current_player_index]

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board.get_board() and self.board.get_board()[move] is None:
                self.board.update_board(move, self.current_player().get_mark())
                break
            else:
                print("Invalid move. Try again.")

    def check_for_winner(self):
        self.winner = self.board.check_winner()

    def check_for_tie(self):
        if all(value is not None for value in self.board.get_board().values()) and not self.winner:
            self.tie = True

    def switch_turn(self):
        self.current_player_index = 1 - self.current_player_index  # Toggle between 0 and 1

    def print_final_message(self):
        if self.winner:
            print(f"Congratulations {self.winner.get_name()}, you win!")
        elif self.tie:
            print("The game ended in a tie.")

    def play_again(self):
        while True:
            response = input("Do you want to play again? (y/n): ").lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


# To run the game
if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()