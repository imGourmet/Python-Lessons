


#CONTINUACIÓN



class Orange: #-------------------> CLASE
    def __init__(self,w,c): #----------> "MÉTODO MÁGICO" PARA DEFINIR LOS "SUBMÉTODOS"
        self.weight = w  #-----------> VARIABLES DE INSTANCIAS U OBJETOS
        self.color = c    #----------->""""""""""""""""""""""""""""""""   
        self.mold = 0    #------------> *******
        print("¡¡Instancia creada!!")                            

    def rot(self, days, temp):  #********* -------> DEFINIMOS LOS PARÁMETROS DE LA NUEVA VARIABLE COMPUESTA 
        self.mold = days * temp                 #    |______(AHORA LAS NARANJAS SE PUEDEN PUDRIR)



or1 = Orange(6, "dark")
print(or1.mold)
or1.rot(10,98)
print(or1.mold)

