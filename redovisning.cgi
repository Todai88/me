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
    			<div class='panel panel-default'>
				    <div class='panel-heading'>
					    <h4 class='panel-title'>
					    <a data-toggle='collapse' data-parent='#redovisnings-grupp' href='#Kmom05'>Kmom05</a>
					    </h4>
				    </div>
				    <div id='Kmom05' class='panel-collapse collapse'>
				    	<div class='panel-body'>
				    			<ul>

								    <li><b>Hur kändes det med datastrukturerna dictionaries och tupler? Har du sett något liknande förut?</b>
Som vanligt så kändes det bra. Det känns som att en av Pythons starkaste styrkor är att språket verkar använda en relativt normaliserad struktur, något som jag nämnt tidigare. Dictionaries och tupler har jag jobbat med tidigare. Tupler mindre än dictionaries, men nog har jag stött på bägge. När man kör mycket JS så blir det ju en del JSON, vilka egentligen är dictionaries. En av mina nuvarande arbetsuppgifter är att fixa en dynamisk RESTful API för våra .NET datacomponents, så då blir det garanterat JSON. Hellre det än XML...</li>

 <li><b>Känns det som du fick ordning på listor, dictionaries och tupler? När man skall använda respektive och hur de kan användas?</b>
Som nämnt ovan så känns hela Pythons struktur rätt normaliserad. Det jag menar är självklart att koden ser snarlik ut i alla sorts datastrukturer. Man kan använda snarlika funktioner i en sträng som man kan i en lista exempelvis. Därav blir det lättare att lära sig nya strukturer. Den huvudsakliga skillnaden mellan typerna är att vissa är immutable och andra inte. En mutable typ kan exempelvis addera data till, en immutable kan man inte göra det till. Detta gör listor mer dynamiska än tupler exempelvis, men samtidigt så är tupler lättare att arbeta MED då du kan finna data i dem betydligt lättare. Detta gör tupler i regel snabbare än listor, då de inte behöver itereras på samma sätt utan data enkelt kan finnas genom predefined functions.
</li>
 <li><b>Använde du något av listor, dictionaries eller tupler när du gjorde uppgifterna, på vilket sätt? </b>
Jodå, det användes en stor del listor när jag arbetade mig igenom uppgifterna. Dock användes inte riktigt några tupler eller dictionaries. De flesta (om inte alla) uppgifterna krävde mer dynamiska collections, så därför valde jag att köra huvudsakligen på listor. Sen hade jag självklart memaloc i åtanke och försökte inte använda mig av för stora listor (eftersom de faktiskt är tyngre att iterera över när man letar efter data...). </li>

 <li><b>Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var mest lärorik? </b>
Jag tyckte de två extrauppgifterna jag gjorde (decrypt och tictactoe) var de mest lärorika. Som Mikael vet så fastnade jag lite lätt på decrypten, vilket grundade sig i att jag hade missat ett if-fall (om det decrypterade tecknet var > 90). Det var lite mer algoritmiskt tänkande i extrauppgifterna, vilket jag gillade skarpt! Det var mindre att bara läsa en fil och skriva ut tecknen, utan mer att arbeta med data. Om jag var tvungen att välja en av dem skulle jag nog välja dekrypteringen. Tic Tac Toe var kul och lärorik den med, men mindre så än dekrypteringen!
</li>
 <li><b>Gjorde du någon av extrauppgifterna? Berätta om det arbetet isåfall.</b>
Som nämnt ovan så gjorde jag två utav tre extrauppgifter. Skippade den om spelet för att den helt enkelt inte såg alltför kul eller givande ut. Jag gjorde inte heller den tidigare iterationen av spelet, så tänkte att det var lika bra att bara skippa och gå vidare med Kmom06 så att jag fortsätter ligga före kursen då jag faktiskt måste bolla mellan kursen och jobb!
</li>
				    		   </ul>
			    		</div>
    				</div>
    			</div>

    			<div class='panel panel-default'>
				    <div class='panel-heading'>
					    <h4 class='panel-title'>
					    <a data-toggle='collapse' data-parent='#redovisnings-grupp' href='#Kmom06'>Kmom06</a>
					    </h4>
				    </div>
				    <div id='Kmom06' class='panel-collapse collapse'>
				    	<div class='panel-body'>
				    			<ul>

<li><b>Har du jobbat med liknande tekniker innan (JSON, HTTP, webbtjänster, SQLite, scrapa från HTML-formatet, kommandorads options), eller var detta helt nytt för dig?</b>
Jodå, det blir en hel del med HTTP-protocoll, JSON-parsing och webtjänster på jobbet (men då huvudsakligen i .NET miljö). Jag håller förnuvarande på att jobba mig igenom en 
automatiserad webAPI i c# (använder mig av reflection för att hitta moduler i rätt feta datakomponenter). 
Jag har dock inte jobbat alltför mycket i varken kommandoraden (i python!) eller med scrapande. Det har varit ordentligt givande. Dock har det tagit mig en stund med att 
lämna in uppgiften då jag har haft så fasansfullt mycket att göra med universiteten (Mikael vet mer om det..). Har i princip spenderat varje dag de senaste två veckorna
med att bara få koll på hur jag ska gå vidare med min utbildning, vilket gjort mig lite sen.

Det ska nämnas att det är väldigt nytt för mig att jobba med samtliga aspekter som ni frågar om just i python, men som vi redan vet så gör python det relativt lätt att 
lära sig nya saker då det har så många bibliotek som är färdiga att bara plocka från och ett rätt schysst community online som fortfarande växer (huvudsakligen pga. devops).
</li>

<li><b>Känns det bra att jobba på kommandoraden, ser du ett användningsområde för den typen av Python-program?</b>

Det känns bra. Det var lite jobbigt i början då jag inte riktigt greppade hur man skulle parsa de olika kommandona (opts, args), så jag jobbade huvudsakligen på opts. 
Det löste sig rätt snabbt när jag fick lite vägledning och verkligen började läsa lite mer i pythondocs online. Som nämnt ovan känns det riktigt skönt att veta
att det finns ett stort gäng personer som själva har jobbat med dessa saker och därmed finns det lättillgänglig information på nätet, så man är inte fast särskilt
länge så länge man är villig att läsa sig fram till ett svar! 

Det finns definitivt användningsområden för kommandorads-program; det flesta som man kör i pen-testing är ju cli-interfaces där man bara exekverar script(s) för att
göra allt från att scrapa hemsidor för att se om man kanske kan se vad för kod som gömmer sig, eller kollar portscans osv. 

Däremot tror jag många nybörjare kan ha svårt att arbeta med denna slags interface, vilket gör det görbra att vi gör det - då man snabbt introducerar nybörjare
vid ett lite svårare moment men lätta uppgifter. Detta gör att det kanske inte är rädda att ta för sig vid senare tillfällen! 
</li>

<li><b>Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var mest lärorik? </b>

Absolut den bästa uppgiften hittils. Jag var verkligen tvungen att titta mig omkring på nätet / gitter för att faktiskt förstå vad jag höll på med och skulle göra.
Huvudsakligen var det ju svårt med cli, men när det väl kom på plats så föll det mesta på plats allt eftersom. Det mesta handlade ju egentligen om att förstå
att även mer avancerade strukturer faktiskt bygger på lättare (JSON-object är ju egentligen dictionaries osv). Det märks att kursens struktur är byggd på ett
sätt som gör det lättare för absoluta nybörjare att lära sig hur man ska arbeta med data genom att bitvis introducera dem till nya strukturer och mer avancerade
moment.

Det som tog mest tid var utan tvekan att förstå hur man skulle parsa opts och args. Jag blandade ihopp de bägge och lyckades därmed köra både args och opts
som opts. Men det löste sig ju - man lever som man lär! :)
</li>

<li><b>Var uppgiften i tuffaste laget, vilken del hade du valt bort om du hade haft det valet?</b>
Nej, det tror jag inte. Nu har jag haft lite flyt med att jag faktiskt har haft lite erfarenhet av python sedan tidigare och har jobbat med andra språk rätt ordentligt.
Men jag kan inte se att en person som faktiskt pluggar språket på heltid skulle ha något större problem med att lösa dessa uppgifter.
Som nämnt ovan så tycker jag det överlag känns som det varit ett riktigt skönt tempo i kursen, man har stegvis blivit introducerad till mer avancerade moment.
Att tidigt introducera en användare vid cli kan vara riktigt bra också, då det gör det lättare för en användare att vid senare tillfälle lära sig mer om 
hur man faktiskt använder ett *nix system.

Om jag var tvungen att ta bort en del skulle det nog vara de lättare delarna av SEO:n. Det kändes mest som att man gjorde samma slags sak som vi gjort i de tidigare momenten med
att extrahera data från strängar (denna gång lite annorlunda, men inte på en sådan nivå att jag känner det var nödvändigt..). Jag hade istället velat se lite mer
fokus på hur man kan använda sig av webapi:er, om man ändå har det som tema på momentet. Kanske sätta upp en webAPI som tillåter post-requests via postman eller något liknande (måst finnas). 
På så vis kan man lära studenterna att man kan skicka data via nätet via Python, vilket jag sannolikt älskat då man kan leka lite med det! :)
</li>
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
