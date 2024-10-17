#! /usr/bin/env python3
import sys

#question number 1
Dict = {'Book': "The Catcher in the Rye" , 'Song': "Eminem - Mockingbird" , 'Tree': "Blue Mimosa"}
print(Dict)

#question number 2
print(Dict['Book'])

#question number 3
fav_thing = 'Book'
print(Dict[fav_thing])

#question number 4
print(Dict['Tree'])

#guestion number 5
Dict['Organism']= "Moon Jellyfish"
print(Dict)

#question number 6
for thing in Dict:
    print(thing, Dict[thing])

#question number none
fav_thing = Dict.copy()
for thing in fav_thing:
    print( f"{thing:<10}      {fav_thing[thing]}")


#question number 8
for thing in fav_thing:
    print(thing)

thing = input('Check the above keys')
print(Dict[thing])

#question number 9
fav_thing['Organism'] = 'Unicorn'
print(fav_thing)

#question number 9
thing1=input()
fav_thing['Organism'] = thing1
print(fav_thing)
print(fav_thing['Organism'])