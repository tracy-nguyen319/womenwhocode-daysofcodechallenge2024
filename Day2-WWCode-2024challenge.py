#Create a program to calculate the area of a circle given its radius

#Import math library
import math

while True:
    #Get the radius and unit of length
    radius = input('Enter the radius of the circle:')
    unit = input('Enter the unit of length used (in or cm):')
    if unit != 'in' and unit != 'cm':
        print('Wrong input, please try again')
    else:
        #Convert to float
        try:
            r = float(radius)
            #Calculate the area in centimeter
            if unit == 'in':    
                area = math.pi*((2.54*r)**2)
            elif unit == 'cm':
                area = math.pi*r**2
            print('Area of the circle given radius', r, unit + ' is', area)
            break
        except:
            print('Wrong input, please try again')