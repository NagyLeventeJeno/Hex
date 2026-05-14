Hex játék:

Kende része:

Telepítés és előfeltételek:
A program futtatásához Python 3.x verzióra van szükség. A grafikai megjelenítéshez a pygame és a tkinter könyvtárakat használjuk. A pygame telepíthető a "pip install pygame" paranccsal. A tkinter a legtöbb Python telepítésnek alapból része, de ha hiányozna, Linuxon a "sudo apt-get install python3-tk" paranccsal telepíthető.

A játék futtatása:
A játék indításához a startmenu.py programot kell futtatni. A grafikus menün keresztül választható ki az egy- vagy kétszemélyes játékmód, valamint a különböző táblaméretek (7x7 vagy 11x11).
Fontos: A program megfelelő működéséhez a startmenu.py, pvp.py és a bot.py fájloknak ugyanabban a mappában kell lenniük.

Irányítás és lehetőségek:
- Korong elhelyezése: Egérkattintással a választott mezőre.
- Újrajátszás: A játék végén, az 'R' billentyű megnyomásával a játék azonnal újraindul, azonos beállításokkal.
- Visszatérés a menübe: Az 'M' billentyű megnyomásával kiléphetünk a menübe, ahol új játékmódot vagy méretet választhatunk.
___________________________________________

Mátyás része:

A játék egyik módja mikor a gép ellen játszunk. A számítógép kezd, majd játék során a több stratégiát is alkalmaz a legyőzésünkre:
- megpróbálja akadályozni a kék (saját szín) útját, úgy hogy érzékeli, ha egy meglévő piros korong mellé teszünk egy kéket
- be vannak táplálva bizonyos stratégiai szempontból fontos koordinátájú mezők, amiket választását előnyben részesíti a gép, ilyenek pl. (1,4), (5,2), (2,2), (4,4)
- miután a fönti szabályokból már nem jön ki új lépés, gép "agya" veszi át az irányítást; itt a gép a legrövidebb utat kezdi el keresni a győzelméhez

A gép agyának működése: 
  A különböző színű mezőkhöz értékeket rendel, a számára kedvező piros mezőket beállítja 0 értkűre, a fehér mezőknek 1 lesz a súlya, míg az ellenfél, kék mezőinek nagy értéket ad, annak érdekében hogy azt elkerülje a legrövidebb út megkonstruálása során. A gép tulajdonképpen egy Dijkstra-algoritmus használ. A shortest_path() függvénnyel visszaadja az optimális útvonalat, majd a reconstruct_path() visszafejti mezőről mezőre és meglépi a megfelelőt és ezt hajtja végre újra és újra mikor sorrakerül

<img width="677" height="564" alt="Képernyőfotó 2026-05-14 - 23 26 51" src="https://github.com/user-attachments/assets/fc3daa0d-ea9e-4f6b-ba8b-f9cb79a64ba9" />

A gép egyből középre tesz, ami stratégiai szempontból a lehető legjobb első lépés, a sok irány megnyílása miatt


<img width="679" height="645" alt="Képernyőfotó 2026-05-14 - 23 25 21" src="https://github.com/user-attachments/assets/dfc7fa00-37d2-45cd-9a70-59dec1da9798" />
<img width="678" height="575" alt="Képernyőfotó 2026-05-14 - 23 25 59" src="https://github.com/user-attachments/assets/d90e4549-69c7-4179-a42b-49ca6a447ce8" />

A stratégia további része, az úgynevezet hidak kialakítása, amely lehetővé teszi a gép számára hogy bebiztosítsa az útvonalát

___________________________________________

Levi része:

Ebben a projektben egy Hex táblajátékot valósítottunk meg.
A Hex játékban a tábla hatszög alakú mezőkből áll és többféle méret létezik.
A Hexben a játékosok egymás után tesznek színes korongokat (piros, kék) a tábla mezőire, ezzel "beszínezve" azokat.
A piros játékos kezd, utána a kék és így tovább.
Ha az egyik játékos az egyik mezőt "beszínezte", akkor azt már nem lehet megváltoztatni.
A játékosok célja, hogy a tábla két szemközti oldalát összekössék egy összefüggő vonallal a saját színükből (a vonalat az egymás mellett lévő azonos színű mezők adják).
A piros játékosnak a tábla tetejét kell az aljával összekötnie, a kék játékosnak a tábla jobb oldalát a bal oldalával.

Futtatás:

A játék futtatásához az alábbi fájlok szükségesek(egy mappában):
  - startmenu.py
  - pvp.py
  - bot.py

A startmenu.py elindításával megjelenik a menü, ahol két lehetőség közül választhatunk: egyjátékos mód vagy kétjátékos mód.
A kétjátékos mód kiválsztása után három gomb jelenik meg: 7x7, 11x11, vissza.
A 7x7 és a 11x11 a játéktábla választható méretei, a vissza gomb visszavisz a startmenübe.
Ha kiválasztjuk valamelyik méretet, akkor elindul a pvp.py fájl a kiválsztott táblamérettel.
Ha az egyjátékos módot választjuk, akkor elindul a bot.py fájl 7x7-es táblamérettel.
Amikor valaki megnyeri a játékot, a játék kiírja, hogy ki nyert, majd utána az ablak nem záródik be, így megtekinthető a nyertes állás, de tovább kattintani már nem lehet.
Az ablakot a piros gombbal lehet bezárni, ekkor visszakerülünk a startmenübe.
A játék futása közben az "m" billentyű megnyomásával visszaléphetünk a startmenübe, az "r" billentyű megnyomásával pedig új játékot kezdhetünk.

Játékos lépése:

A játékos egy üres mezőbe tud kattintani, amibe bele van rajzolva egy kör. A kattintás csak akkor érvényes, ha az a körön belül történik.
Ekkor a mező beszíneződik a játékos színére és többé nem lehet rá kattintani.
Ezután a következő szín jön.
