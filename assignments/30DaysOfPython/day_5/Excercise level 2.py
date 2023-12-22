''' 
Exercises: Level 2
1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
'''
'''Sort the list and find the min and max age'''
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min(ages)
max(ages)

'''Add the min age and the max age again to the list'''
ages.append(min(ages))
ages.append(max(ages))
ages

'''Find the median age (one middle item or two middle items divided by two)'''
ages.sort()
ages[5] + ages[6] / 2

'''Find the average age (sum of all items divided by their number )'''
average = sum(ages)/len(ages)
average

'''Find the range of the ages (max minus min)'''
range = max(ages) - min(ages)
range

'''Compare the value of (min - average) and (max - average), use abs() method'''
comp1 = min(ages)-average 
comp1
comp2 = max(ages)-average
comp2

'''1. Find the middle country(ies) in the countries list'''

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'] 
mid = len(countries)//2
countries[mid]


''' 2. Divide the countries list into two equal lists if it is even if not one more country for the
first half.
'''
if (len(countries)%2 ==0):
    print('It is even')
else:
    countries.insert(0,'Nigeria')
countries

''' 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three
countries and the rest as scandic countries.
'''
Nigeria, China, Russia, *Scandic = countries
Scandic
