file = open('text.txt')
# print(file.read())
# read all the contents of the file

# print(file.read(2))
# will read the first 2 characters of the file

# print(file.readline())
# this will read only the first line

# print(file.readline())
# print(file.readline())
# print(file.readline())
# this will read the first 3 lines




# Print line by line using readLine method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# print(file.readlines())
# willnow put everything in a list/array
for line in file.readlines():
    print(line)


file.close()




