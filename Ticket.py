class Ticket():#影响价格有两个因素，weekend，child
        def __init__(self, weekend=False, child=False):#默认值
                self.exp = 100
                if weekend:
                        self.inc = 1.2
                else:
                        self.inc = 1
                if child:
                        self.discount = 0.5
                else:
                        self.discount = 1
        def calcPrice(self, num):
                return self.exp * self.inc * self.discount * num
