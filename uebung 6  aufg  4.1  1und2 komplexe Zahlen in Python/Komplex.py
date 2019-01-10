
class Komplex:
    ''' Speicherung von Methoden autom. static, wenn nicht mit
    self dekl.. Mit self Dekl. sind sie nicht static, also nur
    mit Instanziierung zu verwenden.
    Für Konst. gilt dies scheinbar nicht. D.h. Vereinbarung
    Konst. groß schreiben letztlich sind es aber auch nur Var..
    Die 3 Konst enthalten je ein Tupel aus zwei Zahlen '''

    NULL = 0, 0
    EINS = 1, 0
    I = 0, 1

    x = 0
    y = 0

    '''Parametrische Überladung im Konstruktor
    wenn nur x als Eingabeoarameter gegeben, dann
    wird y auf 0 gesetzt. Bei zwei Eingabeparametern
    werden diese auf x bzw y gesetzt '''

    def __init__(self, x, y = 0.0): # Konstr. Komplex(x)
        self.x = x
        self.y = 0

    def __init__(self, x, y): # Konstr. Komplex(x, y)
        self.x = x
        self.y = y

    def __toString__(self):
        return self.x, self.y

    def re(self):
        return self.x

    def im(self):
        return self.y

    def betrag(self):
        return (((self.x**2)+(self.y**2)))**(1/2)

    def argument(self):
        return

    def konjungiert(self):
        return self.x, self.y*-1

    def add(k2, k):
        newAddKomplex = ((k.re())+(k2.re()),(k.im())+(k2.im()))
        return newAddKomplex

    def sub(k2, k):
        newSubKomplex = ((k.re())-(k2.re()),(k.im())-(k2.im()))
        return newSubKomplex

    def mult(k2, k):
        newMultKomplex = (((k.re())*(k2.re())-(k.im())*(k2.im())),((k.re())*(k2.im())+(k.im())*(k2.re())))
        return newMultKomplex

    def div(k2, k):
        #              432     112ac2    1123 + 32     112bd2    11234   432     112ac2    1123 + 32     112bd2    11234
        newDivKomplex =((((k.re())*(k2.re())) + (((k.im())*(k2.im()) / ((((k2.re()*(k2.re()) + ((k2.im())*(k2.im())) ) + ( (k.im()))*(k2.re()) - ((k.re())*(k2.im())) / ((k2.re() * (k2.re()) + ((k2.im()) * (k2.im())))))))))))
        return newDivKomplex, "incomplete"  # ich werd wahnsinnig --die vielen Klammern, keine Zeit mehr !!! :(

    def istGleich(k2, k):
        print ("k.re =", k.re(), "vergleich mit k2.re", (k2.re()), "   k2.im", (k.im()), "vergleich mit k2.im",  (k2.im()) )
        if ((k.re())==(k2.re()) and (k.im())==(k2.im())):
            return "true"
        else:
            return "false"



