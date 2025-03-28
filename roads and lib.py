import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    graph=[[] for i in range(n+1)]
    for x,y in cities:
        graph[x].append(y)
        graph[y].append(x)
    total_cost=0
    visited= [False]*(n+1)
    def dfs(u,graph,visited):
        visited[u]=True
        n_cities=1
        for v in graph[u]:
            if visited[v]==False:
                n_cities+=dfs(v,graph,visited)
        return n_cities
        
    for v in range(1,n+1):
        if visited[v]==False:
            n_cities=dfs(v,graph,visited)
            cost1=(n_cities)*c_road+c_lib
            cost2=n_cities*c_lib
            total_cost+=min(cost1,cost2)
    return total_cost
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
