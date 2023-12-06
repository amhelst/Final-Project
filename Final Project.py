# Amhel Sosa
# 00290925
# CIS 153
# Final Project

# This program is a Dominican Republic Province Quiz Game. It will display an image of a DR map and will prompt the user to type a province.
# It will ask for a province name 31 times. One time per province. Once it ends it will create a CSV file with the provinces the user didn't guess correctly for them to learn.

import turtle
import csv

# Set up screen with map
screen = turtle.Screen()
screen.title("Dominican Republic Province Guessing Quiz")
dr_map = "dominican.gif"
screen.setup(width=1020, height=720)
screen.bgpic(dr_map)

# Read provinces from CSV file using the csv module
provinces_data = []
with open("provinces.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        provinces_data.append(row)

name = turtle.Turtle()
name.penup()
name.hideturtle()

correct_guess = []

while len(correct_guess) < 31:
    guess_province = screen.textinput(title=f"{len(correct_guess)}/32", prompt="Name one province")
    if guess_province == "Exit":
        missed_provinces = [province for province in provinces_data if province['Province'] not in correct_guess]
        with open("provinces_to_learn.csv", "w", newline="") as csvfile:
            fieldnames = ['sProvince']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for province in missed_provinces:
                writer.writerow(province)
        break

    if guess_province in [province['Province'] for province in provinces_data]:
        correct_guess.append(guess_province)
        index = [province['Province'] for province in provinces_data].index(guess_province)
        new_x = int(provinces_data[index]['x'])
        new_y = int(provinces_data[index]['y'])
        name.goto(new_x, new_y)
        name.write(f"{guess_province}", font=("Arial", 9, "bold"))

turtle.done()





                   

                   
            
        
    
