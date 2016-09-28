#RUN THE WUMPUS
from random import choice

cave_numbers= range(1,25)
wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or
       player_location == wumpus_friend_location)):
    player_location = choice(cave_numbers)


print "Welcome to hunt the Wumpus!"
print "You can see", len(cave_numbers), "caves"
print "To play, just type the number"
print "of the cave you want to enter next"

while True :
    print "You are in cave", player_location
    if (player_location == wumpus_location -1 or
        player_location == wumpus_location +1) :
        print " I smell a Wumpus"
    print "Which cave next?"
    if (player_location == wumpus_friend_location -1 or
        player_location == wumpus_friend_location +1) :
        print "I smell an even stinkier wumpus!"
    player_input = raw_input('>')
    if (not player_input.isdigit() or
        int(player_input) not in cave_numbers) :
        print player_input, "is not a cave!"

    else :
        player_location = int(player_input)
        if player_location == wumpus_location :
            print "Ohh! You got hugged by a wumpus!"
            break
        if player_location == wumpus_friend_location :
            print "Ohh! You got hugged by the wumpus' friend!"
