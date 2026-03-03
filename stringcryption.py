#------------------------------------------------------------------------------
# File Name:    stringcryption
#------------------------------------------------------------------------------
import hashlib
import answers # Needed to import the functions from the answers module
import re # Regular Expression Module Used For Data Validation In This Module

# Global Counter
caseCount = 1

def main():

    global caseCount

    encryptedData: list[str] = readData()
    #print(answers.case_one_step_zero(encryptedData[0]))
    #print(answers.case_two_step_zero(encryptedData[1]))

    userSubstr = input("Substring To Remove: ")
    substrRemovedData: list[str] = removeSubstr(encryptedData, userSubstr)
    #print(answers.case_one_step_one(substrRemovedData[0]))
    #print(answers.case_two_step_one(substrRemovedData[1]))

    lowercaseData: list[str] = lowercaseElements(substrRemovedData)
    #print(answers.case_one_step_two(lowercaseData[0]))
    #print(answers.case_two_step_two(lowercaseData[1]))

    reversedData: list[str] = reverseData(lowercaseData)
    #print(answers.case_one_step_three(reversedData[0]))
    #print(answers.case_two_step_three(reversedData[1]))

    zRemoved: list[str] = removeZ(reversedData)
    #print(answers.case_one_step_four(zRemoved[0]))
    #print(answers.case_two_step_four(zRemoved[1]))

    noOddIndexes: list[str] = removeOddIndexes(zRemoved)
    #print(answers.case_one_step_five(noOddIndexes[0]))
    #print(answers.case_two_step_five(noOddIndexes[1]))

    removedBackHalf: list[str] = removeBackHalf(noOddIndexes)
    #print(answers.case_one_step_six(removedBackHalf[0]))
    #print(answers.case_two_step_six(removedBackHalf[1]))

    splitData: list[list[str]] = splitEncryptedData(removedBackHalf)
    #print(answers.case_one_step_seven_first_word(splitData[0][0]))
    #print(answers.case_two_step_seven_first_word(splitData[1][0]))

    print()
    print("Step 8 Verification".center(50, '-'))

    for row in range(len(splitData)):
        print(f"Case {caseCount} Last English Word: {splitData[row][-2]}")
        caseCount += 1
    
    print("".center(50, '-'))
    print()

# Reads The Encrypted Data From User Specified File
def readData() -> list[str]:

    global caseCount
    caseCount = 1

    # Regex to user input follows .txt file path format 
    TXT_REGEX: str = r'^([a-zA-Z_0-9]*)\.txt$'

    # Retrieves text file location, if format not correct then inform user and have them re-enter path
    print()
    path: str = input("File To Decrypt: ")
    while not re.fullmatch(TXT_REGEX, path):
        print()
        print("!!!! Invalid Text File Path Format !!!")
        path: str = input("File To Decrypt: ")

    # Trys to read txt file if found, if not program ends
    try:
        encryptedStrings: list[str] = []
        with open('practice04/' + path, 'r') as file:
            print()
            print("Step 0 Validation".center(50, '-'))

            for line in file:
                encryptedStrings.append(line.strip())
                print(f"Case {caseCount} File Read Valid: True")
                caseCount += 1

            print("".center(50, '-'))
            print()

        return encryptedStrings
    except:
        print("File Not Found!" + '\n' + "Goodbye!...")

# Removes Substring Given By User From An Array Passed In 
def removeSubstr(encryptedStrings: list[str], substr: str) -> list[str]:
    
    global caseCount
    caseCount = 1

    validatedStrings: list[str] = []

    print()
    print("Step 1 Validation".center(50, '-'))

    # Goes through each index and replaces the substring within the element with ""
    for data in encryptedStrings:
        if substr in data:
            validatedStrings.append(data.replace(substr, ""))
            print(f"Case {caseCount} Remove Substring Valid: True")
        else:
            print(f"Case {caseCount} Remove Substring Valid: False")
            print(f"   --> Reason: Data Does Not Contain Substring")
        caseCount += 1

    print("".center(50, '-'))
    print()

    return validatedStrings

# Takes An Array As A Parameter And Then Lowercases All The Elements Within The Array
def lowercaseElements(data: list[str]) -> list[str]:

    global caseCount
    caseCount = 1

    lowercaseList: list[str] = []

    print()
    print("Step 2 Validation".center(50, '-'))

    for string in data:
        # Checking to see if string is already lowercase
        if string.lower() != string:
            lowercaseList.append(string.lower())
            print(f"Case {caseCount} Lowercase Valid: True")
        else:
            print(f"Case {caseCount} Remove Substring Valid: False")
            print(f"   --> Reason: Data Already Lowercase")
        caseCount += 1

    print("".center(50, '-'))
    print()

    return lowercaseList

# Interates through list of strings and returns those elements reversed
def reverseData(data: list[str]) -> list[str]:
    
    global caseCount
    caseCount = 1

    reverseList: list[str] = []

    print()
    print("Step 3 Validation".center(50, '-'))

    for string in data:
        reverseList.append(string[::-1])
        print(f"Case {caseCount} Reverse Valid: True")
        caseCount += 1

    print("".center(50, '-'))
    print()

    return reverseList

# Removes all occurences of 'z' in the strings given in list parameter
def removeZ(data: list[str]):
    
    global caseCount
    caseCount = 1

    removedZ: list[str] = []

    print()
    print("Step 4 Validation".center(50, '-'))

    for string in data:
        removedZ.append(string.replace('z', ''))
        print(f"Case {caseCount} Removed z Valid: True")
        caseCount += 1

    print("".center(50, '-'))
    print()

    return removedZ

# Removes all the elements at odd indexes 
def removeOddIndexes(data: list[str]):

    global caseCount
    caseCount = 1

    removedOddIndexes: list[str] = []

    print()
    print("Step 5 Validation".center(50, '-'))

    for string in data:
        finalStr = ""
        for char in range(len(string)):
            if char % 2 == 0:
                finalStr += string[char]
        removedOddIndexes.append(finalStr)
        print(f"Case {caseCount} Removed Odd Indexes Valid: True")
        caseCount += 1

    print("".center(50, '-'))
    print()

    return removedOddIndexes

# Removes the back half of each element
def removeBackHalf(data: list[str]):

    global caseCount
    caseCount = 1

    removedBackHalf: list[str] = []

    print()
    print("Step 6 Validation".center(50, '-'))

    for string in data:
        removedBackHalf.append(string[:int(len(string)/2)])
        print(f"Case {caseCount} Removed Back Half Valid: True")
        caseCount += 1

    print("".center(50, '-'))
    print()

    return removedBackHalf

# Interators through each element and splits it by "ppqq" and appends the returned list to a multi-dimensional list which is lated returned 
def splitEncryptedData(data: list[str]):
    global caseCount
    caseCount = 1

    splitedData: list[list[str]] = []

    print()
    print("Step 7 Validation".center(50, '-'))

    for string in data:
        splitedData.append(list(filter(None, string.split(sep="ppqq"))))
        
        print(f"Case {caseCount} Split Valid: True")
        caseCount += 1

    print("".center(50, '-'))
    print()

    caseCount = 1
    return splitedData

# Make sure this is at the BOTTOM of all your code.
# DO NOT DELETE THIS IF STRUCTURE
if __name__ == '__main__':
    main()