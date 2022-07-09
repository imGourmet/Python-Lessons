


x = 10 
while x > 0:
    print('{}'.format(x))
    x-=1
print("Happy New Year!!")

#Break para parar loops

qs = ["What is your name?","What is your fav. colour?","What is your quest?"]
n = 0 
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n= (n+1) % 3

#Continue sirve para saltar indices del loop:
for i in range(1,6):
    if i == 3:
        continue
    print(i)

i = 1               #Mismo ejemplo con función while
while i <= 5:
    if i == 3:
        i +=1
        continue
    print(i)
    i +=1

