# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:32:24 2019

@author: Asus
"""

import tkinter as tk
import CharacterSheet as character
import Plot as plot

counter = 0 
 
root = tk.Tk()
root.title("Character Sheet")

label = tk.Label(root, text = "Proficiencies", font = 'Helvetica 18 bold')
label.pack()

for skill in sorted(character.Character.skills.keys()):    
    var0 = tk.IntVar()
    a = tk.Checkbutton(root, text=skill, variable = var0)
    a.pack()
    
button = tk.Button(root, text="Exit", width=25, command=root.destroy)
button.pack()

root.mainloop()