


#Para sustituir caracteres podemos usar .replace :

frase0 = "Las sardinas corren por el monte tralala "
frase1 = frase0.replace("a","u")
print("\n",frase1)

#Para encontrar el índice de un carácter usamos .index :

R = input("\n¿Qué letra busca su posición?\n").lower()
try:
    print("\n",frase0.index(R))    #¿VARIAS POSICIONES?
except:
    print("\nNo existe en esta frase.\n")

#consultar si está incluido en el string o no: 

print("\n","sardinas" in frase0,"\n","monte" not in frase0)

#Para incluir comillas en un string --> \"... \"
print("Alberto dijo \"por supuestu gallu.\"")
#Esto se llama escaping para obviar caracteres con funciones específicas en el código

#Alternativas para obviar comillas en particular: 
print('Alberto dijo\n "por supuestu gallu."')
print("Alberto dijo\n 'por supuestu gallu.'")

#Obtener partes de listas o strings:

Funk = ["Aretha Franklyn","Funckadellic","Luther Vandross","Gwen McCrae"]
print("\n",Funk[0:2])
print("\n",frase0[3:19])







