import threading

import pygame as pygame
import numpy as np
from src.Grid import Grid
from src.samuraiSolution import samuraiSolution


class drawingOperations:
    # grid for draw
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    sudokuGrid = [[0 for x in range(21)] for y in range(21)]
    gridsList = []
    solver = samuraiSolution(gridsList=gridsList)
    gridFor10Thread = []

    def __init__(self):
        pass

    # 1
    def readFile(self):
        try:
            file = open("sudoku.txt", "r")
            lines = file.readlines()

            count = 0
            for line in lines:
                chars = list(line)
                if count < 6:
                    for j in range(0, 9, 1):
                        if chars[j] == "*":
                            self.sudokuGrid[count][j] = 0
                        else:
                            self.sudokuGrid[count][j] = int(chars[j])
                    for j in range(9, 18, 1):
                        if chars[j] == "*":
                            self.sudokuGrid[count][j] = 0
                        else:
                            self.sudokuGrid[count][j + 3] = int(chars[j])
                    for j in range(9, 12, 1):
                        self.sudokuGrid[count][j] = -1

                if 6 <= count < 9:
                    for j in range(0, 21, 1):
                        if chars[j] == "*":
                            self.sudokuGrid[count][j] = 0
                        else:
                            self.sudokuGrid[count][j] = int(chars[j])

                if 9 <= count < 12:
                    for j in range(0, 9, 1):
                        if chars[j] == "*":
                            self.sudokuGrid[count][j] = 0
                        else:
                            self.sudokuGrid[count][j + 6] = int(chars[j])
                    for j in range(0, 6, 1):
                        self.sudokuGrid[count][j] = -1
                    for j in range(15, 21, 1):
                        self.sudokuGrid[count][j] = -1

                if 12 <= count < 15:
                    for j in range(0, 21, 1):
                        if chars[j] == "*":
                            self.sudokuGrid[count][j] = 0
                        else:
                            self.sudokuGrid[count][j] = int(chars[j])

                if 15 <= count < 21:
                    for j in range(0, 9, 1):
                        if chars[j] == "*":
                            self.sudokuGrid[count][j] = 0
                        else:
                            self.sudokuGrid[count][j] = int(chars[j])
                    for j in range(9, 18, 1):
                        if chars[j] == "*":
                            self.sudokuGrid[count][j] = 0
                        else:
                            self.sudokuGrid[count][j + 3] = int(chars[j])
                    for j in range(9, 12, 1):
                        self.sudokuGrid[count][j] = -1

                count += 1
        finally:
            file.close()

        self.gridFor10Thread = self.sudokuGrid

    # 2
    def createGridList(self):

        # create gridsList : grid1 grid2 grid3 grid4 grid5 içerir
        box1 = [[0 for x in range(9)] for y in range(9)]
        box2 = [[0 for x in range(9)] for y in range(9)]
        box3 = [[0 for x in range(9)] for y in range(9)]
        box4 = [[0 for x in range(9)] for y in range(9)]
        box5 = [[0 for x in range(9)] for y in range(9)]

        for i in range(0, 21, 1):
            for j in range(0, 21, 1):
                if self.sudokuGrid[i][j] != 0 and self.sudokuGrid[i][j] != -1:
                    if 0 <= i < 9 and 0 <= j < 9:
                        box1[i][j] = self.sudokuGrid[i][j]

                    if 0 <= i < 9 and 12 <= j < 21:
                        box2[i][j - 12] = self.sudokuGrid[i][j]

                    if 6 <= i < 15 and 6 <= j < 15:
                        box3[i - 6][j - 6] = self.sudokuGrid[i][j]

                    if 12 <= i < 21 and 0 <= j < 9:
                        box4[i - 12][j] = self.sudokuGrid[i][j]

                    if 12 <= i < 21 and 12 <= j < 21:
                        box5[i - 12][j - 12] = self.sudokuGrid[i][j]

        grid1 = Grid(box1, [[2, 2]], [2])
        grid2 = Grid(box2, [[2, 0]], [2])
        grid3 = Grid(box3, [[0, 0], [0, 2], [2, 0], [2, 2]], [0, 1, 3, 4])
        grid4 = Grid(box4, [[0, 2]], [2])
        grid5 = Grid(box5, [[0, 0]], [2])

        self.gridsList.append(grid1)
        self.gridsList.append(grid2)
        self.gridsList.append(grid3)
        self.gridsList.append(grid4)
        self.gridsList.append(grid5)

        return self.gridsList

    # tıklanınca gridsList i sudokuGridine atar
    def changeSudokuGrid(self):

        for i in range(0, 21, 1):
            for j in range(0, 21, 1):
                if 9 <= i < 12 and 6 <= j < 15:
                    self.sudokuGrid[i][j] = self.gridsList[2].grid[i - 6][j - 6]
                if 6 <= i < 15 and 9 <= j < 12:
                    self.sudokuGrid[i][j] = self.gridsList[2].grid[i - 6][j - 6]
                if 0 <= i < 9 and 0 <= j < 9:
                    self.sudokuGrid[i][j] = self.gridsList[0].grid[i][j]
                if 0 <= i < 9 and 12 <= j < 21:
                    self.sudokuGrid[i][j] = self.gridsList[1].grid[i][j - 12]
                if 12 <= i < 21 and 0 <= j < 9:
                    self.sudokuGrid[i][j] = self.gridsList[3].grid[i - 12][j]
                if 12 <= i < 21 and 12 <= j < 21:
                    self.sudokuGrid[i][j] = self.gridsList[4].grid[i - 12][j - 12]
                if (0 <= i < 6 or 15 <= i < 21) and 9 <= j < 12:
                    self.sudokuGrid[i][j] = -1
                if 9 <= i < 12 and (0 <= j < 6 or 15 <= j < 21):
                    self.sudokuGrid[i][j] = -1

        return self.sudokuGrid

    def text(self, surface, fontFace, size, x, y, text, color):
        font = pygame.font.SysFont(fontFace, size)
        text = font.render(text, True, color)
        surface.blit(text, (x, y))

    def drawLines(self, surface):
        # yatay çizgiler çizilir
        for i in range(0, 21, 1):
            for j in range(0, 21, 1):
                if self.grid[i][j] == 1:
                    if j % 3 == 0:
                        pygame.draw.line(surface, color=(128, 0, 0), start_pos=(i * 30, j * 30),
                                         end_pos=((i + 1) * 30, j * 30), width=3)
                    else:
                        pygame.draw.line(surface, color=(128, 0, 0), start_pos=(i * 30, j * 30),
                                         end_pos=((i + 1) * 30, j * 30),
                                         width=1)
        pygame.draw.line(surface, color=(128, 0, 0), start_pos=(0, 30 * 9), end_pos=(630, 30 * 9), width=3)
        pygame.draw.line(surface, color=(128, 0, 0), start_pos=(0, 30 * 15), end_pos=(630, 30 * 15), width=3)
        pygame.draw.line(surface, color=(128, 0, 0), start_pos=(0, 30 * 21), end_pos=(630, 30 * 21), width=3)
        # arada kalan boşluktaki çizgiyi silmek için üzerine beyaz çizgi çizilir
        pygame.draw.line(surface, color=(255, 255, 255), start_pos=(30 * 9, 30 * 21), end_pos=(30 * 12, 30 * 21),
                         width=3)

        # dikey çizgiler çizilir
        for i in range(0, 21, 1):
            for j in range(0, 21, 1):
                if self.grid[i][j] == 1:
                    if i % 3 == 0:
                        pygame.draw.line(surface, color=(128, 0, 0), start_pos=(i * 30, j * 30),
                                         end_pos=(i * 30, (j + 1) * 30), width=3)
                    else:
                        pygame.draw.line(surface, color=(128, 0, 0), start_pos=(i * 30, j * 30),
                                         end_pos=(i * 30, (j + 1) * 30),
                                         width=1)
        pygame.draw.line(surface, color=(128, 0, 0), start_pos=(30 * 9, 0), end_pos=(30 * 9, 630), width=3)
        pygame.draw.line(surface, color=(128, 0, 0), start_pos=(30 * 15, 0), end_pos=(30 * 15, 630), width=3)
        pygame.draw.line(surface, color=(128, 0, 0), start_pos=(30 * 21, 0), end_pos=(30 * 21, 630), width=3)
        # arada kalan boşluktaki çizgiyi silmek için üzerine beyaz çizgi çizilir
        pygame.draw.line(surface, color=(255, 255, 255), start_pos=(30 * 21, 9 * 30), end_pos=(30 * 21, 12 * 30),
                         width=3)

    def writeText(self, surface):
        for i in range(0, 21, 1):
            for j in range(0, 21, 1):
                if self.sudokuGrid[i][j] != -1 and self.sudokuGrid[i][j] != 0:
                    if j == 0:
                        self.text(surface, "arial", 30 // 2, 3, i * 30, str(self.sudokuGrid[i][j]), (0, 0, 0))
                    else:
                        self.text(surface, "arial", 30 // 2, j * 31, i * 30, str(self.sudokuGrid[i][j]), (0, 0, 0))

    def draw_board(self, board):
        pygame.init()
        background_color = (255, 255, 255)

        n = board
        screen_size = 651
        sq_sz = screen_size // n
        screen_size = n * sq_sz

        surface = pygame.display.set_mode((screen_size, screen_size))
        pygame.display.set_caption("Samurai Sudoku")

        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            surface.fill(background_color)
            self.drawLines(surface=surface)
            solver = samuraiSolution(gridsList=self.gridsList)
            self.writeText(surface)
            pygame.display.flip()
            self.gridsList = solver.gridsList
            self.threads5()
            self.changeSudokuGrid()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.flip()

        print("control 2")
        pygame.quit()

    def board1(self):
        if self.solver.solve(self.gridsList, 0, 0, 0):
            return True
        else:
            print("1: no solution")

    def board2(self):
        if self.solver.solve(self.gridsList, 1, 0, 0):
            return True
        else:
            print("2: no solution")

    def board3(self):
        if self.solver.solve(self.gridsList, 2, 0, 0):
            return True
        else:
            print("3: no solution")

    def board4(self):
        if self.solver.solve(self.gridsList, 3, 0, 0):
            return True
        else:
            print("4: no solution")

    def board5(self):
        if self.solver.solve(self.gridsList, 4, 0, 0):
            return True
        else:
            print("5: no solution")

    def board1_1(self):
        if self.solver.solve(self.gridsList, 0, 6, 0):
            return True
        else:
            print("1_1: no solution")

    def board2_2(self):
        if self.solver.solve(self.gridsList, 1, 6, 0):
            return True
        else:
            print("2_2: no solution")

    def board3_3(self):
        if self.solver.solve(self.gridsList, 2, 6, 0):
            return True
        else:
            print("3_3: no solution")

    def board4_4(self):
        if self.solver.solve(self.gridsList, 3, 6, 0):
            return True
        else:
            print("4_4: no solution")

    def board5_5(self):
        if self.solver.solve(self.gridsList, 4, 6, 0):
            return True
        else:
            print("5_5: no solution")

    def threads5(self):

        t1 = threading.Thread(target=self.board1)
        t2 = threading.Thread(target=self.board2)
        t3 = threading.Thread(target=self.board3)
        t4 = threading.Thread(target=self.board4)
        t5 = threading.Thread(target=self.board5)

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

    def threads10(self):
        t1 = threading.Thread(target=self.board1)
        t2 = threading.Thread(target=self.board2)
        t3 = threading.Thread(target=self.board3)
        t4 = threading.Thread(target=self.board4)
        t5 = threading.Thread(target=self.board5)
        t6 = threading.Thread(target=self.board1_1)
        t7 = threading.Thread(target=self.board2_2)
        t8 = threading.Thread(target=self.board3_3)
        t9 = threading.Thread(target=self.board4_4)
        t10 = threading.Thread(target=self.board5_5)

        t1.start()
        t6.start()
        t2.start()
        t7.start()
        t4.start()
        t9.start()
        t5.start()
        t10.start()
        t3.start()
        t8.start()
