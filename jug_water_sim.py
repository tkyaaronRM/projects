class Jug:
    #write your codes here
    def __init__(self, capacity):
        self.capacity = capacity
        self.water = 0
        
    def fill(self):
        self.water = self.capacity
        
    def empty(self):
        self.water = 0
        
    def pourInto(self, jug):
        space = jug.capacity - jug.water
        amt = min(space, self.water)
        jug.water += amt
        self.water -= amt
        
j3 = Jug(3)
j5 = Jug(5)

j5.fill()
j5.pourInto(j3)
j3.empty()
j5.pourInto(j3)
j5.fill()
j5.pourInto(j3)