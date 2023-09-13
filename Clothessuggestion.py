# Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.

# The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

# Some examples of expected behaviour:

# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 21
# Will it rain (yes/no): no
# Wear jeans and a T-shirt
# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 11
# Will it rain (yes/no): no
# Wear jeans and a T-shirt
# I recommend a jumper as well
# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 7
# Will it rain (yes/no): no
# Wear jeans and a T-shirt
# I recommend a jumper as well
# Take a jacket with you
# Sample output
# What is the weather forecast for tomorrow?
# Temperature: 3
# Will it rain (yes/no): yes
# Wear jeans and a T-shirt
# I recommend a jumper as well
# Take a jacket with you
# Make it a warm coat, actually
# I think gloves are in order
# Don't forget your umbrella!
print (" whats the weather looking like tomorrow ")
a = int(input (" enter the temoerature for tomorrow in [C] : "))
b = (input (" Is it gonna rain tomorrow ? [Yes/No] : "))
condition  = a > 20 and b == "Yes"
condition1 = 20 > a > 10 and b == "Yes"
condition2 = 10 > a > 0 and b == "Yes"
condition3  = a > 20 and b == "No"
condition4 = 20 > a > 10 and b == "No"
condition5 = 10 > a > 0 and b == "No"
if condition:
    print("Wear jeans and a T-shirt\n Don't forget your umbrella! ")
if condition1:
    print("Wear jeans and a T-shirt\n Don't forget your umbrella! ")
if condition2:
    print("Wear jeans and a T-shirt\n I recommend a jumper as well\n take a jacket with you\n Make it a warm coat, actually\n Don't forget your umbrella! ")
if condition3:
    print("Wear jeans and a T-shirt ")
if condition4:
    print("Wear jeans and a T-shirt ")
if condition5:
    print("Wear jeans and a T-shirt I recommend a jumper as well\n take a jacket with you\n Make it a warm coat, actually")



