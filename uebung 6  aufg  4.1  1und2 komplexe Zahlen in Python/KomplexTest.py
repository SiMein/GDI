import Komplex

komplex1 = Komplex.Komplex(42, 0)
komplex2 = Komplex.Komplex(10.5, -14)
komplex3 = Komplex.Komplex(-3, 28.2)

opkomplex1 = Komplex.Komplex(42, 0)

print("Komplex Zahl Nummer1 ----------------------------- :")
print("KomplexToString :", komplex1.__toString__())
print("KomplexReal :", (komplex1.re()))
print("KomplexImag :", (komplex1.im()))
print("KomplexBetrag :", (komplex1.betrag()))
print("KomplexKonjungiert :", (komplex1.konjungiert()))
print()
              # TypeError: add() takes 1 positional argument but 2 were given
              # Die Funktion verwendet den Uebergabeparamter nicht als ein Objekt,
              # sondern als 2 Zahlen  . Wie kann ich ein EIN Objekt mit 2 Werten uebergeben ???
              # meine Notloesung ist, der Funktion noch eine zweite Variable mit als Parameter
              # zu geben (k und k2)
print("addMethode", opkomplex1.add(komplex1))
print("subMethode", opkomplex1.sub(komplex1))
print("multMethode", opkomplex1.mult(komplex1))
print("divMethode", opkomplex1.div(komplex1))
print("istGleichMethode", opkomplex1.istGleich(komplex1))
print()

print("Komplex Zahl Nummer2 ----------------------------- :")
print("KomplexToString :", komplex2.__toString__())
print("KomplexReal :", (komplex2.re()))
print("KomplexImag :", (komplex2.im()))
print("KomplexBetrag :", (komplex2.betrag()))
print("KomplexKonjungiert :", (komplex2.konjungiert()))
print()
print("addMethode", opkomplex1.add(komplex2))
print("subMethode", opkomplex1.sub(komplex2))
print("multMethode", opkomplex1.mult(komplex2))
print("divMethode", opkomplex1.div(komplex2))
print("istGleichMethode", opkomplex1.istGleich(komplex2))
print()

print("Komplex Zahl Nummer3 ----------------------------- :")
print("KomplexToString :", komplex3.__toString__())
print("KomplexReal :", (komplex3.re()))
print("KomplexImag :", (komplex3.im()))
print("KomplexBetrag :", (komplex3.betrag()))
print("KomplexKonjungiert :", (komplex3.konjungiert()))
print()
print("addMethode", opkomplex1.add(komplex3))
print("subMethode", opkomplex1.sub(komplex3))
print("multMethode", opkomplex1.mult(komplex3))
print("divMethode", opkomplex1.div(komplex3))
print("istGleichMethode", opkomplex1.istGleich(komplex3))
print()




