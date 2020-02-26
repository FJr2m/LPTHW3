from sys import argv

script, filename = argv

print(f"we are going to erase {filename}.")
print("if you dont want that, hit CTRL-C (^C).")
print("if you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

#not need it when in open option 'w' is called
#print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
lines = '{}\n{}\n{}\n'.format(line1,line2,line3)

print("I'm going to write these to the file.")

target.write(lines)

print("And finally, we close it.")
target.close()