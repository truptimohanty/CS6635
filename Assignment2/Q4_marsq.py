#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Draws the starting plot. Don't change this code
def draw_initial_plot(data, x, y):

    # Draw grid and hide labels
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.set_xlim(-.5, len(x)-.5)
    ax.set_ylim(-.5, len(y)-.5)
    ax.grid(True)
    plt.xticks(np.arange(-.5,data.shape[0], step=1))
    plt.yticks(np.arange(-.5,data.shape[1], step=1))
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])

    # Add text on cells
    for i in range(len(x)):
        for j in range(len(y)):
            ax.text(i,j+.1, str(int(data[i,j])), ha='center', va='bottom', size=18)

    return fig, ax


# Load data and make range arrays for looping
data = np.load("scalars_2D.npy") # access scalar values by data[i,j]
x = np.arange(0,data.shape[0])
y = np.arange(0,data.shape[1])


fig, ax = draw_initial_plot(data, x, y)


# Draws a dot at a given point
# point - type of tuple or array with length 2: (x,y) or [x,y]
# color - string of color to draw dot - Ex: ""red", "green", "blue"
def draw_dot(point, color):
    ax.scatter(point[0], point[1], color=color)

# Draws a line from point0 to point1
# point0 - type of tuple or array with length 2: (x,y) or [x,y]
# point1 - type of tuple or array with length 2: (x,y) or [x,y]

def draw_line(point0, point1):
    x = [point0[0], point1[0]]
    y = [point0[1], point1[1]]
    ax.plot(x, y, color="#0096FF")



#-----------------------
# ASSIGNMENT STARTS HERE
#-----------------------

isovalue = 50
linear_interpolation = True # else, midpoint method

# Add colored points to identify if cells are below or above the isovalue threshold
for i in x:
    for j in y:
        # TODO Part 1
        # print(data[i,j])
        if data[i,j] > isovalue:
            color = 'red'          
        else:
            color = 'black'
        draw_dot([i,j], color=color)
        
        continue


# Draw Lines in Marching Squares - Midpoint
def march_sq_midpoint(data, i, j, isovalue):
    # TODO Part 2
    
    # case 1
    if data[i,j] > isovalue and data[i+1,j] <= isovalue and data[i+1,j+1] <= isovalue and data[i,j+1] <= isovalue :
        draw_line([i,j+0.5],[i+0.5,j])  

    #case 2 
    if data[i,j] <= isovalue and data[i+1,j] > isovalue and data[i+1,j+1] <= isovalue and data[i,j+1] <= isovalue :
        draw_line([i+0.5,j],[i+1,j+0.5])

    # case 3
    if data[i,j] > isovalue and data[i+1,j] > isovalue and data[i+1,j+1] <= isovalue and data[i,j+1] <= isovalue :
        draw_line([i,j+0.5],[i+1,j+0.5])

    
    # case 4
    if data[i,j] <= isovalue and data[i+1,j] <= isovalue and data[i+1,j+1] > isovalue and data[i,j+1] <= isovalue :
        draw_line([i+0.5,j+1],[i+1,j+0.5])

    # case 5
    if data[i,j] > isovalue and data[i+1,j] <= isovalue and data[i+1,j+1] > isovalue and data[i,j+1] <= isovalue :
        draw_line([i,j+0.5],[i+0.5,j+1])
        draw_line([i+0.5,j],[i+1,j+0.5])

    # case 6
    if data[i,j] <= isovalue and data[i+1,j] > isovalue and data[i+1,j+1] > isovalue and data[i,j+1] <= isovalue :
        draw_line([i+0.5,j+1],[i+0.5,j])
        

     # case 7
    if data[i,j] > isovalue and data[i+1,j] > isovalue and data[i+1,j+1] > isovalue and data[i,j+1] <= isovalue :
        draw_line([i,j+0.5],[i+0.5,j+1])
        

     # case 8
    if data[i,j] <= isovalue and data[i+1,j] <= isovalue and data[i+1,j+1] <= isovalue and data[i,j+1] > isovalue :
        draw_line([i,j+0.5],[i+0.5,j+1])
        

     # case 9
    if data[i,j] > isovalue and data[i+1,j] <= isovalue and data[i+1,j+1] <= isovalue and data[i,j+1] > isovalue :
        draw_line([i+0.5,j],[i+0.5,j+1]) 

     # case 10
    if data[i,j] <= isovalue and data[i+1,j] > isovalue and data[i+1,j+1] <= isovalue and data[i,j+1] > isovalue :
        draw_line([i,j+0.5],[i+0.5,j])
        draw_line([i+0.5,j+1],[i+1,j+0.5]) 

     # case 11
    if data[i,j] > isovalue and data[i+1,j] > isovalue and data[i+1,j+1] <= isovalue and data[i,j+1] > isovalue :
        draw_line([i+0.5,j+1],[i+1,j+0.5]) 

     ## case 12
    if data[i,j] <= isovalue and data[i+1,j] <= isovalue and data[i+1,j+1] > isovalue and data[i,j+1] > isovalue :
        draw_line([i,j+0.5],[i+1,j+0.5])
        

     # case 13
    if data[i,j] > isovalue and data[i+1,j] <= isovalue and data[i+1,j+1] > isovalue and data[i,j+1] > isovalue :
        draw_line([i+0.5,j],[i+1,j+0.5]) 

     # case 14
    if data[i,j] <= isovalue and data[i+1,j] > isovalue and data[i+1,j+1] > isovalue and data[i,j+1] > isovalue :
        draw_line([i,j+0.5],[i+0.5,j])
    
 

# Draw Lines in Marching Squares - Linear Interpolation
def march_sq_lin_interp(data, i, j, isovalue):
    # TODO Part 3
    v0 = data[i,j]
    v1 = data[i+1,j]
    v2 = data[i+1,j+1]
    v3 = data[i,j+1]

    # case 1
    if v0 > isovalue and v1 <= isovalue and v2 <= isovalue and v3 <= isovalue :
        t1 = (v0-isovalue)/(v0-v3)
        t2 = (v0-isovalue)/(v0-v1)
        draw_line([i,j+t1],[i+t2,j])  

    # case 2 
    if v0 <= isovalue and v1 > isovalue and v2 <= isovalue and v3 <= isovalue :
        t1 = (isovalue-v0)/(v1-v0)
        t2 = (v1-isovalue)/(v1-v2)
        draw_line([i+t1,j],[i+1,j+t2])  

    # case 3
    if v0 > isovalue and v1 > isovalue and v2 <= isovalue and v3 <= isovalue :
        t1 = (v0-isovalue)/(v0-v3)
        t2 = (v1-isovalue)/(v1-v2)
        draw_line([i,j+t1],[i+1,j+t2])

    
    # case 4
    if v0 <= isovalue and v1 <= isovalue and v2 > isovalue and v3 <= isovalue :
        t1 = (isovalue-v3)/(v2-v3)
        t2 = (isovalue-v1)/(v2-v1)
        draw_line([i+t1,j+1],[i+1,j+t2])

    # case 5
    if v0 > isovalue and v1 <= isovalue and v2 > isovalue and v3 <= isovalue :
        t1 = (v0-isovalue)/(v0-v3)
        t2 = (isovalue-v3)/(v2-v3)
        draw_line([i,j+t1],[i+t2,j+1])

        t3 = (v0-isovalue)/(v0-v1)
        t4 = (isovalue-v1)/(v2-v1)
        draw_line([i+t3,j],[i+1,j+t4])

    # case 6
    if v0 <= isovalue and v1 > isovalue and v2 > isovalue and v3 <= isovalue :
        t1 = (isovalue-v0)/(v1-v0)
        t2 = (isovalue-v3)/(v2-v3)
        draw_line([i+t1,j],[i+t2,j+1])
        

     # case 7
    if v0 >isovalue and v1 >isovalue and v2 >isovalue and v3 <= isovalue :
        t1 = (v0-isovalue)/(v0-v3)
        t2 = (isovalue-v3)/(v2-v3)
        draw_line([i,j+t1],[i+t2,j+1])
        

     # case 8
    if v0 <= isovalue and v1 <= isovalue and v2 <= isovalue and v3 > isovalue :
        t1 = (isovalue-v0)/(v3-v0)
        t2 = (v3-isovalue)/(v3-v2)
        draw_line([i,j+t1],[i+t2,j+1])
        

     # case 9
    if v0 >isovalue and v1 <= isovalue and v2 <= isovalue and v3 > isovalue :
        t1 = (v3-isovalue)/(v3-v2)
        t2 = (v0-isovalue)/(v0-v1)
        draw_line([i+t1,j+1],[i+t2,j]) 

     # case 10
    if v0 <= isovalue and v1 > isovalue and v2 <= isovalue and v3 > isovalue :
        t1 = (isovalue-v0)/(v3-v0)
        t2 = (isovalue-v0)/(v1-v0)
        draw_line([i,j+t1],[i+t2,j])

        t3 = (v3-isovalue)/(v3-v2)
        t4 = (v1-isovalue)/(v1-v2)
        draw_line([i+t3,j+1],[i+1,j+t4]) 

     # case 11
    if v0 > isovalue and v1 >isovalue and v2 <= isovalue and v3 > isovalue :
        t1 = (v3-isovalue)/(v3-v2)
        t2 = (v1-isovalue)/(v1-v2)
        draw_line([i+t1,j+1],[i+1,j+t2]) 


     # case 12
    if v0 <= isovalue and v1 <= isovalue and v2 > isovalue and v3 > isovalue :
        t1 = (isovalue-v0)/(v3-v0)
        t2 = (isovalue-v1)/(v2-v1)
        draw_line([i,j+t1],[i+1,j+t2])
        

     # case 13
    if v0 > isovalue and v1 <= isovalue and v2 > isovalue and v3 > isovalue :
        t1 = (v0-isovalue)/(v0-v1)
        t2 = (isovalue-v1)/(v2-v1)
        draw_line([i+t1,j],[i+1,j+t2]) 

    # case 14
    if v0 <= isovalue and v1 >isovalue and v2 > isovalue and v3 > isovalue :
        t1 = (isovalue-v0)/(v3-v0)
        t2 = (isovalue-v0)/(v1-v0)
        draw_line([i,j+t1],[i+t2,j])

    return


# Implement simple marching squares with midpoint approach
for i in x[0:-1]:
    for j in y[0:-1]:
        if (linear_interpolation):
            march_sq_lin_interp(data, i, j, isovalue)
            
        else:
            march_sq_midpoint(data, i, j, isovalue)

plt.show()
