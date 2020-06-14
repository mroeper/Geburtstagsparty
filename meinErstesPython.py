""" DogStrings oder mehrzeilen Kommentar
	bei Michelle,23.01.2020
	Übung
"""
# Das ist ein einzeiliger Kommentar


meinString = "Hast du schon UML geübt?"

for i in range(1,11):
	print(meinString)
print("Hallo")	




# Datentypen/ Variablen

meinBuchstabe = "b"
meinString = "Michelle"

meinInt = 42
meinDouble = 2.5

meinBool = True
meinBool = False

# tuple: benötigen weniger Platz als lists, tuples sind nicht mit einem Index geordnet (können nicht modifiziert werden)

meinTuple = (
	2,
	3.1415,
	"a",
	"Linux ist super!"
)  

# Die list ist ein Array und kann beliebig viel modifiziert werden und ist mit einem Index geordnet 

meineList = [
	2,
	3.1415,
	"a",
	"Linux ist super!"
]

# Ein Dictionary besteht aus Key(Variable name) und Value(Variablen wert) paaren und ist Index geordnet

meinDictionary = {
	"front end":"javaScript", 
	"back end":"PHP",
	"datenbank":"SQL",
	"App dev":"Python"
}


# Input / Output(I/O)

deinName = input("Wie lautet dein Name: \n")
print("Hallo " + deinName + " \n ")


# Entscheidung / conditionals

numA = 42
numB = 16

if numA > numB: 
	print("A ist größer als B. \n")
else: 
	print("A ist kleiner als B \n")

if not(numA == numB and numA < numB):
	print("A ist gleich B \n")
elif numA < numB and numB > numA:
	print("A ist kleiner als B \n")
elif numA > numB or numB < numA:
	print("A ist größer als B \n")
else:
	print("keiner der Konditionen stimmt")
	
	
# Switches fehlen noch
	

# Schleifen / loops
"""
zaehler = 1 
while zaehler < 10:
	print("While-loop: runde ", zaehler)
	zaehler += 1

print("\n")

for zaehler1 in range(1,10):
	print("for-loop: runde ", zaehler1)
	
print("\n")

wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
for tempVar in wochentage:
	print(tempVar)
"""

# Funktionen / Methoden

def meineMethode():
	zaehler = 1 
	while zaehler < 10:
		print("While-loop: runde ", zaehler)
		zaehler += 1

	print("\n")

	for zaehler1 in range(1,10):
		print("for-loop: runde ", zaehler1)

	print("\n")

	wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
	for tempVar in wochentage:
		print(tempVar)

meineMethode()



# Klassen / Objekte

class Pferd: 
	
	# Konstruktor und Atribute
	def __init__(self, name, alter, rasse, groesse, farbe, geschlecht):
		self.name = name
		self.alter = alter
		self.rasse = rasse
		self.groesse = groesse
		self.farbe = farbe
		self.geschlecht = geschlecht
		
		
	# Methoden bzw. Funktionen

	def laufen(self):
		print("Das Pferd galoppiert! \n")
	def fressen(self):
		print("mampf \n")
	def schlafen(self):
		print("zzzzzz zzzzzz \n")
			
	
 # Objektinitializierung

Shima = Pferd("Shima", 16, "Oldenburger", 1.65, "fuchs", "stute") # Objekt der Klasse Pferd/ Shima erstellt
Shima.schlafen()
	
	



