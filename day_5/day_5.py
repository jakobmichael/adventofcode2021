# Part One
print("Solution Part One")

import matplotlib.pyplot as plt
import numpy as np
import itertools
from shapely.geometry import LineString
from shapely.geometry import Point


input = "day_5_input.txt"
test_input = "test_5_input.txt"

line_coordinates = []

with open(test_input) as file:
    for line in file:
        coordinates = line.rstrip().split("->")
        plot_line = []
        for str in coordinates:
            splitted_str = str.split(",")
            for i in range(0,splitted_str.__len__()):
                splitted_str[i] = int(splitted_str[i])
                
            
            plot_line.append(splitted_str)
            
        line_coordinates.append(plot_line)
        
 




x = []
y = []


def get_x_y_vals(coordinates):
    for line in coordinates:
        for points in line:
            x.append(points[0])
            y.append(points[1])




def connectpoints(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')


def draw():
    a = 0
    b = 1
    for line in line_coordinates:
        connectpoints(x,y,a,b)
        a += 2
        b += 2


intersections = []

def get_intersection(line_1, line_2):
    return(line_1.intersection(line_2))

 




get_x_y_vals(line_coordinates)
plt.plot(x,y, "ro")
#draw()
#plt.grid()
#plt.show()

for i in range(0, line_coordinates.__len__()-2):
    for j in range(i+1, line_coordinates.__len__()-1):
        line1 = LineString([(line_coordinates[i][0][0],line_coordinates[i][0][1]), (line_coordinates[i][1][0],line_coordinates[i][1][1])])
        line2 = LineString([(line_coordinates[j][0][0],line_coordinates[j][0][1]), (line_coordinates[j][1][0],line_coordinates[j][1][1])])

        print(line1.coords[0])

        intersection = get_intersection(line1, line2)
       


print(intersections)



