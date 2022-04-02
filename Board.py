import pygame
from pygame.locals import *



green = (0, 255, 0)

pygame.init()
class Board:
    def __init__(self, board) -> None:
        self.board = board

    def check_if_empty(self):
        empty = []
        for row in range(9):
            for c in range(9):
                if self.board[row][c] == 0:
                    empty.append((row, c))
        return empty
    def check_if_not_empty(self):
        not_empty = []
        for row in range(9):
            for c in range(9):
                if self.board[row][c] != 0:
                    not_empty.append((row, c))
        return not_empty
    def check_if_digit_in_empty(self, empty_positions, location: tuple):
        x = location[1]//50
        y = location[0]//50
        if (y, x) in empty_positions:
            return True
        return False



    def create_sqare(self, x, y, content=0, color = (48, 44, 45)):
        font_obj = pygame.font.Font('freesansbold.ttf', 32)
        text = font_obj.render(str(content), False, color)
        text_rect = text.get_rect(center=(x, y))

        return(text, text_rect)



    def draw_board(self):
        finished_board = []
        y = 25
        for row in self.board:
            x = 25
            for col in row:
                finished_board.append(self.create_sqare(x, y, col))
                x +=  50
            y+= 50
        return finished_board
    def update_board(self, x, y,  empty_pos, new_value=0):
        x = x//50
        y = y//50
        if (y, x) in empty_pos:
            self.board[y][x] = new_value
    def check_if_board_valid(self):
        not_empty = self.check_if_not_empty()

        not_empty_dict = {}
        for position in not_empty:
            not_empty_dict[position] = self.board[position[0]][position[1]]

        for pos, val in not_empty_dict.items():
            column = []
            for num in range(9):
                column.append(self.board[num][pos[1]])
            row = pos[0] - (pos[0]%3)
            col_pos = pos[1] - (pos[1]%3)
            square_positions = []
            for r in range(3):
                for c in range(3):
                    if self.board[r+row][c+col_pos] == val:
                        square_positions.append(val)
            if self.board[pos[0]].count(val) > 1 or column.count(val) > 1 or len(square_positions) > 1:
                return False
        return True 
