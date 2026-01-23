# Description: This python module has three functions that have to no relativity to each other.
# The first is a Principal Cost Calculator, it uses three inputs Goal amount, annual interest, and number of years. Formula: P = Goal / (1 + interest) ** years
# The second takes in a positive integer from the user and then prints out a pattern.
# The last program uses a .txt file as its data source and then uses that data to output stats. 
# Sources: none

# Global Variable Used For Input Validation
validInput = False

# Principal Investment Calculator
def principal_investment():
    print('\n')

    print("#######################################")
    print("#                                     #")
    print("#   Principal Investment Calculator   #")
    print("#                                     #")
    print("#######################################")

    global validInput

    while validInput == False:
        try:
            goalAmount = float(input("Goal Amount: $"))
            annualInterest = float(int(input("Annual Interest Rate: %")) / 100)
            numberOfYears = int(input("Number Of Years: "))

            principal = goalAmount / ((1 + annualInterest) ** numberOfYears)

            validInput = True
        except ValueError:
            print("Input Error - Please Re-Enter Valid Data!")
            print('\n')
        except:
            print("Something Went Wrong! Please Re-Enter Valid Data!")
            print('\n')

    print(f'Principal Needed: ${round(principal, 2)}')

    validInput = False

    print('\n')
    main()

# Pattern Generator
def pattern():
    
    print('\n')

    print("#########################")
    print("#                       #")
    print("#   Pattern Generator   #")
    print("#                       #")
    print("#########################")

    global validInput

    
    while validInput == False:
        
        try:
            highPoint = int(input("Highest Point: "))

            if highPoint >= 0:
                validInput = True
            else:
                print("High Point Must Be Greater Then 0")
                pass
                
            for point in range(1, (highPoint * 2)):
                # Checks if highest point was passed, once it was it then calculates how many points are needed to be subtracted to give decreasion affect. 
                if point <= highPoint:
                    print('*' * point)
                else:
                    print('*' * (highPoint - (point - highPoint))) 
        except ValueError:
            print("Highest Point Must Be A Integer & Greater Then 0")
    

    validInput = False
    print('\n')
    main()

# Statistics Based On Static Data From A .txt File 
def stats():

    print('\n')

    print("##################")
    print("#                #")
    print("#   Statistics   #")
    print("#                #")
    print("##################")

    global validInput
    sum, avg, count = 0, 0, 0
    minNum, maxNum = 0, 0

    with open('./cit160reviewdata.txt', "r") as txtNumbers:
        for line in txtNumbers:
            number = float(line.strip("\n"))

            if count == 0:
                minNum, maxNum = number, number
            else:

                # Setting New Min and Max If Needed
                if number < minNum:
                    minNum = number
                if number > maxNum:
                    maxNum = number

            # Getting Sum & Keeping Count For Average
            sum += number
            count += 1

    print(f'Sum: {round(sum, 2)}')
    print(f'Average: {round((sum / count), 2)}')
    print(f'Minimum: {minNum}')
    print(f'Max: {maxNum}')

    print('\n')
    main()

# Entry Point
def main():

    print("############# Functions #############")
    print("# 1. Principal Investment Fucntion  #")
    print("# 2. Pattern Function               #")
    print("# 3. Stats Function                 #")
    print("# 4. Exit                           #")
    print("#####################################")

    strAnswer = input("Function: ")
    while strAnswer != '1' and strAnswer != '2' and strAnswer != '3' and strAnswer != '4':
        print("Choose Function 1, 2, or 3")
        strAnswer = input("Function: ")

    match strAnswer:
        case '1':
            principal_investment()
        case '2':
            pattern()
        case '3':
            stats()
        case '4':
            print("Goodbye!")

if __name__ == '__main__':

    main()
