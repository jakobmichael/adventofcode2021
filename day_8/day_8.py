
def init_state(filename):
    code_collection = {}
    with open(filename) as file:
        line_number = 0
        for line in file:
            note =[]
            output =[]
            temp = line.rstrip().split(" | ")
            
            note = temp[0].rstrip().split(" ")
            output = temp[1].split(" ")

            code_collection[line_number] = {
                "entry":note,
                "output": output
            }
            line_number += 1
            

    return code_collection


def get_number_of_instances(segment_length, dict):
    instances = 0
    for key,value in dict.items():
        for code in value["output"]:
            if len(code) == segment_length:
                instances += 1

    return instances

def get_number_decoding(segment_length, dict):
    decoded = ""
    for key,value in dict.items():
        for code in value["entry"]:
            if len(code) == segment_length:
                decoded = code
                break
       
    return decoded



input = "day_8_input.txt"
test_input_1 = "test_8_input_1.txt"
test_input_2 = "test_8_input_2.txt"

input_data = init_state(test_input_2)




needed_segments = {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}

instances = 0

for key,value in needed_segments.items():
    instances += get_number_of_instances(value, input_data)


print(instances)

#Part Two



    



char_decodings = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
}

char_positions = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
}


for key,value in needed_segments.items():
    char_decodings[key] = get_number_decoding(value, input_data)


    

print(char_decodings)