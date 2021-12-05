class samuraiSolution:
    def __init__(self, gridsList):
        self.gridsList = gridsList

    def printing(self):
        for n in range(len(self.gridsList)):
            for i in range(len(self.gridsList[n].grid)):
                for j in range(len(self.gridsList[n].grid[i])):
                    print(self.gridsList[n].grid[i][j], end=" ")
                print()
            print("------------------")

    @staticmethod
    def isPossible(grid, r, c, n):

        for i in range(9):
            if grid[r][i] == n:
                return False
        for j in range(9):
            if grid[j][c] == n:
                return False

        rStart = int(r - r % 3)
        cStart = int(c - c % 3)
        for i in range(3):
            for j in range(3):
                if grid[i + rStart][j + cStart] == n:
                    return False

        return True

    @staticmethod
    def findIndex(grid, r, c):
        x = int(r / 3)
        y = int(c / 3)

        for i in range(len(grid.groups)):
            group = grid.groups[i]
            if x == group[0] and y == group[1]:
                return i
        return None

    @staticmethod
    def intersect(grid, r, c):
        x = int(r / 3)
        y = int(c / 3)

        for i in range(len(grid.groups)):
            group = grid.groups[i]
            if x == group[0] and y == group[1]:
                return True
        return None

    @staticmethod
    def newIndexes(gridList, n, r, c, index):
        indexes = []
        if gridList[n].groups[index][0] == 0:
            rNew = r + 6
            indexes.append(rNew)
        if gridList[n].groups[index][0] == 2:
            rNew = r % 3
            indexes.append(rNew)
        if gridList[n].groups[index][1] == 0:
            cNew = c + 6
            indexes.append(cNew)
        if gridList[n].groups[index][1] == 2:
            cNew = c % 3
            indexes.append(cNew)
        return indexes

    def solve(self, gridList, n, r, c):
        if c == 9 and r == 8:
            return True
        if c == 9:
            r = r + 1
            c = 0
        if gridList[n].grid[r][c] > 0:
            return self.solve(gridList, n, r, c+1)
        if self.intersect(gridList[n], r, c):
            index = self.findIndex(gridList[n], r, c)
            indexNew = self.newIndexes(self.gridsList, n, r, c, index)

            for num in range(1, 10, 1):
                if self.isPossible(gridList[n].grid, r, c, num):
                    gridNew = gridList[n].grids[index]
                    if self.isPossible(gridList[gridNew].grid, indexNew[0], indexNew[1], num):
                        gridList[n].grid[r][c] = num
                        gridList[gridNew].grid[indexNew[0]][indexNew[1]] = num

                        if self.solve(gridList, n, r, c+1):
                            return True
                gridList[n].grid[r][c] = 0
        for num in range(1, 10, 1):
            if self.isPossible(gridList[n].grid, r, c, num):
                gridList[n].grid[r][c] = num
                if self.solve(gridList, n, r, c + 1):
                    return True
            gridList[n].grid[r][c] = 0
