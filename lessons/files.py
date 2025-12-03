# files + modules

# libraries: eg standard lib, multiple packages. 
# packages: directory of modules
# modules: just python files

# files:
    # - logs.
    # - storing/accessing data
    # - configs
    # - scripts

# types:
#     - text
#     - json, audio, video, csv...


# read + write (append)

# opening:
#file = open("lines.txt", "r") # r (read), W (write + make the file), A(append + make the file)

# commands:

# read() reads an entire file - as a string. 
# readline() reads a line and moves on to the next line.
# readlines() reads all line and returns as a list. 
# seek(n) - go to. defaults to first line. 

# write() writes an entire string
# writelines() write a list to the file. 

# file = open("lines.txt", "r")

# l = file.readlines()

# print(l)

# file.close()

file = open("lines-new.txt", "w")

for n in range(11):
    newline = "this is new line number " + str(n) + "\n"
    file.write(newline)

file.close()




file = open("lines-new.txt", "r")

outfile = ""

for line in range(11):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("lines-new.txt", "w")

file.write(outfile)
file.close()



tips for lab:

use csvReader
clean up/ prep for data. (list comp)
line by line - whaat to capture? append company name s to company list sales to sales list. 
zip() - iterates over elements in multiple tuples. - monthly sales.
format well.  