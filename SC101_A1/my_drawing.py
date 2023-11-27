"""
File: my_drawing.py
Name: 吳宇韻
----------------------
This file uses the campy module to draw
on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Homer Jay Simpson
    The Simpsons is an American animated sitcom offering a satirical
    depiction of American Life. My favorite character is Homer,
    the head of the simpsons family with a group of 5.
    """
    window = GWindow(width=800, height=400)

    # Background color
    background = GRect(800, 400, x=0, y=0)
    window.add(background)
    background.filled = False
    background.fill_color = "skyblue"
    background.color = "skyblue"

    # Homer's quotes
    quotes = GLabel("English?\nWho needs that?\nI'm never going to England.")
    quotes.font = "-23"
    quotes.filled = True
    window.add(quotes, x=20, y=120)

    aphorist = GLabel("— Homer Jay Simpson")
    aphorist.font = "-16"
    aphorist.filled = True
    window.add(aphorist, x=118, y=146)

    # Shirt part
    shirt = GOval(350, 100, x=225, y=360)
    window.add(shirt)
    shirt.filled = False
    shirt.fill_color = "white"
    shirt.color = "white"

    # Neck parts: a combination of an oval (lower) and a rectangle (upper)
    neck_lower = GOval(120, 80, x=340, y=320)
    window.add(neck_lower)
    neck_lower.filled = False
    neck_lower.fill_color = "yellow"
    neck_lower.color = "yellow"

    neck_upper = GRect(120, 45, x=340, y=310)
    window.add(neck_upper)
    neck_upper.filled = False
    neck_upper.fill_color = "yellow"
    neck_upper.color = "yellow"

    # Hair on top of the head:
    hair_lower = GOval(100, 60, x=350, y=12)
    window.add(hair_lower)
    hair_lower.filled = False
    hair_lower.color = "black"

    hair_upper = GOval(130, 90, x=335, y=5)
    window.add(hair_upper)
    hair_upper.filled = False
    hair_upper.color = "black"

    # Hair beside the ear: a combination of 2 lines (left) and 2 lines (right)
    hair_left_short = GLine(311, 175, 304, 160)
    window.add(hair_left_short)
    hair_left_short.filled = False

    hair_left_long = GLine(295, 195, 304, 160)
    window.add(hair_left_long)
    hair_left_long.filled = False

    hair_right_short = GLine(492, 175, 498, 160)
    window.add(hair_right_short)
    hair_right_short.filled = False

    hair_right_short = GLine(507, 195, 498, 160)
    window.add(hair_right_short)
    hair_right_short.filled = False

    # Head parts：a combination of three ovals (center, left, right)
    head_center = GOval(178, 170, x=311, y=20)
    window.add(head_center)
    head_center.filled = False
    head_center.fill_color = "yellow"
    head_center.color = "yellow"

    head_left = GOval(35, 45, x=308, y=105)
    window.add(head_left)
    head_left.filled = False
    head_left.fill_color = "yellow"
    head_left.color = "yellow"

    head_right = GOval(35, 45, x=461, y=105)
    window.add(head_right)
    head_right.filled = False
    head_right.fill_color = "yellow"
    head_right.color = "yellow"

    # Ear parts
    ear_left = GOval(30, 40, x=300, y=175)
    window.add(ear_left)
    ear_left.filled = False
    ear_left.fill_color = "yellow"
    ear_left.color = "yellow"

    ear_right = GOval(30, 40, x=473, y=175)
    window.add(ear_right)
    ear_right.filled = False
    ear_right.fill_color = "yellow"
    ear_right.color = "yellow"

    # Chin part
    chin = GRect(172, 120, x=316, y=162)
    window.add(chin)
    chin.filled = False
    chin.fill_color = "yellow"
    chin.color = "yellow"

    # Mouth parts: a combination of 3 ovals (left, center, right)
    mouth_center = GOval(174, 150, x=313, y=195)
    window.add(mouth_center)
    mouth_center.filled = False
    mouth_center.fill_color = "sandybrown"
    mouth_center.color = "sandybrown"

    mouth_left = GOval(50, 50, x=307, y=242)
    window.add(mouth_left)
    mouth_left.filled = False
    mouth_left.fill_color = "sandybrown"
    mouth_left.color = "sandybrown"

    mouth_right = GOval(50, 50, x=443, y=242)
    window.add(mouth_right)
    mouth_right.filled = False
    mouth_right.fill_color = "sandybrown"
    mouth_right.color = "sandybrown"

    # Smile part: a combination of 1 oval, 1 rect and 2 lines
    # Lip part uses a rectangle to cover an oval, creating a smile
    smile = GOval(126, 70, x=337, y=235)
    smile.filled = True
    smile.fill_color = 'sandybrown'
    window.add(smile)

    smile_c = GRect(135, 45, x=334, y=225)
    smile_c.filled = True
    smile_c.fill_color = "sandybrown"
    smile_c.color = "sandybrown"
    window.add(smile_c)
    # Smile lines: on both sides of the corners of Homer's mouth
    smile_line_left = GLine(332, 276, 340, 260)
    smile_line_left.filled = False
    smile_line_left.fill_color = "black"
    window.add(smile_line_left)

    smile_line_right = GLine(459, 260, 466, 273)
    smile_line_right.filled = False
    smile_line_right.fill_color = "black"
    window.add(smile_line_right)

    # Nose parts: a combination of 2 oval and 2 lines
    # Nose part uses an oval to cover an oval, creating a nose shape
    nose = GOval(45, 45, x=379, y=176)
    window.add(nose)
    nose.filled = False
    nose.fill_color = "yellow"
    nose.color = "black"

    nose2 = GOval(44.5, 44.5, x=379, y=174)
    window.add(nose2)
    nose2.filled = False
    nose2.fill_color = "yellow"
    nose2.color = "yellow"

    nose_root_left = GLine(379, 201, 379, 180)
    window.add(nose_root_left)
    nose_root_left.filled = False

    nose_root_right = GLine(423.5, 201, 423.5, 180)
    window.add(nose_root_right)
    nose_root_right.filled = False

    # Eyes: 2 ovals for the sclera, 2 ovals for iris and pupil
    sclera_left = GOval(80, 80, x=310, y=120)
    window.add(sclera_left)
    sclera_left.filled = False
    sclera_left.fill_color = "white"
    sclera_left.color = "black"

    sclera_right = GOval(80, 80, x=412, y=120)
    window.add(sclera_right)
    sclera_right.filled = False
    sclera_right.fill_color = "white"
    sclera_right.color = "black"

    i_p_left = GOval(18, 18, x=340, y=157)
    window.add(i_p_left)
    i_p_left.filled = False
    i_p_left.fill_color = "black"

    i_p_right = GOval(18, 18, x=442, y=157)
    window.add(i_p_right)
    i_p_right.filled = False
    i_p_right.fill_color = "black"


if __name__ == '__main__':
    main()
