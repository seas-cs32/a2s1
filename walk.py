'''A walk to escape the city for CS 32 Act II, Scene I'''

from city import CitySqGrid

# Our faithful dog
Cosmo = '\N{DOG FACE}'

nyc = CitySqGrid(4, Cosmo)
print(nyc)

loc = nyc.start
while True:
    if loc not in nyc:
        break

    direction = input('Where to? ')
    loc = nyc.move(loc, direction)
    print(nyc)

print('Enjoy your day outside the city!')
