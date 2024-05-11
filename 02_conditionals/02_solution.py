# Movie Ticket Pricing
# Problem: Movie tickets are priced based on age:$12 for adults(18 and over), $8 for children. Everyone get a $2 discount on Wednesday.

age = int(input('Enter your age = '))
isWednesday = True

price = 12 if age>=18 else 8
if isWednesday:
    price-=2
print("Ticket price for you is $"+str(price))
