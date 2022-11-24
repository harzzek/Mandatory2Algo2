def userinput():
    amount = input()
    amount = int(amount)
    nodearray = []
    x = 0
    y = 0

    for x in range(amount):
        nodeStr = input()
        list_of_nodes = nodeStr.split(' ')
        nodeCharArray = list(map(int, list_of_nodes))
        newnode = Node(nodeCharArray[0], nodeCharArray[1], nodeCharArray[2],
                       nodeCharArray[3], nodeCharArray[4], nodeCharArray[5])
        if (newnode.x > x):
            x = newnode.x
        if (newnode.y > y):
            y = newnode.y
        nodearray.append(newnode)

    array2d = create2dArray(x, y)
    placeNodes(nodearray, array2d)
    return nodearray, array2d, x, y


def create2dArray(x, y):
    # Create 2d array
    array2d = [[0] * (y + 1) for i in range(x + 1)]
    return array2d


def print2dArray(array2d):
    for row in array2d:
        print(row)


def o1(array2d, node):
    x = node.x
    y = node.y
    nodelist = []
    for i in range(len(array2d[x])):
        if (array2d[x][i] != 0):
            if (array2d[x][i].x != x or array2d[x][i].y != y):
                nodelist.append(array2d[x][i])
    for i in range(len(array2d)):
        if (array2d[i][y] != 0):
            if (array2d[i][y].x != x or array2d[i][y].y != y):
                nodelist.append(array2d[i][y])
    return nodelist


def createVector(node1, node2):
    return [node2.x - node1.x, node2.y - node1.y]


# eucledian distance
def distanceToNode(node1, node2):
    return ((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2) ** 0.5


def distanceToPoint(node, x, y):
    return ((node.x - x) ** 2 + (node.y - y) ** 2) ** 0.5


def reduceVector(vector):
    gcdNum = gcd(vector[0], vector[1])
    return [int(vector[0] / gcdNum), int(vector[1] / gcdNum)]


def o2(array2d, node, xmax, ymax):
    if (node.x == xmax / 2 and node.y == ymax / 2):
        return 0
    elif node.x < xmax / 2:
        if node.y < ymax / 2:
            radius = distanceToPoint(node, xmax, ymax)
            return radius
        else:
            radius = distanceToPoint(node, xmax, 0)
            return radius
    else:
        if node.y < ymax / 2:
            radius = distanceToPoint(node, 0, ymax)
            return radius
        else:
            radius = distanceToPoint(node, 0, 0)
            return radius


def badO2(nodeArray, chosenNode):
    radius = 0
    nodeToReturn = None
    for node in nodeArray:
        if (node.x != chosenNode.x or node.y != chosenNode.y):
            tempRadius = distanceToNode(node, chosenNode)
            if radius == 0:
                nodeToReturn = node
                radius = tempRadius
            elif tempRadius > radius:
                nodeToReturn = node
                radius = tempRadius
    return nodeToReturn


def o3(array2d, node, toNode):
    x = node.x
    y = node.y
    nodelist = []
    vector = createVector(node, toNode)
    vector = reduceVector(vector)
    while (x != toNode.x or y != toNode.y):
        if (len(nodelist) == 2):
            return True
        x += vector[0]
        y += vector[1]
        if (array2d[x][y] != 0):
            nodelist.append(array2d[x][y])
    return False


def o4(nodeArray, node):
    node.edges.append(nodeArray[len(nodeArray) - 1])

def placeNodes(nodearray, array2d):
    for node in nodearray:
        node.createEdges(nodearray)
        array2d[node.x][node.y] = node


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


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
        print("Node: ", self.x, self.y, self.o1, self.o2, self.o3, self.o4)

    def createEdges(self, nodearray):
        self.edges = nodearray


nodearray, array2d, xmax, ymax = userinput()
xmax = xmax + 1
ymax = ymax + 1
vector = createVector(nodearray[0], nodearray[4])
print(reduceVector(vector))
