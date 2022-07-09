
#Para su reuso es preferible guardar en lista el archivo a leer/escribir

my_list = list()

with open("st.txt","r") as f:
    my_list.append(f.read())

print(my_list)

