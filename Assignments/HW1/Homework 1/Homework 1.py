# Alireza Rafiei | HW1 | NLP

### ........................ Problem #1 ........................ ###

'''
1.
a) Run the script from session 1 and review the different tasks we covered.
Done.

b) Modify the code for each task run the code.
Done.

c) Look up the documentation for lists, dictionaries and strings.
Done.

d) We discussed a little about dictionaries during the session. We only looked at the basic dictionary. Are there other types of dictionaries? What is a defaultdict?
In Python, the basic dictionary (dict) is the most commonly used, but there are several other types of dictionaries provided in the Python Standard Library 
that offer specific features beyond the basic dictionary. They are:

    - OrderedDict: The OrderedDict class preserves the order in which items are inserted, making it 
            useful when the insertion order is important.

    - Counter: This is a dictionary subclass for counting hashable objects. It's a collection where 
            elements are stored as keys and their counts as values.

    - ChainMap: This class is used for quickly linking multiple mappings, so the user can treat them as 
            a single unit. It is often much faster than creating a new dictionary and running 
            multiple update() calls.

    - MappingProxyType: This is a wrapper for making read-only dictionaries. It is generally used to create immutable versions of dictionaries.

defaultdict: This type of dictionary allows the user to specify a default value for the dictionary when a key is not found. 
        It's especially useful when the user appending to nested lists or adding up counts.
'''


### ........................ Problem #2 ........................ ###

'''
2. 
a) Write some code to initialize a list and fill it up with the first n values of the fibonacci sequence. n will be input by the user when the program runs.
'''

n = int(input("How many Fibonacci numbers would you like to generate? "))

fib_seq = []

# Generate the Fibonacci sequence
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    fib_seq.append(0)
elif n == 2:
    fib_seq.extend([0, 1])
else:
    fib_seq.extend([0, 1])
    for i in range(2, n):
        next_fibonacci = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fibonacci)

print("The first {} numbers of the Fibonacci sequence are: {}".format(n, fib_seq))


### ........................ Problem #3 ........................ ###

'''
3. A palindrome is a string that reads the same backwards and forwards. 
a) Write and run some code that checks if a given string is palindrome and prints the result on the screen
'''

print("\nproblem #3 -- Is this string palindrome?")

input_string = input("Enter a string to check if it's a palindrome: ")

# Remove any white spaces and convert to lower case for a case-insensitive and space-insensitive check
sanitized_string = input_string.replace(" ", "").lower()

# Check if the entered string is a palindrome
if sanitized_string == sanitized_string[::-1]:
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")


# Some other examples
string = 'rotstor'
if string == string[::-1]:
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")

string = 'apple'
if string == string[::-1]:
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")


### ........................ Problem #4 ........................ ###

'''
4. Python functions.
a) Look up how to write basic functions in python. 
Done.
b) Convert the previous code to a function. The string must be passed as a function parameter and the function will return True if the string is a palindrome.
'''

def Palindrome_check(given_string):
    
    """
The function checks whether a given string is palindrome or not.

Parameters:
    ----------
    string: str
        The given string that the user wants to check.

Return: 
    ---------
    A boolean variable:
        True: The string is palindrome.
        False: The string is palindrome.
    """

    if given_string == given_string[::-1]:
        palindrome = True
    else:
        palindrome = False
    
    return palindrome

# Providing some examples for a palindrome and a non-palindrome string
print("\nAre <rotator> and <apple> palindrome?")
rotator = Palindrome_check("rotator")
print('rotator {}'.format(rotator))
apple = Palindrome_check("apple")
print('apple {}'.format(apple))


### ........................ Problem #5 ........................ ###

'''
5. Consider the following lists.
names = ['Real Madrid','AC Milan','Manchester United’,’FC Barcelona','Bayern Munich', 'Liverpool FC’, 'Internazionale']
number_of_intl_titles = [14, 7, 3, 5, 6, 6, 3]
country = ['Spain', 'Italy', 'England', 'Spain','Germany', 'England', 'Italy']

The lists contain the names of soccer clubs from Europe, the number of European championships they have won and their countries of origin (in the same sequence).
a) Store the club names and number of titles in a dictionary with the club name as key and the number as the value.
b) Store the total number of titles per country in a dictionary- country as key and the sum of the titles as value.
c) Based on the data, which country has the lowest number of european titles? Which country has the highest? What is the average number of wins per country?
'''

names = ['Real Madrid', 'AC Milan', 'Manchester United', 'FC Barcelona', 'Bayern Munich', 'Liverpool FC', 'Internazionale']
number_of_intl_titles = [14, 7, 3, 5, 6, 6, 3]
country = ['Spain', 'Italy', 'England', 'Spain','Germany', 'England', 'Italy']

club_titles_dict = dict(zip(names, number_of_intl_titles))

print("\nClub names and their number of international titles:")
print(club_titles_dict)


titles_by_country = {}

for i in range(len(names)):
    current_country = country[i]
    current_titles = number_of_intl_titles[i]
    
    if current_country in titles_by_country:
        titles_by_country[current_country] += current_titles
    else:
        titles_by_country[current_country] = current_titles

print("Total number of international titles by country:")
print(titles_by_country)


lowest_country = min(titles_by_country, key=titles_by_country.get)
highest_country = max(titles_by_country, key=titles_by_country.get)

total_countries = len(titles_by_country)
total_wins = sum(titles_by_country.values())
average_wins = total_wins / total_countries

print()
print(f"The country with the lowest number of European titles is {lowest_country} with {titles_by_country[lowest_country]} titles.")
print(f"The country with the highest number of European titles is {highest_country} with {titles_by_country[highest_country]} titles.")
print(f"The average number of wins per country is {average_wins:.2f} titles.")