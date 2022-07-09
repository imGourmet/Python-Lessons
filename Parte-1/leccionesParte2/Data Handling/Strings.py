


author = "Elver Gatiesa"

print(author[0],
author[1],
author[2],author[3],author[4],author[5],author[6],
author[7],author[8],author[9],author[10],author[11],author[12])

artistN = "Tomas" 
artist2N = "Turbado"
print(artistN + artist2N, author.upper(),artistN.lower())

amigo = "Joselito {}".format("Gafotas")
print(amigo)

frase1 = "{} es amigo de  {} desde hace muchos años".format(author,amigo)
print(frase1)


#Aplicación de .methods con inputs

n1 = input("Introduzca un nombre: ")
v = input("Introduzca un verbo: ")
adj = input("Introduzca un adjetivo:  ")
n2 = input("Introduzca otro nombre: ")

sen = """El susodicho {} {} al {} {}""".format(n1,v,n2,adj)
print(sen)

junta = "-".join(sen) #El .join() vacío juntaría el string
print(junta)

#O también puede juntar elementos de una lista con un espacio:

Hard_Techno = ["Shlømo","I Hate Models","Parfait","Clara Cuvé","Nastia","SNTS"]

Djs = " ".join(Hard_Techno)
print(Djs)


