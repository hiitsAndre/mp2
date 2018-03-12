#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:49:39 2018

@author: Daoji Zhang
"""

from collections import defaultdict

station = ['A','B','C','D','E']
Widget1 = ['A','E','D','C','A']
Widget2 = ['B','E','A','C','D']
Widget3 = ['B','A','B','C','E']
Widget4 = ['D','A','D','B','D']
Widget5 = ['B','E','C','B','D']

Nodedis = {('A','A'):0, ('A','B'):1064, ('A','C'):673, ('A','D'):1401, ('A','E'):277,
           ('B','A'):1064, ('B','B'):0, ('B','C'):958, ('B','D'):1934, ('B','E'):337,
           ('C','A'):673, ('C','B'):958, ('C','C'):0, ('C','D'):1001, ('C','E'):399,
           ('D','A'):1401, ('D','B'):1934, ('D','C'):1001, ('D','D'):0, ('D','E'):387,
           ('E','A'):277, ('E','B'):337, ('E','C'):399, ('E','D'):387, ('E','E'):0,
           ('S','A'):0, ('S','B'):0, ('S','C'):0, ('S','D'):0, ('S','E'):0}

#real shortest distance between each node
Realdis = {('A','A'):0, ('A','B'):614, ('A','C'):673, ('A','D'):664, ('A','E'):277,
           ('B','A'):614, ('B','B'):0, ('B','C'):736, ('B','D'):724, ('B','E'):337,
           ('C','A'):673, ('C','B'):736, ('C','C'):0, ('C','D'):786, ('C','E'):399,
           ('D','A'):664, ('D','B'):724, ('D','C'):786, ('D','D'):0, ('D','E'):387,
           ('E','A'):277, ('E','B'):337, ('E','C'):399, ('E','D'):387, ('E','E'):0,
           ('S','A'):0, ('S','B'):0, ('S','C'):0, ('S','D'):0, ('S','E'):0}
           
start = ('S', 'AEDCA', 'BEACD', 'BABCE', 'DADBD', 'BECBD')

evaluated = []
discovered = []
prenode = {}
Gdis = {}
Hdis = {}   #in UCS, Hdis is 0 for every node
Tdis = {}   # in UCS, the Tdis equals to Gdis for every node
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
                
            if Gdis[current]+Nodedis[(current[0],neighbours[i][0])] >= Gdis[neighbours[i]]:
                continue
        
            prenode[neighbours[i]]=current
            Gdis[neighbours[i]] = Gdis[current]+Nodedis[(current[0],neighbours[i][0])]        
            Hdis[neighbours[i]] = Heuristic(neighbours[i])
            Tdis[neighbours[i]] = Gdis[neighbours[i]] + Hdis[neighbours[i]]
    
    
            
def minTdis(nodes):
    minTdis = nodes[0]
    for i in range(len(nodes)):
        if Tdis[nodes[i]]<Tdis[minTdis]:
            minTdis = nodes[i]
    return minTdis

def getNeighbours(node):
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

def findRoute(node):
    step = node
    pathlist = []
    while step!=start:
        pathlist.append(step[0])
        step = prenode[step]
    #pathlist.append(start[0])
    pathlist.reverse()
    return pathlist

def Heuristic(current):#In UCS, the priority queue only depends on g(n), so h(n) will be 0 for every node
    return 0 

def finish(node):
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

totaldis = 0
for i in range(len(finalpath)-1):
    totaldis = totaldis + Nodedis[(finalpath[i],finalpath[i+1])]
print(totaldis)      #this return the final shortest distance

print(len(evaluated))#this will return the amount of expanded node
