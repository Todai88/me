"""
Height converter
"""

height = float(input("What is the plane's elevation in metres? \r\n"))
height = format(height * 3.28084, '.2f')

speed = float(input("What is the plane's speed in km/h? \r\n"))
speed = format(speed * 0.62137, '.2f')

temperature = float(input("Finally, what is the temperature (in celsius) outside? \r\n"))
temperature = format(temperature * (9/5) + 32, '.2f')

print("""\r\n########### OUTPUT ########### \r\n \r\n The elevation is {feet} above the sea level, \r\n
you are going {miles} miles/h, \r\n
finally the temperature outside is {temp} degrees fahrenheit \r\n
########### OUTPUT ###########""".format(feet=height, miles=speed, temp=temperature)) 
