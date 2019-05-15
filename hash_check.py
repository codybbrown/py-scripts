# Cody Brown
# hash_check.py
# Mon Nov 27 07:56:28 CST 2017
# *********************************************************
def main():
    one = "0x8dB85c735f3537D5537B8a7097c585c80E727a33"
    two = "0x8dB85c735f3537D5537B8a7097c585c80E727a33"
    check(one, two)
def check(one, two):
    if one == two:
        print("YES!!")
    else:
        print("NO!!")
if __name__ == "__main__": main() # main func call
