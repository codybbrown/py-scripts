# Sun Jul  9 18:15:42 CDT 2017
# Cody Brown Python Study:   
# *********************************************************
# Reads the directory manifest of the directory it is in and
# prints the results
# *********************************************************

# read lines from text file
fh = open('dir_manifest.txt')
for line in fh.readlines():
	print(line, end='')
