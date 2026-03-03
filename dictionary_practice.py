#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

def main():

    statesAndCities: dict[str] = {}
    with open('activity05/activity05_data.txt', 'r') as file:
        for line in file:
            line = line.strip().split(',')
            statesAndCities[line[1]] = line[0]

    statesAndCities['NV'] = "Los Vegas"

    printDict(statesAndCities)
    print()

    del statesAndCities["NV"]

    statesAndCities = dict(sorted(statesAndCities.items()))
    print("Sorted".center(50, '-'))
    printDict(statesAndCities)

    letter = input("Enter First Letter Of State: ")
    searchDict(letter, statesAndCities)

# Prints Dictionary Passed To It
def printDict(dictionary: dict[str]):
    print("State     City")
    print()
    for key in dictionary:
        print(str(key) + "        " + str(dictionary[key]))

# Searches Dictionary Based On User Input
def searchDict(firstLetter: str, dictionary: dict[str]):
    newDictionary = {key:dictionary[key] for key in dictionary if key[0] == firstLetter}
    print(newDictionary)

if __name__ == "__main__":
    main()