class Ampel():
    def __init__(self):
        self.farbe = "rot"
        
    def setze(self, farbe):
        self.farbe = farbe
        
    def umschalten(self):
        if "rot" == self.farbe:
            self.farbe = "grün"
        elif "grün" == self.farbe:
            self.farbe = "orange"
        else: self.farbe = "rot"
        
        
    def blinken(self):
        self.farbe = "orange blinken"

    def Anzeigen(self):
        print(self.farbe)
        
        
ampel = Ampel()
for i in range (9):
    ampel.umschalten()
    ampel.Anzeigen()
ampel.blinken()
ampel.Anzeigen()
ampel.umschalten()
ampel.Anzeigen()
ampel.umschalten()
ampel.Anzeigen()
ampel.setze("rot")
ampel.Anzeigen()
ampel.blinken()
ampel.Anzeigen()
ampel.umschalten()
ampel.Anzeigen()