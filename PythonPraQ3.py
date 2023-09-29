#Q.3 Write a Python Program to sum all the numbers in a list.
def sumofnumbers(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
print(sumofnumbers((5, 8, 0, 3, 6)))
print(sumofnumbers((7, 11, 15, 23, 1)))
