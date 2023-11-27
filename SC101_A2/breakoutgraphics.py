"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

File: breakoutgraphics.py
Name: 吳宇韻

This is a breakout game which allows gamers to destroy a brick
wall by repeatedly bouncing a ball with a paddle underneath.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10         # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # 改7 Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


# global area
previous_x = 0
previous_y = 0
paddle = 10
lives_label = GLabel('NUM_LIVES= '+str(3))


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.window.add(self.paddle, x=(window_width - paddle_width)/2, y=window_height - paddle_offset)
        self.paddle.filled = True

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.window.add(self.ball, x=(window_width - ball_radius) / 2, y=(window_height - ball_radius) / 2)
        self.ball.filled = True
        self.ball.start_x = (window_width - ball_radius) / 2
        self.ball.start_y = (window_height - ball_radius) / 2

        # Create a lives board
        lives_label.font = '-10'
        self.window.add(lives_label, x=10, y=window_height - lives_label.height)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.handle_paddle_position)
        onmouseclicked(self.game_start)
        self.ball_move = False

        # Draw bricks
        global previous_x, previous_y
        previous_x = 0
        previous_y = BRICK_OFFSET

        for i in range(0, BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(brick_width, brick_height, x=previous_x, y=previous_y)
                self.window.add(self.brick)
                self.brick.filled = True

                if (i//2) % 5 == 0:
                    self.brick.fill_color = "red"
                    self.brick.color = "red"

                elif (i//2) % 5 == 1:
                    self.brick.fill_color = "orange"
                    self.brick.color = "orange"

                elif (i//2) % 5 == 2:
                    self.brick.fill_color = "yellow"
                    self.brick.color = "yellow"

                elif (i//2) % 5 == 3:
                    self.brick.fill_color = "green"
                    self.brick.color = "green"

                elif (i//2) % 5 == 4:
                    self.brick.fill_color = "blue"
                    self.brick.color = "blue"

                previous_x = previous_x + brick_width + brick_spacing

            previous_x = 0
            previous_y = previous_y + brick_height + brick_spacing

    # set_up_handle_position
    def handle_paddle_position(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width / 2
        self.paddle.y = self.window.height - PADDLE_OFFSET

        min_x = 0
        max_x = self.window.width - self.paddle.width
        if self.paddle.x < min_x:
            self.paddle.x = min_x   # Avoid the paddle from going beyond the left side of the window.
        elif self.paddle.x > max_x:
            self.paddle.x = max_x   # Avoid the paddle from going beyond the right side of the window.

    # set_up_first click, event 代表 mouseclick影響的事件,如果有人想要把每個命名都非常清楚可分開命名，為style無好壞之分
    def game_start(self, mouse):
        if not self.ball_move:  # --=+
            self.ball_move = True   # make the ball move
            self.__dx = random.randint(1, MAX_X_SPEED)     # game start時球的速度
            self.__dy = INITIAL_Y_SPEED     # 測試對錯可以透過改變數值例如0 1或很大很小的數值去run檢驗是否錯誤
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):   # user端拿水平速度
        return self.__dx

    def get_dy(self):   # user端拿垂直速度
        return self.__dy

    def set_dx(self, new_dx):   # user端給ㄧ個新水平速度的值，然後讓coder端的速度去做改變
        self.__dx = new_dx     # 速度始終是__dx. 從user端__dx來改得到的新速度

    def set_dy(self, new_dy):  # user端給ㄧ個新水平速度的值，然後讓coder端的速度去做改變
        self.__dy = new_dy
