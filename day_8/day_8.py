
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
    decoded = []
    for code in dict["entry"]:
        if len(code) == segment_length:
            decoded.append(code)
            
    for code in dict["output"]:
        if len(code) == segment_length:
            decoded.append(code)
            
    return decoded



input = "day_8_input.txt"
test_input_1 = "test_8_input_1.txt"
test_input_2 = "test_8_input_2.txt"

input_data = init_state(input)




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



def split(word):
    return [char for char in word]




char_lengths = {
    2: None,
    3: None,
    4: None,
    6: None,
    5: None,
    7: None,
    
}




def get_char_lengths(input):

    for key,value in char_lengths.items():
        char_lengths[key] = (get_number_decoding(key,input))



def decode_chars():

    decoded_chars = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
    }   

    for key,values in char_lengths.items():

        for value in values:

            one_elements = []
            four_elements = []
            nine_elements = []

            contains_one = 0
            contains_four = 0
            contains_nine = 0

            if key == 7:
                decoded_chars[8].append(value)

            if key == 2:
                decoded_chars[1].append(value)
    
            if key == 3:
                decoded_chars[7].append(value)

            if key == 4:
                decoded_chars[4].append(value)

            if key == 6:
                one_elements = split(decoded_chars[1][0])
                four_elements = split(decoded_chars[4][0])
        
                contains_one = 0
                contains_four = 0  

                for char in one_elements:
                    if char in value:
                        contains_one += 1
        
                for char in four_elements:
                    if char in value:
                     contains_four += 1
        
                if contains_one == 1:
                    decoded_chars[6].append(value)
        
                elif contains_four == 3:
                    decoded_chars[0].append(value)
        
                else:
                    decoded_chars[9].append(value)
    

            if key == 5:

                one_elements = split(decoded_chars[1][0])
                nine_elements = split(decoded_chars[9][0])

                for char in one_elements:
                    if char in value:
                        contains_one += 1

                for char in nine_elements:
                    if char in value:
                        contains_nine += 1
        
                if contains_one == 2:
                    decoded_chars[3].append(value)
        
                elif contains_nine == 5:
                    decoded_chars[5].append(value)
        
                else:
                    decoded_chars[2].append(value)

    return decoded_chars



total_sum = []

def decode_output(input,decoded):
    sum = ""
    for code in input["output"]:
        for key,value in decoded.items():
            if code in value:
                sum += str(key)

    total_sum.append(sum)

def sum_all_output_sums():
    output_sum = 0
    for str in total_sum:
        output_sum += int(str)

    return output_sum

for key, value in input_data.items():
    get_char_lengths(value)
    decoded = decode_chars()
    decode_output(value,decoded)






print(sum_all_output_sums())