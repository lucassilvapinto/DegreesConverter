pi = 3.14159
graus = 180

while True:
    while True:
        rad = input("Digit your radian number?\n")
    
        try:
            rad = float(rad)
            break  # Exit loop if conversion is successful
        except ValueError:
            print("Error: Please input a valid number.")

    answer = rad * (graus/pi)
    print("Your radians converted into degrees are: ", answer)
    restart = input("Press Enter to close the window or 1 and ENTER to reset the program...")

    if restart != "1":
        break