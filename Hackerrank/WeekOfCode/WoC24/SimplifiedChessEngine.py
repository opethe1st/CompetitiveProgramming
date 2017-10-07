# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Problem description - https://www.hackerrank.com/contests/w24/challenges/simplified-chess-engine """

#Functions I need to implemeent.
#need to initialize state to the original state of the board. - DONE
#need a possibleMoves function - created the helper function to each type of piece
#need a makeMove function
#need a unMakeMove function
#needs to be optimized a little though
def initialize():
    global board
    board = [['0' for i in xrange(4) ] for j in xrange(4)]
    w,b,m = map(int,raw_input().split())
    for piece in xrange(w):
        typePiece,width,breadth=raw_input().split()
        board[ ord(width[0]) - ord('A') ][ ord(breadth) - ord('1')] = 'W'+typePiece #place white piece
    for piece in xrange(b):
        typePiece,width,breadth=raw_input().split()
        board[ ord(width[0]) - ord('A') ][ ord(breadth) - ord('1')] = 'B'+typePiece #place black pieces

    for b in board:
        print b
    return board,m

def findAllpieces(player):
    global board
    pieces= [] #list of kinds and positions
    if player==False:
        for i in xrange(4):
            for j in xrange(4):
                if board[i][j][0]=='W':
                    pieces.append((board[i][j][1],(i,j)))
    elif player==True:
        for i in xrange(4):
            for j in xrange(4):
                if board[i][j][0]=='B':
                    pieces.append((board[i][j][1],(i,j)))
    return pieces

def BishopMoves(pos,kind):
    global board
    a,b = pos
    p1=[]
    for i in xrange(1,4):
        if 0<=a-i<4 and 0<=b-i<4: 
            if board[a-i][b-i]=='0':
                p1.append((a-i,b-i))
            elif board[a-i][b-i][0]==kind:
                break
            else:
                p1.append((a-i,b-i))
                break
        else:
            break
    
    for i in xrange(1,4):
        if 0<=a+i<4 and 0<=b+i<4: 
            if board[a+i][b+i]=='0':
                p1.append((a+i,b+i))
            elif board[a+i][b+i][0]==kind:
                break
            else:
                p1.append((a+i,b+i))
                break
        else:
            break
    for i in xrange(1,4):
        if 0<=a-i<4 and 0<=b+i<4: 
            if board[a-i][b+i]=='0':
                p1.append((a-i,b+i))
            elif board[a-i][b+i][0]==kind:
                break
            else:
                p1.append((a-i,b+i))
                break
        else:
            break

    for i in xrange(1,4):
        if 0<=a+i<4 and 0<=b-i<4: 
            if board[a+i][b-i]=='0':
                p1.append((a+i,b-i))
            elif board[a+i][b-i][0]==kind:
                break
            else:
                p1.append((a+i,b-i))
                break
        else:
            break
    
    #p1.append((a,b))      
    return p1
#print 'b',BishopMoves((2,2))
def KnightMoves(pos):
    a,b = pos
    possible = [(a+2,b+1),(a+2,b-1),(a-2,b+1),(a-2,b-1),(a+1,b+2),(a+1,b-2),(a-1,b+2),(a-1,b-2)]
    return [move for move in possible if 0<=move[0]<4 and 0<=move[1]<4]
#print KnightMoves((2,2))
def RookMoves(pos,kind):
    #kind is 'W ' or 'B'
    global board
    a,b = pos
    p1=[]
    for i in xrange(1,4):
        if 0<=a-i<4 and 0<=b<4: 
            if board[a-i][b]=='0':
                p1.append((a-i,b))
            elif board[a-i][b][0]==kind:
                break
            else:
                p1.append((a-i,b))
                break
        else:
            break
    for i in xrange(1,4):
        if 0<=a+i<4 and 0<=b<4: 
            if board[a+i][b]=='0':
                p1.append((a+i,b))
            elif board[a+i][b][0]==kind:
                break
            else:
                p1.append((a+i,b))
                break
        else:
            break
    for i in xrange(1,4):
        if 0<=a<4 and 0<=b-i<4: 
            if board[a][b-i]=='0':
                p1.append((a,b-i))
            elif board[a][b-i][0]==kind:
                break
            else:
                p1.append((a,b-i))
                break
        else:
            break
    for i in xrange(1,4):
        if 0<=a<4 and 0<=b+i<4: 
            if board[a][b+i]=='0':
                p1.append((a,b+i))
            elif board[a][b+i][0]==kind:
                break
            else:
                p1.append((a,b+i))
                break
        else:
            break

    #p1.append((a,b))      
    return p1
#print 'r',RookMoves((2,2))
def QueenMoves(pos,kind):
    a,b=pos
    m1 = BishopMoves(pos,kind)
    m2 = RookMoves(pos,kind)
    #print "m",m1+m2
    return m1+m2
#print 'q',QueenMoves((0,0))
def possibleMoves(player):
    #list of type and the position of a piece
    if player==False:
        kindplayer ='W'
    else:
        kindplayer ='B' 
    pieces = findAllpieces(player)
    moves = []
    for piece in pieces:
        #print piece
        kind,position = piece
        if kind=='Q':
            newpositions = QueenMoves(position,kindplayer)
        elif kind=='R':
            newpositions = RookMoves(position,kindplayer)
        elif kind=='N':
            newpositions = KnightMoves(position)
        elif kind=='B':
            newpositions = BishopMoves(position,kindplayer)
        pairsofpositions = [(position,nposition) for nposition in newpositions] 
        moves.extend(pairsofpositions)
    return moves


def makeMove(move,player,oldpiece):
    global board
    prev,p = move
    piece = board[prev[0]][prev[1]]
    removedpiece = board[p[0]][p[1]]
    #if otherspot[0]=='0' or otherspot[0]!=piece[0]: #if not the same player or empty already taken care by possible moves.
    board[prev[0]][prev[1]] = oldpiece
    board[p[0]][p[1]] = piece
    #print "piece",piece
    return removedpiece

def isQueenCaptured():
    global board
    pieces = findAllpieces(True)
    mypieces = findAllpieces(False)
    typePieces =[piece[0] for piece in pieces ]
    mytypePieces = [piece[0] for piece in mypieces ]
    #print typePieces
    if 'Q' not in typePieces and 'Q' in mytypePieces:
        return True
    else:
        return False


def canCaptureQueen(player,nmoves):
    global board
    if nmoves<=0:
        return False  #White cannot win
    else:
        if player==False:
            moves = possibleMoves(player)
            whitewinsOnce = False
            for move in moves:  
                removedpiece = makeMove(move,player,'0')
                print "\t"*(3-nmoves),'player 1',move,'moves left',nmoves-1
                for b in board:
                    print b
                print
                if removedpiece=="BQ":
                    #whitewinsOnce|=True
                    prev,p=move
                    makeMove((p,prev),player,removedpiece)
                    return True #white wins at least once from this position
                else:
                    whitewinsOnce|=canCaptureQueen(not(player),nmoves-1)
                    #if canCaptureQueen(not(player),nmoves-1):
                        #whitewinsOnce|=True
                        #return True #white wins at least once from this position
                prev,p=move
                makeMove((p,prev),player,removedpiece)
            return whitewinsOnce
        else:
            moves = possibleMoves(player)
            blackloses = True
            for move in moves:
                removedpiece = makeMove(move,player,'0')
                print "\t"*(3-nmoves),'player 2',move,'moves left',nmoves-1
                for b in board:
                    print b
                print
                if removedpiece=='WQ':
                    blackloses &=False
                else:
                    blackloses &=canCaptureQueen(not(player),nmoves-1)
                    #if canCaptureQueen(not(player),nmoves-1):
                        #blackloses &=True
                prev,p=move
                makeMove((p,prev),player,removedpiece)
            return blackloses

def whiteWin(m):
    if canCaptureQueen(False,m):
        return "YES"
    else:
        return "NO"

def solve():
    Q = input()
    for _ in xrange(Q):
        global board
        global whitewon
        whitewon = False
        board =[]
        board,m = initialize()
        print whiteWin(m)

solve()
