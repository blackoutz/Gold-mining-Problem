from scipy.spatial import distance
import heapq
from copy import deepcopy
from collections import OrderedDict

map = [[{'Start':0},{'Cost':50},{'Cost':15},{'Cost':31},{'Cost':49},{'Cost':38},{'Cost':11},{'Cost':46},{'Cost':27},{'Cost':28},{'Cost':29},{'Cost':11},{'Cost':10},{'Cost':41},{'Cost':30},{'Cost':13}],
[{'Cost':20},{'Cost':23},{'Cost':29},{'Cost':33},{'Cost':25},{'Cost':39},{'Cost':34},{'Cost':32},{'Cost':12},{'Cost':30},{'Cost':23},{'Cost':17},{'Cost':18},{'Cost':40},{'Cost':39},{'Cost':22}],
[{'Cost':33},{'Cost':24},{'Cost':33},{'Cost':34},{'Cost':40},{'Cost':29},{'Cost':27},{'Cost':46},{'Cost':26},{'Cost':46},{'Cost':37},{'Cost':37},{'Cost':31},{'Rock':0},{'Rock':0},{'Rock':0}],
[{'Cost':27},{'Cost':16},{'Rock':0},{'Rock':0},{'Cost':16},{'Cost':14},{'Cost':37},{'Cost':32},{'Cost':39},{'Cost':36},{'Cost':30},{'Cost':34},{'Cost':18},{'Rock':0},{'Cost':41},{'Cost':41}],
[{'Cost':30},{'Cost':44},{'Cost':18},{'Cost':20},{'Cost':10},{'Cost':27},{'Cost':39},{'Cost':41},{'Cost':18},{'Cost':41},{'Cost':16},{'Cost':10},{'Cost':17},{'Cost':24},{'Cost':43},{'Cost':40}],
[{'Cost':50},{'Cost':33},{'Cost':38},{'Cost':14},{'Cost':30},{'Cost':38},{'Cost':42},{'Cost':31},{'Cost':45},{'Cost':36},{'Cost':49},{'Cost':29},{'Cost':35},{'Cost':44},{'Cost':36},{'Cost':48}],
[{'Cost':29},{'Cost':29},{'Cost':13},{'Cost':49},{'Cost':17},{'Rock':0},{'Cost':49},{'Cost':20},{'Cost':39},{'Cost':47},{'Cost':38},{'Cost':46},{'Cost':41},{'Cost':38},{'Cost':43},{'Cost':47}],
[{'Cost':38},{'Cost':19},{'Cost':10},{'Cost':47},{'Cost':20},{'Rock':0},{'Cost':50},{'Cost':45},{'Cost':50},{'Cost':13},{'Cost':44},{'Cost':49},{'Cost':40},{'Cost':45},{'Cost':36},{'Oil':54237,'Cost':10}],
[{'Cost':24},{'Rock':0},{'Cost':21},{'Cost':39},{'Cost':41},{'Rock':0},{'Cost':50},{'Cost':33},{'Cost':40},{'Cost':30},{'Cost':23},{'Cost':16},{'Oil':91159,'Cost':32},{'Oil':65034,'Cost':11},{'Oil':39582,'Cost':25},{'Oil':78932,'Cost':47}],
[{'Cost':39},{'Cost':47},{'Cost':32},{'Cost':13},{'Cost':20},{'Rock':0},{'Cost':25},{'Cost':42},{'Cost':32},{'Cost':17},{'Cost':44},{'Cost':42},{'Cost':44},{'Cost':34},{'Cost':40},{'Oil':60745,'Cost':15}],
[{'Cost':10},{'Cost':21},{'Oil':57517,'Cost':16},{'Cost':40},{'Cost':37},{'Cost':39},{'Cost':16},{'Cost':39},{'Cost':24},{'Cost':17},{'Cost':49},{'Cost':29},{'Cost':21},{'Cost':12},{'Cost':39},{'Cost':12}],
[{'Cost':16},{'Cost':40},{'Oil':17908,'Cost':17},{'Cost':10},{'Cost':34},{'Cost':21},{'Cost':34},{'Cost':47},{'Cost':48},{'Cost':18},{'Cost':42},{'Cost':23},{'Cost':22},{'Cost':29},{'Cost':40},{'Cost':47}],
[{'Cost':27},{'Cost':23},{'Oil':55470,'Cost':49},{'Oil':41849,'Cost':25},{'Cost':32},{'Cost':27},{'Cost':45},{'Rock':0},{'Rock':0},{'Rock':0},{'Rock':0},{'Cost':32},{'Cost':21},{'Cost':47},{'Cost':31},{'Cost':49}],
[{'Cost':18},{'Cost':45},{'Cost':12},{'Oil':71088,'Cost':37},{'Cost':34},{'Cost':26},{'Cost':37},{'Rock':0},{'Cost':25},{'Cost':20},{'Cost':14},{'Cost':23},{'Cost':22},{'Cost':28},{'Cost':50},{'Cost':36}],
[{'Cost':45},{'Cost':10},{'Cost':10},{'Cost':43},{'Cost':42},{'Cost':45},{'Cost':27},{'Rock':0},{'Cost':47},{'Cost':34},{'Cost':38},{'Cost':21},{'Cost':43},{'Cost':50},{'Cost':31},{'Cost':34}],
[{'Cost':10},{'Cost':22},{'Cost':26},{'Cost':22},{'Cost':13},{'Cost':12},{'Cost':47},{'Rock':0},{'Cost':45},{'Oil':11984,'Cost':22},{'Oil':82595,'Cost':16},{'Cost':37},{'Cost':10},{'Cost':41},{'Cost':23},{'Cost':44}],
[{'Cost':23},{'Cost':15},{'Cost':38},{'Cost':43},{'Cost':32},{'Cost':26},{'Cost':14},{'Rock':0},{'Cost':33},{'Oil':23042,'Cost':29},{'Oil':43840,'Cost':13},{'Cost':14},{'Cost':18},{'Cost':25},{'Cost':18},{'Cost':15}],
[{'Cost':31},{'Rock':0},{'Cost':42},{'Cost':43},{'Cost':27},{'Cost':23},{'Cost':13},{'Cost':28},{'Cost':19},{'Oil':19174,'Cost':35},{'Oil':49269,'Cost':29},{'Cost':43},{'Cost':35},{'Cost':50},{'Cost':38},{'Cost':33}],
[{'Cost':40},{'Cost':23},{'Cost':25},{'Cost':34},{'Cost':26},{'Cost':35},{'Cost':26},{'Cost':50},{'Cost':27},{'Cost':33},{'Cost':16},{'Cost':41},{'Cost':26},{'Cost':20},{'Cost':32},{'Cost':23}],
[{'Cost':14},{'Cost':17},{'Cost':17},{'Cost':31},{'Cost':26},{'Cost':23},{'Cost':32},{'Cost':10},{'Cost':36},{'Cost':48},{'Cost':39},{'Cost':29},{'Cost':43},{'Cost':46},{'Cost':12},{'Cost':37}],
[{'Cost':16},{'Cost':21},{'Cost':45},{'Cost':39},{'Cost':18},{'Cost':32},{'Cost':41},{'Cost':17},{'Cost':24},{'Cost':19},{'Cost':31},{'Cost':31},{'Cost':32},{'Cost':18},{'Cost':27},{'Oil':86461,'Cost':17}],
[{'Cost':35},{'Cost':49},{'Oil':83730,'Cost':15},{'Oil':35960,'Cost':39},{'Cost':11},{'Cost':17},{'Cost':10},{'Cost':17},{'Cost':22},{'Rock':0},{'Cost':41},{'Cost':40},{'Cost':43},{'Cost':32},{'Cost':11},{'Oil':61646,'Cost':28}],
[{'Cost':48},{'Cost':23},{'Oil':17416,'Cost':40},{'Oil':27403,'Cost':42},{'Oil':65923,'Cost':41},{'Oil':60978,'Cost':19},{'Oil':99450,'Cost':25},{'Cost':35},{'Cost':28},{'Rock':0},{'Cost':44},{'Cost':38},{'Cost':50},{'Cost':47},{'Cost':49},{'Oil':20390,'Cost':42}],
[{'Cost':49},{'Cost':48},{'Cost':28},{'Cost':31},{'Cost':42},{'Oil':20103,'Cost':33},{'Cost':23},{'Cost':27},{'Cost':15},{'Cost':13},{'Cost':18},{'Cost':18},{'Cost':35},{'Cost':49},{'Cost':15},{'Cost':44}],
[{'Cost':18},{'Cost':43},{'Cost':44},{'Cost':24},{'Cost':48},{'Cost':39},{'Cost':10},{'Cost':46},{'Cost':12},{'Cost':44},{'Cost':39},{'Cost':31},{'Cost':39},{'Cost':34},{'Cost':13},{'Cost':55}]]

globalPath = []
worthyMap = []

path = []
allOilWell = []

colMax = len(map[0])
rowMax = len(map)

def running(row, col):

    if col < 0 or col >= colMax or row < 0 or row >= rowMax:
        return None

    if 'Mark' in map[row][col]:
        return None
    map[row][col]['Mark'] = 1

    if 'Oil' in map[row][col] and not 'OilMark' in map[row][col]:
        OilWell = []
        findOil(row, col, OilWell)

        minCost = 999999
        minPath = []
        costInYield = 0

        for OilYeild in OilWell:
            newMap = deepcopy(map)
            x, y = OilYeild['Post']
            costInYield += newMap[x][y]['Cost']
            path, cost = findShortestPath(newMap, 0, 0, x, y)

            if cost < minCost:
                minCost = cost
                minPath = path
                costInYield -= newMap[x][y]['Cost']

        sumAllYield = 0

        for i in OilWell:
            sumAllYield += i['Value']

        worthyMap.append({'PathCost':minCost+costInYield, 'Income':sumAllYield, 'Profit':sumAllYield-(minCost+costInYield), 'Path':minPath})
        allOilWell.append(OilWell)

    running(row+1, col)
    running(row-1, col)
    running(row, col+1)
    running(row, col-1)
    
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

    path,cost = ucs((row,col), (x,y), newMap)
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

def ucs(node, goal, grid):
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
            child_cost = grid[x][y]['Cost']
            # If the child hasn't been seen
            if child not in seen:
                # Add it to the heap
                heapq.heappush(queue, (cost + child_cost, child, path))
        # Add the point to the seen items
        seen[point] = cost
    return None

running(0,0)
maxOilWell = 0
winMap = {}

for map in worthyMap:
    print(map)
    if(map['Profit']>maxOilWell):
        maxOilWell = map['Profit']
        winMap = map

print('Winner = ' , winMap)
