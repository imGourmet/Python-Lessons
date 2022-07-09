
#Ejemplo con función open-close

st = open("st.txt","w")
st.write("Hi from Python! \n")
st.close()

#Ejmplo con with-statement

with open("st.txt","w") as f:
    f.write(" \n Hola baby")

