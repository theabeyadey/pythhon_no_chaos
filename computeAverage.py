sum_of_numbers = 0

number = int(input("Enter a valid number: "))

counter = 1
sum_of_numbers = 0 + number

while number!= -1:
    number = int(input("Enter a valid number(Enter -1 to stop): "))
    sum_of_numbers +=number
    counter += 1

    average = sum_of_numbers / counter

    print("Average is",average)

