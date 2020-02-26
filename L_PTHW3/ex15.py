#from the sys library imports argv command whichs the list of 
#command line arguments are passed to a python script
from sys import argv

#sets variables script and filename equal to argv
script, filename = argv
#sets txt variable to open a file given in the command line
txt = open(filename)
#prints name given in command line

print(f"Here's your file {filename}:")
#read the opened file
print(txt.read())

#print("type the file name again:")
#request an imput from the python prompt 
#file_again = input("> ")
#opens file given in the python prompt
#txt_again = open(file_again)
#prints the file after reading it with command read
#print(txt_again.read())
