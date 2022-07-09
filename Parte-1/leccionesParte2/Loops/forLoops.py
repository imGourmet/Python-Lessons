#Una serie de loops básicos

#Ejemplo 1: lista
TV = ["Narcos","GOT","Vice"]
i = 0
for show in TV:
    new = TV[i]
    TV[i] = new
    i += 1
print(TV)

#Ejemplo 2: diccionario
people = {"G. Bluth II":
"A.development","Barney":"HIMYM","Dennis":"Always Sunny"}

for character in people:
    print(character)

#Ejemplo 3: Tupla
coms = ("A. development","Friends","Always Sunny")
for show in coms:
    print(show)


#Loop compuesto
all_shows = []

for show in TV:
    show = show.upper
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

#Función range:
for i in range(1,11):
    print(i)