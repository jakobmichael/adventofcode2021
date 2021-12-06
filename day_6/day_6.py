from sys import stdout


def init_state(filename):
    temp = []
    with open(filename) as file:
        numbers_as_str = file.readline().split(",")
        for number in numbers_as_str:
            temp.append(int(number))
    return temp


input = "day_6_input.txt"
test_input = "test_6_input.txt"

number_of_fish = list(init_state(input))


day = 0
"""
while day < 10:
    #print("\r"+day.__str__())

    upper_bound = number_of_fish.__len__()
    new_fish = []
    for i,fish in enumerate(number_of_fish):
        if(number_of_fish[i] == 0):
            number_of_fish[i] = 6
            new_fish.append(8)
        else:
            number_of_fish[i] -= 1

    for fish in new_fish:
        number_of_fish.append(fish)
    day += 1


print(number_of_fish.__len__())

"""
#Part Two

print('Part Two')

timer_list = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}


for fish in number_of_fish:
    timer_list[fish] += 1

while day < 256:
    print(timer_list)
    temp_0 = timer_list[1]
    timer_list[1] = timer_list[2]
    timer_list[2] = timer_list[3]
    timer_list[3] = timer_list[4]
    timer_list[4] = timer_list[5]
    timer_list[5] = timer_list[6]
    timer_list[6] = timer_list[7] + timer_list[0]
    timer_list[7] = timer_list[8]
    timer_list[8] = timer_list[0]
    timer_list[0] = temp_0

    day += 1


sum = 0

#print(timer_list)

for key, value in timer_list.items():
    sum += value


print(sum)

