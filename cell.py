from line import Line
from point import Point
class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return 
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1,y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        
        if self.has_top_wall:
            line = Line(Point(x1,y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2,y2))
            self._win.draw_line(line, "white")
        
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo = False):

        side1 = abs(self._x2 - self._x1)
        center1_x = self._x1 + side1 / 2
        center1_y = self._y1 + side1 / 2

        side2 = abs(to_cell._x2 - to_cell._x1)
        center2_x = to_cell._x1 + side2 / 2
        center2_y = to_cell._y1 + side2 / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(center1_x,center1_y), Point(center2_x, center2_y))
        self._win.draw_line(line, fill_color)
        


        

