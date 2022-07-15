#********************************************************************
 #                                                                  
 #  Team Edge List Mini-project: FOR LOOP CHALLENGES
 # 
 #   Complete the following loop challenges below. Follow the ToDos
 #   1. COUNTER: Write a loop that prints a happy birthday message for every
 #      year you have been alive.
 #   2. ITERATOR: Write a for for loop that prints every item in a list

 #   3. EVEN COUNTDOWN: Write a for loop that counts down from 100 to 0, 
 #      printing only the odd numers
 #   4. FINDER: Write a function that takes in a list and a word and prints 
 #      CONGRATULATIONS!! if the word is found in the list
 #   5. NESTED: Write a function that logs every letter in a sentence
 # 
 # ***************************************************************/
from json.encoder import INFINITY
import random

print("------------------- CHALLENGE 1 : COUNTER -------------------")

#this list prints every number between 0 and 10, using range

for x in range(11):
    print("Counter at: " + str(x))
   

#-->TODO: Write a loop that prints a happy birthday message for every year you have been alive.
for x in range(16):
    print("Happy Birthday #"+str(x))


print("------------------- CHALLENGE 2 : ITERATOR ----------------------")

#here is a list full of colors...
colors = ['red' , 'violet' , 'cyan' , 'pink' , 'lime' , 'white' , 'yellow', 'black' , 'magenta', 'green', 'orange']

#This is how you can iterate through a list:
for x in colors:
    print("The color is: " + x)

#-->TODO: Declare a list with at least 5 animals. You provide the animals.
animals = ["cow", "frog", "bird", "dog", "cat"]

#-->TODO: Print all the animals in the array with a for loop. 
for animal in animals:
    print(animal)


print("------------------- CHALLENGE 3 : EVEN COUNTDOWN ------------------")


#The line below makes a random number between 0-50 and assigns it to the random variable
random = random.randint(0, 50)

#this if/else statement checks if the number is even using the modulo operator (%)
if random % 2 == 0:
    print(str(random) + " is even!")
else:
    print(str(random) + " is odd!")

#-->TODO: Write a function that counts BACKWARDS from 100 and prints only even numbers
def even_countdown():
    for num in range(100, 0, -1):
        if num % 2 == 0:
            print(num)

even_countdown()
#-->TODO: Write a function that counts BACKWARDS from the given random number and prints only odd numbers

def odd_countdown(random):
    for num in range(random, 0, -1):
        if num % 2 != 0:
            print(num)

odd_countdown(random)

print("------------------- CHALLENGE 4 : Finder ------------------")

#This code uses the in operator to see if an element exists in a list. It only has to appear once.
color = input('Type a one word color and see if it is one of my favorite colors! >> ')
if color in colors:
    print("Yes, that color is a fav")
else:
    print("No, that color is not one of my favorites")

#-->TODO Declare a list of any strings you  want: cities, friends, movies, etc.
cities = ["Athens", "New York", "Philedelphia", "Miami"]


#-->TODO Write function to prompt the user to "Guess" if an element is present in your list. Store their response in a variable. 
#   --> If their guess is in your list, print CONGRATULATIONS!
def guess():
    city = input('Type a city and see if it is in my list of cities! >> ')
    if city in cities:
        print("Yes, it's there!")
    else:
        print("No, that city is not in my list of cities")

#-->TODO Call your function.
guess()


print("------------------- CHALLENGE 5 : Nested ------------------")

#this is how you get the length of a word:
big_word = "antidisestablishmentarianism"
print(f"{big_word} has {len(big_word)} letters")

#this is how you can nest for loops, one inside the other! These loop through all the colors, and then through all the characters in the color
for color in colors:
#for all the colors:
    print(color)
    for c in color:
        print(" - " + c) #log each letter. Remember, a string is also an array of characters.


#-->TODO Write a function that prints every letter in a sentence that a user enters.
def print_characters():
    sentence = input("Please write me a sentence. I'll spell it back to you!")
    sentence = sentence.split()
    for word in sentence:
        for letter in word:
            print(" - " + letter)
    #adding this for up-challenge below: 
    find_min_word(sentence)
    #find_min_word_multiple(sentence)



#-->CHALLENGE: Let the user know which word is the shortest one!
#There are better ways to solve this but I've kept to what the students would already know
#An additional challenge would be to print all the words if there are multiple of the same min length
def find_min_word(sentence):
    min_length = INFINITY
    min_word = ""
    for word in sentence: 
        if len(word) < min_length: 
            min_length = len(word)
            min_word = word
    
    print(f"The shortest word is {min_word}")

#print_characters()

#Not required. Fun up-challenge: 
def find_min_word_multiple(sentence):
    min_length = INFINITY
    min_words = []
    for word in sentence: 
        if len(word) < min_length: 
            min_length = len(word)
            min_words = []
            min_words.append(word)
        elif len(word) == min_length: 
            min_words.append(word)
    print(f"The shortest word(s) is/are {min_words}")

#Call print_characters() down here to avoid NameError for find_min_word functions:
print_characters()