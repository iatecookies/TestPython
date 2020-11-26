from math import floor



def math_floor (x):
    if type(x) not in [float]:
        raise TypeError("Het getal moet een float zijn")

    #input = -3.2 geeft -4
    return floor(x)
    




# return name of the module we are running
if __name__ == "__main__":
    print ("type a decimal number. (Float) ")
    var = float(input( ))
    print("You entered: " + str(var))
    result = math_floor (var)
    print (result)
