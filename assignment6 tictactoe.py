
def show():

game_board = [ ["-" , "-" , "-"] ,
         ["-" , "-" , "-"] ,
         ["-" , "-" , "-"] ]

def show() :
    print()
    for row in game_board :
        for cell in row :
            if row == "-" : 
                print (cell, end= "   ")
            elif row == "X" :
                print (cell, end= "  ")
            elif o == "O" :
                print (cell, end= "  ")
    print()


def chek () :
    if a == 1 :
        a , b = 0 , 0
    elif a == 2 :
        a , b = 0 , 1
    elif a == 3 :
        a , b = 0 , 2
    elif a == 4 :
        a , b = 1 , 0
    elif a == 5 :
        a , b = 1 , 1
    elif a == 6 :
        a , b = 1 , 2
    elif a == 7 :
        a , b = 2 , 0
    elif a == 8 :
        a , b = 2 , 1
    elif a == 9 :
        a , b = 2 , 2
    
    if game_board[a][b] == "-" :
        if c == 1 :
            game_board[a][b] = "X"
            return True
        elif c == 2 :
            game_board[a][b] = "O"
            return True
    else :
        return False

def chek2():

    c = 0

    for row in range(0 ,3) :
        khat0 = game_board[row][0]
        khat1 = game_board[row][1]
        khat2 = game_board[row][2]
        if (khat0 == "X" and khat1 == "X" and khat2 == "X") or (khat0 == "O" and khat1 == "O" and khat2 == "O") :
            return True

    for col in range(0 ,3) :
        col0 = game_board[col][0]
        col1 = game_board[col][1]
        col2 = game_board[col][2]
        if (col0 == "X" and col11 == "X" and col2 == "X") or (col0 == "O" and col1 == "O" and col2 == "O" ) :
            return True

    if (game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X") or (game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O"):
        return True
    elif (game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X") or (game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O") :
        return True
    
    for a in game_board :
        for b in a :
            if b != "-" :
                c += 1
            if c == 9 :
                return "baz"

#player1
def player1 () :

    player1 = int(input("Enter namber : "))

    if chek(player1 , 1) :
        if chek2() == True :
            print("\n")
            print("win")
            print("\n")
            show()
            return True

        elif chek2() == "baz" :
            print("\n")
            print("mosavi")
            print("\n")
            show()
            return True
        show()

    else :
        print ("ghablan entekhab shode")
        player1()

#player2
def player2 () :
    player2 = int(input("Enter namber : "))

    if chek(player1 , 2) :
        if chek2() == True :
            print("\n")
            print("win")
            print("\n")
            show()
            return True

        elif chek2() == "baz" :
            print("\n")
            print("mosavi")
            print("\n")
            show()
            return True
        show()

    else :
        print ("ghablan entekhab shode")
        player2()
    
