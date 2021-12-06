from sys import stdout
import matplotlib.pyplot as plt
import numpy as np
import itertools
from shapely.geometry import LineString
from shapely.geometry import Point

# Part One
print("Solution Part One")

input = "day_5_input.txt"
test_input = "test_5_input.txt"

line_coordinates = []

with open(input) as file:
    for line in file:
        coordinates = line.rstrip().split("->")
        plot_line = []
        for str in coordinates:
            splitted_str = str.split(",")
            for i in range(0,splitted_str.__len__()):
                splitted_str[i] = int(splitted_str[i])
                
            
            plot_line.append(splitted_str)
            
        line_coordinates.append(plot_line)
     

def check_points_in_grid(x1,x2,grid):
    key_check = x1.__str__() + '/' + x2.__str__()
    for point in grid:
        key = list(point.keys())[0]
        if(key == key_check):
            point[key] += 1
           




def generate_valid_lines():
    valid = []
    for line in line_coordinates:
        x1 = line[0][0]
        y1 = line[0][1]

        x2 = line[1][0]
        y2 = line[1][1]  

        if(x1 == x2):
            points_in_line = []
            if(y1 < y2):
              
                for y in range(y1,y2+1):
                    points_in_line.append([x1, y])
            else:
               
                for y in range(y2,y1+1):
                    points_in_line.append([x1, y])

            valid.append(points_in_line)

        if(y1 == y2):
            points_in_line = []
            if(x1 < x2):
               
                for x in range(x1,x2+1):
                    points_in_line.append([x, y1])
            else:
                
                for x in range(x2,x1+1):
                    points_in_line.append([x, y1])

            valid.append(points_in_line)

    return valid



def generate_empty_grid():
    for x in range(0,max_x+1):
        for y in range(0, max_y+1):
            line_grid.append({x.__str__() +'/' +y.__str__() : 0})








def get_x_y_vals(coordinates):
    for line in coordinates:
        for points in line:
            x.append(points[0])
            y.append(points[1])

x = []
y = []

get_x_y_vals(line_coordinates)

max_x = max(x)
max_y = max(y)
line_grid = []


generate_empty_grid()

valid_lines = generate_valid_lines()


for index,line in enumerate(valid_lines):
    stdout.write("\r"+index.__str__() + " of " + valid_lines.__len__().__str__())
    stdout.write("\n") 
    for i,points in enumerate(line):
        stdout.write("\r"+i.__str__() + " of " + line.__len__().__str__())
        stdout.flush()
        check_points_in_grid(points[0],points[1],line_grid)
    stdout.write("\n") 

valid_overlaps = 0


for field in line_grid:
    key = list(field.keys())[0]
    if(field[key] > 1):
       valid_overlaps += 1



print(valid_overlaps)







       




