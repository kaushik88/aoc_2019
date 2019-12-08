data = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,115,2,119,1,119,10,0,99,2,14,0,0"

def get_first_position_from_data(data):
    tokens = data.split(",")
    return get_first_position_from_tokens(tokens)

def get_first_position_from_tokens(tokens):
    i = 0
    while i < len(tokens):
        token = tokens[i]
        token = int(token)
        if token == 1 or token == 2:
            first_position = int(tokens[i+1])
            second_position = int(tokens[i+2])
            third_position = int(tokens[i+3])
            if token == 1:
                """
                print("Adding {} and {} to store in position {}".format(
                    tokens[first_position], 
                    tokens[second_position],
                    third_position
                ))
                """
                tokens[third_position] = str(int(tokens[first_position]) + int(tokens[second_position]))
            else:
                """
                print("Multiplying {} and {} to store in position {}".format(
                    tokens[first_position], 
                    tokens[second_position],
                    third_position
                ))
                """
                tokens[third_position] = str(int(tokens[first_position]) * int(tokens[second_position]))
            i = i+4
        elif token == 99:
            # print("Breaking at position {}".format(i))
            break
        else:
            i += 1
        # print("Tokens", tokens)
    return tokens[0]

def return_pair(data):
    for i in range(99):
        for j in range(99):
            tokens = data.split(",")
            tokens[1] = str(i)
            tokens[2] = str(j)
            first_position = get_first_position_from_tokens(tokens)
            print("Tried with {} and {} and got {}".format(i, j, first_position))
            if first_position == "19690720":
                return (i, j, 100*i+j)
    return (-1, -1)



# all_tokens = get_first_position_from_data(data)
# print("First Position ", int(all_tokens))

print(return_pair(data))