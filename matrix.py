import random

from copy import deepcopy


class Matrix:

    def __init__(self):

        k=input("Enter A matrix arows:")
        self.arows=int(k)
        h=input("Enter A matrix acols:")
        self.acols=int(h)

        l=input("Enter B matrix arows:")
        self.brows=int(l)
        g=input("Enter B matrix acols:")
        self.bcols=int(g)

        x =[1,2,3,4,5,6,7,8,9]
        y =[1,2,3,4,5,6,7,8,9]

        
        self.n = [ [ (random.choice(x)) for i in range(self.acols) ] for j in range(self.arows) ]
        self.m = [ [ (random.choice(y)) for i in range(self.bcols) ] for j in range(self.brows) ]
            
        print(self.n)
        print(self.m)

        for i in range(self.arows):
            for j in range(self.acols):
                print (self.n[i][j], end = ' ')
            print ('')

        for i in range(self.brows):
            for j in range(self.bcols):
                print (self.m[i][j], end = ' ')
            print ('')

        """Construct a (nrows X ncols) matrix"""
        
        

        pass

    def add(self):
        """return a new Matrix object after summation"""
        
        self.c = [[None]*self.acols for i in range(self.arows)]

        if self.arows != self.brows or self.acols !=self.bcols:
            print ("Matrix's Size should be in the same size")
        else:    
            for i in range(self.arows):
                for j in range(self.acols):
                     self.c[i][j] = self.n[i][j] + self.m[i][j]
        return self.c

    


    def sub(self):
        """return a new Matrix object after substraction"""

        self.d =  [[None]*self.acols for i in range(self.arows)]
        self.w = "Matrix's Size should be in the same size"
        
        if self.arows != self.brows or self.acols !=self.bcols:
            return self.w
        else:    
            for i in range(self.arows):
                for j in range(self.acols):
                     self.d[i][j] = self.n[i][j] - self.m[i][j]
        return self.d
        
        
        

    def mul(self):
        """return a new Matrix object after multiplication"""

        self.e = [[None]*self.acols for i in range(self.arows)]
        if self.arows != self.brows or self.acols !=self.bcols:
            return self.w
        else:    
            for i in range(self.arows):
                for j in range(self.acols):
                    self.e[i][j] = (self.n[i][j]) * (self.m[i][j])
        return self.e
        
        

    def transpose(self):
        """return a new Matrix object after transpose"""
        
        self.f = [[None]*self.acols for j in range(self.arows)]

        for i in range(self.arows):
                for j in range(self.acols):
                    self.f[i][j] = self.e[j][i] 
        return self.f


        
    
    def display(self):
        """Display the content in the matrix"""
        
        print("====== A+B =====")

        for i in range(self.arows):
            for j in range(self.acols):
                print (self.c[i][j],end=' ')
                
            print ('')


        print("===== A-B =====")
        
        for i in range(self.arows):
            for j in range(self.acols):
                print (self.d[i][j],end=' ')
                
            print ('')

        print("===== A*B =====")

        for i in range(self.arows):
            for j in range(self.acols):
                print (self.e[i][j],end=' ')
                
            print ('')

        print("===== the transpose of A*B =====")

        for i in range(self.arows):
            for j in range(self.acols):
                print (self.f[i][j],end=' ')

            print ('')

        
m = Matrix()
m.add()
m.sub()
m.mul()
m.transpose()
m.display()
