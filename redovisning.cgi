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
    			    			<div class='panel panel-default'>
				    <div class='panel-heading'>
					    <h4 class='panel-title'>
					    <a data-toggle='collapse' data-parent='#redovisnings-grupp' href='#Kmom10'>Kmom10</a>
					    </h4>
				    </div>
				    <div id='Kmom10' class='panel-collapse collapse'>
				    	<div class='panel-body'>
				    		<div class="row">
				    			<div class="col-xs-6">
				    			<ul>
				    			<li> Utförande </li>
				    			Jag har valt att genomföra moment 1-6 (alltså samtliga moment). Det kändes inte riktigt relevant att bara genomföra de mest grundläggande kraven då jag sedan kursstart har jobbat hårt med att jobba mig igenom alla delmoment (utom cursor-spelet). 
				    			Även fast jag har fått ett par U:n på inlämningarna så tycker jag ändå att de har genomförts med rätt hög standard, då alla U:n har varit små slarvfel. 
				    			Självklart så tycker jag att jag borde gjort det bättre, men överlag känns det ändå bra.
				    				<br>
				    			Spelet startar med att användaren blir tillfrågad utifall hen vill starta ett nytt spel eller ladda. Om hen vill ladda så får hen ge ett namn på en tidigare save. Detta kollas sedan i players.json och om namnet finns bland json-objekten så laddas denna och spelaren sätts i det rum där hen var senast, med all sin tidigare access, inventory och solved. 
				    				<br>
				    			Varje spar-fil har en ett gäng variabler som alla har stor vikt:<br>
				    			<ul>
				    			<li><b>room</b> - var spelaren var senast </li>
				    			<li><b>inventory</b> - ryggsäcken </li>
				    			<li><b>used</b> - alla använda föremål (ett föremål kan inte slängas förens det använts) </li>
				    			<li><b>access</b> - vilka rum användaren har tillgång till (default: 1,3,4,5)</li>
				    			<li><b>solved</b> - vilka rum som är lösta. ett löst rum har en annan description </li>
				    			<li><b>interacted</b> - vilka rum som har interagerats med, viklet ger en annan description </li>
				    			</ul>
				    				<br>
				    			Varje rum har även de ett gäng viktiga attributer. Men innan jag går in alltför detaljerat på dem så vill jag nämna lite om deras struktur.
				    			Min tankeställning var att skapa något som är likt ett abstrakt träd (ADT). Där varje träd har ett unikt ID och var deras riktningar (N/Ö/S/V) referar till ett ID. Dvs att alla riktningar från rot N är barn till N och alla dess barn är barnbarn till N. Här är spelkartan:
				    			<br> <br>   
				    			________xxxxxxx <br>
				    			________x33333x <br>
				    			________x33333x <br>
				    			xxxxxxxxxx///xxxxxxxxxxxxxx <br>
				    			x1111111/22222/44444/555x <br>
				    			xxxxxxxxxx///xxxxxxxxxxxxxx<br>
				    			________x66666x <br>
				    			________x66666x <br>
				    			________xx///xxxxxxxxxx <br>
				    			________x77777/88888x <br>
				    			________x77777x88888x  <br>
				    			________xxxxxxxx///xxxxxxxxxx<br> 
				    			______________x99999/1010x <br>
				    			______________x99999x1010x <br>
				    			______________xxxxxxxxxxxxx <br>
				    				<br>
				    			Som ni kan se så har jag även valt att ha 10 olika rum, eftersom jag ville få med lite extra möjligheter för användaren och lite specifika krav, som att man skulle vara tvungen att ta upp särskilda föremål, använda sig av alla spel för att klara sig igenom allt osv. 
				    				<br>
				    			Varje rum har alltså: 
				    			<ul><br>
 				    			<li><b>id</b> - deras id. </li>
 				    			<li><b>riktning</b> - (N/Ö/S/V) </li>
 				    			<li><b>puzzle</b> - ett pussel, om möjligt</li>
 				    			<li><b>answer</b> - ett svar på pusslet, om ett finns </li>
 				    			<li><b>objekt</b> - ett par objekt. Dessa kan man interagera med och har sina egna attributer beroende på slags objekt</li>
 				    			<li><b>alt_description</b> - en beskrivning av rummet om man interagerat med rummets föremål </li>
 				    			<li><b>solved_ragnar</b> - en beskrivning av rummet som används om man vunnit spelet mot ragnar </li>
 				    			</ul>
 				    				<br>
				    			<b>Krav 1-3</b> har genomförts efter kravspecen. Jag använder mig utav en rätt simpel struktur där vi startar spelet med ./adventure.py <commando> där commando inte är något krav, utan fullkomligt optionellt. 
				    				<br>
				    			<b>Krav</b> 4-6 har genomförts efter kravspecen med lite mindre skillnader; ryggsäcken och spel i spelet fungerar som de ska och efter kravspecen (spel i spelen har inte cursor spelet i sig, då jag skippade den extrauppgiften). Dock så ändrade jag lite i 'spara'. Jag kände att det var viktigare för mig att bibehålla en stark data-integrity, dels för att jag inte litar på spelare rent generellt men även för att jag inte riktigt litar på json-biblioteket eller jsonfiler rent generellt. Jag har därmed valt att endast tillåta spelare att ladda från player.json, alltså INTE från en valfri fil. Han kan inte heller spara till en specifik fil. Utöver det så ska det funka helt klockrent.
				    				<br>
				    			Dock så är jag lite osäker på utifall jag har haft lite strul med CygWin eller om det är något fel i min kod, men det kan tillkomma problem när man kör vissa kommandon i spelet. Det verkar inte hända ofta, vilket får mig att tro att det kan ha med min miljö att göra. Dvs att jag inte kan återskapa felen, utan att en 'inv' vid ett tillfälle kan lyckas flytta dig till ett annat rum. Något som verkligen inte ska hända.
				    				<br>
				    			Utöver det så vet jag om att det finns problem med cygwin och svenska tecken rent generellt. Så om man lyckas skriva in en svensk bokstav vid fel tillfälle så kan spelet tänkas bugga ur fullkomligt. Vilket får spelaren att förlora sitt spel.
				    			Oturligt, men som sagt har det inte riktigt med min kod att göra, utan är ett problem i cygwin.
				    				<br>
				    			Ledtrådar har jag 5 unika av som ges i slumpmässig ordning bestämt av de som inte getts. Om alla ledtrådar har getts så resettas dictionary:n.
				    				<br>
				    			Det ska även nämnas att jag använt mig av cls för att rensa skärmen mellan kommandon. Detta för att spelaren lätt ska få information snabbt och förhoppnignsvis på ett lättföreståeligt sätt. 
				    			Fördelsvis spelar man spelet i fullskärm!

				    			<li> Resonemang </li>

				    			Som nämnt ovan så är integritet något som jag värdesätter i kodande, så tyvärr så valde jag att inte lita på användar-input under genomförandet av sparande. 
				    			Något som jag kanske borde gjort utifrån krav-specen, men det känns inte riktigt alltför viktigt. Förhoppningsvis så har ni lite överseende med det utifrån mitt resonemang ovan (i utförande). Dock förstår jag om ni väljer att reducera poängen från den deluppgiften.
				    			<br>
				    			Jag har även valt att försöka sprida ut mina moduler över ett gäng olika .py-filer. Detta är för att ni lättare ska kunna hålla koll på var ni är och lättare följa data-strömen i programmet. 
				    			<br>
				    			Det är även värt att nämna att krypto-spelet inte är särskilt svårt då det inte kräver att användaren löser något. Min tolkning av specen är att man ska kunna få hjälp att dekryptera kryptot enligt 'den hårda vägen'. Därför ser jag inget krav till att tvinga användaren att ha löst alla dekrypteringar själv. Därför ges möjligheten att skriva 'lös' för att låta programmet lösa dekrypteringen själv. 
				    			Egentligen inte någon större genväg, utan det underlättar bara för spelaren. 
				    			<br>
				    			Det är även värt att nämna antalet rum jag har. Jag valde alltså att utöka mängden rum till 10 för att underlätta för mig själv. Huvudsakligen så började jag lägga in fler rum för att jag ville ha mer content. Det kändes för spartanskt utan saker att interagera med i varje rum. Jag ville ju att spelaren skulle kunna använda sig av alla möjliga kommandon i rummen också, men samtidigt så ville jag att de ageringerna skulle ha BESTÅENDE verkan, så det kunde hållas mellan sparningarna. Så det blev helt enkelt till att göra fler rum...

				    			</ul>
				    			</div>
				    			<div class="col-xs-6">
				    			<ul>

<li><b>Beskrivning av moment</b>
<ul>
<li><b> Kravmomenten:</b></li>
<ol>
<li><b> Getopt. Alternativ. </b></li>
Det är rätt simpelt. Inget speciellt egentligen. Vad jag valt att göra är att implementera en lösning väldigt lik den i kmom06 där vi använder oss av både opts och args. 
Till skillnad från kmom06 så används inte args, då vi bara är intresserade av att se över utifall det skickats in något opt.
Anledningen till att jag valt att implementera en lösning som är snarlik den i kmom06 är för att det minskar på min arbetslast. Ingen riktig förändring har skett, utan det
är i princip samma lösning. 
<br>
Efter att ha fått lite hjälp i gitter så har jag använt _ som variabelnamn istället för args. Jag hoppas alltså att det funkar som det ska. Validering och publicering funkar klockrent.
<br>
<li><b> Vad händer? </b> </li>
Samtliga kommandon från kravspecen har tillämpats enligt samtliga krav. 
Den enda skillnaden är att jag valt att tillåta riktning istället för fram / bak. Så man skriver alltså "gå (riktning)" för att flytta spelaren mellan rum. 
Utöver det så sköts navigeringen mellan rum genom att systemet först ser efter utifall man har tillgång (access) till det rummet. Om inte, så måste man genomföra något för att få tillgång.
Jag har även lagt till så att möjliga kommandon tillåter 'inv', 'inventarier' och 'spara' / 'save' som gör vad man kan förvänta sig att det ska göra.
<br>
Övetlag är det rättframt, kravspecen har följts både utifrån vad som ska fungera och hur det fungerar.
<br>
Målet med min speldesign har varit att hålla varje rum simpelt, med huvudsakligen maximalt ett föremål man kan interagera med alternativt att man ställs inför ett problem för att gå vidare. Detta för att göra spelupplevelsen så enkel som möjligt, men även ge spelaren en så bestående upplevelse som möjligt. Hade jag haft fler saker att interagera med i ett rum skulle både beskrivning och 'persistance' vara betydligt mer avancerad och tidskrävande. Detta känns som en bra mellan-punkt för att uppnå maximal effekt från bägge perspektiv sett.
<br>
<li><b> Interagera med objekt </b></li>
Som nämnt ovan så har varje rum ett gäng objekt i sig, oftast. Varje objekt har ett flertal attributer som alla spelar roll i hur man kan agera med dem. Anledningen till att 
jag gett varje objekt attribut istället för att endast ha dem i beskrivningen är för att ge spelaren en klarare vy om hur de kan agera med dem på ett mer DYNAMISKT sätt. 
Jag vill kunna ta bort / lägga till objekt enkelt utan att behöva ändra en massa funktioner i spelet i sin helhet, varje objekt ska ha ett visst antal attributer för att anses
vara ett fullkomligt objekt. Dessa är:<br>
<ul>
<li>item - föremålets namn</li>
<li>description - en beskrivning av föremålet </li>
<li>interact - en beskrivning om hur man kan interagera med föremålet </li>
<li>open - (fungerar endast på dörrar!). Appenderar en beskrvning på rummet </li>
<li>moveable - ett boleanskt värde som berättar utifall användaren kan flytta på objektet </li>
<li>takeable - ett boleanskt värde som berättar utifall spelaren kan ta föremålet </li>
<li>openable - ett boleanskt värde som berättar utifall spelaren kan öppna föremålet </li>
<li>kickable - ett boleanskt värde som berättar utifall spelaren kan sparka på föremålet </li>
<li>kick - en beskrivning om hur det känns att slå på föremålet (om kickable = true) </li>
<li>open - en beskrivning som skrivs ut ifall spelaren fösöker öppna föremålet. </li>
</ul>
<br>
Som nämnt så tillåter dessa attributer mig att snabbt inkludera nya eller ta bort objekt utan att spelet går sönder. Det är alltså inget som behöver ändras i kod-kroppen för att ett nytt föremål ska fungera, utan föremålet behöver endast ha de ovan nämna attributer för att lätt integeraras.
<br><br>
<li><b> Ryggsäcken och inventarier </b></li>
<br>
Som jag lite snabbt nämnde i mitt utförande så valde jag alltså att implementera en ryggsäck i spelet. Dock fungerar den lite annorlunda från hur kravspecen ser ut. 
Man kan ta upp föremål som är "takable". När dessa tas upp så tas de bort från spelvärlden (genom att sätta in rum-id i player["interacted"] och därmed ändra rumsbeskrivningen). Alla takeable föremål är unika och nyckelföremål. Detta innebär att man inte kan släppa ett föremål förän man använt det, detta är en egen restriktion som jag valt att tillsätta för att säkerställa en bekväm spelupplevelse för spelaren. Jag hade även kunnat tillsätta en ny lista / dictionary i spelar-objektet, vilket i sin tur kunde innehålla var föremålet varit släppt för att låta spelaren gå och ta upp det vid ett senare tillfälle. Men utifrån tidsbrist så har jag valt att skippa den implementeringen.
<br>
Man kan använda föremålen genom att antingen använda dem i kroppen på rummet, alltså när man bara står i rummet. Om det finns något att använda föremålet på, så visas det på skärmen och ett nytt rum låses upp. Om inte, så händer inget särskilt, utan ett snabbt felmeddelande visas. 
Det ska även nämnas att använda items läggs i player["used"] för att säkerställa att användaren kan släppa föremål. Denna variabel sparas med spelaren, så om man sparar och laddar kan man fortfarande släppa föremålet.
<br>
<br>
<li><b> Spara eller scrapa </b></li>
<br>
Som ni säkert vet vid detta tillfälle så har jag valt att genomföra min lösning med en json-fil. Dvs att ajg skippade scrapande av data. Detta för att jag är relativt bekväm med json, men även för att jag inte riktigt orkar bråka med brandväggar osv, då jag försöker kämpa mig igenom kursen relativt snabbt för att hinna med resterande kurser innan slutet på november.
<br>
Som jag även nämnt ovan så har jag på egen hand valt att INTE tillåta spelaren att spara till ny fil, eller ladda från en specifik fil. Detta dels för att underlätta på min arbetsbörda, men huvudsakligen för att jag inte vill ha några problem med data-integritet. Det ska även nämnas att jag helt enkelt inte riktigt litar på json-biblioteket. Det är inte något problem jag har rent specifikt med pythons intergrering, utan ett problem jag har rent generellt med json och att ladda / spara data till formatet. 
<br>
Vi ser även fördelen med att ha så många (viktiga) attributer på spelaren i hur jag sparar / laddar iom att detta ger möjlighet till större 'persistance' mellan spelen.
<br>
<br>
<li><b> Spel i spelen </b></li>
<br>
Jag nämnde tidigare att jag valt att inte tillämpa cursor-spelet då det var den enda extrauppgiften som jag inte genomfört i kursen.
De andra två spelen har implementerats genom att använda samma struktur som de hade under tillämpningen av Marvin(Ragnar)-momenten. Med den enda skilladen att
de bägge spelen är separata moduler som aktiveras när en spelare möter på Ragnar i de rum de är uppsatta i. Anledningen till att jag valt att ge dem egna moduler 
är för att göra det lättare för er som rättar att kunna finna eventuella fel (även fast jag inte funnit något) i de separata modulerna istället för att felsöka 
en stor fil.
<br>
Som sagt så kräver inte kryptot att man behöver dekryptera något på egen hand, utan man kan använda sig av Ragnar för att lösa allt själv ('den hårda väge'), men man kan självklart försöka själv. 
Jag har även valt att genomföra kryptot efter de rader som fanns tillgängliga i textfilen för kmom05 istället för att köra någon rotation själv. Jag tyckte det kändes som den rätta saken att göra eftersom varje mening har en annan rotation än den tidigare. Dessutom så är det utifrån den specen som ni bedömde mig (oss) tidigare.
<br>
Tic-tac-toe spelet är snarlikt den tidigare implementeringen. Det är alltså inte någon särskilt avancerad AI, utan en rätt simpel sådan. Detta gör det relativt lätt för spelaren att klara av spelet. Dessutom har den med sig sin tidigare validering, så spelaren kan varken avsiktligt eller oavsiktligt förstöra spelet genom att skriva in felaktig input. 
<br>
</ol><br>
<li><b> Projektredovisning </b></li>
<br>
Jag måste erkänna att projektet tog betydligt längre tid än vad jag själv uppskattade att det skulle ta. Detta pga flera olika anledningar, dålig tidsuppfattning, men även pga. att vissa delmoment var uppriktigt svåra att implementera.
Huvudsakligen skulle jag vilja tipsa min forntida jag att använda mig av mer tid för att designa spelet och dess delar innan jag skulle börja implementera dem; ha en god koll på hur spelar-objektet, rums-objekten, föremåls-objekten osv skulle se ut innan jag började implementera kod.
Dock är jag lite av den gamla skolan och föredrar att jobba emot ett mål genom att genomföra mindre delmoment för att sedan göra ändringar mitt i projektet. Något som i detta fall var lite extra bökigt. Antagligen för att jag fortfarande är relativt ny till Python och dess bibliotek. 
<br>
Som sagt tyckte jag det var relativt svårt. Inte överdrivet, men jag kan garanterat se varför vissa studenter med lite mindre erfarenhet skulle kunna tycka att det kändes riktigt svårt. Det var liksom en rätt brant kurva från kmom06-kmom10; från att vara guidad genom delmomenten så gavs man helt plötsligt rätt mycket frihet. Jag älskade det själv, även fast det var lite svårt, men jag kan se hur det kan vara betydligt jobbigare för någon som inte har ett gäng års erfarenhet av programering under bältet.
<br>
Jag skulle väl uppskattningsvis vilja säga att jag lagt ner omkring 25 timmar på projektet, ge eller ta 5 timmar. Hade jag kunnat göra om det skulle jag tillämpat åtminstone ett timmar bara för att göra en ordentlig ritning av systemet. Sen börjat prototypa från den specen. Dvs tillämpa en slags HCI-approach, men med fokus på mjukvaran, inte på interaktionsdesignen: 1. gather requirements, 2. design alternatives, 3. prototype, 4. evaluate.
<br>
Överlag tycker jag det var ett riktigt bra projekt och jag gillade skarpt att man fick ta tag i projektet lite som man ville. Men som jag nämnde ovan tror jag att kurvan kan ha varit lite för brant för vissa personer. Jag har inte riktigt varit alltför aktiv på gitter den senaste veckan, men jag kan itne tänka mig annat än att ni lär ha fått rätt många frågor om hur man ska gå tillväga för att tillämpa vissa strukturer och rent generllt kring flow-control osv. 
<br>
Rent konkret vad som var svårt är dock lite jobbigt att gå in på... Rent generellt så var det strukturen som jag själv tillämpade i början när jag inte var på rätfot om hur objekten skulle se ut och vad som skulle finnas i dem. En fråga jag ställde mig själv i mitten av projektet var varför jag inte har en lokal version av rooms.json i varje spelare för att se till att persistance finns kvar, detta löste jag dock lite mer fint genom att tillämpa de olika attributerna för spelaren. 
<br>
Vad som var lätt är väl egentligen allt, när man väl börjar koda. Det handlar inte om någon särskilt komplicerad kod eller struktur. Det gäller egentligen bara om att komma till en sådan del i projektet att man börjar få rätsak på saker och ting. Innan dess var det bara att bråka med strukturen av saker och ting. Kodandet självt har varit relativt enkelt. 
<br>
Jag vill avsluta med att nämna att jag lärt mig en hel del utifrån bara projektet sett. Tack för det! :)
<br><br>
<li><b> Avslutningsvis </b></li>
<br>
Jag tycker ni har gett en riktigt bra kurs som täckt all den mest grundläggande men även till viss del avancerade delarna av Python. En riktigt bra kurs som lärt mig en hel del av språkets specifika nischer. Jag trodde inte heller att jag skulle bli så utmanad av projektet som jag faktiskt blev i slutändan. Något som jag verkligen uppskattar.
<br>
Angående kursmaterialet så kan jag dock inte uttrycka mig alltför mycket. Jag har huvudsakligen använt mig av SO, Google och Gitter om jag verkligen behövt hjälp med något konkret.
Jag gillar exemplen som finns tillgängliga på github och i kurskatalogen, vilket gör det betydligt lättare för nybörjare att komma in i språket samt även förklarar lite mer avancerade ämnen i språket. 
Jag hade nog själv kanske velat se mindre bråk med pylint än vad jag stött på. Jag kan inte riktigt komma på något konkret vid detta tillfälle, men jag vet att jag haft mina frustrerande möten med den ibland. 
Jag vill även passa på att nämna att det är RIKTIGT uppskattat att ni konsekvent tvingat oss användare att använda en terminal för att genomföra kommandon. Detta är något som många studenter kanske varit lite obekväma med först, men något som garanterat kommer hjälpa dem senare. Inklusive mig.
<br>
Lärarlaget har varit riktigt bemötande, absolut inga problem där. Jag gillar även att vi använder gitter, vilket ger studenter som mig själv möjlighet att hjälpa personer som har lite mindre erfarenhet. Jag har lärt mig att jag lär mig mycket av att lära andra med de problem de kanske sitter på.
<br>
Jag har redan rekommenderat en föredetta kurskamrat att ta kurspaketet alt. söka programmet till hösten då hon har valt att sluta vid Chalmers/GU av precis samma anledningar som mig själv.
Anledningen till att jag rekommenderade kursen var huvudsakligen för att lärarlaget varit så oerhört bemötande och hjälpsamma.
<br>
Ni och kursen får 10 av 10 toasters. Bra jobbat!
</ul>
				    		   </div>
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
