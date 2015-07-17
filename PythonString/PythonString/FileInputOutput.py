# Create a new file by initializing it, opening it for writing, then closing it.

from FileInputOutput import fo

fo = open("C:\E\Github\Python-Scripts\FileOpen.txt", "w")
filestring = fo.read(20);
print("The best site in the world is ", filestring)

# Close opend file
fo.close()
