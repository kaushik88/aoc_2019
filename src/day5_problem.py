data = "3,225,1,225,6,6,1100,1,238,225,104,0,101,71,150,224,101,-123,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,2,205,209,224,1001,224,-3403,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1101,55,24,224,1001,224,-79,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1,153,218,224,1001,224,-109,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1002,201,72,224,1001,224,-2088,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,70,29,225,102,5,214,224,101,-250,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1101,12,52,225,1101,60,71,225,1001,123,41,224,1001,224,-111,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,78,66,224,1001,224,-5148,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,29,77,225,1102,41,67,225,1102,83,32,225,1101,93,50,225,1102,53,49,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,677,224,1002,223,2,223,1005,224,329,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,359,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,419,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,434,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,449,1001,223,1,223,1008,226,677,224,1002,223,2,223,1006,224,464,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,479,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,539,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,569,101,1,223,223,107,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,599,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,614,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,644,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,659,101,1,223,223,108,226,677,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226"

def get_outputs_from_data(data):
    tokens = data.split(",")
    print("Length of Input = {}".format(len(tokens)))
    return get_outputs(tokens)

def safe_get_mode(token_list, index):
    if index >= 0 and index < len(token_list):
        return token_list[index]
    return 0

def get_token_value(token_digits, digit_index, tokens, token_index):
    token_mode = safe_get_mode(token_digits, digit_index)
    token_value = int(tokens[token_index]) if token_mode == 1 else int(tokens[int(tokens[token_index])])
    return token_value

def get_outputs(tokens, input='5'):
    outputs = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        token_digits = [int(d) for d in token]
        print("Token Digits", token_digits)
        last_token = token_digits[len(token_digits) - 1]
        if last_token == 1 or last_token == 2:
            first_value = get_token_value(token_digits, len(token_digits) - 3, tokens, i+1)
            second_value = get_token_value(token_digits, len(token_digits) - 4, tokens, i+2)
            third_position = int(tokens[i+3])
            if last_token == 1:
                print("Adding {} and {} to store in position {}".format(
                    first_value, 
                    second_value,
                    third_position
                ))
                tokens[third_position] = str(first_value + second_value)
            else:
                print("Multiplying {} and {} to store in position {}".format(
                    first_value, 
                    second_value,
                    third_position
                ))
                tokens[third_position] = str(first_value * second_value)
            i = i+4
        elif last_token == 3 or last_token == 4:
            if last_token == 3:
                print("Storing {} to position {}".format(input, tokens[i+1]))
                tokens[int(tokens[i+1])] = input
            else:
                print("Output at {} from {} to {}".format(i, tokens[i], tokens[i+1]))
                token_value = get_token_value(token_digits, len(token_digits) - 3, tokens, i+1)
                outputs.append(token_value)
            i = i + 2
        elif last_token == 5 or last_token == 6:
            next_token = get_token_value(token_digits, len(token_digits) - 3, tokens, i+1)
            second_token = get_token_value(token_digits, len(token_digits) - 4, tokens, i+2)
            if last_token == 5 and next_token != 0:
                i = second_token
            elif last_token == 6 and next_token == 0:
                i = second_token
            else:
                i += 3
        elif last_token == 7 or last_token == 8:
            next_token = get_token_value(token_digits, len(token_digits) - 3, tokens, i+1)
            second_token = get_token_value(token_digits, len(token_digits) - 4, tokens, i+2)
            third_position = int(tokens[i+3])
            if last_token == 7:
                if next_token < second_token:
                    tokens[third_position] = str(1)
                else:
                    tokens[third_position] = str(0)
            if last_token == 8:
                if next_token == second_token:
                    tokens[third_position] = str(1)
                else:
                    tokens[third_position] = str(0)
            i += 4
        elif last_token == 9:
            # print("Breaking at position {}".format(i))
            break
        else:
            print("WAAAT", i, tokens[i])
            outputs.append("-1")
            i += 1
        # print("Tokens", tokens)
    return outputs

print("\n\n OUTPUT: ")
print("OUTPUT ", get_outputs_from_data(data))