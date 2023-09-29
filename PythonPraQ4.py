#Q.4 Write a Python Program to multiply all the numbers in a list.
def multipyallnumbers(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total
print(multipyallnumbers((7, 21, 12, 9, 10)))
print(multipyallnumbers((4, 13, 67, 20, 32)))