import numpy
n,m=map(int,input().split())
A=numpy.array([[*map(int,input().split())]for i in range(n)])
print(numpy.mean(A,axis=1))
print(numpy.var(A,axis=0))
print(round(numpy.std(A),11))
