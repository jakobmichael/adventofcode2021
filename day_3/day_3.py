# Part One
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
        digit = int(digit)
        dec_num += (digit * m)
        m = m * 2

    return dec_num


gamma_rate_dec = convert_binary_to_decimal(gamma_rate_bin)
epsilon_rate_bin = convert_binary_to_decimal(epsilon_rate_bin)

print(gamma_rate_dec*epsilon_rate_bin)


# Part Two
print("Solution Part Two")

original_codes = []



with open(input) as file:
    for line in file:
        original_codes.append(line.rstrip())


def get_quantity_of_bits_at_pos(codes, pos):
    ones = int(0)
    zeros = int(0)
    for code in codes:
        if(int(code[pos]) == 1):
            ones += 1
        elif(int(code[pos]) == 0):
            zeros += 1

    return [ones, zeros]





def getOxygenRate(mode):
    remaining_codes = []
    remaining_codes.append(original_codes)
    index = 0
    
  
    while  remaining_codes[remaining_codes.__len__()-1].__len__() > 1:

        remaining_code = []

        sum_of_bits = get_quantity_of_bits_at_pos(
            remaining_codes[index], index)
            
      

        rel_bit = '1'
     

        if(mode == 'oxygen'):
            if(sum_of_bits[0] < sum_of_bits[1]):
                rel_bit = '0'
        elif(mode == 'co2'):
            if(sum_of_bits[0] < sum_of_bits[1]):
                rel_bit = '1'
            elif(sum_of_bits[1] <= sum_of_bits[0]):
                rel_bit = '0'

   

        for code in remaining_codes[index]:

            if(code[index] == rel_bit):
                remaining_code.append(code)
        index += 1
        remaining_codes.append(remaining_code)
    
   

    return remaining_codes[remaining_codes.__len__()-1][0]


oxygen_rate = convert_binary_to_decimal(getOxygenRate('oxygen'))
co2_scrubber= convert_binary_to_decimal(getOxygenRate('co2'))

print(oxygen_rate*co2_scrubber)