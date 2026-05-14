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

___________________________________________

Levi része:

Ebben a projektben egy Hex táblajátékot valósítottunk meg.
A Hex játékban a tábla hatszög alakú mezőkből áll és többféle méret létezik.
Mi egy 7x7-es verziót készítettünk el.
A Hexben a játékosok egymás után tesznek színes korongokat (piros, kék) a tábla mezőire, ezzel "beszínezve" azokat.
A piros játékos kezd, utána a kék és így tovább.
Ha az egyik játékos az egyik mezőt "beszínezte", akkor azt már nem lehet megváltoztatni.
A játékosok célja, hogy a tábla két szemközti oldalát összekössék egy összefüggő vonallal a saját színükből (a vonalat az egymás mellett lévő azonos színű mezők adják).
A piros játékosnak a tábla tetejét kell az aljával összekötnie, a kék játékosnak a tábla jobb oldalát a bal oldalával.

Futtatás:

A játék futtatásához az alábbi fájlok szükségesek:
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
