# 1. Declare an empty list
lst = list()

# 2. Declare a list with more than 5 items
lst = [1,2,3,4,5,6,7]

# 3. Find the length of your list
print(len(lst))    # 7

# 4. Get the first item, the middle item and the last item of the list
print(lst[0])
print(lst[3])
print(lst[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status,address)
mixed_data_types = ['surajo', 26, 1.65, 'single', 'Giwa']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google,Microsoft, Apple, IBM, Oracle and Amazon.
it_companies= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
first = it_companies[0]
mid = it_companies[3]
last = it_companies[-1]
print(first, mid, last)

# 10. Print the list after modifying one of the companies
it_companies[4] = 'DanGote'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Twitter')
it_companies

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4,'WhatsApp')
it_companies

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2].upper() # MICROSOFT

# 14. Join the it_companies with a string '#;  '
joined = '#;  '.join(it_companies)
print(joined)

# 15. Check if a certain company exists in the it_companies list.
exists = 'IBM' in it_companies
exists

# 16. Sort the list using sort() method
it_companies.sort()
it_companies

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
it_companies

# 18. Slice out the first 3 companies from the list
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[3:])

# 20. Slice out the middle IT company or companies from the list


# 21. Remove the first IT company from the list
it_companies.pop(0)
it_companies

# 22. Remove the middle IT company or companies from the list
it_companies.pop(5)
it_companies

# 23. Remove the last IT company from the list
it_companies.pop(len(it_companies)-1)
it_companies

# 24. Remove all IT companies from the list
it_companies.clear()
it_companies

# 25. Destroy the IT companies list
del it_companies

'''26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_lst = front_end + back_end
joined_lst

# 27. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined_lst.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
full_stack