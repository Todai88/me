#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Update this.

"""


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


# Here comes the content of the webpage 
content = """<!doctype html>
<meta charset="utf-8">
<title>Min me-sida</title>
<pre>
Joakims me-sida
###############################################################################

</pre>

<body>

<p>Mitt namn är Joakim Bajoul Kakaei. Jag är 27 år gammal och har sedan förra året<br> 
bott i en stad en liten bit utanför London där jag jobbar som .NET utvecklare<br> 
för ett mindre 'Software house'. Tillsammans med mina medarbetare så <br> 
utvecklar vi simplistiska och intuitiva helhetslösningar för våra klienter<br> 
i byggnads- och järnvägsbranschen - tro det eller ej, men infrastrukturen<br> 
här i England är betydligt värre än hemma i Sverige. </p>

<p>Innan jag flyttade till England så bodde jag i Seoul, Sydkorea där jag <br> 
studerade vid Seoul National University via ett utbyte med Göteborgs<br> 
Universitet (där jag förnuvarande arbetar mig igenom de sista faserna<br> 
av min kandidat i Software Engineering and Management). </p>

<p>Jag har sedan måga år tillbaka jobbat som bartender vid en hel del <br> 
väldigt väletablerade barer, både som vanlig knegare och som manager.<br> 
På senare år har jag även gått med Försvarsmakten som deltidsanställd<br> 
pansarskyttesoldat vid P4, något som är väldigt annorlunda från vad jag <br> 
gjorde VPL som. </p>

Anyways. Ni når mig lättast via min mail (joabaj88@gmail.com).<br> 

Har ni vägarna förbi kan ni alltid spana in min hemsida som jag arbetar med<br> 
vid sidan av jobbet:<br> <br> 

<a href="http://portfolio.kimput.com"> min portfolio </a><br> <br> 
och några andra roliga moduler:<br> 
<a href="http://portfolio.kimput.com/quotes/random.html"> en modul som spottar ut slumpmässiga citat </a><br> 
<a href="http://portfolio.kimput.com/weather/index.html"> en modul som visar v'dret i ditt område (funkar via din IP; kan därför vara lite felkalibrerad). </a><br> <br> 

Ha det bäst! :)<br> 

</body>

"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
