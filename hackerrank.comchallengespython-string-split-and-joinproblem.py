def split_and_join(line):
    words = line.split(" ")
    result = "-".join(words)
    return result

input_line = input("")
result = split_and_join(input_line)
print(result)