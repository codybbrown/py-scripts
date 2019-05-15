# Cody Brown
# generator_func_range.py
# Fri Jul 21 21:56:05 CDT 2017
# *********************************************************
def main():
    # iterate using the generator
    for i in inclusive_range(30, 50, 2): # start, stop, step values
        print(i, end=' ')


def inclusive_range(*args): # create a tuple from args list
    print(args)
    numargs = len(args)

    if numargs < 1: raise TypeError("requires at least one argument")
    elif numargs == 1:
        stop = args[0] # assigning the single arg to range stop
        start = 0 # default range start value
        step = 1 # default range step value
    elif numargs == 2:
        (start, stop) = args # assign args to start and stop
        step = 1 # default step value
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError("inclusive_range expected at most 3 arguments")
    i = start
    while i <= stop:
        yield i
        i += step
if __name__ == "__main__": main() # main func call
