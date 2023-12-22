it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Samsung', 'Verison', 'Tecno'])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)

# 5. What is the difference between remove and discard

# Unlike remove(), the discard() method does not raise an exception when an element is missing from the set.