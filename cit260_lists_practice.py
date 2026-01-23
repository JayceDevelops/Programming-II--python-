# Description: This module has 3 functions. The first generates an list with populated with random number from 1-100 (inclusive) then prints out characteristics of the list. 
# The second takes in 5 lists as parameters nouns, adjectives, verbs, prepositions, and articles and then creates a sentence using random words within those lists
# The last funtion uses static data from a two types of files (user chooses) and then prints a letter grade for that data
# Sources: none

import random

# Generates An Array Of n Size Then Prints Out Characteristics Of The Array 
def randomNumArray(num):

    array = []

    # Adding Random Numbers Between 1 and 100 (Inclusive) To Array
    for index in range(num):
        array.append(random.randint(1, 100))

    # Start To Printing Characteristics Of Array
    print('List: ', end='')
    print(*array)

    print('Reverse: ', end='')
    print(*array[::-1])

    print('Odd Indexes: ', end='')
    print(*array[1::2])

    print('Even Elements: ', end='')
    for number in array:
        if number % 2 == 0:
            print(number, end=' ')
            
    print('\nFirst, Middle, Last: ', end='')
    print(array[0], end=' ')
    if len(array) % 2 == 0:
        middle = int(len(array) / 2)
        print(str(array[middle - 1]) + ' ' + str(array[middle]), end=' ')
    else:
        print(str(array[int(len(array) / 2)]), end=' ')
    
    print(str(array[-1]), end=' ')

# Generates Sentences Given Nouns, Adjectives, Verbs, Prepositions, and Articles
def sentenceGenerator(nouns, adjectives, verbs, preps, articles):
    return random.choice(articles) + ' ' + random.choice(adjectives) + ' ' + random.choice(nouns) + ', ' + random.choice(verbs) + ' ' + random.choice(preps) + \
    ' ' + random.choice(articles) + ' ' + random.choice(adjectives) + ' ' + random.choice(nouns) 

# Uses Static Data Given In A .txt File Chosen By The User Then Outputs Letter Grades Depending On Percentage Grade
def gradeCalculator(file):

    grades = []

    with open('./practice02/' + file) as txtFile:
        lines = txtFile.readlines() 

        for line in lines:
            grades.append(line.strip('\n'))

    best = float(max(grades))
    studentGrade = ''

    for grade in range(len(grades)):
        if float(grades[grade]) >= best - 15:
            studentGrade = 'A'
        elif float(grades[grade]) >= best - 25:
            studentGrade = 'B'
        elif float(grades[grade]) >= best - 35:
            studentGrade = 'C'
        elif float(grades[grade]) >= best - 45:
            studentGrade = 'D'
        else:
            studentGrade = 'F'
        
        print(f'Student {grade + 1} score is {grades[grade]} and grade is {studentGrade}')

def main():

    valid = False

    print("######## Functions #########")
    print("#                          #")
    print("#  1. Random Number Array  #")
    print("#  2. Sentence Generator   #")
    print("#  3. Grade Calculator     #")
    print("#  4. Exit                 #")
    print("#                          #")
    print("############################")

    answer = input("Function: ")

    while answer != '1' and answer != '2' and answer != '3' and answer != '4':
        print("Input Error - Please Enter 1, 2, 3 or 4")
        answer = input("Function: ")
    
    match answer:

        case '1':
            while valid == False:
                try:
                    number = int(input("Size: "))
                    if number > 0:
                        randomNumArray(number)
                        print('\n')
                        valid = True
                except ValueError:
                    print("Input Error: Data Must Be A Integer and Greater Then 0")

            valid = False
            pass

        case '2':

            nouns = ["cat", "river", "city", "teacher", "music",
                     "mountain", "computer", "book", "car", "tree",
                     "child", "dog", "house", "phone", "idea",
                     "ocean", "friend", "food", "sun", "road"]
    
            adjectives = ["happy", "bright", "quiet", "fast", "cold",
                          "warm", "brave", "curious", "tall", "short",
                          "strong", "gentle", "smart", "lazy", "funny",
                          "serious", "kind", "loud", "fun", "rude"]
    
            verbs = ["run", "jump", "think", "eat", "sleep",
                     "read", "write", "sing", "drive", "build",
                     "watch", "listen", "create", "learn", "teach",
                     "play", "walk", "talk", "swim", "climb"]
    
            prepositions = ["above", "across", "against", "among", "around",
                            "before", "behind", "below", "beneath", "beside",
                            "between", "during", "inside", "near", "outside",
                            "over", "through", "toward", "under", "within"]
    
            articles = ["the", "a"]

            for i in range(5):
                print(sentenceGenerator(nouns, adjectives, verbs, prepositions, articles))
        
        case '3':
            
            file = input("Filename With Student Data: ")

            while file != 'grades1.txt' and file != 'grades2.txt':
                print("File Not Found!")
                file = input("Filename With Student Data: ")

            gradeCalculator(file)
    
    if answer != '4':
        print('\n')
        main()
    else:
        print("Goodbye!")
    

if __name__ == '__main__':
    main()