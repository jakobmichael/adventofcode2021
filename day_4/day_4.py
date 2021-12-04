# Part One
print("Solution Part One")

input = "day_4_input.txt"
test_input = "test_4_input.txt"

drawn_numbers = []
boards =[]


with open(test_input) as file:
    temp = file.readline().split(",")
    for string in temp:
        drawn_numbers.append(int(string))


with open(test_input) as file:
    for i in range(2):
        file.next()
    board = []
    index = 0
    for line in file:
        temp = line.rsplit()
       
        row = []
        for string in temp:
            row.append(int(string))

        if(row.__len__() > 0):  
            board.append(row) 
            index += 1
        
        if(index == 5):
            boards.append(board)
            index = 0
            board = []

for board in boards:
    print(board)





        


