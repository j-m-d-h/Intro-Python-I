"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

txt = open('foo.txt', 'r')
print(txt.read())
txt.close()



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

txt1 = open('bar.txt', 'w')
txt1.write("Line1\nLineDos\nLineFinal")
txt1.close()
txt1 = open('bar.txt', 'r')
print(txt1.read())
txt1.close()
