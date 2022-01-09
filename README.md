# eZadarWebScraping
Projekt u sklopu kolegija Upravljanje znanjem

ODJEL ZA INFORMATIKU
AK. GOD.: 2021./22.
OPIS ZADATKA
TEMA PROJEKNIH ZADATAKA: Stvaranje znanja na temelju prikupljenih podataka s weba (novinskih
portala ili društvenih mreža)

1.DIO PROJEKTNOG ZADATKA

Konačan cilj projekta je analiziranje podataka koji su prikupljeni s weba automatskim postupcima te
generiranje novog znanja koje je temeljeno na otkrivenim činjenicama. Nakon faze prikupljanja,
čišćenja i organiziranja podataka, u drugoj fazi slijedi analiza takvih podataka. U postupku analize mogu
se koristiti napredne tehnike za automatsko prikupljanje podataka, algoritmi za računalnu obradu
prirodnog jezika, statističku analizu prikupljenih podataka te različite tehnike za modeliranje podataka
poput reprezentacije prikupljenih tekstualnih podataka vektorima niske dimenzionalnosti, različiti
algoritmi/modeli strojnog i dubokog učenja, kompleksne mreže, itd.

Zadatak 1. dijela projekta je da student samostalno prikupe tekstualne podatke s weba kako bi imali
testni skup podataka na kojem će kasnije, u 2. dijelu projekta, testirati pojedini algoritam za analizu
podataka, ovisno o problemu koji se modelira.

Na prikupljenim podacima mogu se napraviti analize o događajima koji su se dogodili, a bili su
zastupljeni na internetskim portalima i/ili društvenim mrežama. Primjerice, mogu se analizirati
događaji poput potresa u Hrvatskoj, održavanja dana žalosti povodom potresa koji je pogodio
Banovinu, događaji vezani za koronakrizu, pojava 3. i 4. vala pandemije, pojava cjepiva, cijepljenje i
uvođenje COVID potvrda, turizam u RH 2021, trend održavanja online nastave zbog pojave pandemije,
smrt medijski poznate osobe, Olimpijske igre, itd.

VAŽA NAPOMENA: robotsko ili automatizirano skupljanje podataka koristit ćemo u svrhe učenja,
istraživanja i proučavanja tematike iz domene upravljanja znanjem na društvenim mrežama,
internetskim portalima ili dijelovima internetskih portala koji to dopuštaju. Prikupljeni podaci se neće
javno objavljivati na drugim javnim web mjestima, a koristit će se u svrhu učenja i istraživanja na
kolegiju UPZ.

ODABIR PORTALA

Zadatak je proučiti hrvatske portale dostupne na webu te se odlučiti za jedan portal s kojeg ćete
preuzimati (skrepati) podatke. Primjeri:

  • Net.hr
  • Tportal.hr
  • 24sata.hr
  • Indeks.hr
  • Hrt.hr
  • Rtl.hr
  • hr.n1info.com
  • novatv.dnevnik.hr
  • Dnevnik.hr
  • Telegram.hr
  • Dnevno.hr
  • Jutarnji.hr
  • Vecernji.hr
  • Slobodnadalmacija.hr
  • regionalexpress.hr
  • novilist.hr
  • evarazdin.hr
  • …

UPUTE ZA PRIKUPLJANJE I ORGANIZACIJU PODATAKA

Na pojedinim novinskim portalima nalaze se slični podaci poput naslova pojedinog članka, pripadnog
teksta za svaki članak/vijest, naziv autora članka, datum objave, komentari ispod članka, ključne riječi,
tagovi i sl. Međutim, organizacija podataka i struktura HTML-a se bitno razlikuje za svaki pojedini web
portal. Pojedini portali neke elemente imaju, dok ih drugi nemaju – primjerice #tagovi ili komentari
ispod članka. Zadatak studenta je da analizira strukturu portala i strukturu članka te za svaki članak
prikupi osnovne podatke, a to su:
  1) LINK,
  2) NASLOV,
  3) POTPUNI TEKST ČLANKA,
  4) DATUM OBJAVE i
  5) KATEGORIJA/PODKATEGORIJA.
  
Osim toga, zadatak studenta je da osim prethodno navedenih osnovnih podataka, samostalno odredi
i dodatne metapodatke o članku, koji se mogu preuzeti s pojedinog portala. To su primjerice:
  1) FACEBOOK KOMENTARI,
  2) BROJ „SHERANJA“ ČLANKA,
  3) BROJ KOMENTARA,
  4) #TAGOVI ili KLJUČNE RIJEČI,
  5) …

Za prikupljanje Facebook komentara koji se odnose na pojedini novinski članak, mogu se prikupiti
dodatni ocjenski bodovi.

Podatke je potrebno strukturirati u CSV i JSON format. U nastavku je prikazana struktura organizacije
podataka u jednu CSV datoteku s podacima preuzetih s novinskog portala. Svaki redak u tablici
predstavlja podatke o jednom članku s portala.
Atributi u zaglavlju tablice su redom:

  • id
  • link
  • naslov
  • podnaslov
  • autor_članka
  • br_autorovih_članaka (ukupan broj članaka koje je autor objavio na portalu)
  • datum_objave_članka
  • br_preporuka_za_članak
  • br_komentara
  • tekst_članka
  • tagovi

Zadatak studenta je da na sličan način organiziraju strukturu svojih podataka koje će prikupljati
poštujući navedene upute i ograničenja.
PROGRAMSKI ALATI
Preporuča se korištenje programskog jezika Python 3. Prema želji studenta može se koristiti bilo koji
drugi programski jezik.

Python biblioteke koje se mogu koristiti za izvlačenje podataka iz HTML-a:
  • Beautiful Soup
  • Scrapy
  • Selenium
  • …
Osim navedenih, mogu se koristiti i drugi paketi koji sadrže pojedine module i funkcije koji mogu biti
od pomoći u specifičnim programskih zahtjevima, npr. pandas, json, scv, i sl.

OPIS PROCESA PRIKUPLJANJA PODATAKA

Proces prikupljanja podataka podijeljen je u 2 faze. U prvoj fazi potrebno je s web portala prikupiti sve
linkove s dostupnim vijestima u zadanom vremenskom periodu. Vremenski period za koji podaci/vijesti
moraju biti prikupljeni s portala su sve one vijesti koje datiraju iz perioda 1.1.2021. – 31.12.2021.
uključujući i sve objave koje su bile 1.1. i 30.12. Preporuka je da se svi prikupljeni linkovi pohrane u
prikladnu strukturu, primjerice listu ili .txt datoteku kako bi imali konačan popis linkova s kojih je
potrebno preuzeti podatke. Za svaki portal je potrebno pokupiti sve linkove iz svih rubrika/kategorija
koje portal ima, primjerice politika, sport, kultura, vijesti, crna kronika, život, i sl.
Nakon toga slijedi druga faza u kojoj se za svaki link iz liste linkova koju smo definirali u prvoj fazi,
prikupljaju podaci i metapodaci o svakom članku na portalu. U ovoj fazi, prije početka skupljanja
podataka, potrebno je načiniti popis atributa csv datoteke za pojedini portal i javiti se asistentu na
sbeliga@inf.uniri.hr za konzultacije i odobrenje. Nakon pregleda atributa (podataka i metapodataka
koje je student definirao za pojedini portal da su bitni), student će dobiti odobrenje da može nastaviti
s radom i prikupljanjem podataka. Studenti koji se ne konzultiraju na vrijeme o podacima koje će s
portala preuzimati, mogu u kasnijoj fazi biti vraćeni na fazu prikupljanja (u slučaju da su izostavili
pojedini važan podatak).

PREDAJA 1. DIJELA PROJEKTA

Kao rezultat prvog dijela projekta, u sustav Merlin je potrebno predati CSV i JSON file s preuzetim
podacima sa zadanog portala. CSV i JSON file sadrže iste podatke, samo je format datoteke drugačiji.
Datoteke nazovite prema nazivu portala s kojeg ste prikupljali podatke – npr. dnevnik.csv i
dnevnik.json i popis linkova dnevnik_linkovi.txt.
2. DIO PROJEKTNOG ZADATKA
Svaki student za podatke koje je prikupio u 1. dijelu zadatka, na određenom web portalu, vrši analizu
vezanu za tematiku pandemije izazvane koronavirusom. Analiza se vrši u nekoliko koraka, kako slijedi
dalje u opisu.

I. KVANTIFICIRANJE ČLANAKA U MEDIJIMA

Cilj prvog koraka u analizi je kvantificirati broj vijesti (objava; članaka) u medijskom prostoru koji su u
2020. godini pisali i izvještavali o koronavirusu. Student samostalno izrađuje listu pojmova vezanih za
pandemiju izazvanu koronavirusom za koje smatra da su se često pojavljivale u medijskom prostoru, a
istodobno vjerodostojno opisuju tu tematiku. Takva lista pojmova koristit će se za filtriranje „korona“
vijesti. Primjerice, to su pojmovi : SARS-CoV-2, COVID-19, corona, korona, koronavirus, korona-virus,
epidemija, pandemija, samoizolacija, novozaražen, koronakriza, propusnica, e-propusnica, cjepivo,
cijepljenje, lockdown, WHO, stožer civilne zaštite i sl. Na temelju takvog popisa pojmova potrebno je
izdvojiti objave na portalu koje sadrže te riječi (u naslovu, tekstu, tagovima i sl.) te u konačnici
numerički kvantificirati:

  a) Ukupan broj objava na portalu za vremenski period 1.1.2021. – 31.12.2021.
  b) Broj vijesti vezanih za korona tematiku.
  c) Broj vijesti vezanih za cijepljenje. (sadrže ključnu riječ cijepljenje, procijepljenost i sl. ili nazive
  cjepiva BionTech, Pfizer, Sputnik V, AstraZeneca i sl.)
  d) Broj vijesti vezanih za antimaskere.*
  e) Broj vijseti vezanih za antivaksere.*
  *Studenti samostalno definiraju listu riječi ili kriterije po kojima će odrediti takve vijesti.
  Rezultate je potrebno dobiti programskim rješenjem (skriptom, programskim kodom). Osim prikaza
  podataka iz koraka a) , b), c) i d) istu analitiku potrebno je tablično pokazati za svaki dan u godini
  (datum; broj svih objava na portalu; broj objava vezanih za koronu). Dodatno, tablično je potrebno
  prikazati i sumarni rezultat po mjesecima, dakle zbir objava, ali posebno za siječanj, veljaču, travanj, …,
  studenti.
  
Za vremenski period 1.1.2021. – 31.12.2021. potrebno je načiniti dodatnu analizu po kategorijama
objava koje web portal sadrži. Primjerice, za sport, politiku, kulturu i sl. napraviti također analizu koliko
je ukupno bilo objava u kategoriji, a koliko se objava odnosi na korona tematiku. Ovaj dio analize po
kategorijama nije potrebno raditi po mjesecima, već za svih 12 mjeseci u cjelini i to samo za kategorije.

II. VIZUALIZACIJA REZULTATA

U ovom koraku analize potrebno je podatke dobivene analizom u prethodnom koraku prikazati
vizualno koristeći razne vrste grafikona i prikaza.
Potrebno je vizualizirati podatke za:
  a) cjeloviti vremenski period 1.1.2021. – 31.12.2021. (u cjelini svih 11 mjeseci) za cijeli portal
  gdje se vidi udio korona objava i svih ostalih objava,
  b) posebno po mjesecima,
  c) posebno po kategorijama.
Studenti sami određuju vrstu grafikona za koji smatraju da najbolje prikazuje dobivene rezultate.
Također, samostalno biraju hoće li vizualizacije biti statične ili dinamične (pružaju korisniku
interaktivnost da klika po grafikonu, samostalno bira kategoriju/boju/veličinu i sl.). Dakle, prema želji
moguće je izraditi i web sučelje u kojem korisnik može sam kreirati grafikone i pregledavati rezultate.

III. ANALIZA JEZIČNOG DISKURSA KORIŠTENOG NA PORTALU

Potrebno je analizirati najčešće korištene pojmove i termine u objavama koje se analiziraju, a vezane
su za korona tematiku. Na temelju analize potrebno je zaključiti kakvim diskursom se na portalu pisalo
(pozitivan, negativan, sretan, depresivan, štur, raznolik i sl.) ovisno o nalazima najčešće korištenih riječi
u tekstovima. Potrebno je napraviti liste najčešće korištenih riječi u objavama na portalu po mjesecima.
U tekst koji se analizira spadaju i naslovi i tagovi (ako ih portal ima). U postupku predprocesiranja teksta
potrebno je iz teksta izbaciti simbole poput „ # () / * $ & ; : i sl. a tek tada raditi daljnju analizu s tekstom.
Dobivenu listu unigrama (riječ s frekvencijom pojavljivanja u tekstovima) potrebno je očistiti od
zaustavnih riječi. Zaustavne riječi su one koje se najčešće koriste, a nisu ključne za značenje u prijenosu 
informacija. To su zamjenice, veznici, prilozi, prijedlozi, usklici i sl. (npr. to su riječi ja, ti, on, i, ili, no,
već, nego, kada, zašto, … itd.). Sve takve riječi potrebno je isključiti iz dobivenog popisa unigrama, kako
bi u njemu ostale pretežito imenice. Takve riječi koje ostanu na listi, nositelji su informacijskih
vrijednosti, te su nam važne u analizi i opisu diskursa koji se koristi na web portalu.
Takva lista najčešćih pojmova mora sadržavati TOP 25 najčešće korištenih riječi za svaki mjesec.
Potrebno ih je:
  a) prikazati tablično (vidi se riječ i frekvencija njenog pojavljivanja)
  b) prikazati grafički (student sam bira način vizualizacije, npr. određena vrsta grafa, word-clouda
  i sl.)
Za dobivene liste najčešće terminologije po mjesecima, potrebno je izračunati Jaccard indeks. Pomoću
njega moguće je kvantificirati promjene u korištenim riječima (a time i korištenim diskursu) za pojedini
mjesec. Jaccard indeks proučiti na https://en.wikipedia.org/wiki/Jaccard_index te samostalno
predložiti kako bi se izračunale i numerički prikazale promjene korištenih riječi po mjesecima.
Promjene u diskursu prikazati tablično/grafički. Osim Jaccard indexa, studenti mogu predložiti i neku
dodatnu (neku drugu) mjeru kojom bi se mogle mjeriti (kvantificirati) promjene u jezičnom diskursu
(dodatni bodovi).

IV. DODATNA ANALIZA

Studenti mogu samostalno predložiti što bi se još moglo analizirati vezano za korona tematiku na
njihovom portalu za dodatne bodove.
Za cijeli projekt potrebno je napisati kratku tehničku dokumentaciju (kratko dokumentirati programski
kod). Drugi dio dokumentacije uključuje opise i interpretaciju dobivenih grafikona, tablica i rezultata.
ROK ZA PREDAJU CIJELOG PROJEKTA: 11.1.2022.
U sustav Merlin predaju se sve programske datoteke, sve slike, grafikoni i tehnička dokumentacija
(.docx/.pdf).
