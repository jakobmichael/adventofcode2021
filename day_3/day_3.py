#Part One
print("Solution Part One")

diagnostics = []
input = "day_3_input.txt"
test_input = "test_3_input.txt"

gamma_rate_bin = ""
epsilon_rate_bin = ""

common_bits = []

def split(word):
    return [char for char in word]

with open(test_input) as file:
    for line in file:
        diagnostics.append(split(line.rstrip()))



for i in range(0, len(diagnostics[0])):
    bits = []
    for code in diagnostics:
        bits.append(code[i])
    common_bits.append(bits)


for bits in common_bits:
    count_ones = 0
    count_zeros = 0
    for bit in bits: 
        if(bit == '0'):
            count_zeros += 1
        elif(bit == '1'):
            count_ones += 1
    
    if(count_ones > count_zeros):
        gamma_rate_bin += '1'
        epsilon_rate_bin += '0'        
    else:
        gamma_rate_bin += '0'
        epsilon_rate_bin += '1'


def convert_binary_to_decimal(binary):
    m = 1
    dec_num = 0
    for digit in reversed(binary):
        digit= int(digit)
        dec_num += (digit * m)
        m = m * 2
    
    return dec_num


gamma_rate_dec= convert_binary_to_decimal(gamma_rate_bin)
epsilon_rate_bin = convert_binary_to_decimal(epsilon_rate_bin)

print(gamma_rate_dec*epsilon_rate_bin)


#Part Two
print("Solution Part Two")

remaining_numbers = diagnostics.copy()



oxygen_generator_rating = ""

def check_input_for_bits(pos, bit):
    for number in remaining_numbers:
        if(number[pos] != bit):
            # remaining_numbers.remove(number)
            print("")
            
common_bits_2 = []
   

def get_common_bits():
    for i in range(0, len(remaining_numbers[0])):
        bits = []
        for code in remaining_numbers:
            bits.append(code[i])
        common_bits_2.append(bits)
        
get_common_bits()

pos = 0
for bits in common_bits_2:
    print(bits)
    count_ones = 0
    count_zeros = 0
    for bit in bits: 
        if(bit == '0'):
            count_zeros += 1
        elif(bit == '1'):
            count_ones += 1
    
    if(count_ones > count_zeros):
        check_input_for_bits(pos, '1')   
    elif(count_ones < count_zeros):
        check_input_for_bits(pos, '0')   
    else:
        check_input_for_bits(pos, '1')  
    pos += 1
    get_common_bits()
    print(count_ones)


