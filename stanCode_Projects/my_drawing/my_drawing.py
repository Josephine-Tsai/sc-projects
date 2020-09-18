"""
File: my_drawing.py
Name: Josephine
----------------------
This file uses campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    This function shows my favorite character - Ryan(a cute lion), and he is trying to say something.
    """
    window = GWindow(width=800, height=600, title='Ryan')
    # Head
    head = GOval(170, 160, x=120, y=200)
    head.filled = True
    head.color = 'darkorange'
    head.fill_color = 'darkorange'
    window.add(head)
    # Ears
    ear = GOval(55, 55)
    ear.filled = True
    ear.color = 'darkorange'
    ear.fill_color = 'darkorange'
    window.add(ear, x=120, y=190)
    ear2 = GOval(55, 55)
    ear2.filled = True
    ear2.color = 'darkorange'
    ear2.fill_color = 'darkorange'
    window.add(ear2, x=235, y=190)
    # Body
    body = GRect(90, 80, x=160, y=335)
    body.filled = True
    body.color = 'darkorange'
    body.fill_color = 'darkorange'
    window.add(body)
    body2 = GOval(90, 70, x=160, y=385)
    body2.filled = True
    body2.color = 'darkorange'
    body2.fill_color = 'darkorange'
    window.add(body2)
    # Hands
    hand = GOval(30, 90, x=140, y=345)
    hand.filled = True
    hand.color = 'darkorange'
    hand.fill_color = 'darkorange'
    window.add(hand)
    hand2 = GOval(30, 90, x=240, y=345)
    hand2.filled = True
    hand2.color = 'darkorange'
    hand2.fill_color = 'darkorange'
    window.add(hand2)
    # Legs
    leg = GOval(30, 70, x=170, y=420)
    leg.filled = True
    leg.color = 'darkorange'
    leg.fill_color = 'darkorange'
    window.add(leg)
    leg2 = GOval(30, 70, x=210, y=420)
    leg2.filled = True
    leg2.color = 'darkorange'
    leg2.fill_color = 'darkorange'
    window.add(leg2)
    # Eyebrows
    eyebrow = GOval(35, 5, x=150, y=255)
    eyebrow.filled = True
    eyebrow.color = 'brown'
    eyebrow.fill_color = 'brown'
    window.add(eyebrow)
    eyebrow2 = GOval(35, 5, x=225, y=255)
    eyebrow2.filled = True
    eyebrow2.color = 'brown'
    eyebrow2.fill_color = 'brown'
    window.add(eyebrow2)
    # Eyes
    eye = GOval(10, 10, x=165, y=270)
    eye.filled = True
    eye.color = 'brown'
    eye.fill_color = 'brown'
    window.add(eye)
    eye2 = GOval(10, 10, x=235, y=270)
    eye2.filled = True
    eye2.color = 'brown'
    eye2.fill_color = 'brown'
    window.add(eye2)
    # Nose
    nose_bg1 = GOval(20, 20, x=187, y=290)
    nose_bg1.filled = True
    nose_bg1.color = 'white'
    nose_bg1.fill_color = 'white'
    window.add(nose_bg1)
    nose_bg2 = GOval(20, 20, x=203, y=290)
    nose_bg2.filled = True
    nose_bg2.color = 'white'
    nose_bg2.fill_color = 'white'
    window.add(nose_bg2)
    nose = GOval(12, 10, x=199, y=286)
    nose.filled = True
    nose.color = 'brown'
    nose.fill_color = 'brown'
    window.add(nose)
    # Stomach
    stomach = GOval(55, 65, x=178, y=365)
    stomach.filled = True
    stomach.color = 'white'
    stomach.fill_color = 'white'
    window.add(stomach)
    # Dialog box
    box1 = GOval(20, 20)
    window.add(box1, x=318, y=233)
    box2 = GOval(30, 30)
    window.add(box2, x=340, y=200)
    box3 = GOval(250, 120)
    window.add(box3, x=360, y=100)
    # Words
    label = GLabel('I love stanCode!')
    label.font = '-25'
    window.add(label, 395, 180)


if __name__ == '__main__':
    main()
