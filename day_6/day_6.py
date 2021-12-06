

def init_state(filename):
    temp = []
    with open(filename) as file:
        numbers_as_str = file.readline().split(",")
        for number in numbers_as_str:
            temp.append(int(number))
    return temp


input = "day_6_input.txt"
test_input = "test_6_input.txt"

number_of_fish = init_state(test_input)

day = 0
while day < 7:
    upper_bound = number_of_fish.__len__()
    new_fish = []
    for i in range(0, upper_bound):
        if(number_of_fish[i] == 0):
            number_of_fish[i] = 6
            new_fish.append(8)
        number_of_fish[i] -= 1

    for fish in new_fish:
        number_of_fish.append(fish)
    day += 1

print(number_of_fish)
