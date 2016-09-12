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
<title>Min redovisnings-sida</title>
<pre>
<h1 class='strong text-center'>Min Redovisnings-sida </h1>




</pre>

<head>
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>


<div class='container'>
<h2 class='text-center'> Redovisningar </h2>
<p><strong>Nedan ser ni alla mina redovisningar. </strong></p>
<div class='panel-group' id='redovisnings-grupp'>
<div class='panel panel-default'>
<div class='panel-heading'>
<h4 class='panel-title'>
<a data-toggle='collapse' data-parent='#redovisnings-grupp' href='#Kmom01'>Kmom01</a>
</h4>
</div>

<div id='Kmom01' class='panel-collapse collapse'>
<div class='panel-body'>
<div class='row'>
<div class='col-xs-6'>
<h2 class='lead strong'> 'En me-sida i Python som cgi-skript' </h2>
<ul>
<li><b>Vilken utvecklingsmiljö använder du?</b></li>
Jag använder mig utav Sublime Text 3 i denna kurs då jag föredrar att lära mig
genom att begränsa
autocomplete så mycket som möjligt. :)

<li><b>Är du bekant med Python sedan tidigare?</b></li>
Jag har väl stött på Python vid tillfällen. Ett tag var jag riktigt sugen på
att bli penetrationstestare, något jag släppt det senaste.
Istället har jag valt att arbeta mig mot att bli webutvecklare
och därmed använda mig utav det jag lärt mig i ett mer förebyggande syfte.
Pga ovan nämnt intresse så stötte jag på Python vid tillfällen. Jag har dock inte
arbetat alltför mycket med språket. Alltså mer teoretisk än praktisk erfarenhet.

<li><b>Är du bekant med programmering och problemlösning sedan tidigare?</b></li>
Jodå. Jag är knappast någon guru när det gället programmering,  men nog kan jag
en del.
Till vardags jobbar jag med .NET utveckling (VB / C#, MS SQL etc).
Sen leker jag lite med webutveckling vid sidan av jobbet eller när det finns plats
för lite slötid på jobbet. Då huvudsakligen genom att leka med JS, jquery etc.

<li><b>Är du bekant med terminalen och Unix-kommandon sedan tidigare?</b></li>
Bekant kan jag nog säga att jag är. Dock är jag inte särskilt bekväm med terminalen som
jag kanske borde vara... Iom att vi huvudsakligen jobbar med .NET så sitter vi i
Windows-miljö, vilket inte riktigt kräver någon större erfarenhet av terminalen..

<li><b>Gick det bra att komma i gång med kursmomentet, var det lagom, för litet, för stort?</b></li>
Jo, men det tror jag.
Jag lyckades missa en liten del (init). Men annars än det så har det
inte varit något större bekymmer annat än svenskan. Jag är född och
uppväxt i Sverige, men jag pratar inte svenska särskilt ofta och
har varken pratat, läst eller skrivit svenska regelbundet sedan jag åkte till Korea.

<li><b>Vilken del av kursmaterialet (böcker, artiklar, videor, etc) uppskattade du mest?</b></li>
Jag har hittils inte rört kursmaterialet, utan jag tror snarare på
att lära medans man kodar.
Jag tänkte kika lite på materialet under helgen.
</ul>
</div>
<div class='col-xs-6'>
<h2 class='lead strong'> 'Mitt första Python-script' </h2>

<ul>
<li><b> Svårigheter </b></li>
Jag tyckte inte det var några konstigheter med självaste programmeringen.
Dock så stötte jag på två större bekymmer som jag inte kunde lösa själv:
<br>
<ol>
<li>CRLF-encoding som behövdes ändras till LF (löstes via LineEdit i ST3),
LF-encoding krävdes av test-cases, men inte av kompilatorn, vilket var lite
udda... </li>
<li>Mitt .cgi script uppskattades inte av webservern, utan jag fick
ett internal error när jag försökte kolla upp redovisningen.
Dock löstes detta snabbt med hjälp av Mikael då det visades vara ett mellanslag
i början av min kod (python-indentation i ett nötskal...).
</li>
</ol>
<br>
<li><b> Problem </b></li>
Några problem hade jag inte riktigt. Scripten är ju riktigt grundläggande, fokus låg
helt klart mer på att se till att alla kommer igång med scriptandet istället för att
lägga fokus på att göra det svårt för oss.
<li><b> Lösningar </b></li>
Inga riktiga lösningar av betydelse.
Det enda jag kan påpeka är att det kan vara lättare för nya användare att köra
Sublime Text med LineEndings då det minskar risken för CRLF > LF.
<li><b> Lärdomar </b></li>
Som nämnt ovan så har jag inte riktigt lärt mig mycket annat än att verkligen
ha indentations i åtanke och att jag lärt mig hur man ska rensa CRLF-encoding.
<li><b> Resultatet </b></li>
Resultatet är mycket lovande.
</ul>
</div>
</div>
</div>
</div>
</div>
<div class='panel panel-default'>
<div class='panel-heading'>
<h4 class='panel-title'>
<a data-toggle='collapse' data-parent='#redovisnings-grupp' href='#Kmom02'>Kmom02</a>
</h4>
</div>
<div id='Kmom02' class='panel-collapse collapse'>
<div class='panel-body'>
<ul>

<li><b>Hur känns syntaxen i Python? Är det enkelt att se programmets struktur och vad det gör?</b></li>
Jo visst känns det bra. Riktigt trötsamt att behöva tänka på indenteringar osv.
Fick lite osköna felmeddelanden av pylint (nämner dem nedan).
Överlag känns det väldigt likt hur jag jobbar i .NET, åtminstone hittils.
<li><b>Hur går det med valideringen av uppgifterna? Är du överens med pylint om eventuella felmeddelanden vid valideringen?</b></li>
Valideringarna funkar väl. Problemet jag hade denna gången var huvudsakligen att pylint visar felmeddelanden även fast
kompilatorn kompilerar väl och exekverar gött.

Ett par exempel är ju självklart kravet på doctypes i metodkropparna. Ett annat mer konkret exempel var hur det krävdes
doctype i toppen av filen (marvin1.py), även fast min lokala kompilator funkar väl. Min lokala funkar dock INTE
då jag har en doctype (kommentar) över importerna och encoding-arna...

<li><b>Hur gick det att utföra uppgifterna, var de enkla eller svåra?</b></li>
Fortfarande inget alltför utmanande. Dock är det rätt skönt att ribban ökas sakta men säkert.
Jag är dock övertygad om att personer med mindre erfarenhet än mig finner många av
frågorna betydligt mer utmanande.

Huvudutmaningen för mig är mer att se över syntaxen osv snarare än att bli uppjagad om hur
man type-castar osv.
</ul>
</div>
	</div>
	</div>
    			<div class='panel panel-default'>
				    <div class='panel-heading'>
					    <h4 class='panel-title'>
					    <a data-toggle='collapse' data-parent='#redovisnings-grupp' href='#Kmom03'>Kmom03</a>
					    </h4>
				    </div>
				    <div id='Kmom03' class='panel-collapse collapse'>
				    	<div class='panel-body'>
				    			<ul>

								    <li><b>Har du programmerat med filhantering tidigare, känns det lätt eller svårt?</b></li>
								    Jag har jobbat med filhantering i ett par olika språk; java, c#, python, c++ osv.
								    I jämförelse med många andra språk så måste jag erkänna att python gör det rätt enkelt.
								    En sak som gör det rätt skönt är att du inte behöver bry dig om att stänga filer osv eftersom EOF hanteras automatiskt.
								    En annan sak är självklart hur enkelt det är att jobba med strängar.
								    <li><b>Vad tycker du om video som läromedel, tycker du att de tillför något som läromedel?</b></li>
								    Jag älskar videor som läromedel. Självklart behöver man köra lite programmering också för att verkligen lära sig, men
								    utöver det så måste jag erkänna att jag älskar det!
								    Jag kollar gärna på videor när jag är på löpbandet på gymmet. :)

								    <li><b>Du har gjort din första modul i Python, känns strukturen bra?</b></li>
								    Jo, visst gör den det.
								    Jag blir riktigt less på importerna, dock. Jag hade gärna velat kunna importera alla funktioner i en fil, men det kan
								    man ju inte utifall man har oanvända funktioner i ens importerade fil. I mitt fall hade jag en funktion (validateInt())
								    som inte användes av main(), därför gavs jag en varning av pylint...

								    <li><b>Vad tyckte du om de olika uppgifterna? Hur tänkte du när du utförde dem? Var de utmanande eller lätta?</b></li>
								    De har inte riktigt börjat bli utmanande. Vad har varit utmanande är att varva hård utveckling på dagarna och sedan jobba
								    igenom kursen på kvällen.
								    Det känns dock som att det är en rätt linjär kurva, vilket säkert är skönt för alla nybörjare! :)
				    		   </ul>
			    		</div>
    				</div>
    			</div>

    			<div class='panel panel-default'>
				    <div class='panel-heading'>
					    <h4 class='panel-title'>
					    <a data-toggle='collapse' data-parent='#redovisnings-grupp' href='#Kmom04'>Kmom04</a>
					    </h4>
				    </div>
				    <div id='Kmom04' class='panel-collapse collapse'>
				    	<div class='panel-body'>
				    			<ul>

								    <li><b>Var det svårt att bekanta sig med datastrukturen för listor eller flöt det på bra?</b></li>
								    Jag måste erkänna att vissa saker med lists i Python känns lite svårlästa, som hur man 
								    slicear. Dock så är just de överkomplicerade grejorna vad som gör Python enhetligt i jämförelse 
								    med andra språk. Ett exempel är hur man gör en slice på samma sätt i strängar som i listor, 
								    något som säkert gör det lättare för en nybörjare om man väl greppat ett användningsområde.
								    Jag tycker att slice känns lite väl svårläst mot andra språk (som javascript); array.slice(from, to) mot list[from:to]
								    eller javascripts splice: array.splice(index, howMany, item1, item2....,itemN, itemN+1).

								    Som nämnt känns det lätt att använda, men kanske lite väl svårt att läsa. Så 8 av 10 toasters för användbarhet,
								    men 5 av 10 toasters för läshet.

								    <li><b>Har du jobbat med listor, eller arrayer, i andra programmeringsspråk – kan du isåfall jämföra Python listor mot andra programmeringsspråk?</b></li>
								    Som nämnt så har jag arbetat med arrayer och listor i ett par språk. Jämförelsevis så känns det som att Python har många bra
								    pre-defined functions för datastrukturer, men som jag nämnde ovan så känns det nästan lite som att man tycker att användningsfallen
								    är viktigare än den användbarhet (usefulness > usability).

								    <li><b>Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var mest lärorik när det gäller listor?</b></li>
								    Rent spontant tyker jag fortfarande att det är lite för lätt för att verkligen ta någon större lärdom från dem.
								    Visserligen lär jag mig mer om hur syntaxen fungerar, men utöver det så känns det rätt enkelt att lära sig Python.

								    Vad tog längst tid? Tror det var någon uppgift i answers.py som blev lite fel för att jag inte riktigt kunde förstå vad 
								    som skulle göras eftersom frågan var lite udda formulerad. När väl det stod klart vad som var målbilden så tog det några
								    sekunder att implementera.

								    En sak jag faktiskt lärt mig var hur pythons lists fungerar, hur de får allokerat minne.
								    Dvs att en lista med desamma element i sig inte är densamma som en annan lista med samma element eftersom
								    de har olika minnesallokeringar. 
								    Alltså:
								    [1,2,3] och [1,2,3] har samma element i sig, men kan vara olika eftersom de har annorlunda minnesallokeringar.
								    De har desamma element i sig, men är två helt olika objekt!
				    		   </ul>
			    		</div>
    				</div>
    			</div>
	</div>
	</div>
	</body>
"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
