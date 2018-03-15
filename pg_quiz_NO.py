import pyautogui as pg
import time

points = 0

# Question 1

answer = pg.prompt(
"""
Which would you rather do?

a) Rangers
b) Giants
c) Raptors
 """
)

#give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question 2

answer = pg.prompt(
"""
Which would you rather do?

a) Rangers
b) Giants
c) Raptors
 """
)

#give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question 1

answer = pg.prompt(
"""
What's your favorite city

a) New York
b) Chicago
c)LA 
"""
)

#give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
# Question 3

answer = pg.prompt(
"""
Which would you rather do?

a) Rangers
b) Giants
c) Raptors
 """
)

#give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
