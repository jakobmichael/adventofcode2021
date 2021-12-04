# Part One
print("Solution Part One")

input = "day_4_input.txt"
test_input = "test_4_input.txt"

drawn_numbers = []
boards = []


with open(input) as file:
    temp = file.readline().split(",")
    for string in temp:
        drawn_numbers.append(int(string))


with open(input) as file:
    for i in range(2):
        file.next()
    board = []
    index = 0
    for line in file:
        temp = line.rsplit()

        row = []
        for string in temp:
            row.append(int(string))

        if row.__len__() > 0:
            board.append(row)
            index += 1

        if index == 5:
            boards.append(board)
            index = 0
            board = []


def check_rows_for_adjacent(row):
    return all(numbers == "x" for numbers in row)


def replace_same_numbers(board, drawn_number):
    for row in board:
        for index, number in enumerate(row):
            if number == drawn_number:
                row[index] = "x"
    return board


def check_column_for_adjacent(board):
    for i in range(0, board[0].__len__()):
        numbers_at_same_index = []
        for row in board:
            numbers_at_same_index.append(row[i])

        if all(numbers == "x" for numbers in numbers_at_same_index):
            return True
        


def play_bingo(random_number):
    for board in boards:
        new_board = replace_same_numbers(board, random_number)
        for row in new_board:
            if check_rows_for_adjacent(row):
                return new_board
        if check_column_for_adjacent(new_board):
            return new_board
            


number_for_bingo = None
winning_board = None
number_of_won_boards = 0
last_index = 0


for j in range(0,100):

    for i in range(last_index, drawn_numbers.__len__()):
        if play_bingo(drawn_numbers[i]) != None:
            number_for_bingo = drawn_numbers[i]
            winning_board = play_bingo(drawn_numbers[i])
            number_of_won_boards += 1
            boards.remove(winning_board)
            last_index = drawn_numbers.index(number_for_bingo)
            break









board_score = 0
for row in winning_board:
    for number in row:
        if number != "x":
            board_score += number

final_score = board_score * number_for_bingo

print(last_index)
print(drawn_numbers.index(number_for_bingo))
print
print(number_of_won_boards)
print(final_score)
print(winning_board)
print(number_for_bingo)
