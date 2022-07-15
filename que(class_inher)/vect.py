class C2dVec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
class C3dVec(C2dVec):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.kcap = k

v2d = C2dVec(1,4)
v3d = C3dVec(1,8,9)


    
