def evens_and_odds(number):
 """Counts the number of even and odd digits in a positive integer.

 Args:
   number: A positive integer.

 Returns:
   A string containing the counts of even and odd digits.
 """

 even_count = 0
 odd_count = 0

 while number > 0:
   #digit = number % 10
   if number % 2 == 0:
     even_count += 1
   else:
     odd_count += 1
   number //= 10

 return f"The number of odds are {odd_count}.\nThe number of evens are {even_count}."

print(evens_and_odds(100))  # Output: The number of odds are 50.\nThe number of evens are 51.
