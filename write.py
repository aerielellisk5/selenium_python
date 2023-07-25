# file = open('text.txt')


# read and store all the lines in list
# reverse the list
# write the list back to the file

with open('text.txt', 'r') as reader:
    content = reader.readlines() # get the file contents
    print(content)
    with open('text1.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
    