#Write a function to count the number of vowels in a given string 

#My assumption is that y is not a vowel
#Create a function
def count_the_vowels():
    count = 0
    word = input('Enter your word: ')
    #Create a loop to check the vowels existed
    for char in word:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            count += 1
        else:
            continue
    print('The number of vowels from the input is:', count)

count_the_vowels()    