#Part One
print("Solution Part One: ");

depths = [];
input = "day_1_input.txt";
testInput = "test_1_input.txt";

with open(input) as file:
    for line in file:
        depths.append(line.rstrip());



count1 = 0;
previousDepth = depths[0];
for i in range(0, depths.__len__()):
    if(depths[i] >= previousDepth):
        count1 += 1;
   
    previousDepth = depths[i];

print(count1);

#Part Two
print("Solution Part Two: ");

count2 = 0;
previousSum = int(depths[0]) + int(depths[1]) + int(depths[2]);

for i in range(0, depths.__len__() - 2):
    nextSum = int(depths[i]) + int(depths[i+1]) + int(depths[i+2]);
    #print(previousSum);
    if(nextSum > previousSum):
        count2 += 1;
    previousSum = nextSum;

print(count2);


