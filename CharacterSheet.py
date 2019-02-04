# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 14:19:22 2019

@author: Asus
"""

def modifier(score):
    score = int(score)
    
    return (score - 10) // 2

class Character:
    index = 0
    
    proficiencies = []
    
    abilities = {"Strength": 12, "Dexterity": 16, "Constitution": 14, "Intelligence": 10, "Wisdom": 16, "Charisma": 9}        
    
    skills = {"Athletics": 0, "Acrobatics": 0, "Sleight of Hand": 0, "Stealth": 0, "Arcana": 0,  "History": 0,
              "Investigation": 0, "Nature": 0, "Religion": 0,"Animal Handling": 0, "Insight": 0, "Medicine": 0, 
              "Perception": 0, "Survival": 0, "Deception": 0, "Intimidation": 0, "Performance": 0, "Persuasion": 0}

    for skill in skills:
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
            
        if skill in proficiencies:
            skills[skill] = 10 + (modifier(abilities[ability]) + 2) * 2
        else:
            skills[skill] = 10 + modifier(abilities[ability]) * 2  
                
        index += 1