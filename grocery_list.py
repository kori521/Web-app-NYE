import sqlite3

groceries = [
	"alma",
	"banán",
	"mandarin",
	"kapor",
	"tojás",
	"liszt",
	"müzli",
	"méz",
	"fagylalt",
	"gyümölcslé",
	"ketcsup",
	"citrom",
	"margarin",
	"hagyma",
	"burgonya",
	"rozmaring",
	"só",
	"tárkony",
	"ecet",
	"görögdinnye",
	"körte",
	"uborka",
	"fokhagyma",
	"sárgarépa",
	"péksütemények",
	"padlizsán",
	"tej",
	"kávé",
	"tea",
	"rizs",
	"tészta",
	"lencse",
	"édesburgonya",
	"eper",
	"vörösáfonya",
	"mangó",
	"paprika",
	"cukkini",
	"lime",
	"alaplé",
	"gomba",
	"csirke",
	"marhahús",
	"sertéshús",
	"hal",
	"tejszín",
	"fűszerpaprika",
	"kurkuma",
	"fahéj",
	"sütőtök",
	"bazsalikom",
	"paradicsom",
	"kenyér",
	"torta",
	"csokoládé",
	"rágógumi",
	"ananász",
	"narancs",
	"saláta",
	"sajt",
	"koriander"
]

groceries = sorted(groceries)

connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
	cursor.execute("insert into groceries (name) values (?)",[groceries[i]])
	print("added ", groceries[i])

connection.commit()
connection.close()