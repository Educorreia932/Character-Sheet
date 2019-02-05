# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:32:24 2019

@author: Asus
"""

import tkinter as tk
from math import pi
import matplotlib.pyplot as plt

def modifier(score):
    score = int(score)
    
    return (score - 10) // 2

class Character:   
    proficiencies = []
    
    abilities = {"Strength": 12, "Dexterity": 16, "Constitution": 14, "Intelligence": 10, "Wisdom": 16, "Charisma": 9}        
    
    skills = {"Athletics": 0, "Acrobatics": 0, "Sleight of Hand": 0, "Stealth": 0, "Arcana": 0,  "History": 0,
              "Investigation": 0, "Nature": 0, "Religion": 0,"Animal Handling": 0, "Insight": 0, "Medicine": 0, 
              "Perception": 0, "Survival": 0, "Deception": 0, "Intimidation": 0, "Performance": 0, "Persuasion": 0}

counter = 0 
variables = []
skills = []
teste = []
 
root = tk.Tk()
root.title("Character Sheet")

label = tk.Label(root, text = "Proficiencies", font = 'Helvetica 18 bold')
label.pack()

def addSkill():
    if exec("var" + str(counter) + ".get() == 1"):
        Character.proficiencies.append(skills[counter].replace('_', ' '))
    elif exec("var" + str(counter) + ".get() == 0"):
        pass

for skill in sorted(Character.skills.keys()): 
    skills.append(skill.replace(" ", "_"))
    exec("var" + str(counter) + " = tk.IntVar()")
    exec(skill.replace(" ", "") + "= tk.Checkbutton(root, text=skill, variable = var" + str(counter) + ", command = addSkill)")
    exec(skill.replace(" ", "") + ".pack()")    
    variables.append("var" + str(counter))
        
    counter += 1

counter = 0

exit_button = tk.Button(root, text="Exit", width=25, command = root.destroy)
exit_button.pack()

root.mainloop()

index = 0

for skill in Character.skills:
        if index == 0:
            ability = "Strength"
                
        elif index >= 1 and index <= 3:
            ability = "Dexterity"
            
        elif index >= 4 and index <= 8:
            ability = "Intelligence"
                
        elif index >= 9 and index <= 13:
            ability = "Wisdom"
                
        elif index >= 14:
            ability = "Charisma"            
            
        if skill in Character.proficiencies:
            Character.skills[skill] = 10 + (modifier(Character.abilities[ability]) + 2) * 2
        else:
            Character.skills[skill] = 10 + modifier(Character.abilities[ability]) * 2  
            
        index += 1    
        
char = list(Character.skills.keys())
values = list(Character.skills.values())

N = len(char)

x_as = [n / float(N) * 2 * pi for n in range(N)]

values += values[:1]
x_as += x_as[:1]

# Set color of axes
plt.rc('axes', linewidth = 0.5, edgecolor="#888888")
      
# Create polar plot       
ax = plt.subplot(111, polar = True)

# Set clockwise rotation. That is:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Set position of y-labels
ax.set_rlabel_position(0)

# Set color and linestyle of grid
ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)

# Set number of radial axes and remove labels
plt.xticks(x_as[:-1], [])

# Set yticks
plt.yticks([4, 8, 12, 16, 20], ["4", "8", "12", "16", "20"])

# Plot data
ax.plot(x_as, values, linewidth=0, linestyle='solid', zorder=3)

# Fill area
ax.fill(x_as, values, 'b', alpha=0.3)

# Set axes limits
plt.ylim(0, 20)

# Draw ytick labels to make sure they fit properly
for i in range(N):
    angle_rad = i / float(N) * 2 * pi

    if angle_rad == 0:
        ha, distance_ax = "center", 10
    elif 0 < angle_rad < pi:
        ha, distance_ax = "left", 1
    elif angle_rad == pi:
        ha, distance_ax = "center", 1
    else:
        ha, distance_ax = "right", 1

    ax.text(angle_rad, 20 + distance_ax, char[i], size = 10, horizontalalignment = ha, verticalalignment = "center")  