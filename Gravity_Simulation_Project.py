# Gravity Simulation Project
# My First Python project

from visual import *
from visual.graph import *
from math import *
from About import about
from Binary_Star import binary_star_system
from Earth import earth_sun_moon
from Plot import energy_plot_system
from Control import controls


# ________________MAIN MENU__________________

while(True):
    print("*********************************")
    print("  WELCOME TO GRAVITY SIMULATOR  ")
    print("\n")
    print("  1. About this project  ")
    print("  2. Three body star system")
    print("  3. Earth-Sun-Moon system")
    print("  4. Binary star system ")
    print("  5. Two body system with energy plot ")
    print("  6. Exit")
    print("\n")
    option=int(input("  Choose your option : "))
    if(option==1):
        about()
        controls()
    elif(option==2):
        controls()
        three_body_problem()
    elif(option==3):
        controls()
        earth_sun_moon()
    elif(option==4):
        controls()
        binary_star_system()
    elif(option==5):
        controls()
        energy_plot_system()
    elif(option==6):
        break
    else:
        print("Invalid Input!")
