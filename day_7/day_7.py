def init_state(filename):
    temp = []
    with open(filename) as file:
        numbers_as_str = file.readline().split(",")
        for number in numbers_as_str:
            temp.append(int(number))
    return temp


def get_fuel_for_change():
    pos = 0
    while pos < max_position:
        needed_fuel[pos] = 0
        for index, position in enumerate(crab_positions):
            if position > pos:
                needed_fuel[pos] += position - pos
            else:
                needed_fuel[pos] += pos - position
        pos += 1


def get_minimum_fuel(fuel_list):
    min_fuel = max_position * len(fuel_list)

    for key, value in fuel_list.items():
        if(value < min_fuel):
            min_fuel = value
    return min_fuel


def get_next_fuel_for_change():
    pos = 0
    while pos <= max_position:
        needed_fuel[pos] = 0
        for index, position in enumerate(crab_positions):
            fuel = 0
            if position > pos:
                fuel = position - pos
            else:
                fuel = pos - position

            add_steps = 0
            for n in range(0, fuel+1):
                add_steps += n

            needed_fuel[pos] += add_steps

        pos += 1


input = "day_7_input.txt"
test_input = "test_7_input.txt"

crab_positions = init_state(input)
max_position = max(crab_positions)
needed_fuel = {}


# get_fuel_for_change()
get_next_fuel_for_change()
print(get_minimum_fuel(needed_fuel))
