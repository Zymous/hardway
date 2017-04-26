# Reading files

from sys import argv
# script, filename = argv
# txt = open(filename)
#
# print "Here's your file %r:" % filename
# print txt.read()

print "Type the filename again:"
file_again = raw_input("> ") # inut the filename on the console command

txt_again = open(file_again) # open the file and return a file object

print txt_again.read() # read the message from filename and print out
txt_again.close()
