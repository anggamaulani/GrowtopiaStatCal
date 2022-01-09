statBlock = int(input('Number of Science Stations: '))
statHarvest = int(input('Times Harvested (max 2x/day): '))

punch = statBlock * statHarvest

xp = punch
xp = xp * 1.1
yellow = int(punch * 0.15)
blue = int(punch * 0.13)
pink = int(punch * 0.07)
green = int(punch * 0.4)
red = int(punch * 0.25)

print('\n[ YELLOW CHEMICAL ] > {0:,}'.format(yellow))
print('[ BLUE CHEMICAL ] > {0:,}'.format(blue))
print('[ PINK CHEMICAL ] > {0:,}'.format(pink))
print('[ GREEN CHEMICAL ] > {0:,}'.format(green))
print('[ RED CHEMICAL ] > {0:,}'.format(red))
print('[ EXP EARNED ] > {0:,}\n'.format(xp))
