for thousands in range(1, 9):
    for tens in range(0, 9):
        for units in range(0, 9):

            number = (thousands * 100) + (tens * 10) + units
            sum_of_square = (thousands ** 2) + (tens ** 2) + (units ** 2)

            if sum_of_square == number:
                
                print(number)
