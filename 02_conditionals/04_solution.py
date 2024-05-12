# Banana Ripeness Checker
# Determine if a banana is ripe, overripe, or unripe based on its color.(eg.,Banana:Green-Unripe,Yellow-Ripe,Brown-Overripe)

color = (input('Please enter the color of banana = ')).lower()
colorlist  = ('green','yellow','brown')

if color not in colorlist:
    print('please enter a green or yellow or brown color')
    exit()
    
if color == 'green':
    print('Unripe')
elif color == 'yellow':
    print('Ripe')
else:
    print('Overripe')


