def init_state(filename):
    height_map = []
    with open(filename) as file:

        for line in file:
            temp = []
            for char in line.rstrip():
                temp.append(int(char))

            height_map.append(temp)

    return height_map


def get_minimum_heights(map):
    adjacent_heights = []
    for index, row in enumerate(map):
        for i, height in enumerate(row):

            if index == 0:
                if i == 0:

                    if height < row[i+1] and height < map[index+1][i]:
                        adjacent_heights.append(height)
                elif i + 1 == row.__len__():
                    if height < row[i-1] and height < map[index+1][i]:
                        adjacent_heights.append(height)
                else:
                    if height < row[i-1] and height < row[i+1] and height < map[index+1][i]:
                        adjacent_heights.append(height)

            elif index + 1 == map.__len__():
                if i == 0:
                    if height < row[i+1] and height < map[index-1][i]:
                        adjacent_heights.append(height)
                elif i + 1 == row.__len__():
                    if height < row[i-1] and height < map[index-1][i]:
                        adjacent_heights.append(height)
                else:
                    if height < row[i-1] and height < row[i+1] and height < map[index-1][i]:
                        adjacent_heights.append(height)

            else:
                if i == 0:
                    if height < row[i+1] and height < map[index-1][i] and height < map[index+1][i]:
                        adjacent_heights.append(height)
                elif i + 1 == row.__len__():
                    if height < row[i-1] and height < map[index-1][i] and height < map[index+1][i]:
                        adjacent_heights.append(height)
                else:
                    if height < row[i-1] and height < row[i+1] and height < map[index-1][i] and height < map[index+1][i]:
                        adjacent_heights.append(height)

    return adjacent_heights


def calculate_risk_level(minimum_heights):
    risk_lvl = 0
    for height in minimum_heights:
        risk_lvl += 1 + height
    return risk_lvl


input = "day_9_input.txt"
test_input = "test_9_input.txt"

height_map = init_state(input)

adjacent_heights = get_minimum_heights(height_map)

risk_lvl = calculate_risk_level(adjacent_heights)

print(risk_lvl)
