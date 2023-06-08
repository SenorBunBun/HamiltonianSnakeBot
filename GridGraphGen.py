import math
import Backtracking

def GridGraphGen(height,width):
    totalnodes = height*width
    graphlist = []
    for node in range(totalnodes):
        tempnode = [0] * totalnodes
        row = node // width
        col = node - row*width

        firstrow = row == 0
        lastrow = row == height-1

        firstcol = col == 0
        lastcol = col == width - 1

        if firstrow:
            if firstcol:
                tempnode[node + width] = 1
                tempnode[node + 1] = 1
                #print(node, tempnode)
            elif lastcol:
                tempnode[node + width] = 1
                tempnode[node - 1] = 1
                #print(node, tempnode)
            else:
                tempnode[node - 1] = 1
                tempnode[node + 1] = 1
                tempnode[node + width] = 1
                #print(node, tempnode)
        elif lastrow:
            if firstcol:
                tempnode[node - width] = 1
                tempnode[node + 1] = 1
                #print(node, tempnode)
            elif lastcol:
                tempnode[node - width] = 1
                tempnode[node - 1] = 1
                #print(node, tempnode)
            else:
                tempnode[node - 1] = 1
                tempnode[node + 1] = 1
                tempnode[node - width] = 1
                #print(node, tempnode)
        else:
            if firstcol:
                tempnode[node - width] = 1
                tempnode[node + width] = 1
                tempnode[node + 1] = 1
            elif lastcol:
                tempnode[node - width] = 1
                tempnode[node + width] = 1
                tempnode[node - 1] = 1
            else:
                tempnode[node - width] = 1
                tempnode[node + width] = 1
                tempnode[node - 1] = 1
                tempnode[node + 1] = 1
        graphlist.append(tempnode)
    print("graph generated")
    return graphlist

from typing import List

def find_hamiltonian_cycle(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    path = [0]
    while len(path) > 0:
        curr = path[-1]
        # Check if all vertices have been visited
        if len(path) == n:
            # Check if the last vertex is connected to the first vertex
            if graph[curr][0] == 1:
                return path
        # Find an unvisited neighbor
        for i in range(n):
            if graph[curr][i] == 1 and i not in path:
                path.append(i)
                break
        else:
            # No unvisited neighbors, backtrack
            path.pop()
    return []
print("AA")
graph = GridGraphGen(4,4)
print(graph)
print(find_hamiltonian_cycle(graph))
