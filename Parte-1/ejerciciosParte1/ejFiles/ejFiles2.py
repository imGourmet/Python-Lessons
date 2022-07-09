#Crear archivo .csv con las siguientes listas:


import csv


with open("pelis.csv","w", newline='') as f:
        w = csv.writer(f,delimiter=",")
        w.writerow(["1","2","3"])
        w.writerow(["Top Gun","Risky Business","Minority Report"])
        w.writerow(["Titanic","The Revenant","Inception"])
        w.writerow(["Training Day","Man on Fire","Flight"])
        





