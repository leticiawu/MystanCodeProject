"""
File: draw_line.py
Name: 吳宇韻
-------------------------
This file uses campy mouse event to punch
holes (GOval) and draw GLine on GWindow.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 13

# Global Variable
window = GWindow()
count = 0
hole = None     # Track hole's variable
line = None     # Track line's variable

previous_x = None   # Track the previous coordinate variable of x
previous_y = None   # Track the previous coordinate variable of y


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(mouse):
    global hole, line, previous_x, previous_y

    if hole is not None:
        window.remove(hole)
        hole = None

        line = GLine(x0=previous_x, y0=previous_y, x1=mouse.x, y1=mouse.y)
        window.add(line)
        line.filled = True

    else:
        previous_x = mouse.x
        previous_y = mouse.y

        hole = GOval(SIZE, SIZE, x=mouse.x, y=mouse.y)
        hole.filled = False
        window.add(hole)

        if line is not None:
            window.remove(line)
            line = None


if __name__ == "__main__":
    main()
