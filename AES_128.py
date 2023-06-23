#AES 128 standard

inverse_sbox = [[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
                [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
                [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
                [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
                [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
                [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
                [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
                [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
                [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
                [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
                [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
                [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
                [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
                [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
                [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
                [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]

sbox = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]
def substitute_bytes(state):
    row_index = 0
    for row in state:
        cell_index = 0
        for cell in row:
            sbox_x_digit = int(cell / 16)
            sbox_y_digit = cell % 16
            substitute = sbox[sbox_x_digit][sbox_y_digit]
            state[row_index][cell_index] = substitute
            cell_index+=1
        row_index += 1
    return state

def shift_rows(state):
        for row_index in range(4):
            state[row_index] = state[row_index][row_index:] + state[row_index][:row_index]
        return state

def delete_two_byte_overflow(integer):
        if (integer > 255):
            integer = integer ^ 27
        if (integer > 255):
            integer %= 256
        return integer

def get_gf2 (integer):
    integer = integer * 2
    integer = delete_two_byte_overflow(integer)
    return integer

def get_gf3 (integer):
    return get_gf2(integer) ^ delete_two_byte_overflow(integer)

def get_gf4 (integer):
    return get_gf2(get_gf2(integer))

def get_gf8 (integer):
    return get_gf2(get_gf4(integer))

def get_gf9 (integer):
    return get_gf8(integer) ^ delete_two_byte_overflow(integer)

def get_gf11 (integer):
    return get_gf8(integer) ^ get_gf2(integer) ^ delete_two_byte_overflow(integer)

def get_gf13 (integer):
    return get_gf8(integer) ^ get_gf4(integer) ^ delete_two_byte_overflow(integer)

def get_gf14 (integer):
    return get_gf8(integer) ^ get_gf4(integer) ^ get_gf2(integer)

multiplier_matrix = [[2, 3, 1, 1],
                     [1, 2, 3, 1],
                     [1, 1, 2, 3],
                     [3, 1, 1, 2]]

def mix_columns(state):
    tmp_state = []
    for row_index in range(4):
        for cell_index in range(4):
            new_cell = 0
            for multiplier_index in range(4):
                tmp = 0
                if (multiplier_matrix[cell_index][multiplier_index] == 1):
                    tmp = state[multiplier_index][row_index]
                elif (multiplier_matrix[cell_index][multiplier_index] == 2):
                    tmp = get_gf2(state[multiplier_index][row_index])
                elif (multiplier_matrix[cell_index][multiplier_index] == 3):
                    tmp = get_gf3(state[multiplier_index][row_index])
                new_cell ^= tmp
            tmp_state.append(new_cell)
    for row_index in range(4):
        for column_index in range(4):
            state[column_index][row_index] = tmp_state[row_index * 4 + column_index]
    return state

def rotate_word(four_int_list):
    four_int_list = four_int_list[1:] + four_int_list[:1]
    return four_int_list

def substitute_word(four_int_list):
    value_index = 0
    for value in four_int_list:
        sbox_x_digit = int(value / 16)
        sbox_y_digit = value % 16
        substitute = sbox[sbox_x_digit][sbox_y_digit]
        four_int_list[value_index] = substitute
        value_index += 1
    return four_int_list

round_constants = [[0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36],
                   [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                   [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                   [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]]

def key_expansion(key, constants, round_index):
    tmp_list = []
    tmp_list_of_round_keys = []
    new_round_key = []
    for row_index in range(4):
        if row_index == 0:
            for column_index in range(4):
                tmp_list.append(key[column_index][3-row_index])
            tmp_list = rotate_word(tmp_list)
            tmp_list = substitute_word(tmp_list)
            for column_index in range(4):
                tmp_list[column_index] = constants[column_index][round_index] ^ tmp_list[column_index]
            for column_index in range(4):
                tmp_list[column_index] = key[column_index][row_index] ^ tmp_list[column_index]
                tmp_list_of_round_keys.append(tmp_list[column_index])
        else:
            for column_index in range(4):
                tmp_list[column_index] = key[column_index][row_index] ^ tmp_list[column_index]
                tmp_list_of_round_keys.append(tmp_list[column_index])
    tmp_list_of_round_keys = [tmp_list_of_round_keys[i * 4:(i + 1) * 4] for i in range((len(tmp_list_of_round_keys) + 4 - 1) // 4 )]
    for i in range(len(tmp_list_of_round_keys[0])):
        tmp = []
        for v in tmp_list_of_round_keys:
            tmp.append(v[i])
        new_round_key.append(tmp)
    return new_round_key

def add_round_key(state, key):
    for row_index in range(4):
        for column_index in range(4):
            state[row_index][column_index] ^= key[row_index][column_index]
    return state

def inverse_shift_rows(state):
    for row_index in range(4):
            state[row_index] = state[row_index][-row_index:] + state[row_index][:-row_index]
    return state

def inverse_substitute_bytes(state):
    row_index = 0
    for row in state:
        cell_index = 0
        for cell in row:
            inverse_sbox_x_digit = int(cell / 16)
            inverse_sbox_y_digit = cell % 16
            substitute = inverse_sbox[inverse_sbox_x_digit][inverse_sbox_y_digit]
            state[row_index][cell_index] = substitute
            cell_index+=1
        row_index += 1
    return state

inverse_multiplier_matrix = [[14, 11, 13,  9],
                             [ 9, 14, 11, 13],
                             [13,  9, 14, 11],
                             [11, 13,  9, 14]]

def inverse_mix_columns(state):
    tmp_state = []
    for row_index in range(4):
        for cell_index in range(4):
            new_cell = 0
            for multiplier_index in range(4):
                tmp = 0
                if (inverse_multiplier_matrix[cell_index][multiplier_index] == 9):
                    tmp = get_gf9(state[multiplier_index][row_index])
                elif (inverse_multiplier_matrix[cell_index][multiplier_index] == 11):
                    tmp = get_gf11(state[multiplier_index][row_index])
                elif (inverse_multiplier_matrix[cell_index][multiplier_index] == 13):
                    tmp = get_gf13(state[multiplier_index][row_index])
                elif (inverse_multiplier_matrix[cell_index][multiplier_index] == 14):
                    tmp = get_gf14(state[multiplier_index][row_index])
                new_cell ^= tmp
            tmp_state.append(new_cell)
    for row_index in range(4):
        for column_index in range(4):
            state[column_index][row_index] = tmp_state[row_index * 4 + column_index]
    return state

def list_to_matrix(list):
    matrix = [list[i * 4:(i + 1) * 4] for i in range((len(list) + 4 - 1) // 4)] 
    return matrix

def matrix_to_list(matrix):
    list = []
    for row_index in range(4):
        for cell_index in range(4):
            list.append(matrix[row_index][cell_index])
    return list

def string_to_char_list(string):
    list = []
    for letter in string:
        list.append(letter)
    return list

def char_list_to_string(list):
    string = ""
    for cell in list:
        string += cell
    return string

def append_hex_list_tail(list):
    while len(list) % 16 != 0:
        list.append('0x00')
    return list

def cut_hex_list_tail(list):
    list = [value for value in list if value != '\x00']
    return list

def convert_list_hex_to_int(list):
    for i in range(len(list)):
        list[i] = int(list[i], 16)
    return list

def convert_list_char_to_hex(list):
    for i in range(len(list)):
        list[i] = hex(ord(list[i]))
    return list

def convert_list_hex_to_char(list):
    for i in range(len(list)):
        c = chr(list[i])
        list[i] = c
    return list

def generate_round_keys(init_key_matrix):
    rounds = 10
    keys = []
    keys.append(init_key_matrix)
    for key_id in range(rounds):
        keys.append(key_expansion(keys[key_id-1], round_constants, key_id))
    return keys
def encrypt_string(plaintext_string, round_key_matrices):
    #setup
    plaintext_list = string_to_char_list(plaintext_string)
    plaintext_list = convert_list_char_to_hex(plaintext_list)
    plaintext_list = append_hex_list_tail(plaintext_list)
    plaintext_list = convert_list_hex_to_int(plaintext_list)
    state = list_to_matrix(plaintext_list)
    #round 0
    state = add_round_key(state, round_key_matrices[0])
    for round in range (9):
        #round 1-9
        state = substitute_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_key_matrices[round + 1])
    #round 10
    state = substitute_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_key_matrices[10])
    #result
    cyphertext_list = matrix_to_list(state)
    cyphertext_list = convert_list_hex_to_char(cyphertext_list)
    cyphertext = char_list_to_string(cyphertext_list)
    return cyphertext

def decrypt_string(cyphertext_string, round_key_matrices):
    #setup for decryption
    cyphertext_list = string_to_char_list(cyphertext_string)
    cyphertext_list = convert_list_char_to_hex(cyphertext_list)
    cyphertext_list = convert_list_hex_to_int(cyphertext_list)
    state = list_to_matrix(cyphertext_list)
    #ROUND 0
    state = add_round_key(state, round_key_matrices[10])
    state = inverse_shift_rows(state)
    state = inverse_substitute_bytes(state)
    for round in range (9):
        #ROUND 1-9
        state = add_round_key(state, round_key_matrices[9-round])
        state = inverse_mix_columns(state)
        state = inverse_shift_rows(state)
        state = inverse_substitute_bytes(state)
    #ROUND 10
    state = add_round_key(state, round_key_matrices[0])
    #state to string
    cyphertext_list = matrix_to_list(state)
    cyphertext_list = convert_list_hex_to_char(cyphertext_list)
    cyphertext_list = cut_hex_list_tail(cyphertext_list)
    plaintext = char_list_to_string(cyphertext_list)
    return plaintext

def text_to_string_list(text):
    string_list = [text[i:i+16] for i in range(0, len(text), 16)]
    return string_list

def string_list_to_text(string_list):
    text = ""
    text = text.join([str(elem) for elem in string_list])
    return text

def encrypt(plaintext_string_list, round_key_matrices):
    cyphertext = ""
    cyphertext_string = ""
    for string_index in range(len(plaintext_string_list)):
        cyphertext_string = encrypt_string(plaintext_string_list[string_index], round_key_matrices)
        cyphertext += cyphertext_string
    return cyphertext
def decrypt(cyphertext_string_list, round_key_matrices):
    plaintext = ""
    plaintext_string = ""
    for string_index in range(len(cyphertext_string_list)):
        plaintext_string = decrypt_string(cyphertext_string_list[string_index], round_key_matrices)
        plaintext += plaintext_string
    return plaintext

def lenghten_string(string, char_index):
    if len(string) == 1:
        string += chr(int(hex(ord(string[0])), 16) ^ 0x1b)
    elif len(string) % 2 == 1:
        string += chr((int(hex(ord(string[int(len(string)/2)])), 16)+ char_index) ^ int(hex(ord(string[-1:])), 16))
    else:
        string += chr(int(hex(ord(string[int(len(string)/2 - 1)])), 16) ^ (int(hex(ord(string[int(len(string)/2)])), 16)) + char_index)
    return string

def shorten_string(string, char_index):
    string_list = string_to_char_list(string)
    string_list[char_index] = chr(int(hex(ord(string_list[char_index])), 16) ^ int(hex(ord(string_list[char_index + 1])), 16))
    string_list.pop(char_index + 1)
    string = char_list_to_string(string_list)
    return string

def key_lenght_to_16(key_string):
    if len(key_string) < 16:
        index = 0
        while len(key_string) != 16:
            key_string = lenghten_string(key_string, index)
            index += 1
    elif len(key_string) > 16:
        index = 0
        while len(key_string) != 16:
            key_string = shorten_string(key_string, index)
            index = (index + 2) % 16
    return key_string

import os
#FILE PROCESSING
def file_processing(input_file_path, output_file_path, round_keys, mode):
    input_file = open(input_file_path, 'r', encoding="latin_1")
    output_file = open(output_file_path, 'a', encoding="latin_1")
    lines = convert_list_to_string_length_16(input_file.readlines())
    for line_index in range(len(lines)):
        if mode == "encrypt":
            plaintext = lines[line_index]
            plaintext_string_list = text_to_string_list(plaintext)
            cyphertext = encrypt(plaintext_string_list, round_keys)
            output_file.write(cyphertext)
        elif mode == "decrypt":   
            cyphertext = lines[line_index]
            cyphertext_string_list = text_to_string_list(cyphertext)
            plaintext = decrypt(cyphertext_string_list, round_keys)
            output_file.write(plaintext)
    input_file.close()
    output_file.close()

def convert_list_to_string_length_16(list):
    temp_string = ""
    string_length_16_list = []
    for y in range(len(list)):
        list[y] = temp_string + list[y]
        temp_string = ""
        split = [list[y][i:i+16] for i in range(0, len(list[y]), 16)]
        if len(split[len(split)-1]) < 16 and y != len(list)-1:
            temp_string = split[len(split)-1]
            split.pop(len(split)-1)
        for string in split:
            string_length_16_list.append(string)
    return string_length_16_list

def directory_processing(mode, round_keys): #mode is a string value "encrypt" or "decrypt"
    if mode == "decrypt":
        input_directory = "data_to_decrypt/"
        output_directory = "decrypted_data/"
    elif mode == "encrypt":
        input_directory = "data/"
        output_directory = "data_to_decrypt/"
    else:
        output_directory = "misc/"
    input_file_list = os.listdir(input_directory)
    output_file_list = os.listdir(output_directory)
    for file_index in range(len(input_file_list)):
        input_file_path = input_directory + input_file_list[file_index]
        output_file_path = output_directory + mode +"ed_file_" + str(len(output_file_list) + file_index)
        file_processing(input_file_path, output_file_path, round_keys, mode)

def key_processing(key):
    key_length_16 = key_lenght_to_16(key)
    print("Key length adjusted : ", key_length_16)
    key_char_list = string_to_char_list(key_length_16)
    key_hex_list = convert_list_char_to_hex(key_char_list)
    key_int_list = convert_list_hex_to_int(key_hex_list)
    key_matrix = list_to_matrix(key_int_list)
    round_keys = generate_round_keys(key_matrix)
    return round_keys

print("#######################################################################")
print("############################### AES 128 ###############################")
print("#######################################################################")
key = ""
while key == "":
    key = input("Please enter the key : ")
keys = key_processing(key)
print("#######################################################################")
control_input = input("Pick an option: e = encrypt files, d = decrypt files, any other = exit program : ")
if control_input == "e":
    directory_processing("encrypt", keys)
    print("Encryption finished. Encrypted files are available in 'data_to_decrypt' folder")
    print("Exiting program.")
elif control_input == "d":
    directory_processing("decrypt", keys)
    print("Decryption finished. Decrypted files are available in 'decrypted_data' folder")
    print("Exiting program.")
else:
    print("Exiting program.")