# 1. Create an empty tuple
tpl = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Jafar', 'Mustapha')
sisters = ('Jamila', 'Amina', 'Nusaiba', 'Maryam')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4. How many siblings do you have?
len(siblings)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Adam', 'Aisha')
family_members = siblings + parents
family_members