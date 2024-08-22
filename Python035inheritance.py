class A:
    def m(self):
       print("m of A is called") 

class B(A):
    def _m(self):
       print("m of BBB is called") 

class C(A):
    def m(self):
       print("m of C is called") 
       
class D(B,C):
    def m(self):
        print("m of D is called")
        B._m(self)
        
obj = D()
obj.m()