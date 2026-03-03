#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------
import hashlib

# Are these numbers in the fibonacci sequence?
x = 77142615991003007354243408787406820707977283561965144160477401245880193574283190293286151
y = 2422308238804407089268820758059737271890428034963283291423237466738923487762205937312441964529423332944990116110066323372235058978516564015277004931960761593992730308301490464065917906637454573375206452747367

# What index does this number appear?
z = 884548379995562146692720280949741243263467182475990183992006298527509912670654663590551486122598203154881041207985796182382599539256662230264617810473262323420985956746547993465233151687321709521866741492587022459666601708131634932488688871154362616245306898815287252692135942975866382629498070437613552693782925210641989151202357859414187356314513837425644360293025247504804600339407712169043164374073924491997885387787641955054909791254287516181726553196839207252315507013004470053064086200152403056776221918532828288607111482119606070529773344709928199663528953303782516138620539955475248087100911372720359418162984851861625141863826095937423295853623890698159942895855394258593344260791140587891790909244377113965675207740518232009964371022074958903037297990485786484204974346116498396002411876388478479732827747489619592796722961111670917412557783262121622531597914774590881138628499819479362342690281188174717590762789431367159729476655006706455138178871407944226161209084601330748130790145495060565515481125121457191153670774857779310971076514616173850288116261704301346892938285482917335440310419298208767477414902070346968900256274315393933349834500789941917449854407163861320751858731348522454938216209493500632104768433189487015091564482508500145870254629920365165728823656353643933402083229475305591378265543360450009250

# Number of indexes to generate of the Fibonacci Sequence.
# NOTE: The first index is F0
N = 7000

# global list
fibList = [0, 1]

# The main logic of your assignment belongs here.
def main():
    createList()
    write500Fib()
    findNumber(x)
    findNumber(y)
    findNumber(z)
    tenthPrime()
    pass

# Your functions go here========================================================

# Generates Fibonacci List
def createList():
    global fibList

    print(f"Generating Fib Sequence Up To The {N}th Element")
    for i in range(1, N):
        fibList.append(int(fibList[i] + fibList[i - 1]))

# Writes The First 500 Indexes Of The Fibonacci List To fib.txt
def write500Fib():
    global fibList

    if len(fibList) >= 500:
        print("Saving First 500 Elements To fib.txt")
        with open('fib.txt', 'w') as file:
            for num in range(500):
                file.write(str(fibList[num]) + '\n')
    else:
        print("List Not Long Enough")

# Prints The Element At Index 420
def checkValueAt420():
    global fibList

    if len(fibList) >= 420:
        print(f"The Element At Index 420 Is {fibList[420]}")
    else:
        print("List Not Long Enough")

# Prints The Element At Index 6515
def checkValueAt6515():
    global fibList

    if len(fibList) >= 6515:
        print(f"The Element At Index 420 Is {fibList[6515]}")
    else:
        print("List Not Long Enough")

# Prints If X Is A Fib Number Or Not Using 
def findNumber(num: int) -> None:
    global fibList

    if fibList.count(num) > 0:
        print(f"The Number {num} Is A Fibonacci Number")
    else:
        print(f"The Number {num} Is Not A Fibonacci Number")
    print('\n')

# Prints The Tenth Prime Number In fibList
def tenthPrime():
    global fibList

    for i in range(3, len(fibList)):
        if is_tenth_prime(fibList[i]):
            print(f"The Tenth Prime Number In The Fibonacci Sequence Is {fibList[i]}")
    
# END of your functions=========================================================


# Predefined Functions (DO NOT CHANGE)==========================================

# Given an integer as an argument it returns True if the number is correct
# or False if the number is incorrect. 
def is_420(number: int) -> bool:
    guess = str(number)                         #cast arg to a string
    result = hashlib.md5(guess.encode())        #change into ASCII, generate MD5 hash
    
    #compare resulting hash from argument to the correct answer hash
    if result.hexdigest() == "600db279e9c650b544ab43cfd45998c9":
        return True
    
    return False

# Given an integer as an argument it returns True if the number is correct
# or False if the number is incorrect. 
def is_6515(number: int) -> bool:
    guess: str = str(number)
    result = hashlib.md5(guess.encode())

    if result.hexdigest() == "1d55d9d2fce920bffc55f1a7665f6c4e":
        return True
    
    return False

# Given an integer as an argument this returns True if the number is correct
# or False if the number is incorrect. 
def is_tenth_prime(number: int) -> bool:
    guess: str = str(number)
    result = hashlib.md5(guess.encode())

    if result.hexdigest() == "55d0ef4ee6ca383c6f6251a180aec199":
        return True
    
    return False

#===============================================================================

if __name__ == '__main__':
    main()