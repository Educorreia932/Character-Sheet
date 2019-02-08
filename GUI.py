# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:32:24 2019

@author: Asus
"""

import tkinter as tk       
from math import pi
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

#Functions
def modifier(score):
    score = int(score)
    
    return (score - 10) // 2

def addSkill():
    if var0.get() == 1:
        Character.proficiencies.append(skills[0].replace('_', ' '))
    if var1.get() == 1:
        Character.proficiencies.append(skills[1].replace('_', ' '))
    if var2.get() == 1:
        Character.proficiencies.append(skills[2].replace('_', ' '))
    if var3.get() == 1:
        Character.proficiencies.append(skills[3].replace('_', ' '))
    if var4.get() == 1:
        Character.proficiencies.append(skills[4].replace('_', ' '))
    if var5.get() == 1:
        Character.proficiencies.append(skills[5].replace('_', ' '))
    if var6.get() == 1:
        Character.proficiencies.append(skills[6].replace('_', ' '))
    if var7.get() == 1:
        Character.proficiencies.append(skills[7].replace('_', ' '))
    if var8.get() == 1:
        Character.proficiencies.append(skills[8].replace('_', ' '))
    if var9.get() == 1:
        Character.proficiencies.append(skills[9].replace('_', ' '))
    if var10.get() == 1:
        Character.proficiencies.append(skills[10].replace('_', ' '))
    if var11.get() == 1:
        Character.proficiencies.append(skills[11].replace('_', ' '))
    if var12.get() == 1:
        Character.proficiencies.append(skills[12].replace('_', ' '))
    if var13.get() == 1:
        Character.proficiencies.append(skills[13].replace('_', ' '))
    if var14.get() == 1:
        Character.proficiencies.append(skills[14].replace('_', ' '))
    if var15.get() == 1:
        Character.proficiencies.append(skills[15].replace('_', ' '))
    if var16.get() == 1:
        Character.proficiencies.append(skills[16].replace('_', ' '))
    if var17.get() == 1:
        Character.proficiencies.append(skills[17].replace('_', ' '))
        
def Exit():
    Character.abilities["Strength"] = Strength.get()
    Character.abilities["Dexterity"] = Dexterity.get()
    Character.abilities["Constitution"] = Constitution.get()
    Character.abilities["Intelligence"] = Intelligence.get()
    Character.abilities["Wisdom"] = Wisdom.get()
    Character.abilities["Charisma"] = Charisma.get()
    Character.bonus = int(proficiency.get())
    root.destroy()
        
class Character:   
    proficiencies = []
    
    bonus = 0
    
    abilities = {"Strength": 10, "Dexterity": 10, "Constitution": 10, "Intelligence": 10, "Wisdom": 10, "Charisma": 10}        
    
    skills = {"Athletics": 0, "Acrobatics": 0, "Sleight of Hand": 0, "Stealth": 0, "Arcana": 0,  "History": 0,
              "Investigation": 0, "Nature": 0, "Religion": 0,"Animal Handling": 0, "Insight": 0, "Medicine": 0, 
              "Perception": 0, "Survival": 0, "Deception": 0, "Intimidation": 0, "Performance": 0, "Persuasion": 0}

counter = 0
variables = []
skills = []

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Character Sheet")

label3 = tk.Label(root, text = "Proficiency Bonus", font = "Helvetica 18 bold")
label3.pack()
label3.place(relx = 0.469, rely = 0)

bonus = tk.StringVar()
proficiency = tk.Entry(root, bd = 2, text = "proficiency", textvariable = bonus)
proficiency.pack()
proficiency.place(relx = 0.5, rely = 0.07)

label1 = tk.Label(root, text = "Abilities", font = 'Helvetica 18 bold')
label1.pack()
label1.place(relx = 0.258, rely = 0)

relation = 0.1
relation_two = 0.07

for ability in Character.abilities.keys():
    exec("label" + ability + "= tk.Label(root, text = ability)")
    exec("label" + ability + ".pack()")
    exec("label" + ability + ".place(relx = '0.275', rely =" + str(relation_two) + ")")
    exec("num" + str(counter) + "= tk.StringVar()")
    exec(ability + "= tk.Entry(root, bd = 2,text = ability, textvariable = num" + str(counter) + ")")
    exec(ability + ".pack()")
    exec(ability + ".place(relx = '0.25', rely =" + str(relation) + ")")
    
    relation += 0.1
    relation_two += 0.1

label2 = tk.Label(root, text = "Proficiencies", font = 'Helvetica 18 bold')
label2.pack()
label2.place(relx = "0.75", rely = "0")

counter = 0
relation = 0.05

for skill in sorted(Character.skills.keys()): 
    skills.append(skill.replace(" ", "_"))
    exec("var" + str(counter) + " = tk.IntVar()")
    exec(skill.replace(" ", "") + "= tk.Checkbutton(root, text = skill, variable = var" + str(counter) + ", command = addSkill)")
    exec(skill.replace(" ", "") + ".pack()") 
    exec(skill.replace(" ", "") + ".place(relx = '0.75', rely =" + str(relation) + ")")
    relation += 0.05
    variables.append("var" + str(counter))
        
    counter += 1

exit_button = tk.Button(root, text="Submit", width=25, command = Exit)
exit_button.pack()
exit_button.place(relx= 0.5, rely = 0.5)

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
            Character.skills[skill] = modifier(Character.abilities[ability]) + Character.bonus
        else:
            Character.skills[skill] = modifier(Character.abilities[ability])
            
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
plt.yticks([-9, -6, -3, 0, 3, 6, 9], ["-9", "-6", "-3", "0", "+3", "+6", "+9"])

# Plot data
ax.plot(x_as, values, linewidth=0, linestyle='solid', zorder=3)

# Fill area
ax.fill(x_as, values, 'b', alpha=0.3)

# Set axes limits
plt.ylim(-9, 9)

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

    ax.text(angle_rad, 10 + distance_ax, char[i], size = 10, horizontalalignment = ha, verticalalignment = "center")

plt.show()
