"""
File: bouncing_ball
Name: 吳宇韻
-------------------------
This file uses campy mouse event to punch a ball (GOval)
and make a simple animation by campy library.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball_move = False   # Initialize the ball movement to False
vy = 0
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(window)
    ball = set_up_ball()
    window.add(ball, x=START_X, y=START_Y)
    global count
    count = 0

    global ball_move, vy
    vy = 0
    ball_move = False
    onmouseclicked(bounce)

    while True:
        if count == 3:
            ball_move = False   # Stop ball movement if 'count' reach 3
            break
        else:
            if ball_move is True:
                vy += GRAVITY
                ball.move(VX, vy)
            if ball.y <= 0 or ball.y+ball.height >= window.height and vy > 0:
                # Add condition 'vy > 0' to avoid direction reversal when hitting the floor
                vy = -vy * REDUCE
            else:
                if ball.x > window.width:
                    count += 1
                    ball.move(START_X-ball.x, START_Y-ball.y)
                    ball_move = False   # Stop ball movement
            pause(DELAY)


def set_up_ball():
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    return ball


def bounce(mouse):
    global ball_move
    ball_move = True


if __name__ == "__main__":
    main()
