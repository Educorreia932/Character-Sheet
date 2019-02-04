# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:32:24 2019

@author: Asus
"""

import tkinter as tk
import CharacterSheet as character
import Plot as plot

counter = 0 
variables = []
skills = []
teste = []
 
root = tk.Tk()
root.title("Character Sheet")

label = tk.Label(root, text = "Proficiencies", font = 'Helvetica 18 bold')
label.pack()

for skill in sorted(character.Character.skills.keys()):    
    exec("var" + str(counter) + " = tk.BooleanVar()")
    exec(skill.replace(" ", "") + "= tk.Checkbutton(root, text=skill, variable = var" + str(counter) + ", command = root.destroy)")
    exec(skill.replace(" ", "") + ".pack()")
    skills.append(skill.replace(" ", "_"))
    variables.append("var" + str(counter))
    
    counter += 1

counter = 0

#character.Character.proficiencies.append(skills[counter].replace("_", " "))     

exit_button = tk.Button(root, text="Exit", width=25, command = root.destroy)
exit_button.pack()

root.mainloop()