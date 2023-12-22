age = [22, 19, 24, 25, 26, 24, 25, 24]
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = list(age)
print(len(age) == len(ages)) # True: so they are of the same length

# 2. Explain the difference between the following data types: string, list, tuple and set
'''
* String data type is the data type that holds textual values
* List is a collection of multiple data type, it is mutable, and can hold duplicate values.
* Tuple is like list but is immutable
* Set is also like a list but it cannot hold duplicate values.
'''
# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
sentence_spl = sentence.split()
unique_words = set(sentence_spl)
print('The unique words are ', len(unique_words), ' in number')
print('The unique words are: ', unique_words)
