# Opening of file.
fileFound = 0
while(fileFound != 1):
    try:        
        filename = input('Enter the file name: ')
        userFile = open(filename)
        fileFound = 1
    except FileNotFoundError:
        print("This file does not exist. Try again.\n")


# Initalize list to have 1 element to occupy list[0] index.
allLines = [" "]

# Count number of lines in file and append each line to list.
lineCount = 0
for line in userFile:       
    allLines.append(line)
    lineCount += 1

# Close the file after getting the needed data.
userFile.close()

# Display number of lines.
print("The file has " + str(lineCount) + " lines.")

# Let the user keep entering lines to output.
userLine = 1
while(userLine != 0):
    userLine = int(input(("Enter a line to output from 1 to " + str(lineCount) + ". (0 to exit): ")))
    print(allLines[userLine])