#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()
	

# Send the HTTP header
#print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: text/html;charset=utf-8")
print("")


height = format(1100 * 3.28084, '.2f')
 
speed = format(1000 * 0.62137, '.2f')
 
temperature = format(-50 * (9/5) + 32, '.2f')


toPrint = """<br><b>########### OUTPUT ###########</b>
<br><br>Your plane's elevation is {feet} feet above the sea level.<br>
You are going {miles} miles per hour, <br>
Finally, the temperature outside is {temp} degrees fahrenheit <br> <br>
<b>########### OUTPUT ###########</b>""".format(feet=height, miles=speed, temp=temperature) 

# Here comes the content of the webpage 
content = """<!doctype html>
<meta charset="utf-8">
<title>Min redovisnings-sida</title>
<pre>
<h1>Min Redovisnings-sida </h1>




</pre>

<body>
 {printer}
</body>

"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content.format(printer=toPrint))
 
