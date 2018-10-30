from scipy.spatial import distance
import heapq
from copy import deepcopy
from collections import OrderedDict
oill =0
map =[[{'Start':0},{'Cost':47},{'Cost':50},{'Cost':28},{'Cost':16},{'Cost':31},{'Cost':44},{'Cost':32},{'Cost':21},{'Cost':18},{'Cost':39},{'Cost':28},{'Cost':50},{'Cost':17},{'Cost':38},{'Cost':11},{'Cost':48},{'Cost':30},{'Cost':49},{'Cost':20},{'Cost':28},{'Cost':10},{'Cost':19},{'Cost':25},{'Cost':25}],
[{'Cost':31},{'Cost':44},{'Cost':20},{'Cost':10},{'Cost':46},{'Cost':33},{'Cost':43},{'Cost':19},{'Cost':43},{'Cost':33},{'Cost':36},{'Cost':25},{'Cost':48},{'Cost':43},{'Cost':31},{'Cost':32},{'Cost':26},{'Cost':11},{'Cost':18},{'Cost':19},{'Cost':27},{'Oil':42819,'Cost':22},{'Cost':39},{'Cost':32},{'Cost':36}],
[{'Cost':36},{'Cost':15},{'Cost':15},{'Cost':42},{'Cost':19},{'Cost':25},{'Cost':19},{'Cost':11},{'Cost':21},{'Cost':27},{'Cost':18},{'Cost':17},{'Cost':44},{'Rock':0},{'Rock':0},{'Rock':0},{'Cost':21},{'Cost':18},{'Cost':17},{'Cost':21},{'Oil':14885,'Cost':48},{'Oil':99034,'Cost':42},{'Oil':97716,'Cost':24},{'Oil':26787,'Cost':27},{'Cost':43}],
[{'Cost':35},{'Cost':26},{'Rock':0},{'Rock':0},{'Cost':17},{'Cost':11},{'Cost':19},{'Cost':15},{'Cost':41},{'Cost':19},{'Cost':11},{'Cost':31},{'Cost':17},{'Rock':0},{'Cost':42},{'Cost':31},{'Cost':44},{'Cost':20},{'Cost':33},{'Cost':41},{'Oil':85832,'Cost':13},{'Cost':11},{'Cost':30},{'Cost':38},{'Cost':36}],
[{'Cost':40},{'Cost':15},{'Cost':15},{'Cost':50},{'Cost':45},{'Cost':17},{'Cost':31},{'Cost':13},{'Cost':50},{'Cost':50},{'Cost':28},{'Cost':46},{'Cost':12},{'Cost':32},{'Cost':46},{'Cost':10},{'Cost':22},{'Cost':44},{'Cost':23},{'Cost':50},{'Oil':96198,'Cost':40},{'Cost':38},{'Cost':21},{'Cost':16},{'Cost':31}],
[{'Cost':14},{'Cost':27},{'Cost':40},{'Cost':12},{'Cost':11},{'Cost':16},{'Cost':40},{'Cost':50},{'Cost':17},{'Cost':18},{'Cost':42},{'Cost':40},{'Cost':36},{'Cost':27},{'Cost':32},{'Cost':42},{'Cost':14},{'Cost':39},{'Cost':27},{'Cost':40},{'Cost':42},{'Cost':19},{'Cost':50},{'Cost':45},{'Cost':34}],
[{'Cost':33},{'Cost':36},{'Cost':19},{'Cost':45},{'Cost':12},{'Rock':0},{'Cost':29},{'Cost':10},{'Cost':27},{'Cost':47},{'Cost':35},{'Cost':13},{'Cost':49},{'Cost':31},{'Cost':28},{'Cost':15},{'Cost':50},{'Cost':47},{'Cost':27},{'Cost':27},{'Oil':74492,'Cost':34},{'Oil':91558,'Cost':38},{'Cost':38},{'Cost':34},{'Cost':14}],
[{'Cost':36},{'Cost':11},{'Cost':36},{'Cost':15},{'Cost':30},{'Rock':0},{'Cost':18},{'Cost':33},{'Cost':37},{'Cost':36},{'Cost':24},{'Cost':41},{'Cost':14},{'Cost':18},{'Cost':12},{'Oil':79286,'Cost':21},{'Cost':11},{'Cost':11},{'Rock':0},{'Cost':36},{'Cost':38},{'Oil':44764,'Cost':30},{'Cost':17},{'Cost':19},{'Cost':42}],
[{'Cost':49},{'Rock':0},{'Cost':12},{'Cost':32},{'Cost':27},{'Rock':0},{'Cost':28},{'Cost':20},{'Cost':33},{'Cost':20},{'Cost':26},{'Cost':19},{'Oil':83235,'Cost':43},{'Oil':53336,'Cost':49},{'Oil':35034,'Cost':38},{'Oil':20560,'Cost':29},{'Cost':40},{'Cost':36},{'Rock':0},{'Cost':29},{'Oil':31653,'Cost':17},{'Oil':17392,'Cost':47},{'Cost':32},{'Cost':25},{'Cost':46}],
[{'Cost':38},{'Cost':30},{'Cost':38},{'Cost':33},{'Cost':15},{'Rock':0},{'Cost':36},{'Cost':27},{'Cost':12},{'Cost':49},{'Cost':41},{'Cost':38},{'Cost':17},{'Cost':12},{'Cost':31},{'Oil':56988,'Cost':47},{'Oil':36637,'Cost':45},{'Cost':10},{'Cost':30},{'Cost':50},{'Cost':16},{'Cost':16},{'Cost':35},{'Cost':22},{'Cost':36}],
[{'Cost':43},{'Cost':36},{'Oil':43908,'Cost':41},{'Cost':41},{'Cost':24},{'Cost':26},{'Cost':50},{'Cost':23},{'Cost':38},{'Cost':37},{'Cost':23},{'Cost':16},{'Cost':16},{'Cost':15},{'Cost':23},{'Cost':43},{'Cost':22},{'Cost':40},{'Cost':11},{'Cost':26},{'Cost':24},{'Cost':49},{'Cost':33},{'Cost':23},{'Cost':18}],
[{'Cost':34},{'Cost':39},{'Oil':61054,'Cost':44},{'Cost':49},{'Cost':13},{'Cost':26},{'Cost':43},{'Cost':49},{'Cost':32},{'Cost':50},{'Cost':28},{'Cost':45},{'Cost':42},{'Cost':31},{'Cost':45},{'Cost':32},{'Cost':34},{'Cost':23},{'Cost':29},{'Cost':11},{'Cost':49},{'Cost':24},{'Cost':25},{'Cost':37},{'Cost':41}],
[{'Cost':44},{'Cost':16},{'Oil':31653,'Cost':31},{'Oil':67958,'Cost':30},{'Cost':43},{'Cost':29},{'Cost':16},{'Rock':0},{'Rock':0},{'Rock':0},{'Rock':0},{'Cost':50},{'Cost':27},{'Cost':15},{'Cost':39},{'Cost':22},{'Cost':37},{'Cost':15},{'Cost':49},{'Cost':21},{'Cost':49},{'Cost':14},{'Cost':14},{'Rock':0},{'Cost':32}],
[{'Cost':21},{'Cost':44},{'Cost':38},{'Oil':68076,'Cost':18},{'Cost':21},{'Cost':41},{'Cost':19},{'Rock':0},{'Cost':26},{'Cost':13},{'Cost':25},{'Cost':27},{'Cost':12},{'Cost':32},{'Cost':15},{'Cost':20},{'Cost':22},{'Cost':12},{'Cost':34},{'Cost':21},{'Cost':11},{'Cost':16},{'Cost':17},{'Cost':27},{'Cost':24}],
[{'Cost':29},{'Cost':41},{'Cost':24},{'Cost':50},{'Cost':25},{'Cost':29},{'Cost':19},{'Rock':0},{'Cost':23},{'Cost':34},{'Cost':49},{'Cost':30},{'Cost':49},{'Cost':48},{'Cost':20},{'Cost':43},{'Cost':23},{'Cost':12},{'Cost':44},{'Cost':21},{'Cost':43},{'Cost':40},{'Cost':11},{'Cost':18},{'Cost':33}],
[{'Cost':37},{'Cost':46},{'Cost':26},{'Cost':41},{'Cost':35},{'Cost':19},{'Cost':38},{'Rock':0},{'Cost':33},{'Oil':45596,'Cost':50},{'Oil':70439,'Cost':47},{'Cost':49},{'Cost':44},{'Cost':40},{'Cost':17},{'Cost':29},{'Cost':44},{'Cost':35},{'Cost':18},{'Cost':47},{'Cost':19},{'Cost':20},{'Cost':33},{'Cost':20},{'Cost':23}],
[{'Cost':36},{'Cost':37},{'Cost':48},{'Cost':18},{'Cost':42},{'Cost':37},{'Cost':48},{'Rock':0},{'Cost':19},{'Oil':94571,'Cost':49},{'Oil':14286,'Cost':41},{'Cost':42},{'Cost':43},{'Cost':26},{'Cost':23},{'Cost':18},{'Cost':33},{'Rock':0},{'Rock':0},{'Cost':10},{'Cost':26},{'Cost':46},{'Cost':50},{'Cost':25},{'Cost':39}],
[{'Cost':44},{'Rock':0},{'Cost':42},{'Cost':11},{'Cost':44},{'Cost':21},{'Cost':15},{'Cost':31},{'Cost':33},{'Oil':56247,'Cost':48},{'Oil':66208,'Cost':41},{'Cost':25},{'Cost':21},{'Cost':38},{'Cost':15},{'Cost':28},{'Rock':0},{'Rock':0},{'Cost':29},{'Cost':46},{'Cost':28},{'Cost':33},{'Cost':14},{'Cost':11},{'Cost':30}],
[{'Cost':14},{'Cost':19},{'Cost':49},{'Cost':47},{'Cost':29},{'Cost':45},{'Cost':28},{'Cost':26},{'Cost':15},{'Cost':39},{'Cost':17},{'Cost':20},{'Cost':38},{'Cost':47},{'Cost':49},{'Cost':30},{'Cost':44},{'Cost':14},{'Cost':41},{'Cost':32},{'Oil':67096,'Cost':28},{'Cost':21},{'Cost':35},{'Cost':22},{'Cost':37}],
[{'Cost':16},{'Cost':48},{'Cost':10},{'Cost':31},{'Cost':45},{'Cost':48},{'Cost':48},{'Cost':12},{'Cost':21},{'Cost':39},{'Cost':23},{'Cost':36},{'Cost':21},{'Cost':16},{'Cost':33},{'Cost':26},{'Cost':15},{'Cost':49},{'Cost':49},{'Cost':11},{'Oil':16465,'Cost':24},{'Cost':33},{'Cost':50},{'Cost':50},{'Cost':49}],
[{'Cost':20},{'Cost':33},{'Cost':27},{'Cost':32},{'Cost':21},{'Cost':19},{'Cost':37},{'Cost':15},{'Cost':18},{'Cost':49},{'Cost':50},{'Cost':27},{'Cost':32},{'Cost':24},{'Cost':13},{'Oil':22347,'Cost':37},{'Oil':53548,'Cost':39},{'Oil':86404,'Cost':46},{'Cost':13},{'Cost':47},{'Cost':39},{'Cost':40},{'Cost':49},{'Cost':12},{'Cost':10}],
[{'Cost':20},{'Cost':40},{'Oil':43815,'Cost':24},{'Oil':39967,'Cost':46},{'Cost':47},{'Cost':37},{'Cost':20},{'Cost':23},{'Cost':45},{'Rock':0},{'Cost':21},{'Cost':39},{'Cost':25},{'Cost':31},{'Cost':29},{'Oil':22588,'Cost':50},{'Cost':11},{'Oil':18920,'Cost':15},{'Cost':49},{'Cost':12},{'Cost':44},{'Cost':22},{'Rock':0},{'Cost':42},{'Cost':25}],
[{'Cost':33},{'Cost':16},{'Oil':43202,'Cost':40},{'Oil':79965,'Cost':11},{'Oil':91270,'Cost':47},{'Oil':25689,'Cost':33},{'Oil':73288,'Cost':31},{'Cost':20},{'Cost':36},{'Rock':0},{'Cost':30},{'Cost':17},{'Cost':40},{'Cost':20},{'Cost':30},{'Oil':19131,'Cost':21},{'Cost':44},{'Oil':50240,'Cost':13},{'Oil':64749,'Cost':28},{'Cost':45},{'Cost':27},{'Cost':20},{'Rock':0},{'Rock':0},{'Cost':21}],
[{'Cost':34},{'Cost':32},{'Cost':45},{'Cost':48},{'Cost':28},{'Oil':77762,'Cost':18},{'Cost':40},{'Cost':27},{'Cost':29},{'Cost':45},{'Cost':26},{'Cost':24},{'Cost':47},{'Cost':26},{'Cost':13},{'Cost':17},{'Cost':17},{'Cost':48},{'Cost':34},{'Cost':23},{'Cost':21},{'Cost':44},{'Cost':11},{'Cost':29},{'Cost':43}],
[{'Cost':12},{'Cost':32},{'Cost':13},{'Cost':17},{'Cost':28},{'Cost':39},{'Cost':47},{'Cost':33},{'Cost':47},{'Cost':14},{'Cost':24},{'Cost':48},{'Cost':10},{'Cost':45},{'Cost':17},{'Cost':13},{'Cost':27},{'Cost':13},{'Cost':45},{'Cost':35},{'Cost':29},{'Cost':22},{'Cost':19},{'Cost':44},{'Cost':34}]]


globalPath = []
worthyMap = []

path = []
allOilWell = []
colMax = len(map[0])
rowMax = len(map)

def nearest_oil(row,col):
    min_dis = 99
    for i in range(25):
        for j in range(25):
            if 'Oil' in map[i][j] and 'OilMark' not in map[i][j]:
                tmp = heuristic((i,j),(row,col))
            else:
                tmp = 99
            if tmp < min_dis:
                min_dis = tmp
    return min_dis
            

def running(row, col, displacement):
    nearest = nearest_oil(row,col)
    if displacement <= nearest:
        return None
#    print(row+1,col+1,nearest,displacement)
    if col < 0 or col >= colMax or row < 0 or row >= rowMax:
        return None

#    if 'Mark' in map[row][col]:
#        return None
#    map[row][col]['Mark'] = 1

    if 'Oil' in map[row][col] and not 'OilMark' in map[row][col]:
        OilWell = []
        global oill 
        oill += 1
        nearest = 99
#        print('found')
        findOil(row, col, OilWell)

        minCost = 999999
        minPath = []
        costInYield = 0
        tmpCost = 0
        for OilYeild in OilWell:
            newMap = deepcopy(map)
            x, y = OilYeild['Post']
            costInYield += newMap[x][y]['Cost']
            path, cost = findShortestPath(newMap, 0, 0, x, y)

            if cost < minCost:
                minCost = cost
                minPath = path
                tmpCost -= newMap[x][y]['Cost']
        costInYield -= tmpCost
        sumAllYield = 0

        for i in OilWell:
            sumAllYield += i['Value']

        worthyMap.append({'PathCost':minCost+costInYield, 'Income':sumAllYield, 'Profit':sumAllYield-(minCost+costInYield), 'Path':minPath})
        allOilWell.append(OilWell)

    running(row+1, col,nearest)
    running(row-1, col,nearest)
    running(row, col+1,nearest)
    running(row, col-1,nearest)
    
def findOil(row, col, OilWell):

    if col < 0 or col >= colMax or row < 0 or row >= rowMax:
        return None

    if 'OilMark' in map[row][col]:
        return None

    if not('Oil' in map[row][col]):
        return None
    else:
        OilWell.append({'Value':map[row][col]['Oil'], 'Post':[row, col]})
    map[row][col]['OilMark'] = 1

    findOil(row + 1, col, OilWell)
    findOil(row - 1, col, OilWell)
    findOil(row, col + 1, OilWell)
    findOil(row, col - 1, OilWell)

def findShortestPath(newMap, row, col, x, y):

    path,cost = Astar((row,col), (x,y), newMap)
    return path,cost

def children(point, newMap):

    row, col = point

    coordinate = {}

    coordinate['Up']    = newMap[row-1][col]['Cost'] if row-1 >= 0     and not 'SM' in newMap[row-1][col] and not 'Rock' in newMap[row-1][col] and not 'Start' in newMap[row-1][col] else 9999
    coordinate['Down']  = newMap[row+1][col]['Cost'] if row+1 < rowMax and not 'SM' in newMap[row+1][col] and not 'Rock' in newMap[row+1][col] and not 'Start' in newMap[row+1][col] else 9999
    coordinate['Left']  = newMap[row][col-1]['Cost'] if col-1 >= 0     and not 'SM' in newMap[row][col-1] and not 'Rock' in newMap[row][col-1] and not 'Start' in newMap[row][col-1] else 9999
    coordinate['Right'] = newMap[row][col+1]['Cost'] if col+1 < colMax and not 'SM' in newMap[row][col+1] and not 'Rock' in newMap[row][col+1] and not 'Start' in newMap[row][col+1] else 9999

    children = [(row - 1, col), (row + 1, col),(row, col - 1), (row, col + 1)]

    direction = []

    for key,val in coordinate.items():
        if(key == 'Up' and val != 9999):
            direction.append(children[0])
        elif(key == 'Down' and val != 9999):
            direction.append(children[1])
        elif(key == 'Left' and val != 9999):
            direction.append(children[2])
        elif (key == 'Right' and val != 9999):
            direction.append(children[3])
    return direction

def Astar(node, goal, grid):
    # Initialize the queue with the root node
    queue = [(0, node, [])]
    # The list of seen items
    seen = {}
    # While the queue isn't empty
    while queue:
        # Pop the cost, point and path from the queue
        cost, point, path = heapq.heappop(queue)
        # If it has been seen, and has a lower cost, bail
        if point in seen and seen[point] < cost:
            continue
        # Update the path
        path = path + [point]
        # If we have found the goal, return the point
        if point == goal:
            return path,cost
        # Loop through the children
        for child in children(point, grid):
            # Calculate the basic cost
            x,y = child
            child_cost = grid[x][y]['Cost']+heuristic(goal,(x,y))
            # If the child hasn't been seen
            if child not in seen:
                # Add it to the heap
                heapq.heappush(queue, (cost + child_cost, child, path))
        # Add the point to the seen items
        seen[point] = cost
    return None

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

running(0,0,99)
maxOilWell = 0
winMap = {}

for map in worthyMap:
    #print(map)
    if(map['Profit']>maxOilWell):
        maxOilWell = map['Profit']
        winMap = map

print('Winner = ' , winMap)
