import random

wordDict = {'American Cities':['Denver','Malibu','Atlanta','Chicago','Orlando','Savannah','Nashville'], \
            'Holidays': ['Christmas','Easter','Valentines Day','Independence Day','Thanksgiving'], \
            'Colors': ['green','red','orange','blue','purple','brown','prink','black'], \
            'Foods': ['pizza','hotdog','hamburger','pasta','steak','soup','chicken']}

from unicodedata import category, name
name=input("Player name?")
print("Good luck!", name)

def askCat (wordDict):
    category = str( input ("To start the game, please choose a category: \n American Cities (A), Holidays(H), Colors(C), Foods (F) "))
    print()
    if category == 'A':
        print ("You chose the American Cities category.")
        print("your word is the name of an American city use correct capitalization")
        cat = (wordDict['American Cities'])
    elif category == 'H':
        print ("You chose the Holidays category.")
        print("Your word is a holiday use correct capitalization.")
        cat = (wordDict['Holidays'])
    elif category == 'C':
        print ("You chose the Colors category.")
        print ("Your word is a color")
        cat = (wordDict['Colors'])
    elif category == 'F':
        print ("You chose the Foods category.")
        print("Your word is a type of food")
        cat = (wordDict['Foods'])
    else:
        print ("You entered an invalid category. Try again!")
        print()
        askCat(wordDict)
    return random.choice(cat)

#Print random word
randWord = askCat(wordDict)
word=(randWord)
from unicodedata import category, name



repeat = True 
while repeat == True :

 
    print("Your word has", len(word), "letters.")


    guesses = '7'
    turns = 7

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1

        if failed == 0:
            print("You Win")
            print("The word is: ", word)
            break


        guess = input("Guess your word:")

    
        guesses += guess


        if guess not in word:

            turns -= 1

          
            print("Incorrect")

            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You are out of guesses and you lose the game! The correct word was " + word )
                play_again = input("Would you like to play again? Type Y for yes and N for No!")
                if play_again == "N":
                    repeat = False
                        
