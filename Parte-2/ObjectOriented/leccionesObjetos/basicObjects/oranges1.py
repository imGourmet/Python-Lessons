


#Programación orientada a objetos


class Orange: #-------------------> CLASE
    def __init__(self,w,c):
        self.weight = w  #-----------> VARIABLES DE INSTANCIAS U OBJETOS
        self.color = c    #----------->""""""""""""""""""""""""""""""""   
        print("¡¡Instancia creada!!")
        
or1 = Orange(10,"Dark orange")    #-------> "INSTANCIALIZAR UNA CLASE"
#|_____/----------------------------------> INSTANCIA (OBJETO DE LA CLASE)

print(or1)

#ahora se pueden OBTENER Y MODIFICAR sus respectivas VARIABLES:

print(or1.weight)
print(or1.color)

or1.weight = 100
or1.color = "Light orange"

print(or1.weight)
print(or1.color)


#CREAMOS MÁS OBJETOS O INSTANCIAS:

or2 = Orange(4,"Yellow")
or3 = Orange(18,"Red")