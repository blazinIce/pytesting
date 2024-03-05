#Here are some very simple fuctions that are going to perform the task of adding and dividing two given numbers

def add(number1, number2):
    return number1 + number2

def divide(number1, number2):
    if number2 == 0:
        raise ValueError

    return  number1 / number2