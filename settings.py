
# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ORANGE_DARK = (255,140,0)
ORANGE_RED = (255,69,0)
BROWN = (139,69,19)
BLUE = (65,105,225)
FOREST_GREEN = (124, 205, 124)

TILESIZE = 40

WIDTH = TILESIZE*10  
HEIGHT = TILESIZE*10  

# game settings
#WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
#HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 5
TITLE = "Railroad"


GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


#x,y
city_place = [[0,1,0,7,8,9,8,9,4,5,5,6,5,6],[0,0,1,0,0,0,1,1,7,7,8,8,9,9]]
mountain_place = [[3,3,2,2,1,1,2],[0,1,2,3,5,6,6]]
water_place = [[6,7,6,7,8,9,7,8,9,8,9,7,8,9],[5,5,6,6,6,6,7,7,7,8,8,9,9,9]] 
sand_place = [[4,5,4,5,3,4,5,3,4,5,6,4,5,6,7,8,5,8,9,5,6,7],[0,0,1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,6,7,8]]

railH_place = [[1,1,1,4,4],[1,2,3,5,6]]
railV_place = [[2,3,5,6],[4,4,4,4]]
railC_place = [[1,4,7],[4,4,4]]

railway_stations = {'A':[1,1], 'B':[4,6]}

class Possition():
    def __init__(self, arrC, railway_stations):
        self.arrC =arrC
        self.railway_stations=railway_stations
    #return array of vertex in arrC (in this case in array of central rails)
    def centerNames(self):
        res = []
        for i in range(len(self.arrC[0])):
            res.append("C"+str(i+1))
        return res

    def stationNames(self):
        res = []
        for i in self.railway_stations.keys():
            res.append(i)
        return res
    
    def getPossition(self, n):
        if (n in railway_stations):
            return railway_stations.get(n)
        elif(n[0]=="C"):
            for i in range(len(railC_place[0])+1):
                if (i==int(n[1])):
                    return [railC_place[0][i-1], railC_place[1][i-1]]
        else:
            return "error"

    def arrayNames(self):
        res = [] 

        for i in self.centerNames():
            res.append(i)
        for i in self.stationNames():
            res.append(i)
        return res
    
    def arrayPossitions(self):
        res = []

        for i in self.arrayNames():
            res.append(i)
            res.append(self.getPossition(i))
        return res

    def isNeighbour(self, a, b):
        self.getPossition(a)
        if (True):
            return True
        else:
            return False

    
    def findNeighborhood(self):
        res = []
        arrNames = self.arrayNames()

        for i in arrNames:
            for j in arrNames:
                if (self.isNeighbour(i, j)):
                    res.append(j)


        return res

pos = Possition(railC_place, railway_stations)

#print(pos.getPossition("C1"))

print(pos.arrayPossitions())


def appendSort(arr1, arr2):  
    rail =  list(zip(arr1[0], arr1[1])) +  list(zip(arr2[0], arr2[1]))
    rail.sort()
    
    return rail

def railSort(arr1, arr2):   
    railarr=appendSort(arr1, arr2)
    a,b=zip(*railarr)
    railarr=[]; railarr.append(a); railarr.append(b)
    return railarr

def finalSort():
    railarr=railSort(railH_place, railC_place)
    railarr=railSort(railV_place, railarr)
    return railarr
