# Pet Food Recommendation
# Recommend a type of pet food based on the pet's species and age. (e.g., Dog:<5years- Puppy food, Cat:>2years-Senior cat food)

valid_pet_type = ('dog','cat')

while True:
    pet_type = input('Please enter pet type(dog or cat): ').lower()
    if pet_type in valid_pet_type:
        break
    else:
        print('Invalid input: please enter dog or cat')

while True:
    try:
        pet_age = int(input('Please enter pet age: '))
        break
    except ValueError:
        print('Invalid input: please enter age as number')
    

if pet_type == 'dog':
    if pet_age < 5:
        result = 'puppy food'
    else:
        result = 'senior dog food'
else:
    if pet_age<=2:
        result = 'kitten food'
    else:
        result = 'senior cat food'
        
print(result)