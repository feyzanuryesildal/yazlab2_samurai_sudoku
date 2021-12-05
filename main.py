import threading
import time

from Cython import inline
from matplotlib import pyplot as plt

sure_baslangici= time.time()
from src.drawingOperations import drawingOperations
from src.samuraiSolution import samuraiSolution

draw = drawingOperations()
draw.readFile()
gridsList = draw.createGridList()
draw.draw_board(21)
sure_bitisi = time.time() -sure_baslangici
print(' geçen süre: ')
print(sure_bitisi)
plt.plot(sure_bitisi)
plt.ylabel("Geçen Süre")
plt.xlabel("Değerler")
plt.show()