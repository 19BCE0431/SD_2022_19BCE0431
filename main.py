board = [['-' for i in range(5)] for i in range(5)]
def show_board():
    for i in board:
        print(i)
show_board()

playerA=input("Enter character names: ").split()
board[4]=["A-"+ i for i in playerA]
playerB=input("Enter character names: ").split()
board[0]=["B-"+ i for i in playerB]
show_board()

def Amove(index,pos,choice):
     if choice=='L' and pos>0 and board[index][pos-1][0]!='A':
         if board[index][pos-1][0]=='B':
             board[index][pos],board[index][pos-1]='-',board[index][pos]
         else:
            board[index][pos],board[index][pos-1]=board[index][pos-1],board[index][pos]
     elif choice=='R' and pos<4 and board[index][pos+1][0]!='A':
         if board[index][pos+1][0]=='B':
             board[index][pos],board[index][pos-1]='-',board[index][pos]
         else:
             board[index][pos],board[index][pos+1]=board[index][pos+1],board[index][pos]
     elif choice=='F' and index>0 and board[index-1][pos][0]!='A':
         if board[index-1][pos][0]=='B':
             board[index][pos],board[index-1][pos]='-',board[index][pos]
         else:
             board[index][pos],board[index-1][pos]=board[index-1][pos],board[index][pos]
     elif choice=='B' and index<4 and board[index+1][pos][0]!='A':
         if board[index+1][pos][0]=='B':
             board[index][pos],board[index+1][pos]='-',board[index][pos]
         else:
             board[index][pos],board[index+1][pos]=board[index+1][pos],board[index][pos]
     else:
         return "Enter valid move"

def Bmove(index,pos,choice):
    if choice=='L' and pos>0 and board[index][pos-1][0]!='A':
        if board[index][pos-1][0]=='B':
            board[index][pos],board[index][pos-1]='-',board[index][pos]
        else:
            board[index][pos],board[index][pos-1]=board[index][pos-1],board[index][pos]
    elif choice=='R' and pos<4 and board[index][pos+1][0]!='A':
        if board[index][pos+1][0]=='B':
            board[index][pos],board[index][pos-1]='-',board[index][pos]
        else:
            board[index][pos],board[index][pos+1]=board[index][pos+1],board[index][pos]
    elif choice=='B' and index>0 and board[index-1][pos][0]!='A':
        if board[index-1][pos][0]=='B':
            board[index][pos],board[index-1][pos]='-',board[index][pos]
        else:
            board[index][pos],board[index-1][pos]=board[index-1][pos],board[index][pos]
    elif choice=='F' and index<4 and board[index+1][pos][0]!='A':
        if board[index+1][pos][0]=='B':
            board[index][pos],board[index+1][pos]='-',board[index][pos]
        else:
            board[index][pos],board[index+1][pos]=board[index+1][pos],board[index][pos]
    else:
        return "Enter valid move"

def index_2d(charA):
    for i, x in enumerate(board):
        if charA in x:
            return (int(i), int(x.index(charA)))

# for i,x in enumerate(board):
#     print(i,x)

# print(['A-p1', 'A-p3', 'A-p2', 'A-p4', 'A-p5'].index("A-p2"))



def askuserA():
    moveA=input("Player A move: in format [<character-name>:<F/B/L/R]")
    charA,choiceA,choiceA1=moveA[0:2],moveA[3],moveA[-1]
    indexA, posA = index_2d("A-"+charA)
    if(charA=='h1'):
        Amove(indexA,posA,choiceA)
        indexA, posA = index_2d("A-"+charA)
        Amove(indexA,posA,choiceA)
    elif(charA=='h2'):
        Amove(indexA,posA,choiceA)
        indexA, posA = index_2d("A-"+charA)
        Amove(indexA,posA,choiceA1)
    elif(charA=='h3'):
        Amove(indexA,posA,choiceA)
        indexA, posA = index_2d("A-"+charA)
        Amove(indexA,posA,choiceA)
        indexA, posA = index_2d("A-"+charA)
        Amove(indexA,posA,choiceA1)
    else:
        Amove(indexA,posA,choiceA)
    show_board()
def askuserB():
    moveB=input("Player B move: in format [<character-name>:<F/B/L/R]")
    charB,choiceB,choiceB1=moveB[0:2],moveB[3],moveB[-1]
    indexB, posB = index_2d("B-"+charB)
    if(charB=='h1'):
        Bmove(indexB,posB,choiceB)
        indexB, posB = index_2d("B-"+charB)
        Bmove(indexB,posB,choiceB)
    elif(charB=='h2'):
        Amove(indexB,posB,choiceB)
        indexB, posB = index_2d("B-"+charB)
        Amove(indexB,posB,choiceB1)
    elif(charB=='h3'):
        Bmove(indexB,posB,choiceB)
        indexB, posB = index_2d("B-"+charB)
        Bmove(indexB,posB,choiceB)
        indexB, posB = index_2d("B-"+charB)
        Amove(indexB,posB,choiceB1)
    else:
        Bmove(indexB,posB,choiceB)
    show_board()

while True:
    askuserA()
    askuserB()







