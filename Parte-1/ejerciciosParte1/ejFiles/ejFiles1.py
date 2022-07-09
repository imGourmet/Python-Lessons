#Pregunta entrada usuario y guarda ésta en otro archivo




add = input("¿De dónde eres?")

with open("st.txt","w") as f:
    f.write(add)