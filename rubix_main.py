'''
---------------------
  Rubix Cube Solver
---------------------
'''

#Imports
import json

#Global variables
cube = {'a1':'n','a2':'n','a3':'n','a4':'n','a5':'n','a6':'n','a7':'n','a8':'n',\
        'b1':'n','b2':'n','b3':'n','b4':'n','b5':'n','b6':'n','b7':'n','b8':'n',\
        'c1':'n','c2':'n','c3':'n','c4':'n','c5':'n','c6':'n','c7':'n','c8':'n',\
        'd1':'n','d2':'n','d3':'n','d4':'n','d5':'n','d6':'n','d7':'n','d8':'n',\
        'e1':'n','e2':'n','e3':'n','e4':'n','e5':'n','e6':'n','e7':'n','e8':'n',\
        'f1':'n','f2':'n','f3':'n','f4':'n','f5':'n','f6':'n','f7':'n','f8':'n'}

#shuffle = "r r d r' d f l l b f' u u r"
solved_cube = {'a1':'w','a2':'w','a3':'w','a4':'w','a5':'w','a6':'w','a7':'w','a8':'w',\
              'b1':'o','b2':'o','b3':'o','b4':'o','b5':'o','b6':'o','b7':'o','b8':'o',\
              'c1':'y','c2':'y','c3':'y','c4':'y','c5':'y','c6':'y','c7':'y','c8':'y',\
              'd1':'r','d2':'r','d3':'r','d4':'r','d5':'r','d6':'r','d7':'r','d8':'r',\
              'e1':'b','e2':'b','e3':'b','e4':'b','e5':'b','e6':'b','e7':'b','e8':'b',\
              'f1':'g','f2':'g','f3':'g','f4':'g','f5':'g','f6':'g','f7':'g','f8':'g'}

movelist = []

#Function to define moves on a rubix cube
def makemove(move,test=False):
    global cube

    #defined moves:
    #   r  : right column up
    #   r' : right column down
    #   l  : left column down
    #   l' : left column up
    #   f  : front face clockwise
    #   f' : front face anticlockwise
    #   b  : back face anticlockwise
    #   b' : back face clockwise
    #   u  : upper row left
    #   u' : upper row right
    #   d  : lower row right
    #   d' : lower row left

    
    temporary_cube = cube.copy()
    fromlst,tolst = [],[]
    if move == 'r':
        fromlst = ['a3','a5','a8','b3','b5','b8','c1','c4','c6','d3','d5','d8','e1','e2','e3','e4','e5','e6','e7','e8']
        tolst = ['d3','d5','d8','a3','a5','a8','b8','b5','b3','c6','c4','c1','e6','e4','e1','e7','e2','e8','e5','e3']
    elif move == "r'":
        tolst = ['a3','a5','a8','b3','b5','b8','c1','c4','c6','d3','d5','d8','e1','e2','e3','e4','e5','e6','e7','e8']
        fromlst = ['d3','d5','d8','a3','a5','a8','b8','b5','b3','c6','c4','c1','e6','e4','e1','e7','e2','e8','e5','e3']

    elif move == 'l':
        fromlst = ['a1','a4','a6','d1','d4','d6','b1','b4','b6','c8','c5','c3','f1','f2','f3','f4','f5','f6','f7','f8']
        tolst = ['b1','b4','b6','a1','a4','a6','c8','c5','c3','d1','d4','d6','f6','f4','f1','f7','f2','f8','f5','f3']
    elif move == "l'":
        tolst = ['a1','a4','a6','d1','d4','d6','b1','b4','b6','c8','c5','c3','f1','f2','f3','f4','f5','f6','f7','f8']
        fromlst = ['b1','b4','b6','a1','a4','a6','c8','c5','c3','d1','d4','d6','f6','f4','f1','f7','f2','f8','f5','f3']

    elif move == 'f':
        fromlst = ['a1','a2','a3','a4','a5','a6','a7','a8','b6','b7','b8','f8','f5','f3','d3','d2','d1','e1','e4','e6']
        tolst = ['a6','a4','a1','a7','a2','a8','a5','a3','f8','f5','f3','d3','d2','d1','e1','e4','e6','b6','b7','b8']
    elif move == "f'":
        tolst = ['a1','a2','a3','a4','a5','a6','a7','a8','b6','b7','b8','f8','f5','f3','d3','d2','d1','e1','e4','e6']
        fromlst = ['a6','a4','a1','a7','a2','a8','a5','a3','f8','f5','f3','d3','d2','d1','e1','e4','e6','b6','b7','b8']

    elif move == 'b': 
        fromlst = ['c1','c2','c3','c4','c5','c6','c7','c8','e3','e5','e8','d6','d7','d8','f1','f4','f6','b1','b2','b3']
        tolst = ['c6','c4','c1','c7','c2','c8','c5','c3','d8','d7','d6','f1','f4','f6','b3','b2','b1','e3','e5','e8']
    elif move == "b'":
        tolst = ['c1','c2','c3','c4','c5','c6','c7','c8','e3','e5','e8','d6','d7','d8','f1','f4','f6','b1','b2','b3']
        fromlst = ['c6','c4','c1','c7','c2','c8','c5','c3','d8','d7','d6','f1','f4','f6','b3','b2','b1','e3','e5','e8']

    elif move == 'u':
        fromlst = ['b1','b2','b3','b4','b5','b6','b7','b8','a1','a2','a3','e1','e2','e3','c1','c2','c3','f1','f2','f3']
        tolst = ['b6','b4','b1','b7','b2','b8','b5','b3','e1','e2','e3','c1','c2','c3','f1','f2','f3','a1','a2','a3']
    elif move == "u'":
        tolst = ['b1','b2','b3','b4','b5','b6','b7','b8','a1','a2','a3','e1','e2','e3','c1','c2','c3','f1','f2','f3']
        fromlst = ['b6','b4','b1','b7','b2','b8','b5','b3','e1','e2','e3','c1','c2','c3','f1','f2','f3','a1','a2','a3']
    
    elif move == 'd':
        fromlst = ['d1','d2','d3','d4','d5','d6','d7','d8','a6','a7','a8','f6','f7','f8','c6','c7','c8','e6','e7','e8']
        tolst = ['d6','d4','d1','d7','d2','d8','d5','d3','f6','f7','f8','c6','c7','c8','e6','e7','e8','a6','a7','a8']
    elif move == "d'":
        tolst = ['d1','d2','d3','d4','d5','d6','d7','d8','a6','a7','a8','f6','f7','f8','c6','c7','c8','e6','e7','e8']
        fromlst = ['d6','d4','d1','d7','d2','d8','d5','d3','f6','f7','f8','c6','c7','c8','e6','e7','e8','a6','a7','a8']
    
    #make the move
    if not test:
        movelist.append(move)
        print(move)
    for i in range(len(fromlst)):
        cube[fromlst[i]] = temporary_cube[tolst[i]]

#Function to make multiple moves on a rubix cube
def makemoves(moves, test = False, shuffle = False):
    moves_split = moves.split(' ')
    for i in moves_split:
        if shuffle:
            makemove(i,test=True)
        else:
            makemove(i)
            
        if test:
            #testprinting
            printcube()
                    
       

    
def printcube():
    templist = list(cube.items())
    for i in range(len(templist)):
        print(templist[i],end = ' ')
        if (i+1)%8 == 0:
            print()
    print()
    print()


###shuffle cube (testing)
##cube=solved_cube.copy()
##makemoves(shuffle,shuffle=True)

##for i in ['a','b','c','d','e','f']:
##    for j in ['1','2','3','4','5','6','7','8']:
##        cube[i+j] = input('Enter '+i+j+': ')

cube = {'a1': 'o', 'a2': 'w', 'a3': 'r', 'a4': 'y', 'a5': 'b', 'a6': 'y', 'a7': 'r', 'a8': 'g', 'b1': 'r', 'b2': 'o', 'b3': 'y', 'b4': 'b', 'b5': 'r', 'b6': 'w', 'b7': 'g', 'b8': 'g', 'c1': 'r', 'c2': 'w', 'c3': 'b', 'c4': 'w', 'c5': 'g', 'c6': 'r', 'c7': 'b', 'c8': 'g', 'd1': 'b', 'd2': 'g', 'd3': 'o', 'd4': 'y', 'd5': 'y', 'd6': 'w', 'd7': 'y', 'd8': 'y', 'e1': 'w', 'e2': 'b', 'e3': 'b', 'e4': 'w', 'e5': 'r', 'e6': 'y', 'e7': 'g', 'e8': 'g', 'f1': 'w', 'f2': 'o', 'f3': 'b', 'f4': 'o', 'f5': 'o', 'f6': 'o', 'f7': 'r', 'f8': 'o'}
print("CURRENT CUBE:")
print(cube)

#####
# White layer
#####

#solving white middle peices
while cube['a2'] != 'w' or cube['a4'] != 'w' or cube['a5'] != 'w' or cube['a7'] != 'w':
    #reset
    while cube['a2'] == 'w':
        makemove('f')
    #Get position of all white middle peices
    whiteloc = []
    for i,j in cube.items():
        if j == 'w':
            whiteloc.append(i)
            
    if 'b7' in whiteloc or 'e4' in whiteloc or 'd2' in whiteloc or 'f5' in whiteloc:   
        if cube['b7'] == 'w': makemoves("u f' l")
        elif cube['e4'] == 'w': makemoves("r u")
        elif cube['d2'] == 'w': makemoves("d f r")
        elif cube['f5'] == 'w': makemoves("l' u'")
        continue

    if 'b2' in whiteloc or 'e5' in whiteloc or 'd7' in whiteloc or 'f4' in whiteloc:
        while cube['b2'] != 'w': makemove('b')
        makemoves("b u u b' u u")
        continue

    if 'b4' in whiteloc or 'e2' in whiteloc or 'd5' in whiteloc or 'f7' in whiteloc:
        if cube['b4'] == 'w': makemoves("f' l")
        elif cube['e2'] == 'w': makemove("u")
        elif cube['d5'] == 'w': makemoves("f r")
        elif cube['f7'] == 'w': makemoves("f f d")
        continue

    if 'b5' in whiteloc or 'e7' in whiteloc or 'd4' in whiteloc or 'f2' in whiteloc:
        if cube['b5'] == 'w': makemoves("f r'")
        elif cube['e7'] == 'w': makemove("f f d'")
        elif cube['d4'] == 'w': makemoves("f' l'")
        elif cube['f2'] == 'w': makemove("u'")
        continue

    if 'c2' in whiteloc or 'c4' in whiteloc or 'c5' in whiteloc or 'c7' in whiteloc:
        while cube['c2'] != 'w': makemove('b')
        makemoves('u u')
        
#correcting colours
while cube['b7'] != 'o': makemove('f')
if cube['e4'] != 'b':
    if cube['d2'] == 'b': makemoves("d' f d f' d'")
    else: makemoves("r f f r' f f r")
if cube['d2'] != 'r':
    makemoves("d' f' d f")
print("WHITE CROSS SOLVED\n\n")
#solving white corners


#whitecorners = [['a1','b6','f3'],['a3','b8','e1'],['a6','f8','d1'],['a8','e6','d3'],['c1','b3','e3'],['c3','b1','f1'],['c6','e8','d8'],['c8','d6','f6']]
while cube['a1'] != 'w' or cube['a3'] != 'w' or cube['a6'] != 'w' or cube['a8'] != 'w':
    whiteloc = []
    for i,j in cube.items():
        if j == 'w' and ('2' not in i and '4' not in i and '5' not in i and '7' not in i):
            whiteloc.append(i)
            
    if 'b3' in whiteloc or 'e8' in whiteloc or 'd6' in whiteloc or 'f1' in whiteloc:
        while cube['b3'] != 'w': makemove('b')
        while cube['c1'] != cube['b7']: makemove('f')
        makemoves("u' b' u")
        continue

    if 'b1' in whiteloc or 'e3' in whiteloc or 'd8' in whiteloc or 'f6' in whiteloc:
        while cube['b1'] != 'w': makemove('b')
        while cube['c3'] != cube['b7']: makemove('f')
        makemoves("u b u'")
        continue

    if 'c1' in whiteloc or 'c3' in whiteloc or 'c6' in whiteloc or 'c8' in whiteloc:
        while cube['c3'] != 'w': makemove('b')
        while cube['a1'] == 'w': makemove('f')
        makemoves("u b u'")
        continue
    
    if 'b6' in whiteloc or 'f8' in whiteloc or 'd3' in whiteloc or 'e1' in whiteloc:
        while cube['b6'] != 'w': makemove('f')
        makemoves("u b u'")
        continue

    if 'b8' in whiteloc or 'f3' in whiteloc or 'd1' in whiteloc or 'e6' in whiteloc:
        while cube['b8'] != 'w': makemove('f')
        makemoves("u' b' u")
        continue
    
print("WHITE FACE SOLVED\n\n")
#solving first layer
while cube['b7'] != 'o': makemoves('f')
#top left
if cube['b6'] != 'o':
    while cube['b6'] != 'o': makemoves('f')
    makemoves("l' b' l")
    while cube['b7'] != 'o': makemoves('f')
    makemoves("l' b l")
    while cube['a1'] != "w": makemoves("f'")
    makemoves("l' b l")
    while cube['b7'] != 'o': makemoves('f')

#top right
if cube['b8'] != 'o':
    while cube['b8'] != 'o': makemoves('f')
    makemoves("r b r'")
    while cube['b7'] != 'o': makemoves('f')
    makemoves("r b' r'")
    while cube['a3'] != "w": makemoves("f'")
    makemoves("r b' r'")
    while cube['b7'] != 'o': makemoves('f')

#bottom left
if cube['d1'] != 'r':
    while cube['d1'] != 'r': makemoves('f')
    makemoves("l b l'")
    while cube['d2'] != 'r': makemoves('f')
    makemoves("l b' l'")
    while cube['a6'] != 'r': makemoves("f'")
    makemoves("l b' l'")
    while cube['b7'] != 'o': makemoves('f')

#bottom right
if cube['d3'] != 'r':
    while cube['d3'] != 'r': makemoves('f')
    makemoves("r' b' r")
    while cube['d2'] != 'r': makemoves('f')
    makemoves("r' b r")
    while cube['a8'] != 'r': makemoves("f'")
    makemoves("r' b r")
    while cube['b7'] != 'o': makemoves('f')

print('FIRST LAYER SOLVED\n\n')


#####
# Second layer
#####


while cube['b4'] != 'o' or cube['b5'] != 'o' or cube['d4'] != 'r' or cube['d5'] != 'r' or\
      cube['e2'] != 'b' or cube['e7'] != 'b' or cube['f2'] != 'g' or cube['f7'] != 'g':
    #Check for all inside
    if cube['b4'] != 'y' and cube['b5'] != 'y' and cube['e2'] != 'y' and cube['e7'] != 'y' and\
       cube['f2'] != 'y' and cube['f7'] != 'y' and cube['d4'] != 'y' and cube['d5'] != 'y':
        #all are inside, but are inside wrong
        #figure out which one is wrong
        if cube['b4'] != 'o' or cube['f2'] != 'g': makemoves("b' l' b l b u b' u'")
        elif cube['b5'] != 'o' or cube['e2'] != 'b': makemoves("b r b' r' b' u' b u")
        elif cube['d4'] != 'r' or cube['f7'] != 'g': makemoves("b l b' l' b' d' b d")
        elif cube['d5'] != 'r' or cube['e7'] != 'b': makemoves("b' r' b r b d b' d'")
        #makemoves("b' l' b l b u b' u'")
        

##    while cube['b2'] != 'o' or cube['e5'] != 'b' or cube['d7'] != 'r' or cube['f4'] != 'g':
##        makemove('b')
##        print('a')

    while True:
        if cube['b2'] == 'o' and cube['c2'] != 'y': break
        elif cube['e5'] == 'b' and cube['c4'] != 'y': break
        elif cube['d7'] == 'r' and cube['c7'] != 'y': break
        elif cube['f4'] == 'g' and cube['c5'] != 'y': break
        makemove('b')

    
    if cube['b2'] == 'o' and cube['c2'] != 'y':
        if cube['c2'] == 'g': makemoves("b' l' b l b u b' u'")
        elif cube['c2'] == 'b': makemoves("b r b' r' b' u' b u")
    elif cube['e5'] == 'b' and cube['c4'] != 'y':
        if cube['c4'] == 'o': makemoves("b' u' b u b r b' r'")
        elif cube['c4'] == 'r': makemoves("b d b' d' b' r' b r")
    elif cube['d7'] == 'r' and cube['c7'] != 'y':
        if cube['c7'] == 'b': makemoves("b' r' b r b d b' d'")
        elif cube['c7'] == 'g': makemoves("b l b' l' b' d' b d")
    elif cube['f4'] == 'g' and cube['c5'] != 'y':
        if cube['c5'] == 'r' : makemoves("b' d' b d b l b' l'")
        elif cube['c5'] == 'o': makemoves("b u b' u' b' l' b l")
    else: makemove('b')
    
##    else:
##        printcube()
##        if cube['b4'] != 'o': makemoves("b' l' b l b u b' u'")
##        elif cube['b5'] != 'o': makemoves("b r b' r' b' u' b u")
##        elif cube['d4'] != 'r': makemoves("b l b' l' b' d' b d")
##        elif cube['d5'] != 'r': makemoves("b' r' b r b d b' d'")
        
print('SECOND LAYER SOLVED\n\n')


#####
# Third Layer
#####

#Yellow cross
while cube['c2'] != 'y' or cube['c4'] != 'y' or cube['c5'] != 'y' or cube['c7'] != 'y':
    yellowloc = []
    for i,j in cube.items():
        if j == 'y' and ('2' in i or '4' in i or '5' in i or '7' in i):
            yellowloc.append(i)
    fixedyellow = len([i for i in yellowloc if i[0] == 'c'])

    if fixedyellow == 0:
        makemoves("u b r b' r' u'")
        continue
    while cube['c5'] != 'y' and (cube['c4'] != 'y' or cube['c7'] != 'y'): makemove('b')
    if cube['c4'] == 'y': makemoves("u r b r' b' u'")
    elif cube['c7'] == 'y': makemoves("u b r b' r' u'")
print("YELLOW CROSS SOLVED\n\n")

#yellow face
while cube['c1'] != 'y' or cube['c3'] != 'y' or cube['c6'] != 'y' or cube['c8'] != 'y':
    yellowloc = []
    for i,j in cube.items():
        if j == 'y' and ('2' not in i and '4' not in i and '5' not in i and '7' not in i):
            yellowloc.append(i)
    yellowfixed = len([i for i in yellowloc if i[0] == 'c'])
    if yellowfixed == 0: makemoves("r b r' b r b b r'")
    elif yellowfixed == 2:
        while cube['b1'] != 'y' and cube['f1'] != 'y': makemove('b')
        makemoves("r b r' b r b b r'")
    elif yellowfixed == 1:
        while cube['c3'] != 'y':
            makemove('b')
        if cube['b3'] == 'y':
            makemoves("r b r' b r b b r'")
        elif cube['e3'] == 'y':
            makemoves("b' l' b' l b' l' b' b' l")
    
print('YELLOW FACE SOLVED\n\n')

#orienting yellow corners
while cube['b3'] != 'o' or cube['b1'] != 'o' or cube['d6'] != 'r' or cube['d8'] != 'r':
##    correctcorners = 0
##    while correctcorners < 2:
##        makemove('b')
##        correctcorners = 0
##        correctcornerslst = []
##        if cube['b1'] == 'o':
##            correctcorners+=1
##            correctcornerslst.append('C')
##        if cube['b3'] == 'o':
##            correctcorners+=1
##            correctcornerslst.append('D')
##        if cube['d6'] == 'r':
##            correctcorners+=1
##            correctcornerslst.append('A')
##        if cube['d8'] == 'r':
##            correctcorners+=1
##            correctcornerslst.append('B')
##    
##    print(correctcorners, correctcornerslst)
##    if correctcorners == 2:
##        if correctcornerslst == ['A','D'] or correctcornerslst == ['B','C'] or correctcornerslst == ['D','A'] or correctcornerslst == ['C','B']:
##            makemoves("r' u r' d d r u' r' d d r r b'")
##        else:
##            while correctcornerslst != ['A','B'] or correctcornerslst != ['B','A']:
##                correctcornerslst = []
##                makemove('b')
##                print(cube['b1'],cube['b3'],cube['d6'],cube['d8'])
##                if cube['b1'] == 'o' or cube['f1'] == 'g': correctcornerslst.append('C')
##                if cube['b3'] == 'o' or cube['e3'] == 'b': correctcornerslst.append('D')
##                if cube['d6'] == 'r' or cube['f6'] == 'g': correctcornerslst.append('A')
##                if cube['d8'] == 'r' or cube['f8'] == 'g': correctcornerslst.append('B')
##            print('aaaaaaaaaa')
##            makemoves("r' u r' d d r u' r' d d r r b'")

##    correctcolour = cube['d6']
##    #find other matching color
##    if correctcolour == cube['d8']: mode = 1 #A B
##    elif correctcolour == cube['e3']: mode = 2 #A D
##    elif correctcolour == cube['b1']: mode = 3 #A C
##    print(correctcolour,mode)
##    if mode == 1:
##        makemoves("r' u r' d d r u' r' d d r r b'")
##    elif mode == 3:
##        makemove("b'")# r' u r' d d r u' r' d d r r b'")
##        printcube()
##    elif mode == 2:
##        makemoves("r' u r' d d r u' r' d d r r b'")

    if cube['d6'] == cube['d8']:
        makemoves("r' u r' d d r u' r' d d r r b'")
        break
    elif cube['e3'] == cube['e8']: makemove("b'")
    elif cube['b1'] == cube['b3']: makemoves("b b")
    elif cube['f1'] == cube['f6']: makemove("b")
    else: makemoves("r' u r' d d r u' r' d d r r b'")
    
print('YELLOW CORNERS FIXED\n\n')

if cube['b1'] != cube['b2'] and cube['e3'] != cube['e5'] and cube['d8'] != cube['d7'] and cube['f6'] != cube['f4']:
    makemoves("u u b' l r' u u l' r b' u u")
#orienting yellow middle peices
while cube['d6'] != cube['d7']:
    makemove('b')

if cube['f4'] == cube['b1']: #anticlockwise
    makemoves("u u b' l r' u u l' r b' u u")
elif cube['f4'] == cube['e3']: #clockwise
    makemoves("u u b l r' u u l' r b' u u")
##if cube['b2'] != 'o' and cube['f4'] != 'g' and cube['d7'] != 'r' and cube['e5'] != 'b':
##    makemoves("u u b l r' u u l' r b u u")
##while cube['d7'] != cube['d8']: makemove('b')
##if cube['b2'] == cube['f1']: makemoves("u u b l r' u u l' r b u u")
##else: makemoves: makemoves("u u b' l r' u u l' r b' u u")

while cube['b2'] != 'o': makemove('b')
print("THIRD LAYER SOLVED\n\n")
print(movelist)
    
