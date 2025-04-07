from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(50,50,100,100)
    win.wait_for_close()

main()
