#------------------------------------------------------------------------------
# File Name:    Dictionary Decoder
# Date:         03/02/2026
#------------------------------------------------------------------------------

# Used for regular expressions
import re

# Used to give CLI a cool look
import time
import sys

# This is the encrypted string that you must convert back into a meaningful sentence.
ENCRYPTED = '342914-467980197300000-38412000-3885-13402296-67094560500-41358661344-62141664-33928155600-1102962420-685898930883600-9079200-92400-3767400-2905980-31082158140'

GREEN = '\033[92m'
RESET = '\033[0m'

def main():
    
    # Regex used to verify txt file is provided
    txtRegex = r'^([a-zA-Z_0-9]*)\.txt$'

    fileName: str = input("File Name: ")
    while not re.fullmatch(txtRegex, fileName):
        print()
        print("Error - Input Error")
        fileName = input("File Name: ")
    print()
    
    print("Processing data...")
    time.sleep(1)
    processedData: list[str] = processData(fileName)
    print(f"{GREEN}Success!\n")

    print(f"{RESET}Getting Word Count...")
    time.sleep(1)
    wordCount: dict = getWordCount(processedData)
    print(f"{GREEN}Success!\n")

    print(f"{RESET}Creating Decryption Keys...")
    time.sleep(1)
    decryptionKeys: dict = createDecryptionKey(wordCount)
    print(f"{GREEN}Success!\n")

    print(f"{RESET}Decrypting Data...")
    time.sleep(1)
    decryptedString: str = getDecryptedText(decryptionKeys)
    print(f'{GREEN}{decryptedString}')


# Reads a .txt file and then processes the data according to instruction
def processData(fileName: str) -> list:

    # Used to remove any puncuation
    specialCharRegex = r'[\'\,\!\?\-]{1}'

    processedData: list[str] = []

    # Opens .txt file then process the data 
    try:
        with open('practice05/' + fileName, 'r') as File:
        
            lines = File.readlines()
            
            for line in lines:

                # Lowers and Splits the line with ' '
                line = line.lower()
                words: list[str] = line.split()

                # Uses regex to check if the word contains puncuation and then removes it 
                # from the word and adds it to out processed data array
                for word in words:
                    punctuation: list[chr] = re.findall(specialCharRegex, word)
                    if len(punctuation) == 1:
                        word = word.replace(punctuation[0], '')
                    else:
                        for punct in punctuation:
                            word = word.replace(punct, '')
                    processedData.append(word) 

        return processedData

    except:
        print("File Not Found...")
        print("Goodbye...")
        
        # Ends program 
        sys.exit()

# Gets the count for each word in the given list of strings and returns in dictionary form
def getWordCount(data: list[str]) -> dict:
    wordCount = {}

    for word in data:
        if word not in wordCount:
            wordCount[word] = data.count(word)
    
    return wordCount

# Creates a dictionary storing the keys using the given alogirtm
def createDecryptionKey(data: dict) -> dict:
    
    decryptionKey: dict = {}

    for key in data:
        if data[key] > 1:
            encryptionNumber: int = 1
            encryptionNumber *= data[key]
            
            for char in key:
                encryptionNumber *= ord(char)
        
            decryptionKey[encryptionNumber] = key
    
    return decryptionKey

# Decrypts the key based on the given encrypted string 
def getDecryptedText(data: dict) -> str:
    global ENCRYPTED

    encryptedWords: list[str] = ENCRYPTED.split('-')
    words: list[str] = []

    for encryptWord in encryptedWords:
        encryptWord = int(encryptWord)
        if encryptWord in data:
            words.append(data[encryptWord])
    
    return ' '.join(words)

if __name__ == '__main__':
    main()