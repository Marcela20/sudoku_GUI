import pygame
import sys
from Board import Board
import csv
import time
from Sudoku import Sudoku
import copy


dis_width = 450
dis_height = 450
window_size = (dis_width, dis_height)
window = pygame.display.set_mode(window_size, 0, 32)
pygame.display.set_caption("sudoku")
pygame.init()
running = True
board_1 = [[1, 0, 0, 3, 4, 5, 0, 7, 9],
        [3, 4, 5, 6, 7, 9, 8, 1, 2],
        [6, 7, 9, 1, 2, 8, 5, 3, 4,],
        [2, 1, 3, 4, 6, 7, 9, 8, 5],
        [4, 5, 6, 8, 9, 1, 7, 2, 3],
        [7, 9, 0, 5, 3, 2, 4, 6, 1],
        [8, 3, 1, 9, 5, 6, 2, 4, 7],
        [5, 2, 4, 7, 8, 3, 1, 9, 6],
        [9, 6, 7, 2, 1, 4, 3, 5, 8]]

board_2 =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def create_boards_from_csv(file):
    with open(file, 'r') as file_to_process:
        csv_reader = csv.reader(file_to_process, delimiter=',')
        boards = []
        b = (list(csv_reader))
        a = len(b)
        for elem in range(0, a, 9):
            board = []

            if elem < a-7:
                for r in range(elem, elem+9):
                    board.append(b[r])
                if len(boards) >= 1:
                    if boards[-1] != board:
                        boards.append(board)
                else:

                    boards.append(board)
        return boards

boards = create_boards_from_csv('results.csv')
pause = False
wait = False
user_digit = 0
can_enter_number = False

board_2_copy = copy.deepcopy(board_2)
result = Sudoku(board_2)
result.solve_sudku()


while running:

    if not wait:
        b = Board(board_2_copy)
        empty_positions = b.check_if_empty() 
        window.fill([0,0,0])
        wait = True

    if not pause:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            board = b.draw_board()
            for square in board:
                if b.check_if_digit_in_empty(empty_positions, (square[1].y,square[1].x)):
                    pygame.draw.rect(window,(230, 209, 215),[square[1].x-15, square[1].y-10, 48, 48])
                else:
                    pygame.draw.rect(window,(255, 255, 255),[square[1].x-15, square[1].y-10, 48, 48])

                window.blit(square[0],square[1])
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_0 = mouse[0]
                    mouse_1 = mouse[1]
                    can_enter_number = True
                if can_enter_number:
                    if square[1].x-15<= mouse_0<=( square[1].x)-15+48 and square[1].y-10 <= mouse_1<=( square[1].y-10)+48:
                        if b.check_if_digit_in_empty(empty_positions, (mouse_1, mouse_0)):
                            pygame.draw.rect(window,(240, 239, 204),[square[1].x-15, square[1].y-10, 48, 48])
                        if event.type == pygame.KEYDOWN:
                            try:
                                user_digit = int(event.unicode)
                                b.update_board(mouse[0], mouse[1], empty_positions, new_value = user_digit)

                                is_valid = b.check_if_board_valid()
                                if not is_valid:
                                    pygame.draw.rect(window,(140, 49, 55),[square[1].x-15, square[1].y-10, 48, 48])
                                    pygame.display.update()
                                    time.sleep(0.5)
                                    user_digit = 0
                                    b.update_board(mouse[0], mouse[1], empty_positions, new_value = user_digit)
                            except ValueError:
                                pass
                            can_enter_number = False

                            user_digit = 0


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    for try_board in boards:
                        
                        b = Board(try_board)
                        board = b.draw_board()

                        for square in board:
                            if b.check_if_digit_in_empty(empty_positions, (square[1].y,square[1].x)):
                                pygame.draw.rect(window,(230, 209, 215),[square[1].x-15, square[1].y-10, 48, 48])
                            else:
                                pygame.draw.rect(window,(255, 255, 255),[square[1].x-15, square[1].y-10, 48, 48])
                            # pygame.draw.rect(window,(255, 255, 255),[square[1].x-15, square[1].y-10, 48, 48])
                            window.blit(square[0],square[1])
                            pygame.display.update()

                        pause = True
                    
                

                    
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()




