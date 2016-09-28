Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # memory data is stored in variables
>>> #e.g.:
>>> player_name='Bob'
>>> wumpus_location= 2
>>> player_input= raw_input('>')
> I don't have a clue
>>> player_input
" I don't have a clue"
>>> # if statement
>>> if x==y :
	print 'x is equal to y'
if player_name=='Bob' :
	
SyntaxError: invalid syntax
>>> if x==y :
	print 'x is equal to y'
	if player_name=='Bob' :
		print 'Hello Bob!'
	else :
		print "Hey! You're not Bob"

		

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    if x==y :
NameError: name 'x' is not defined
>>> x=5
>>> y=3
>>> if x==y :
	print 'x is equal to y'
	if player_name=='Bob' :
		print 'Hello Bob!'
	else :
		print "Hey! You're not Bob"

		
>>> if x==y :
	print 'x is equal to y'
	if player_name=='Bob' :
		print 'Hello Bob!'
	else :
		print "Hey! You're not Bob"

		
>>> if player_name == 'Bob' :
	print : 'Hi Bob'
	
SyntaxError: invalid syntax
>>> if player_name == 'Bob' :
	print  'Hi Bob'
	else :
		
SyntaxError: invalid syntax
>>> if player_name == 'Bob' :
	print  'Hi Bob'
else : print 'Not Bob'

Hi Bob
>>> if x==y :
	print 'x is equal to y'
	if player_name=='Bob' :
		print 'Hello Bob!'

	
>>> 
>>> if x==y :
	print 'x is equal to y'
if player_name=='Bob' :
		print 'Hello Bob!'
		
SyntaxError: invalid syntax
>>> 
>>> if x==y :
	print 'x is equal to y'
if player_name=='Bob' :
		print 'Hello Bob!'
		
SyntaxError: invalid syntax
>>> if x==y :
	print 'x is equal to y'

>>> 
>>> if x == y :
	print 'x is equal to y'

	
>>> # yes they are not equal...
>>> if x==y :
	print 'x is equal to y'
	if player_name=='Bob' :
		print 'Hello Bob!'

		
>>> if x==y :
	print 'x is equal to y'

	if player_name=='Bob' :
		print 'Hello Bob!'

		
>>> if x==y :
	print 'x is equal to y'
		if player_name=='Bob' :
			print 'Hello Bob!'
			
  File "<pyshell#41>", line 3
    if player_name=='Bob' :
    ^
IndentationError: unexpected indent
>>> 
>>> if x==y :
	print 'x is equal to y'
	if player_name=='Bob' :
			print 'Hello Bob!'

			
>>> if x==y :
	print 'x is equal to y'
	if player_name=='Bob' :
		print 'Hello Bob!'

		
>>> if x==y :
print 'x is equal to y'
	if player_name=='Bob' :
print 'Hello Bob!'
  File "<pyshell#47>", line 2
    print 'x is equal to y'
        ^
IndentationError: expected an indented block
>>> if x==y :
	print 'x is equal to y'
	if player_name=='Bob' :
	print 'Hello Bob!'
	
  File "<pyshell#48>", line 4
    print 'Hello Bob!'
        ^
IndentationError: expected an indented block
>>> if x==y :
	print 'x is equal to y'
	if player_name=='Bob' :
		print 'Hello Bob!'

		
>>> if x==y :
	print 'x is equal to y'
		if player_name=='Bob' :
			print 'Hello Bob!'
			
  File "<pyshell#51>", line 3
    if player_name=='Bob' :
    ^
IndentationError: unexpected indent
>>> if x==y :
	print 'x is equal to y'
	 if player_name=='Bob' :
		print 'Hello Bob!'
		
  File "<pyshell#52>", line 3
    if player_name=='Bob' :
    ^
IndentationError: unexpected indent
>>> if x==y :
	print 'x is equal to y'
		if player_name=='Bob' :	print 'Hello Bob!'
		
  File "<pyshell#53>", line 3
    if player_name=='Bob' :	print 'Hello Bob!'
    ^
IndentationError: unexpected indent
>>> if x==y :
	print 'x is equal to y'
		if player_name=='Bob' :	print 'Hello Bob!'
		
  File "<pyshell#54>", line 3
    if player_name=='Bob' :	print 'Hello Bob!'
    ^
IndentationError: unexpected indent
>>> if x==y :
	print 'x is equal to y'
		if player_name=='Bob' :
			
  File "<pyshell#55>", line 3
    if player_name=='Bob' :
    ^
IndentationError: unexpected indent
>>> if x==y :
	print 'x is equal to y'
		if player_name=='Bob' : print 'no'
		
  File "<pyshell#56>", line 3
    if player_name=='Bob' : print 'no'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'
	if player_name = 'Bob' : print 'hi Bob'
	
  File "<pyshell#58>", line 2
    if player_name = 'Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'
if player_name = 'Bob' : print 'hi Bob'
SyntaxError: invalid syntax
>>> if x == y: print 'x = y'
 if player_name = 'Bob' : print 'hi Bob'
 
  File "<pyshell#60>", line 2
    if player_name = 'Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'
		if player_name = 'Bob' : print 'hi Bob'
		
  File "<pyshell#61>", line 2
    if player_name = 'Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'
    if player_name = 'Bob' : print 'hi Bob'
    
  File "<pyshell#62>", line 2
    if player_name = 'Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'
        if player_name = 'Bob' : print 'hi Bob'
        
  File "<pyshell#63>", line 2
    if player_name = 'Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'
        if player_name =='Bob' : print 'hi Bob'
        
  File "<pyshell#64>", line 2
    if player_name =='Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'
if player_name =='Bob' : print 'hi Bob'
SyntaxError: invalid syntax
>>> if x == y: print 'x = y'
	if player_name =='Bob' : print 'hi Bob'
	
  File "<pyshell#66>", line 2
    if player_name =='Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'

>>> if player_name =='Bob' : print 'hi Bob'

hi Bob
>>> if x == y: print 'x = y'
	if player_name =='Bob' : print 'hi Bob'
	
  File "<pyshell#71>", line 2
    if player_name =='Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'

	if player_name =='Bob' : print 'hi Bob'
	
  File "<pyshell#72>", line 3
    if player_name =='Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'
if player_name =='Bob' : print 'hi Bob'
SyntaxError: invalid syntax
>>> 
>>> if x == y: print 'x = y'
    if player_name =='Bob' : print 'hi Bob'
    
  File "<pyshell#75>", line 2
    if player_name =='Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'
 if player_name =='Bob' : print 'hi Bob'
 
  File "<pyshell#76>", line 2
    if player_name =='Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'
   if player_name =='Bob' : print 'hi Bob'
   
  File "<pyshell#77>", line 2
    if player_name =='Bob' : print 'hi Bob'
    ^
IndentationError: unexpected indent
>>> if x == y: print 'x = y'        if player_name =='Bob' : print 'hi Bob'
SyntaxError: invalid syntax
>>> if x == y: print 'x = y'        if player_name =='Bob' : print 'hi Bob'
SyntaxError: invalid syntax
>>> if x == y: print 'x = y'        if player_name =='Bob' :
	
SyntaxError: invalid syntax
>>> if x == y: print 'x = y'        if player_name =='Bob' :
	
SyntaxError: invalid syntax
>>> if x==y :
	print 'x is equal to y'
	if player_name=='Bob' :
		print 'Hello Bob!'

		
>>> # while loop loops as long as a condition you specify is true
>>> # a break statement controls when the loop stops
>>> while True :
	print 'What word am I thinking of?'
	answer = raw_input(">")
	if answer == 'cheese'
	
SyntaxError: invalid syntax
>>> while True :
	print 'What word am I thinking of?'
	answer = raw_input(">")
	if answer == 'cheese' :
		print 'You guessed it!'
		break
	else : print 'No, not that word...'

	
What word am I thinking of?
>ham
No, not that word...
What word am I thinking of?
>cheese
You guessed it!
>>> # functions:
>>> cave_numbers= range(1,21)
>>> print 'you can see' len(cave_numbers) 'caves'
SyntaxError: invalid syntax
>>> print 'you can see', len(cave_numbers), 'caves'
you can see 20 caves
>>> # ok, so I really need a comma to separate the stuff in the print statement
>>> 
>>> # the loops can be: while loops and for loops
>>> # while loops are based on a condition like an if statemtn
>>> # for loops run once for each element of a list
>>> 
>>> # MY FIRST VERSION OF HUNT THE WUMPUS
>>> from random import choice
>>> cave_numbers=range(1,21)
>>> cave_numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> wumpus_location = choice(cave_numbers)
>>> wumpus_location
10
>>> wumpus_location
10
>>> wumpus_location
10
>>> player_location=choice(cave_numbers)
>>> while player_location == wumpus.location :
	player_location = choice(cave_numbers)

	

Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    while player_location == wumpus.location :
NameError: name 'wumpus' is not defined
>>> while player_location == wumpus_location :
	player_location = choice(cave_numbers)

	
>>> # I've saved the code in hunt_the_wumpus.py
>>> 
>>> # using lists:
>>> shopping_list = ['milk', 'bread', 'cheese', 'bow and arrow']
>>> print shopping_list
['milk', 'bread', 'cheese', 'bow and arrow']
>>> print shopping_list[0]
milk
>>> print shopping_list[-1]
bow and arrow
>>> # get the last item with -1
>>> #check if an item is in the list:
>>> if 'milk' in shopping_list :
	print 'good you've mentioned the milk'
	
SyntaxError: invalid syntax
>>> if 'milk' in shopping_list :
	print "good you've mentioned the milk"

	
good you've mentioned the milk
>>> supermarket_list = ['milk', 'bread', 'cheese']
>>> wumpus_needs = ['bow and arrow', 'lantern']
>>> my_shopping_lists = [supermarket_list, wumpus_needs]
>>> wumpus_needs.append('sunglasses')
>>> wumpus_needs.remove('bow and arrow')
>>> print wumpus_needs
['lantern', 'sunglasses']
>>> print my_shopping_lists
[['milk', 'bread', 'cheese'], ['lantern', 'sunglasses']]
>>> two_wumpus_needs = wumpus_needs[0:3]
>>> two_wumpus_needs
['lantern', 'sunglasses']
>>> last_one = wumpus_needs[-1:]
>>> last_one
['sunglasses']
>>> first_one = wumpus_needs[:1]
>>> first_one
['lantern']
>>> last_one = wumpus_needs[1:]
>>> last_one
['sunglasses']
>>> #create an empty list:
>>> a=[]
>>> a
[]
>>> a.append('you')
>>> a
['you']
>>> a.appent('me')

Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a.appent('me')
AttributeError: 'list' object has no attribute 'appent'
>>> a.append('me')
>>> s

Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a
['you', 'me']
>>> b=['you and me']
>>> a.append(b)
>>> s

Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> a
['you', 'me', ['you and me']]
>>> # for loops
>>> 
========================================= RESTART: Shell =========================================
>>> from random import choice
>>> cave_numbers = range(0,20)
>>> caves =[]
>>> for i in cave_numbers :
	caves.append([])

	
>>> for i in cave_numbers :
	for j in range(3) :
		passage_to = choice(cave_numbers)
		caves[i].append(passage_to)

		
>>> print caves
[[5, 4, 3], [11, 15, 1], [8, 4, 6], [15, 11, 11], [19, 3, 16], [16, 0, 10], [14, 2, 11], [16, 1, 18], [3, 18, 6], [0, 10, 1], [15, 1, 0], [17, 2, 18], [12, 17, 15], [13, 19, 17], [3, 11, 2], [9, 16, 18], [3, 15, 3], [13, 10, 1], [9, 17, 14], [15, 9, 7]]
>>> # so, what happend above:
>>> 
========================================= RESTART: Shell =========================================
>>> from random import choice
>>> cave_numbers = range(0,20)
>>> caves =[]
>>> for i in cave_numbers :
	for j in range(3) :
		passage_to = choice(cave_numbers)
		caves[i].append(passage_to)

		

Traceback (most recent call last):
  File "<pyshell#178>", line 4, in <module>
    caves[i].append(passage_to)
IndexError: list index out of range
>>> 
========================================= RESTART: Shell =========================================
>>> from random import choice
>>> cave_numbers = range(0,20)
>>> caves =[]
>>> for i in cave_numbers :
	caves.append([])

	
>>> for i in cave_numbers :
	for j in range(3) :
		passage_to = choice(cave_numbers)
		caves[i].append(passage_to)

		
>>> print caves
[[1, 14, 3], [12, 4, 8], [18, 7, 16], [10, 17, 6], [12, 10, 7], [1, 19, 4], [18, 16, 11], [16, 8, 10], [11, 17, 6], [2, 11, 4], [17, 2, 12], [14, 5, 5], [11, 10, 15], [3, 2, 11], [3, 16, 14], [1, 4, 19], [12, 15, 12], [19, 2, 1], [18, 5, 12], [10, 3, 13]]
>>> #so, you have a number of caves. you create then an empty list of caves which you will fill later.
>>> # for each cave index you append a new empty list to the first list.
>>> # for each cave index and for each  passage_to you run the choice funciton 3 times
>>> # you fill the caves with i (which are the cave indexes) and apped to them 3 other caves specified by the passage_to variable.
>>> 
