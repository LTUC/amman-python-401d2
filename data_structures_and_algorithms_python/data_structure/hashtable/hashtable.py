class Hashmap:
    def __init__(self , size  = 1024):
        self.size = size 
        self.map = [None]* size


    def add(self,key ,value):
        idx = self.Get_hash(key)
        # there is no colision
        if not self.map[idx]:
            self.map[idx] = [[key, value],]
        # there is a colision
        else:
            self.map[idx].append([key , value])
        self.map[idx] = [key , value]


    def find(self,key):
        idx = self.Get_hash(key)
        if  self.map[idx]:
            while  self.map[idx]:
                if  self.map[idx][0] == key:
                    return  self.map[idx][1]
               



    def contains(self, key):
        idx = self.Get_hash(key)
        if not self.map[idx]:
            return False
        else: 
            while self.map[idx] :
                if self.map[idx][0] == key:
                    return True   



    def Get_hash(self , key):
        # 1. calculate the sum of all asccii codes.
        ascii_total = 0
        for ch in key:
            ascii_total += ord(ch) 
        # 2. multiply by the prime number.
        hashed = ascii_total * 17
        # 3. modula by size of array.
        hashed = hashed % self.size
        return hashed 


# ----------------------------- 
       





