age = 25
height = 1.75
complex = 1 + 3j

'''4. Write a script that prompts the user to enter base and height of the triangle and
calculate an area of this triangle (area = 0.5 x b x h).'''

b = int(input('Enter base: '))
h = int(input('Enter height: '))
area = 0.5 * h * b
print('The area of the triangle is ', area )

'''5. Write a script that prompts the user to enter side a, side b, and side c of the triangle.
Calculate the perimeter of the triangle (perimeter = a + b + c).
'''
# Taking user input
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

# Calculating the perimeter
perimeter = a + b + c
print(perimeter)

'''6. Get length and width of a rectangle using prompt. Calculate its area (area = length x
width) and perimeter (perimeter = 2 x (length + width))'''

# Prompting the user
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))

# calculating the area
area = length * width
print('The area is: ', area)

# calculating the perimeter
perimeter = 2 * (length + width)
print('The perimeter is ', perimeter)

'''7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and
circumference (c = 2 x pi x r) where pi = 3.14.'''

# Prompting the user 
r = int(input('Enter the redius: '))
pi = 3.14

# Calculating the area
area = pi * r ** 2
print('The area is ', area)


'''8. Calculate the slope, x-intercept and y-intercept of y = 2x -2'''

# Getting the data...
x = int(input('Enter the value of x:'))
 # Calculate the slope
y = 2 * x - 2
print('The slope is ', y)


'''9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2)
and point (6,10)
'''
x1, x2, y1, y2 = 2, 6, 2, 10
m = y2 - y1 / x2 - x1
print('The Slope = ', m)

'''10. Compare the slopes in tasks 8 and 9.'''
print('The comparism is: ', m == y)

'''11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out
at what x value y is going to be 0.
'''
x = int(input('Enter the x value: '))
y = x ** 2 + 6 * x + 9
print('The y value is ', y)

'''12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.'''
print(len('python') != len('dragon'))


'''13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
'''
print(('on' in 'python') and ('on' in 'dragon'))


'''14. I hope this course is not full of jargon. Use in operator to check if jargon is in the
sentence.'''
 
sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)


'''15. There is no 'on' in both dragon and python'''
'on' in 'python' and 'on' in 'dragon'

'''16. Find the length of the text python and convert the value to float and convert it to
string
'''

python_len = len('python')
print(python_len)

py_float = float(python_len)
print(py_float)

py_str = str(py_float)
print(py_str)


'''17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a
number is even or not using python?'''

num = int(input('Enter the number: '))
if num % 2 == 0:
    print('The given number is even')
else:
    print('The given number is not even')


'''18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.'''

print(7 // 3 == int(2.7))


'''19. Check if type of '10' is equal to type of 10'''
print(type('10') == type(10))

'''20. Check if int('9.8') is equal to 10'''
print(int('9.8') == 10)


'''21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of
the person?
'''
# Prompting the user for data
hour = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))

#Calculating the earning
earning = hour * rate
print('Your weekly earning is', earning)


'''22. Write a script that prompts the user to enter number of years. Calculate the number of
seconds a person can live. Assume a person can live hundred years'''

# Prompting the for info...
years = int(input('Enter the number of years you have lived: '))
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print('You have lived for ', seconds, 'seconds')


'''23. Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125 '''
