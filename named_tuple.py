# Cody Brown
# named_tuple.py
# Mon Dec 25 06:57:14 CST 2017
# *********************************************************
def main():
    from collections import namedtuple

    Car = namedtuple('Car', 'color mileage')
    Saxophone = namedtuple('Saxophone', 'make model')
    my_car = Car('Red', 3425.6)
    my_sax = Saxophone('Tenor', 'Borgani')
    print(my_car.color, my_car.mileage)
    print(my_sax.make, my_sax.model)


if __name__ == "__main__": main() # main func call
