print("Clases V2 Joel Perea")
# Zona de Clases
class Datos:
    #El Constructor
    def __init__(self,estatura,peso):
        self.estatura = estatura
        self.peso = peso
    def mostrar_Datos(self):
        print(f"Estatura : {self.estatura} mts, Peso {self.peso} kg")
    def mi_lista(self):
        Juegos=[f"Metal Gear Rising","Terraria","Clash of clans"]
        print(Juegos)
        for Juegitos in Juegos:
            print(Juegitos)
#Diccionario            
Juegotes = {
  "Juego 1:": "Metal Gear rising",
  "Juego 2:": "Terraria",
  "Juego 3:": "Clash of Clans"
}

#Tuplas
Cortes_de_pelo=("low fade","Undercut","Buzz Cut")
print("")

#Set
Top_armas={"Fusil de tirador designado térmico ","Escopeta de barril ","Subfusil de combate "
           ,"Tarro de avispas salvajes ","Cañón de Cybertron "}
print("")

# Creacion de objetos info
info=Datos(1.70,70)

# Utilizando Objeto --> info
info.mostrar_Datos()
print("")
print("Lista de Juegos Joel Perea")
print("")
info.mi_lista()
print("")

for x, y in Juegotes.items():
  print(x, y)
print("")
for zy in Cortes_de_pelo:
  print(zy)
print("")
for Armas in Top_armas:
   print(Armas)
print("")