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
