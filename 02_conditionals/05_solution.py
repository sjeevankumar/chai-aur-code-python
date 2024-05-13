# Weather Activity Suggestion
# Suggest an activity based on the weather(e.g.,Sunny-Go for a walk, Rainy-Read a book, Snowy-Build a snowman)

# Define valid weather conditions
valid_weather_conditions = ('sunny','rainy','snowy')

# Loop until a valid weather condition is entered
while True:
    weather = input('How is the weather? ').lower()
    if weather in valid_weather_conditions:
        break
    else:
        print('Please enter one of these: sunny, rainy, or snowy')

# Respond based on the weather condition
if weather == 'sunny':
    print('Go for a walk')
elif weather == 'rainy':
    print('Read a book')
else:
    print('Build a snowman')