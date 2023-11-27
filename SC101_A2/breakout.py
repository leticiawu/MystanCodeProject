"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

File: breakout.py
Name: 吳宇韻

This is a breakout game which allows gamers to destroy a brick
wall by repeatedly bouncing a ball with a paddle underneath.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics, lives_label

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

# global variable
lives = 0


def main():
    graphics = BreakoutGraphics()
    global lives
    lives = 0
    graphics.ball_move = False

    while True:
        if lives == NUM_LIVES:   # Stop ball movement if 'lives' reach 3
            graphics.ball_move = False
            break
        else:
            if graphics.ball_move is True:

                # 拿速度
                dx = graphics.get_dx()
                dy = graphics.get_dy()

                # 移動
                graphics.ball.move(dx, dy)

                # 拿四個頂點的座標
                ball_left_x = graphics.ball.x
                ball_right_x = graphics.ball.x + graphics.ball.width
                ball_top_y = graphics.ball.y
                ball_bottom_y = graphics.ball.y + graphics.ball.height

                # 判斷碰撞狀況：反彈、消除
                # 消除：球的四個頂點與磚塊碰撞
                for x, y in [(ball_left_x, ball_top_y), (ball_left_x, ball_bottom_y), (ball_right_x, ball_top_y),
                             (ball_right_x, ball_bottom_y)]:
                    obj = graphics.window.get_object_at(x, y)
                    if obj is not None:
                        if obj == graphics.paddle:
                            if dy > 0:
                                graphics.set_dy(-dy)
                        else:
                            if not obj == lives_label:  # 確保label 'NUM LIVES' 不會在球碰撞時被消滅
                                graphics.window.remove(obj)
                                graphics.set_dy(-dy)
                else:
                    # 反彈：球碰到牆壁左、右邊
                    if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
                        graphics.set_dx(-dx)
                    # 反彈：球碰到牆壁上邊
                    if graphics.ball.y <= 0:
                        graphics.set_dy(-dy)
                    # 反彈：球碰到牆壁下邊
                    if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                        graphics.ball_move = False  # Stop ball movement
                        graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
                        graphics.ball.y = (graphics.window.height - graphics.ball.height) / 2
                        lives += 1

                        lives_label.text = 'NUM_LIVES ' + str(NUM_LIVES - lives)
            pause(FRAME_RATE)


# 備註區：
# 第50行 錯：if obj == graphics.paddle and dy > 0: 會走else，paddle就會被消掉
# 拆解目標：
# 目標1 碰到四面牆壁要反彈
# 目標2 碰到磚頭要把磚頭刪掉 tip: 會使用到window.get_object()..., window.remove()
# 目標3 碰到paddle要反彈


if __name__ == '__main__':
    main()
