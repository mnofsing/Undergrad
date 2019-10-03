# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:12:10 2019

@author: nofse
"""
import nqueens
import random
def schedule(t,decayRate):
    return t*decayRate

def simulatedAnnealing(startBoard,decayRate,threshHold):
    
    current = startBoard
    T = 100
    numLoops = 0
    
    while(T > threshHold):
        
        
        T = schedule(T,decayRate)
        if(T == 0):
            return current
        nextList = nqueens.getSuccessorStates(current)
        
        nextNum = random.randint(0,len(nextList))
        nextState = nextList[nextNum - 1]        
        h = nqueens.numAttackingQueens(current) - nqueens.numAttackingQueens(nextState)        
        if (h > 0):
            current = nextState
        elif(h <= 0 and random.randrange(0,1) < abs((h/T))):
            numLoops = numLoops + 1
            current = nextState
        
    current.printBoard()
    return h
    
    
   
    
def main():
    
    print('**********************************')
    print('BOARD SIZE: 4 DECAY RATE 0.9 TRHESHOLD: 0.000001')
    print('**********************************')
    hAvg = 0
    for x in range(10):
        print('RUN', x)
        startingBoard = nqueens.Board(4)
        startingBoard.rand()
        startingBoard.printBoard()
        print('INITIAL h VALUE',nqueens.numAttackingQueens(startingBoard))
        print('')
        hAvg = simulatedAnnealing(startingBoard,0.9,0.000001)  
        
    print('AVERAGE h VALUE: ',hAvg/10)

    print('**********************************')
    print('BOARD SIZE: 8 DECAY RATE 0.9 TRHESHOLD: 0.000001')
    print('**********************************')
    hAvg = 0
    for x in range(10):
        print('RUN', x)
        startingBoard = nqueens.Board(8)
        startingBoard.rand()
        startingBoard.printBoard()
        print('INITIAL h VALUE',nqueens.numAttackingQueens(startingBoard))
        print('')
        hAvg = hAvg + simulatedAnnealing(startingBoard,0.9,0.000001)
    print('AVERAGE h VALUE: ',hAvg/10)
   
    print('**********************************')
    print('BOARD SIZE: 16 DECAY RATE 0.9 TRHESHOLD: 0.000001')
    print('**********************************')
    hAvg = 0
    for x in range(10):
        print('RUN', x)
        startingBoard = nqueens.Board(16)
        startingBoard.rand()
        startingBoard.printBoard()
        print('INITIAL h VALUE',nqueens.numAttackingQueens(startingBoard))
        print('')
        hAvg = hAvg + simulatedAnnealing(startingBoard,0.9,0.000001)
        print('')
    print('AVERAGE h VALUE: ',hAvg/10)
    print('**********************************')
    print('BOARD SIZE: 4 DECAY RATE 0.75 TRHESHOLD: 0.0000001')
    print('**********************************')
    hAvg = 0
    for x in range(10):
        print('RUN', x)
        startingBoard = nqueens.Board(4)
        startingBoard.rand()
        startingBoard.printBoard()
        print('INITIAL h VALUE',nqueens.numAttackingQueens(startingBoard))
        print('')
        hAvg = hAvg + simulatedAnnealing(startingBoard,0.75,0.0000001)        
    print('AVERAGE h VALUE: ',hAvg/10)
    
    
    #FINISH THE h VAL PRINTING

    print('**********************************')
    print('BOARD SIZE: 8 DECAY RATE 0.75 TRHESHOLD: 0.0000001')
    print('**********************************')
    hAvg = 0
    for x in range(10):
        print('RUN', x)
        startingBoard = nqueens.Board(8)
        startingBoard.rand()
        startingBoard.printBoard()
        print('INITIAL h VALUE',nqueens.numAttackingQueens(startingBoard))
        print('')
        hAvg = hAvg + simulatedAnnealing(startingBoard,0.75,0.0000001)
    print('AVERAGE h VALUE: ',hAvg/10)

    print('**********************************')
    print('BOARD SIZE: 16 DECAY RATE 0.75 TRHESHOLD: 0.0000001')
    print('**********************************')
    hAvg = 0
    for x in range(10):
        print('RUN', x)
        startingBoard = nqueens.Board(16)
        startingBoard.rand()
        startingBoard.printBoard()
        print('INITIAL h VALUE',nqueens.numAttackingQueens(startingBoard))
        print('')
        hAvg = hAvg + simulatedAnnealing(startingBoard,0.75,0.0000001)
    print('AVERAGE h VALUE: ',hAvg/10)
        
        
    print('**********************************')
    print('BOARD SIZE: 4 DECAY RATE 0.5 TRHESHOLD: 0.00000001')
    print('**********************************')
    hAvg = 0
    for x in range(10):
        print('RUN', x)
        startingBoard = nqueens.Board(4)
        startingBoard.rand()
        startingBoard.printBoard()
        print('INITIAL h VALUE',nqueens.numAttackingQueens(startingBoard))
        print('')
        hAvg = hAvg + simulatedAnnealing(startingBoard,0.5,0.00000001) 
    print('AVERAGE h VALUE: ',hAvg/10)
    print('**********************************')
    print('BOARD SIZE: 8 DECAY RATE 0.75 TRHESHOLD: 0.0000001')
    print('**********************************')
    hAvg = 0
    for x in range(10):
        print('RUN', x)
        startingBoard = nqueens.Board(8)
        startingBoard.rand()
        startingBoard.printBoard()
        print('INITIAL h VALUE',nqueens.numAttackingQueens(startingBoard))
        print('')
        hAvg = hAvg + simulatedAnnealing(startingBoard,0.5,0.00000001)
    print('AVERAGE h VALUE: ',hAvg/10)
    print('**********************************')
    print('BOARD SIZE: 16 DECAY RATE 0.75 TRHESHOLD: 0.0000001')
    print('**********************************')
    hAvg = 0
    for x in range(10):
        print('RUN', x)
        startingBoard = nqueens.Board(16)
        startingBoard.rand()
        startingBoard.printBoard()
        print('INITIAL h VALUE',nqueens.numAttackingQueens(startingBoard))
        print('')
        hAvg = hAvg + simulatedAnnealing(startingBoard,0.5,0.00000001)
    print('AVERAGE h VALUE: ',hAvg/10)
    
    
    
    
if __name__== "__main__":
  main()