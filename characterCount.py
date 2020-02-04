import pprint  # A module which allows item to be outputted in a more readable format
# Below: Opens the rj text file which contains the entirety of Romeo and Juliet in Read Mode and stores in n
n = open("rj.txt", "r")
message = n.read()  # Reads all the lines in n and stores in variable message
count = {}  # creates a dictionary to store characters and their related count char:count

for char in message.upper():  # Loops through the string in uppercase, meaning no duplication of upper and lower
    if char != " " and char != "\n":  # ignores newline and space characters
        count.setdefault(char, 0)  # Sets the default value of a character to 0 in the dictionary
        count[char] = count[char]+1  # Increments the count by one

pprint.pprint(count)  # Pretty Prints the count
max_val = max(list(count.values()))  # Gets the maximum value
for i in list(count.keys()):
    if count[i] == max_val:
        max_item = i

# Below: Outputs what the most common character is with its count
print("The most common character excluding spaces is " + str(max_item) + " which appears " + str(max_val) + " Times!")

