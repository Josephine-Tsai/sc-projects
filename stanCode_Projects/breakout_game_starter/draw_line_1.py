"""
File: draw_line.py
Name: Josephine
-------------------------
This file uses campy module to
draw lines and dots on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the dot
SIZE = 8

# Global variables
window = GWindow(800, 600)
dot = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(function)


def function(event):
    """
    When the user clicks the mouse, this function will make a dot at that point.
    """
    global dot
    dot = GOval(SIZE, SIZE, x=event.x - SIZE/2, y=event.y - SIZE/2)
    window.add(dot)
    onmouseclicked(draw_line)


def draw_line(event):
    """
    When the user clicks the mouse again, this function will remove the former dot and draw a line.
    """
    line = GLine(dot.x+SIZE/2, dot.y+SIZE/2, event.x, event.y)
    window.add(line)
    window.remove(dot)
    onmouseclicked(function)




if __name__ == "__main__":
    main()
