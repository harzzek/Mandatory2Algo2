def userinput():
    amount = input()
    nodearray = []
    for x in range(amount.isdigit()):
        nodeStr = input()
        nodeCharArray = nodeStr.split()
        newnode = Node(nodeCharArray[0], nodeCharArray[1], nodeCharArray[2], nodeCharArray[3],
                       nodeCharArray[4], nodeCharArray[5])
        nodearray.append(newnode)
    return nodearray

class Node:
    def __init__(self, x, y, o1, o2, o3, o4):
        self.x = x
        self.y = y
        self.o1 = o1
        self.o2 = o2
        self.o3 = o3
        self.o4 = o4

    def print(self):
        print(self.x)
        print(self.y)
        print(self.o1)
        print(self.o2)
        print(self.o3)
        print(self.o4)

userinput()

## scheduling algorithm
