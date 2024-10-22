
import ctypes

class DynamicArray:
    
    def __init__(self):
        
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)
        
    def __str__(self):
        
        temp=""
        
        for i in range(self.n):
            
            temp=temp + str(self.A[i]) + ","
            
        temp=temp[:-1]
        
        return "[" + temp + "]"
            
        
    def append(self, ele):
        
        if self.n==self.capacity:
            
            self._resize(2*self.capacity)
            
        self.A[self.n]=ele
        self.n+=1
            
    def __len__(self):
        
        return self.n
    
    def __getitem__(self, pos):
        
        if 0<=pos<=self.n:
            
            return self.A[pos]
        
        else:
            
            print("IndexError")
            
    def __delitem__(self, index):
        
        for i in range(index, self.n-1):
            
            self.A[i]=self.A[i+1]
            
        self.n-=1
        
    def remove(self, item):
        
        for i in range(self.n):
            
            if self.A[i]==item:
                
                for j in range(i, self.n-1):
                    
                    self.A[j]=self.A[j+1]
                    
                self.n-=1
                    
                break
            
            
    def _resize(self, capacity):
        
        B=self.make_array(capacity)
        
        for i in range(self.n):
            
            B[i]=self.A[i]
            
        self.A=B
        self.capacity=capacity
        
        
        
    def make_array(self,capacity):
        
        return (capacity * ctypes.py_object)()
arr1=DynamicArray()
arr1.append(1)
arr1.append(2)
len(arr1)
2
arr1[0]
1
arr1[1]
2
print(arr1)
[1,2]
arr1.append(4)
print(arr1)
[1,2,4]
del arr1[1]
print(arr1)
[1,4]
del arr1[0]
print(arr1)
[4]
arr1.append(1)
print(arr1)
[4,1]
arr1.append(3)
arr1.append(5)
print(arr1)
[4,1,3,5]
arr1.remove(1)
print(arr1)
[4,3,5]
arr1.remove(5)
print(arr1)
[4,3]
arr1.remove(100)
print(arr1)
[4,3]
arr2=DynamicArray()
arr2

print(arr2)
[]
 
