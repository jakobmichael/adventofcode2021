#Part One
print("Solution Part One");

directions = [];
input = "day_2_input.txt";
testInput = "test_2_input.txt";

with open(input) as file:
    for line in file:
        directions.append(line.rstrip().split(" "));


depth = 0;
horizontal = 0;
aim  = 0;

for line in directions:
    direction = line[0];

    if(direction == "up"):
        #depth -= int(line[1]);
        aim -= int(line[1]);
    elif(direction == "down"):
        #depth += int(line[1]);
        aim += int(line[1]);
    elif(direction == "forward"):
        horizontal += int(line[1]);
        depth += aim * int(line[1]);

  

print(depth * horizontal);
