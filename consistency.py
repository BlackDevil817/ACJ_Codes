import numpy as np
A=np.matrix([[1,2,-1],[2,1,4],[3,3,4]])
B=np.matrix([[1],[2],[1]])
AB=np.concatenate((A,B),axis=1)
rA=np.linalg.matrix_rank(A)
rAB=np.linalg.matrix_rank(AB)
n=(rA==rAB)
if (rA==rAB):
    if (rA==n):
        print("The system has unique  Solution")
        print(np.linalg.solve(A,B))
    else:
        print("The system has infinitely many solutions")
else:
    print("The system has inconsistent solution")