# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples in Python are both used to store values.

>> Lists are an ordered set of values and can be changed or reordered. Declared with square brackets [ ]

>> Tuples are different in that their values are immutable and cannot be changed after initiation. So its structure remains intact. Declared with parenthesis ( ). Being immutable also means that tuples can be used as keys in dictionaries.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are unordered lists that cannot consists of duplicates.  
>> A list of coins you have in your pocket could be:  
>> `[penny, penny, nickel, dime, dime, dim, quarter]`

>> But a set of the types of coins you have won't be duplicated.  
>> You'd have a set of `[penny, nickel, dime, quarter]`

>> Sets are much faster than lists to find an element because items in sets have unique values and can be hashed. Performance wise, it is in constant time. Performance for searching through a list depends on the length of the list

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's lambda functions allow you to define a quick anonymous function that can be used in arguments for other functions.  
>> For example, if I want to sort a list of numbers based on the right most digit, I can use a lambda function in the key argument of the sorted function.

>> `my_list = [15, 27, 51, 96, 39, 88, 60]`  
>> `print sorted(my_list, key = lambda x: x%10)`  
>> Will return: `[60, 51, 15, 96, 27, 88, 39]`

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a quick way to build lists based on certain criteria. It consists of square brackets containing expressions along with a number of for and if clauses.

>> For example: I want to cube all the multiples of 7 between 1 and 10000  
>> With list comprehensions, I simply do:  
>> `[x**3 for x in range(1,10001) if x%3==0]`  
>> With map and filter, I will have to write:  
>> `map(lambda x: x**3, filter(lambda x: x%3==0, range(1,10001)))`  
>> In this case, list comprehension took 5.97ms, and map+filter took 6.04ms

>> List comprehensions are typically easier to read and is more pythonic, but in certain situations, `map` may have a slight edge in performance. Also, for complicated functions that do not fit in a lambda function, you will have to use map+filter.

>> Set comprehensions are performed similarly to list comprehensions except you use curly brackets { }, and the resulting list does not contain repeating values.  
>> For example, in a class of 500 students, I can find the set of grades that are lower than 60%  
>> `grades = [random.randint(0,100) for x in xrange(500)]`  
>> `failing_grades = {x for x in grades if x < 60}`

>> Dict comprehensions are also performed similarly, but instead of just defining values, you can define key:value pairs through list comprehensions.  
>> Let's say a student's extra credit points is unfairly based on the length of their name. I can make a dict with the students' names:extra credit points:  
>> `student = ['andrew', 'bob', 'carol', 'denise', 'ernie', 'francis', 'gertrude']`  
>> `extra_credit = {name:len(name) for name in student}`  
>> Result: `{'gertrude': 8, 'ernie': 5, 'andrew': 6, 'denise': 6, 'carol': 5, 'francis': 7, 'bob': 3}`


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7,850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
