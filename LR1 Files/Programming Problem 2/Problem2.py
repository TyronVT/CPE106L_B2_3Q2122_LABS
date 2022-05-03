# Opening the File
while True:
    try:
        filename = input("Enter a filename:")
        file = open(filename, "r")
        break 
    except FileNotFoundError:
        print("File not found. Try again.")

# Read all lines of the file
raw_lines = file.readlines()

# Close the file
file.close()

# Remove newline (\n) character per line using list comprehension
text_lines = [line.strip() for line in raw_lines]

# Print the requested line, 0 to exit
while True:
    line_number = int(input(f"Enter the line number [1 - {len(text_lines)}, 0 to exit]: "))
    if line_number == 0:
        print("Program is Exiting")
        break 
    print(text_lines[line_number-1])
