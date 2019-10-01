# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:11:35 2019

@author: nofse
"""
import heapq

class Node:
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent
        self.g = 0 #path cost
        self.h = 0 #heuristic cost
        self.f = 0 #A* 
        self.Astar = True
        print("NODE CREATED")
        print(self)
    def push(self,theList):
        heapq.heappush(theList,(self.h,self))
    def pushA(self,theList):
        heapq.heappush(theList,(self.f,self))
    def __lt__(self,other):
        if (self.Astar == True):
            return self.f <= other.f
        else:
            return self.h <= other.h
def readGrid(filename):
	#print('In readGrid')
	grid = []
	with open(filename) as f:
		for l in f.readlines():
			grid.append([int(x) for x in l.split()])
	
	f.close()
	print('Exiting readGrid')
	return grid


def outputGrid(grid, start, goal, path):
	#print('In outputGrid')
	filenameStr = 'path.txt'

	# Open filename
	f = open(filenameStr, 'w')

	# Mark the start and goal points
	grid[start[0]][start[1]] = 'S'
	grid[goal[0]][goal[1]] = 'G'

	# Mark intermediate points with *
	for i, p in enumerate(path):
		if i > 0 and i < len(path)-1:
			grid[p[0]][p[1]] = '*'

	# Write the grid to a file
	for r, row in enumerate(grid):
		for c, col in enumerate(row):
			
			# Don't add a ' ' at the end of a line
			if c < len(row)-1:
				f.write(str(col)+' ')
			else:
				f.write(str(col))

		# Don't add a '\n' after the last line
		if r < len(grid)-1:
			f.write("\n")

	# Close file
	f.close()
	

def heuristic(goal,newNode):#distance between created node and goal location
    dist = abs(goal[0] - newNode.value[0]) + abs(goal[1] - newNode.value[1])
    return dist


    
    

def greedy(grid,start,goal):    
    nodesExpanded = 0
    startNode = Node(start,'Source')                        
    openList = []
    heapq.heapify(openList)
    heapq.heappush(openList,(startNode.h,startNode))
    closedList = []
    current =  heapq.heappop(openList)[1] 
    current.Astar = False
    searchNotDone = True
    
    
    
    while searchNotDone:            #WHILE LOOP TO ITERATE THROUGHT THE GRID
        print('IN WHILE LOOP')
        
        if(current.value == goal):          #GOAL CHECK
            print('FOUND GOAL')
            outputGrid(grid,start,goal,setPath(current,nodesExpanded))
            break
        children = expandNode(current,openList,closedList,grid,goal) 
        print('CHIDREN FOUND')
        nodesExpanded = nodesExpanded + 1
        print(children)
        for location in children:
            if(location not in openList and location not in closedList):
                
                n = Node(location,current)
                n.h = heuristic(goal,n)
                n.Astar = False
                n.push(openList)
            
        heapq.heapify(openList)
        closedList.append(current.value)
        current = heapq.heappop(openList)[1]
        
    
    
    
    
def ACompute(nodeHval,node,grid,current):
    tempHval = nodeHval
    node.g = current.g + grid[node.value[0]][node.value[1]]
    fVal = tempHval + node.g
    return fVal


def searchASTAR(grid,start,goal):
    nodesExpanded = 0
    startNode = Node(start,'Source')                        
    openList = []
    heapq.heapify(openList)
    heapq.heappush(openList,(startNode.f,startNode))
    closedList = []
    current =  heapq.heappop(openList)[1] 
    searchNotDone = True
    
    
    
    while searchNotDone:            #WHILE LOOP TO ITERATE THROUGHT THE GRID
        print('IN WHILE LOOP')
        
        if(current.value == goal):          #GOAL CHECK
            print('FOUND GOAL')
            outputGrid(grid,start,goal,setPath(current,nodesExpanded))
            break
        children = expandNode(current,openList,closedList,grid,goal) 
        print('CHIDREN FOUND')
        nodesExpanded = nodesExpanded + 1
        print(children)
        for location in children:
            if(location not in openList and location not in closedList):
                
                n = Node(location,current)
                n.h = heuristic(goal,n)
                n.f = ACompute(n.h,n,grid,current)
                n.pushA(openList)
            
        heapq.heapify(openList)
        closedList.append(current.value)
        current = heapq.heappop(openList)[1]
    
    
    
def informedSearch():
    print('stub')




def getNeighbors(location,grid):
    print('GETTING NEIGHBORS OF:')
    print(location)
    result = []
    print(location.value)
    up = [location.value[0]-1,location.value[1]]
    print('UP')
    print(up)
    if (up[0] > -1 and grid[up[0]][up[1]] != 0):
        result.append(up)
    down = [location.value[0]+1,location.value[1]]
    if (down[0] < len(grid) and grid[down[0]][down[1]] != 0 ):
        result.append(down)
    
    left = [location.value[0],location.value[1]-1]
    if (left[1] > -1 and grid[left[0]][left[1]] != 0):
        result.append(left) 
    right = [location.value[0],location.value[1]+1]
    if (right[1] < len(grid[right[0]]) and grid[right[0]][right[1]] != 0):
        result.append(right)
    return result

def expandNode(currentNode,Olist,Clist,grid,goal):
    print('EXPANDING NODES')
    result = getNeighbors(currentNode,grid)
    expanded = []
    for location in result:
        if (location == goal):
            print('EXPANDENODE FOUND GOAL')
            expanded.append(location)
            break
        else:
            expanded.append(location)
    return expanded
def setPath(current,nodesExpanded):
    print('PRINTING PATH')
    path = [current.value]
    findStart = True
    while findStart:
        if (current.parent == 'Source'):
            #return path list?
            print('FOUND PATH USING MANHATTAN DISTANCE')
            print('NODES EXPANDED: ',nodesExpanded)
            findStart = False
            return path
        else:
            print(current.parent.value)
            path.append(current.parent.value)
            current = current.parent

    
def main():
    print('IN MAIN')
    grid = readGrid('GRID.txt')
    print(grid)
    start = [1,1]
    goal =  [4,4]
    #greedy(grid,start,goal)
    searchASTAR(grid,start,goal)
    print('DONE')


if __name__== "__main__":
  main()