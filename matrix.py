import random

from copy import deepcopy


class Matrix:

    def __init__(self,rows,cols):

        self.rows = rows
        self.cols = cols

        x =[1,2,3,4,5,6,7,8,9]
        
        self.n = [ [ (random.choice(x)) for i in range(cols) ] for j in range(rows) ]



    def add(self,m):
        
        self.c = [[None]*self.cols for i in range(self.rows)]
        md = Matrix(self.rows,self.cols)

        if self.rows != m.rows or self.cols != m.cols:
            print("Matrix's Size should be in the same size")

        else:    
            for i in range(self.rows):
                for j in range(self.cols):
                    md.n[i][j] = self.n[i][j] + m.n[i][j]
        
            return md

    
    def sub(self,m):
        """return a new Matrix object after substraction"""

        self.d =  [[None]*self.cols for i in range(self.rows)]
        me = Matrix(self.rows,self.cols)
        
        if self.rows != m.rows or self.cols != m.cols:
            print("Matrix's Size should be in the same size")

        else:    
            for i in range(self.rows):
                for j in range(self.cols):
                    me.n[i][j] = self.n[i][j] - m.n[i][j]
        
            return me
        
        
    def mul(self,m):

        self.e = [[None]*self.cols for i in range(self.rows)]
        mf = Matrix(self.rows,m.cols)

        if self.cols != m.rows :
            
            print("Matrix's Size should be in the same size")

        else:    
            for i in range(self.rows):
                for j in range(m.cols):
                    mf.n[i][j] = 0
                    for k in range (self.cols):
                        mf.n[i][j] += self.n[i][k] * m.n[k][j]
            
            return mf
        
        
    def transpose(self):
        
        self.f = [[None]*self.cols for j in range(self.rows)]
        mg = Matrix(self.rows,self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                mg.n[i][j] = self.n[j][i] 
        return mg

        
    def display(self):
        
        for i in range(self.rows):
            for j in range(self.cols):
                print (self.n[i][j],end=' ')
                
            print ('')


k=input("Enter A matrix arows:")
arows=int(k)
h=input("Enter A matrix acols:")
acols=int(h)

l=input("Enter B matrix arows:")
brows=int(l)
g=input("Enter B matrix acols:")
bcols=int(g)


ma = Matrix(arows,acols)
mb = Matrix(brows,bcols)

print("=========== MatrixA ============")
ma.display()

print("=========== MatrixB ============")
mb.display()

print("==============A+B ==============")
C = ma.add(mb)
if C != None :
    C.display()

print("============== A-B ==============")
C = ma.sub(mb)
if C != None :
    C.display()

print("============== A*B ==============")
C = ma.mul(mb)

if C != None :
    C.display()
    C = C.transpose()
    print("====== the transpose of A*B =====")
    C.display()

else:
    print("====== the transpose of A*B =====")
    print("Matrix's Size should be in the same size")
