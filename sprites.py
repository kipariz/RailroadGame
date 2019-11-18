from settings import *

railsPosition = (finalSort())

railH_place = [[1, 1, 1, 4, 4], [1, 2, 3, 5, 6]]
railV_place = [[2, 3, 5, 6], [4, 4, 4, 4]]
railC_place = [[1, 4, 7], [4, 4, 4]]

railway_stations = {'A': [1, 1], 'B': [4, 6]}


class Train(object):
    
    def getRailIndex(self, x, y):

        for i in range(len(railsPosition[0])):
            if (x == (railsPosition[0][i]) and y == (railsPosition[1][i])):
                return(i)

        return "The train isn't at rails yet!"

    # move function means that train is already on rails, so we check is next cell have a rail and move on if true
    def getPlace(self, x, y):
        iteration = self.getRailIndex(x, y)
        nextX = railsPosition[0][iteration+1]
        nextY = railsPosition[1][iteration+1]
        return [iteration, nextX, nextY]

    def move(self, x, y):
        place = self.getPlace(x, y)

        iteration = place[0]
        nextX = place[1]
        nextY = place[2]

        deltaX = (nextX-x)
        deltaY = (nextY-y)
        if(deltaX == 0 and deltaY == 1):
            return "up"
        elif(deltaX == 1 and deltaY == 0):
            return "right"
        elif(deltaX == 0 and deltaY == -1):
            return "down"
        elif(deltaX == -1 and deltaY == 0):
            return "left"

        else:
            # log
            return("there is no rails, try else cell")

    # def searchRoude(self, start, end):

    def mirror(self, name):
        if (name == "down"):
            return "up"
        elif (name == "up"):
            return "down"
        elif (name == "left"):
            return "right"
        elif (name == "right"):
            return "left"

    def nextCentral():
        for i in range(len(railsPosition[0])):
            pass
            # if x+1 == x
                # continue
            # else:
                # if x,y == c
                    # add c(x,y) to graph
                # else error


if __name__ == "__main__":
    train = Train()
    A = [1, 1]
    B = [4, 6]
    # train.trip(A, B)#определять маршрут и возвращать его (["down", "left", "down"])

    # train.move(1,1)
    # train.getAll()
