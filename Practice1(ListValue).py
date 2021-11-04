import time


dagen = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"]

print("Alle dagen in de week zijn:")
print(dagen)
time.sleep(3)
print("Alle werkdagen zijn?")
print(dagen[0:5])
time.sleep(3)
print("Alle weekenddagen zijn?")
print(dagen[5:])
time.sleep(3)
print("Dagen in de omgekeerde volgorde:")
dagen.reverse()
print(dagen)
time.sleep(3)
print("Alle werkdagen in de omgekeerde volgorde zijn?")
dagen.reverse()
print(dagen[0:5])
time.sleep(3)
print("Alle weekenddagen omgekeerd zijn?")
dagen.reverse
print(dagen[5:])
