# Transportation Mode Selection
# Choose a mode of transportation based on the distance(e.g.,<3km:Walk, 3-15km:Bike, >15km:Car)

# Loop until a valid distance is entered
while True:
    distance_km = int(input('Please enter the distance in kilometers: '))
    if distance_km <=0:
        print('Distance cannot be zero or negative.')
    else:
        break
    
# Determine the recommended mode of transport based on the distance
if distance_km < 3:
    transport = 'Walk'
elif distance_km <= 15:
    transport = 'Bike'
else:
    transport = 'Car'

print("AI recommends you the transport of: "+transport)