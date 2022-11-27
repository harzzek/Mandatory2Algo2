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
        newnode = Node(x, nodeCharArray[0], nodeCharArray[1], nodeCharArray[2],
                       nodeCharArray[3], nodeCharArray[4], nodeCharArray[5])
        if (newnode.x > x):
            x = newnode.x
        if (newnode.y > y):
            y = newnode.y
        nodearray.append(newnode)

    array2d = create2dArray(x, y)
    placeNodes(nodearray, array2d)
    return nodearray, array2d, amount


def create2dArray(x, y):
    # Create 2d array
    array2d = [[0] * (y + 1) for i in range(x + 1)]
    return array2d


def print2dArray(array2d):
    for row in array2d:
        print(row)


def o1(nodeArray, array2d, node):
    x = node.x
    y = node.y
    nodelist = []
    for i in range(len(array2d[x])):
        if (array2d[x][i] != 0):
            if (array2d[x][i].x != x or array2d[x][i].y != y):
                if isEndNode(nodeArray, array2d[x][i]):
                    boo = cheeseO4(nodeArray, node)
                    if boo: node.numO1 -= 1
                else:
                    nodelist.append(array2d[x][i])
    for i in range(len(array2d)):
        if (array2d[i][y] != 0):
            if (array2d[i][y].x != x or array2d[i][y].y != y):
                if isEndNode(nodeArray, array2d[i][y]):
                    boo = cheeseO4(nodeArray, node)
                    if boo: node.numO1 -= 1
                else:
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
    if gcdNum < 0:
        gcdNum = gcdNum * -1
    return [int(vector[0] / gcdNum), int(vector[1] / gcdNum)]


def isEndNode(nodeArray, node):
    if node == nodeArray[len(nodeArray) - 1]:
        return True
    return False


def o2(node, xmax, ymax):
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


def badO2(nodeArray, node):
    radius = 0
    nodeToReturn = None
    for edge in nodeArray:
        if (edge.x != node.x or edge.y != node.y):
            tempRadius = distanceToNode(edge, node)
            if radius == 0:
                nodeToReturn = edge
                radius = tempRadius
            elif tempRadius > radius:
                nodeToReturn = edge
                radius = tempRadius
    if isEndNode(nodeArray, nodeToReturn):
        boo = cheeseO4(nodeArray, node)
        if boo: node.numO2 -= 1
    else:
        return nodeToReturn


def o3(nodeArray, array2d, node):
    nodelist = []
    for toNode in nodeArray:
        nodecross = 0
        x = node.x
        y = node.y
        if node.x != toNode.x or node.y != toNode.y:
            vector = createVector(node, toNode)
            vector = reduceVector(vector)
            while x != toNode.x or y != toNode.y:
                if nodecross == 2:
                    if isEndNode(nodeArray, toNode):
                        boo = cheeseO4(nodeArray, node)
                        if boo: node.numO3 -= 1
                    else:
                        nodelist.append(toNode)
                    break
                x += vector[0]
                y += vector[1]
                if array2d[x][y] != 0:
                    nodecross += 1
    return nodelist


def o4(nodeArray, node):
    node.edgeso4.append(nodeArray[len(nodeArray) - 1])


def cheeseO4(nodeArray, node):
    if (node.numO4 == 0):
        node.numO4 += 1
        o4(nodeArray, node)
        return True
    return False


def placeNodes(nodearray, array2d):
    for node in nodearray:
        array2d[node.x][node.y] = node


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Node:

    def __init__(self, index, x, y, numO1, numO2, numO3, numO4):
        self.index = index
        self.x = x
        self.y = y
        self.numO1 = numO1
        self.numO2 = numO2
        self.numO3 = numO3
        self.numO4 = numO4
        self.edgeso1 = []
        self.edgeso2 = []
        self.edgeso3 = []
        self.edgeso4 = []

    def print(self):
        print("Node: ", self.x, self.y, self.numO1, self.numO2, self.numO3, self.numO4)


def validateEdges(array2d, nodeArray, node):
    validEdges = []

    if node.numO4 > 0:
        o4(nodeArray, node)
    if node.numO1 > 0:
        validEdges.extend(o1(nodeArray, array2d, node))
        node.edgeso1 = validEdges
        validEdges = []
    if node.numO2 > 0:
        validEdges.append(badO2(nodeArray, node))
        node.edgeso2 = validEdges
        validEdges = []
    if node.numO3 > 0:
        validEdges.extend(o3(nodeArray, array2d, node))
        node.edgeso3 = validEdges


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s.index] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False

    def fordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

    def printGraph(self):
        for i in range(self.ROW):
            for j in range(self.ROW):
                print(self.graph[i][j], end=" ")
            print()



def createGraph(nodeArray):
    graph = []
    for node in nodeArray:
        row = []
        for node2 in nodeArray:
            row.append(0)
        graph.append(row)
    for node in nodeArray:
        for edge in node.edgeso1:
            graph[node.index][edge.index] = node.numO1
        for edge in node.edgeso2:
            graph[node.index][edge.index] = node.numO2
        for edge in node.edgeso3:
            graph[node.index][edge.index] = node.numO3
        for edge in node.edgeso4:
            graph[node.index][edge.index] = node.numO4
    return graph


nodeArray, array2d, amount = userinput()
for node in nodeArray:
    validateEdges(array2d, nodeArray, node)
graphForClass = createGraph(nodeArray)
graph = Graph(graphForClass)
graph.printGraph()
