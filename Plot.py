# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 23:27:56 2019

@author: Asus
"""

import CharacterSheet as character
from math import pi
import matplotlib.pyplot as plt

char = list(character.Character.skills.keys())
values = list(character.Character.skills.values())

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