# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

# STEPS
# 1 Input
print('Word, Vowel and Consonant Counter!')
sentence = input('Sentence: ')
# 2 Loop
numVowels = 0
numNumbers = 0
numConsonants = 0
numWords = 1

for l in range(len(sentence)):
    
    if sentence[l] == 'a' or sentence[l] == 'e'or sentence[l] == 'i' or sentence[l] == 'o' or sentence[l] == 'u' or sentence[l] == 'A' or sentence[l] == 'E' or sentence[l] == 'I' or sentence[l] == 'O' or sentence[l] == 'U':
            numVowels = numVowels + 1
    elif sentence[l] == 'b' or sentence[l] == 'B' or sentence[l] == 'c' or sentence[l] == 'C' or sentence[l] == 'd' or sentence[l] == 'D' or sentence[l] == 'f' or sentence[l] == 'F' or sentence[l] == 'g' or sentence[l] == 'G' or sentence[l] == 'h' or sentence[l] == 'H' or sentence[l] == 'j' or sentence[l] == 'J' or sentence[l] == 'k' or sentence[l] == 'K' or sentence[l] == 'l' or sentence[l] == 'L' or sentence[l] == 'm' or sentence[l] == 'M' or sentence[l] == 'n' or sentence[l] == 'N' or sentence[l] == 'p' or sentence[l] == 'P' or sentence[l] == 'q' or sentence[l] == 'Q' or sentence[l] == 'r' or sentence[l] == 'R' or sentence[l] == 's' or sentence[l] == 'S' or sentence[l] == 't' or sentence[l] == 'T' or sentence[l] == 'v' or sentence[l] == 'V' or sentence[l] == 'w' or sentence[l] == 'W' or sentence[l] == 'x' or sentence[l] == 'X' or sentence[l] == 'y' or sentence[l] == 'Y' or sentence[l] == 'z' or sentence[l] == 'Z':
            numConsonants = numConsonants + 1
    elif sentence[l] == '1' or sentence[l] == '2' or sentence[l] == '3' or sentence[l] == '4' or sentence[l] == '5' or sentence[l] == '6' or sentence[l] == '7' or sentence[l] == '8' or sentence[l] == '9' or sentence[l] == '0':
            numNumbers = numNumbers + 1
    elif (sentence[l].isspace()) == True:
            numWords = numWords + 1
    
if sentence[-1].isspace() == True:
        numWords = numWords - 1

print('Vowels: ', numVowels)
print('Consonants: ', numConsonants)
print('Numbers: ', numNumbers)
print('Words: ', numWords)

