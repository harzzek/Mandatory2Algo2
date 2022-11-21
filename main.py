import sys


def userinput():
    amount = input()
    amount= int(amount)
    nodearray = []
    x = 0
    y = 0

    for x in range(amount):
        nodeStr = input()
        list_of_nodes = nodeStr.split(' ')
        nodeCharArray =  list(map(int, list_of_nodes))
        newnode = Node(nodeCharArray[0], nodeCharArray[1], nodeCharArray[2],
                       nodeCharArray[3], nodeCharArray[4], nodeCharArray[5])
        if(newnode.x > x):
            x = newnode.x
        if(newnode.y > y):
            y = newnode.y
        nodearray.append(newnode)

    array2d = create2dArray(x,y)
    placeNodes(nodearray, array2d)
    return nodearray, array2d


def create2dArray(x, y):
    # Create 2d array
    array2d = [[0]*(y+1) for i in range(x+1)]
    return array2d



def placeNodes(nodearray, array2d):
    for node in nodearray:
        node.createEdges(nodearray)
        array2d[node.x][node.y] = node

class Node:
    edges = []
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

    def createEdges(self, nodearray):
        self.edges = nodearray


nodearray, array2d = userinput()

