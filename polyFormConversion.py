import numpy as np


def getNum(string, i):
    counter = 1
    value = ""
    while True:
        change = i - counter
        if abs(change) != change:
            break
        if string[change].isdigit() or string[change] == '-':
            value = value + string[i-counter]
            counter = counter + 1
        else:
            break
    if value != "":
        return int(value[::-1])
    else:
        return 1




def setDegrees(string):
    current_coefficent = [] # Run logic based off of ^ not off of x to enusre degree is placed first. 
    current_degree = 11111
    for i, char in enumerate(string): # Structures array, accounting for changes in the degree.

        if char == "x":

            if string[i+1] == "+":
                if current_degree != 11111:
                    if 1 != int(current_degree) - 1:
                        difference = int(current_degree) - 1
                        for i in range(difference-1):
                            current_coefficent.append(0)
                current_degree = 1
                current_coefficent.append("y")

            if string[i+1] == "^":

                print("Current degree:", current_degree)
                print("Current string I + 1:", string[i+2])
                print("Subtraction:", int(current_degree)-1)
                if current_degree != 11111:
                    if int(string[i+2]) != int(current_degree) - 1:
                        difference =  int(current_degree) - int(string[i+2])
                        current_degree = int(string[i+2])
                        for i in range(difference-1): # difference might be difference - 1 
                            current_coefficent.append(0)

                    else:
                        current_degree = string[i+2]
                else:
                    current_degree = string[i+2]
                current_coefficent.append("y")

    if string[len(string)-1].isdigit():
        if int(current_degree) - 1 != 0:
            difference = int(current_degree)
            current_degree = 0
            for i in range(difference - 1):
                current_coefficent.append(0)
        current_coefficent.append("y")
    else:
        current_coefficent.append(0)

    return current_coefficent
                    

def setCoefficents(string):
    current_coefficent = setDegrees(string)
    coefficent_values = list()
    for i, char in enumerate(string): # Seeks coefficents, then places them into the degree structured array respectively. 
        
        if char == "x":
            if string[i-1].isdigit():
                coefficent_values.append(int(getNum(string, i)))
            else:
                coefficent_values.append(1)

    if string[len(string)-1].isdigit():
        coefficent_values.append(int(getNum(string, len(string))))

    for num, char in enumerate(current_coefficent):
        if char == "y":
            current_coefficent[num] = coefficent_values[0]
            coefficent_values.pop(0)
    
    print(current_coefficent)

    return np.poly1d(current_coefficent)


x = setCoefficents("x^3+-10x^2+29x+-56")
y = setCoefficents("x+-7")

quotient, remainder = np.polydiv(x, y) 
  
print(quotient) 
print(remainder) 
