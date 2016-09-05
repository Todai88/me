"""
Height converter
"""
 
height = format(1100 * 3.28084, '.2f')
 
speed = format(1000 * 0.62137, '.2f')
 
temperature = format(-50 * (9/5) + 32, '.2f')

print("""\r\n########### OUTPUT ###########\r\n\r\nThe elevation is {feet} above the sea level, \r\n
you are going {miles} miles/h, \r\n
finally the temperature outside is {temp} degrees fahrenheit \r\n
########### OUTPUT ###########""".format(feet=height, miles=speed, temp=temperature)) 
