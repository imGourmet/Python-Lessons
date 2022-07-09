
import random


palab = ["cabrales","francia","austria","pernanbuco"]

def hangman(word):
    wrong = 0
    stages = ["",
             "___________          "
             "|                    "
             "|           |        "
             "|           O        "
             "|          /|\       "
             "|          / \       "
             "|                    "
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("¡Bienvenido al ahorcado!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Adivina una letra: "            
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))   
        if "__" not in board:
            print("Victoria!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("¡Derrota! La respuesta es: {}".format(word))


hangman(random.choice(palab))






