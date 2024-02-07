#Create a program that swaps the values of two variables.

#Gather input
a = input('Enter the first value: ')
b = input('Enter the second value: ')

#Before swap
print('Before swapping: ' + a + ', ' + b)

#Find the middleman
c = a

#Swap
a = b
b = c

#After swap
print('After swapping: '+ a +', ' + b)
