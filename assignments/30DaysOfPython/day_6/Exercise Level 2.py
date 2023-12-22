# 1. Unpack siblings and parents from family_members

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Banana', 'Orange', 'Apple')
vegetables = ('Tomato', 'Lettuse', 'Amaranth')
animal_products = ('Milk', 'Meat', 'Egg')
food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
food_stuff_lt

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
len(food_stuff_lt)/2
print('The middle item is', food_stuff_lt[4])

# 5. Slice out the first three items and the last three items from food_staff_lt list
print('the first three items are: ', food_stuff_lt[:3])
print('the last three items are: ', food_stuff_lt[-3:])

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
'Estonia' in nordic_countries

# Check if 'Iceland' is a nordic country
'Iceland' in nordic_countries