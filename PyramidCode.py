def decode(message_file):

    message_dictionary = {}
    with open(message_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2 and parts[0].isdigit():
                message_dictionary[int(parts[0])] = parts[1]
    
    max_num = max(message_dictionary.keys())
    triangular_numbers = []
    n = 1
    while (tri_num := n * (n + 1) // 2) <= max_num:
        triangular_numbers.append(tri_num)
        n += 1

    decoded_message = [] 

    for num in triangular_numbers:
        if num in message_dictionary:
            word = message_dictionary[num]
            decoded_message.append(word)

    return ' '.join(decoded_message)

message = decode('coding_qual_input.txt')
print(message)
