# Coffee Customization
# Customize a coffee order: "Small","Medium", or "Large" with an option for "Extra shot" of expresso

valid_order_size = ('small','medium','large')
valid_extra_shot = ('yes','no')

while True:
    order_size = input('Please enter coffee size (small, medium, or large): ').lower()
    if order_size in valid_order_size:
        break
    else:
        print('Invalid input. Please enter small, medium, or large.')
        
while True:
    extra_shot = input('Do you want an extra shot (yes or no)? ').lower()
    if extra_shot in valid_extra_shot:
        break
    else:
        print('Invalid input. Please enter yes or no')

if extra_shot == 'yes':
    coffee = f"{order_size} coffee with an extra shot"
else:
    coffee = f"{order_size} coffee"

print('Order: '+coffee)



