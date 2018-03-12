#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:42:39 2018

@author: Daoji Zhang
"""

from collections import defaultdict

station = ['A','B','C','D','E']
Widget1 = ['A','E','D','C','A']
Widget2 = ['B','E','A','C','D']
Widget3 = ['B','A','B','C','E']
Widget4 = ['D','A','D','B','D']
Widget5 = ['B','E','C','B','D']

#each node contains 6 elements, node[0] is current position, node[1]-node[5] are remained part of these 5 widgets
start = ('S', 'AEDCA', 'BEACD', 'BABCE', 'DADBD', 'BECBD') #the start point is at 'S' with five completed widgets

evaluated = []
discovered = []
prenode = {}
Gdis = {}
Hdis = {} #in UCS, this Hdis is 0 for every node
Tdis = {}  #Tdis will equal to the Gdis in UCS
Gdis = defaultdict(lambda: 1000000, Gdis) #both total distance and distance from start set to infinity
Tdis = defaultdict(lambda: 1000000, Tdis)

def AstarSearch():           
    discovered.append(start)
    Gdis[start]=0
    Hdis[start]=Heuristic(start)
    Tdis[start]=Hdis[start]
    while len(discovered)!=0:
        current = minTdis(discovered)
        #print(findRoute[current])
        if(finish(current)==1):
            return findRoute(current)
        
        discovered.remove(current)
        evaluated.append(current)
        
        neighbours = getNeighbours(current)
        for i in range(len(neighbours)):
            if neighbours[i] in evaluated:
                continue
            if neighbours[i] not in discovered:
                discovered.append(neighbours[i])
                
            if Gdis[current]+1 >= Gdis[neighbours[i]]:
                continue
        
            prenode[neighbours[i]]=current
            Gdis[neighbours[i]] = Gdis[current]+1          
            Hdis[neighbours[i]] = Heuristic(neighbours[i])
            Tdis[neighbours[i]] = Gdis[neighbours[i]] + Hdis[neighbours[i]]
    
    
            
def minTdis(nodes):    #return the smallest Total distance (g(n)+h(n))
    minTdis = nodes[0]
    for i in range(len(nodes)):
        if Tdis[nodes[i]]<Tdis[minTdis]:
            minTdis = nodes[i]
    return minTdis

def getNeighbours(node): #return the neighbours of current node
    result = []
    
    temp = []
    for i in range(1,6):
        if node[i]!='':
            if (node[i][0]=='A'):
                temp.append(node[i][1:])
            else:
                temp.append(node[i])
            #print(temp)
        else:
            temp.append('')
    result.append(('A', temp[0], temp[1], temp[2], temp[3], temp[4]))
    
    temp = []
    for i in range(1,6):
        if node[i]!='':
            if (node[i][0]=='B'):
                temp.append(node[i][1:])
            else:
                temp.append(node[i])
        else:
            temp.append('')
    result.append(('B', temp[0], temp[1], temp[2], temp[3], temp[4]))
    
    temp = []
    for i in range(1,6):
        if node[i]!='':
            if (node[i][0]=='C'):
                temp.append(node[i][1:])
            else:
                temp.append(node[i])
        else:
            temp.append('')
    result.append(('C', temp[0], temp[1], temp[2], temp[3], temp[4]))
    
    temp = []
    for i in range(1,6):
        if node[i]!='':
            if (node[i][0]=='D'):
                temp.append(node[i][1:])
            else:
                temp.append(node[i])
        else:
            temp.append('')
    result.append(('D', temp[0], temp[1], temp[2], temp[3], temp[4]))
    
    temp = []
    for i in range(1,6):
        if node[i]!='':
            if (node[i][0]=='E'):
                temp.append(node[i][1:])
            else:
                temp.append(node[i])
        else:
            temp.append('')
    result.append(('E', temp[0], temp[1], temp[2], temp[3], temp[4]))
    
    return result

def findRoute(node):  #This will find the path of the truck, and it does not include start 'S'
    step = node
    pathlist = []
    while step!=start:
        pathlist.append(step[0])
        step = prenode[step]
    #pathlist.append(start[0])
    pathlist.reverse()
    return pathlist

def Heuristic(node):  # In the Uniform cost search, the priority queue only depends on g(n), so the h(n) part is 0
    return 0 

def finish(node):  #check if this path have completed all 5 widgets
    result = 0
    for i in node[1:]:
        if i == '':
            result = 1
        else:
            result = 0
            break
    return result


finalpath = AstarSearch()
print(finalpath)

print(len(evaluated)) #this returns the amount of expanded nodes


    
    
    
    
        
            
                
    
    
    
