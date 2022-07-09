

z = [1,3,5,7]

while True:
    answer = input("Guess a number or type q to quit \n")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
            print("please type a number or q to quit \n")
    if answer in z :
        print("You guessed correctly! \n")
    else:
        print("You guessed incorrectly \n")

 
   
    
  

