# Cody Brown
# tuples_lists.py
# Fri Sep 29 10:48:23 CDT 2017
# *********************************************************
def main():

	t = 1,2,3,4,5
	t1 = (1,)
	s = "string test"
	l = 'str', 5, 0.33, [3, 5, 6]

	get_class(t, t1, s, l, l[3])

def get_class(*args):
	for arg in args:
		print(type(arg))

if __name__ == "__main__": main() # main func call
