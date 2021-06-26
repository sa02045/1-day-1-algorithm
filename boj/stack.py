class stack:
    def __init__(self) -> None:
        self.top =[]

    def __len__(self):
        return len(self.top)
    def push(self,item):
        self.top.append(item)
    def isEmpty(self):
        return self.__len__ ==0
    
    def pop(self):
        if self.isEmpty(self):
            return False
        return self.top.pop(-1)