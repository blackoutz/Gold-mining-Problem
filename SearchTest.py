from scipy.spatial import distance
import heapq
from collections import OrderedDict

map = [[{'S':0},{'W':50},{'W':15},{'W':31},{'W':49},{'W':38},{'W':11},{'W':46},{'W':27},{'W':28},{'W':29},{'W':11},{'W':10},{'W':41},{'W':30},{'W':13}],
[{'W':20},{'W':23},{'W':29},{'W':33},{'W':25},{'W':39},{'W':34},{'W':32},{'W':12},{'W':30},{'W':23},{'W':17},{'W':18},{'W':40},{'W':39},{'W':22}],
[{'W':33},{'W':24},{'W':33},{'W':34},{'W':40},{'W':29},{'W':27},{'W':46},{'W':26},{'W':46},{'W':37},{'W':37},{'W':31},{'R':0},{'R':0},{'R':0}],
[{'W':27},{'W':16},{'R':0},{'R':0},{'W':16},{'W':14},{'W':37},{'W':32},{'W':39},{'W':36},{'W':30},{'W':34},{'W':18},{'R':0},{'W':41},{'W':41}],
[{'W':30},{'W':44},{'W':18},{'W':20},{'W':10},{'W':27},{'W':39},{'W':41},{'W':18},{'W':41},{'W':16},{'W':10},{'W':17},{'W':24},{'W':43},{'W':40}],
[{'W':50},{'W':33},{'W':38},{'W':14},{'W':30},{'W':38},{'W':42},{'W':31},{'W':45},{'W':36},{'W':49},{'W':29},{'W':35},{'W':44},{'W':36},{'W':48}],
[{'W':29},{'W':29},{'W':13},{'W':49},{'W':17},{'R':0},{'W':49},{'W':20},{'W':39},{'W':47},{'W':38},{'W':46},{'W':41},{'W':38},{'W':43},{'W':47}],
[{'W':38},{'W':19},{'W':10},{'W':47},{'W':20},{'R':0},{'W':50},{'W':45},{'W':50},{'W':13},{'W':44},{'W':49},{'W':40},{'W':45},{'W':36},{'G':54237,'W':10}],
[{'W':24},{'R':0},{'W':21},{'W':39},{'W':41},{'R':0},{'W':50},{'W':33},{'W':40},{'W':30},{'W':23},{'W':16},{'G':91159,'W':32},{'G':65034,'W':11},{'G':39582,'W':25},{'G':78932,'W':47}],
[{'W':39},{'W':47},{'W':32},{'W':13},{'W':20},{'R':0},{'W':25},{'W':42},{'W':32},{'W':17},{'W':44},{'W':42},{'W':44},{'W':34},{'W':40},{'G':60745,'W':15}],
[{'W':10},{'W':21},{'G':57517,'W':16},{'W':40},{'W':37},{'W':39},{'W':16},{'W':39},{'W':24},{'W':17},{'W':49},{'W':29},{'W':21},{'W':12},{'W':39},{'W':12}],
[{'W':16},{'W':40},{'G':17908,'W':17},{'W':10},{'W':34},{'W':21},{'W':34},{'W':47},{'W':48},{'W':18},{'W':42},{'W':23},{'W':22},{'W':29},{'W':40},{'W':47}],
[{'W':27},{'W':23},{'G':55470,'W':49},{'G':41849,'W':25},{'W':32},{'W':27},{'W':45},{'R':0},{'R':0},{'R':0},{'R':0},{'W':32},{'W':21},{'W':47},{'W':31},{'W':49}],
[{'W':18},{'W':45},{'W':12},{'G':71088,'W':37},{'W':34},{'W':26},{'W':37},{'R':0},{'W':25},{'W':20},{'W':14},{'W':23},{'W':22},{'W':28},{'W':50},{'W':36}],
[{'W':45},{'W':10},{'W':10},{'W':43},{'W':42},{'W':45},{'W':27},{'R':0},{'W':47},{'W':34},{'W':38},{'W':21},{'W':43},{'W':50},{'W':31},{'W':34}],
[{'W':10},{'W':22},{'W':26},{'W':22},{'W':13},{'W':12},{'W':47},{'R':0},{'W':45},{'G':11984,'W':22},{'G':82595,'W':16},{'W':37},{'W':10},{'W':41},{'W':23},{'W':44}],
[{'W':23},{'W':15},{'W':38},{'W':43},{'W':32},{'W':26},{'W':14},{'R':0},{'W':33},{'G':23042,'W':29},{'G':43840,'W':13},{'W':14},{'W':18},{'W':25},{'W':18},{'W':15}],
[{'W':31},{'R':0},{'W':42},{'W':43},{'W':27},{'W':23},{'W':13},{'W':28},{'W':19},{'G':19174,'W':35},{'G':49269,'W':29},{'W':43},{'W':35},{'W':50},{'W':38},{'W':33}],
[{'W':40},{'W':23},{'W':25},{'W':34},{'W':26},{'W':35},{'W':26},{'W':50},{'W':27},{'W':33},{'W':16},{'W':41},{'W':26},{'W':20},{'W':32},{'W':23}],
[{'W':14},{'W':17},{'W':17},{'W':31},{'W':26},{'W':23},{'W':32},{'W':10},{'W':36},{'W':48},{'W':39},{'W':29},{'W':43},{'W':46},{'W':12},{'W':37}],
[{'W':16},{'W':21},{'W':45},{'W':39},{'W':18},{'W':32},{'W':41},{'W':17},{'W':24},{'W':19},{'W':31},{'W':31},{'W':32},{'W':18},{'W':27},{'G':86461,'W':17}],
[{'W':35},{'W':49},{'G':83730,'W':15},{'G':35960,'W':39},{'W':11},{'W':17},{'W':10},{'W':17},{'W':22},{'R':0},{'W':41},{'W':40},{'W':43},{'W':32},{'W':11},{'G':61646,'W':28}],
[{'W':48},{'W':23},{'G':17416,'W':40},{'G':27403,'W':42},{'G':65923,'W':41},{'G':60978,'W':19},{'G':99450,'W':25},{'W':35},{'W':28},{'R':0},{'W':44},{'W':38},{'W':50},{'W':47},{'W':49},{'G':20390,'W':42}],
[{'W':49},{'W':48},{'W':28},{'W':31},{'W':42},{'G':20103,'W':33},{'W':23},{'W':27},{'W':15},{'W':13},{'W':18},{'W':18},{'W':35},{'W':49},{'W':15},{'W':44}],
[{'W':18},{'W':43},{'W':44},{'W':24},{'W':48},{'W':39},{'W':10},{'W':46},{'W':12},{'W':44},{'W':39},{'W':31},{'W':39},{'W':34},{'W':13},{'W':55}]]


START = (0,0)
globalPath = []
globalCost = []
worthyMap = []
allMine = []
colMax = len(map[0])
rowMax = len(map)

print(colMax)
print(rowMax)



def running(row, col):

    if col < 0:
        return None
    elif col >= colMax:
        return None
    if row < 0:
        return None
    elif row >= rowMax:
        return None

    if 'M' in map[row][col]:
        return None
    map[row][col]['M'] = 1
    #path.append([row, col])

    if 'G' in map[row][col] and not 'GM' in map[row][col]:
        mine = []
        findGold(row,col,mine)
        # minCost = 999999
        # minPath = []
        # for gold in mine:
        #     newMap = map[:]
        #     x,y = gold['pos']
        #     path , cost = findShortestPath(newMap,x,y)
        #     if cost < minCost:
        #         minCost = cost
        #         minPath = path
        #
        # worthyMap.append({'cost':minCost, 'path':minPath})
        allMine.append(mine)

    running(row+1, col)
    running(row-1, col)
    running(row, col+1)
    running(row, col-1)

def findClosetPoint(mine):
    startPoint = (0,0)
    minDistace = 999999
    closetPoint = []
    for m in mine:
        dst = distance.euclidean( startPoint,( m['pos'][0], m['pos'][1] ) )
        if minDistace > dst :
            minDistace = dst
            closetPoint = [m['pos'][0], m['pos'][1]]
    return closetPoint

def findShortestPath(newMap,row,col):

    if col < 0:
        return None
    elif col >= colMax:
        return None
    if row < 0:
        return None
    elif row >= rowMax:
        return None

    if 'SM' in newMap[row][col]:
        return None
    newMap[row][col]['SM'] = 1

    path,cost = ucs((0,0), (7,15), newMap)
    print(cost)
    return path,cost

    '''
    directD = {}
    directD['up'] = {'row': row-1, 'col': col}
    directD['down'] = {'row': row+1, 'col': col}
    directD['left'] = {'row': row, 'col': col-1}
    directD['right'] = {'row': row, 'col': col+1}

    coordinate = {}

    coordinate['up'] = newMap[row-1][col]['W'] if row-1 > 0 and not 'SM' in newMap[row-1][col] and not 'R' in newMap[row-1][col] else 9999
    coordinate['down'] = newMap[row+1][col]['W'] if row+1 > 0 and not 'SM' in newMap[row+1][col] and not 'R' in newMap[row+1][col] else 9999
    coordinate['left'] = newMap[row][col-1]['W'] if col-1 > 0 and not 'SM' in newMap[row][col-1] and not 'R' in newMap[row][col-1] else 9999
    coordinate['right'] = newMap[row][col+1]['W'] if col+1 > 0 and not 'SM' in newMap[row][col+1] and not 'R' in newMap[row][col+1] else 9999
    sort = OrderedDict(sorted(coordinate.items(), key=lambda t: t[1]))
    a,b,c,d = sort.keys()
    print(sort,a,b,c,d)
    choose = min(coordinate, key=coordinate.get)
    Ncol,Nrow = directD[choose].values()
    Ncost = coordinate[choose]
    #print(Nrow,Ncol)
    lastPath.append([Nrow,Ncol])
    print(lastPath)
    print(Ncost+cost)
    findShortestPath(newMap,Nrow,Ncol,mine,lastPath,cost+Ncost)
    '''
    #
    #
    # if min(up,down,left,right) == up:
    #     findShortestPath()
    #
    # lastPath.append([row,col])
    #
    # if(min(map[row+1][col]))


def children(point, newMap):
    row, col = point

    coordinate = {}

    coordinate['up'] = newMap[row-1][col]['W'] if row-1 >= 0 and not 'SM' in newMap[row-1][col] and not 'R' in newMap[row-1][col] else 9999
    coordinate['down'] = newMap[row+1][col]['W'] if row+1 < rowMax and not 'SM' in newMap[row+1][col] and not 'R' in newMap[row+1][col] else 9999
    coordinate['left'] = newMap[row][col-1]['W'] if col-1 >= 0 and not 'SM' in newMap[row][col-1] and not 'R' in newMap[row][col-1] else 9999
    coordinate['right'] = newMap[row][col+1]['W'] if col+1 < colMax and not 'SM' in newMap[row][col+1] and not 'R' in newMap[row][col+1] else 9999

    children = [(row - 1, col), (row + 1, col),(row, col - 1), (row, col + 1) ]
    #print(coordinate)
    direction = []
    for key,val in coordinate.items():
        if(key == 'up' and val != 9999):
            direction.append(children[0])
        elif(key == 'down' and val != 9999):
            direction.append(children[1])
        elif(key == 'left' and val != 9999):
            direction.append(children[2])
        elif (key == 'right' and val != 9999):
            direction.append(children[3])
    #print(direction)
    return direction

    #
    # for child in children:
    #     for key,val in coordinate:
    #         for
    #         print('KEY ' ,key ,val)
    #return [child for child in children if grid[child[0]][child[1]] != '%']

    return coordinate



def ucs(node, goal, grid):
    # Initialize the queue with the root node
    q = [(0, node, [])]
    # The list of seen items
    seen = {}
    # While the queue isn't empty
    while q:
        # Pop the cost, point and path from the queue
        cost, point, path = heapq.heappop(q)
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
            child_cost = grid[x][y]['W']
            # If the child hasn't been seen
            if child not in seen:
                # Add it to the heap
                heapq.heappush(q, (cost + child_cost, child, path))
        # Add the point to the seen items
        seen[point] = cost
    return None

def findGold(row, col, mine):
    if col < 0:
        return None
    elif col >= colMax:
        return None
    if row < 0:
        return None
    elif row >= rowMax:
        return None

    if 'GM' in map[row][col]:
        return None
    if not('G' in map[row][col]):
        return None
    else:
        mine.append({'value':map[row][col]['G'], 'pos':[row, col]})
    map[row][col]['GM'] = 1

    findGold(row + 1, col, mine)
    findGold(row - 1, col, mine)
    findGold(row, col + 1, mine)
    findGold(row, col - 1, mine)


running(0,0)
#print(allMine)
#print(worthyMap)

# lastPath = []
# cost = 0
newMap = map[:]
shortestPath,cost = findShortestPath(newMap,10,2)
print(shortestPath)

# children((0,2),map)

