"""
File: bouncing_ball.py
Name: Josephine
-------------------------
This file shows a simple animation of the bouncing ball by campy library.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 100

# Global variable (the 800*500 window)
window = GWindow(800, 500, title='bouncing_ball.py')
# Global variable (the ball)
ball = GOval(SIZE, SIZE)
# Global variable (counting the roll of the bouncing ball animation)
roll = 1


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)
    onmouseclicked(ball_start)


def ball_start(event):
    """
    When the user clicks the mouse, this function will start displaying the bouncing ball animation.
    Also, this function will not be affected by clicking the mouse while the ball is bouncing.
    (It can only play three times, after three times, the ball will get back to the original place.)
    """
    global roll
    # This condition is a gate which can limit the 'onmouseclicked' function.
    if ball.x == START_X and ball.y == START_Y and roll <= 3:
        vy = 4
        while True:
            vy += GRAVITY
            ball.move(VX, vy)
            pause(DELAY)
            # When the ball touches the ground, it will change its direction.
            if ball.y+ball.height >= window.height or vy == 0:
                vy = -vy*REDUCE
            # When the ball runs out the window, the while loop will stop working.
            elif ball.x > window.width:
                roll += 1
                break
        # Put the ball to the original place.
        window.add(ball, START_X, START_Y)



if __name__ == "__main__":
    main()
