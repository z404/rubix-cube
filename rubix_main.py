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

solved_cube = {'a1':'w','a2':'w','a3':'w','a4':'w','a5':'w','a6':'w','a7':'w','a8':'w',\
              'b1':'o','b2':'o','b3':'o','b4':'o','b5':'o','b6':'o','b7':'o','b8':'o',\
              'c1':'y','c2':'y','c3':'y','c4':'y','c5':'y','c6':'y','c7':'y','c8':'y',\
              'd1':'r','d2':'r','d3':'r','d4':'r','d5':'r','d6':'r','d7':'r','d8':'r',\
              'e1':'b','e2':'b','e3':'b','e4':'b','e5':'b','e6':'b','e7':'b','e8':'b',\
              'f1':'g','f2':'g','f3':'g','f4':'g','f5':'g','f6':'g','f7':'g','f8':'g'}

def makemove(move):
    global cube

    #for testing
    global solved_cube
    cube = solved_cube
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
        fromlst = ['c1','c2','c3','c4','c5','c6','c7','c8','e3','e5','e8','d8','d7','d6','f1','f4','f6','b1','b2','b3']
        tolst = ['c6','c4','c1','c7','c2','c8','c5','c3','d8','d7','d6','f1','f4','f6','b3','b2','b1','e3','e5','e8']
    elif move == "b'":
        tolst = ['c1','c2','c3','c4','c5','c6','c7','c8','e3','e5','e8','d8','d7','d6','f1','f4','f6','b1','b2','b3']
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
    for i in range(len(fromlst)):
        cube[fromlst[i]] = temporary_cube[tolst[i]]

    #testprint
    itemlst = list(cube.items())
    for i in range(len(itemlst)):
        print(itemlst[i],end=' ')
        if (i+1)%8 == 0:
            print()
        
        
