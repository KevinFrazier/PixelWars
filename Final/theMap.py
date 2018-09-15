from tile import Tile
import random, time
from tkinter import *

from threading import Thread,  Timer

'''
needs:
semi- random behavior
animation

animation:
need a Thread

Thread will go into each tile of the grid and change the image
where is the images stored?
array of images in Tile? -> this helps the transverse process

how to do this?

animation function:

overwrite image

then after:
redraw

'''

'''
changing
'''

class Map(Frame):

    def __init__(self, size):

        Frame.__init__(self)
        self.pack()

        #images
        #cursor
        self.cursor = PhotoImage(file="cursor.gif")
        #terrain
        self.spriteDimension = 20
        self.grass = PhotoImage(file = "grass.gif")
        self.water1 = PhotoImage(file = "water.gif")
        self.street = PhotoImage(file = "street.gif")
        self.mountain = PhotoImage(file = "mountain.gif")
        # self.water2 = PhotoImage(file="Terrain2-2.gif")
        # self.water3 = PhotoImage(file="Terrain2-3.gif")
        # self.water4 = PhotoImage(file="Terrain2-4.gif")

        # player 1 units
        self.infantry1 = PhotoImage(file= "infantry.gif")
        self.tank1 = PhotoImage(file="tank.gif")
        self.helicopter1 = PhotoImage(file="helicopter.gif")
        self.base1 = PhotoImage(file="base.gif")
        self.camp1 = PhotoImage(file="camp.gif")
        # player 2 units
        self.infantry2 = PhotoImage(file="infantry2.gif")
        self.tank2 = PhotoImage(file="tank2.gif")
        self.helicopter2 = PhotoImage(file="helicopter2.gif")
        self.base2 = PhotoImage(file="base2.gif")
        self.camp2 = PhotoImage(file="camp2.gif")

        self.imageList = [[self.base1, self.camp1, self.infantry1, self.tank1, self.helicopter1],
                          [self.base2, self.camp2, self.infantry2, self.tank2, self.helicopter2]]

        self._mapSize = size
        self._grid = self.randomize()
        self._unitGrid = self.allocate(None)

        canvas_dimension = self._mapSize * self.spriteDimension

        self._screen = Canvas(self, width=canvas_dimension, height=canvas_dimension)
        self._screen.pack()

        self.draw_grid()




    # def startAnimation(self):
    #     print("CALLED")
    #     self._screen.delete("all")
    #     for vertical in self._grid:
    #         for horizontal in vertical:
    #                 horizontal.Animate()
    #
    #     self.draw_grid()

        # self.after(1000,self.startAnimation)

    def draw_grid(self):
        self._screen.delete("all")
        for vertical in self._grid:
            for horizontal in vertical:

                    self._screen.create_image((int(horizontal.getX() * self.spriteDimension),
                                               int(horizontal.getY() * self.spriteDimension)), anchor=NW,
                                              image=horizontal.getSprite())

        for x in range(self._mapSize):
            for y in range(self._mapSize):
                if self._unitGrid[x][y] != None:
                    self._screen.create_image((x* self.spriteDimension,
                                               y * self.spriteDimension), anchor=NW,
                                              image=self._unitGrid[x][y])
                    

    def drawImage(self, playerNumber, x, y, type):
        item = self._screen.create_image((x*self.spriteDimension, y*self.spriteDimension),anchor = NW, image = (self.imageList[playerNumber][type]))
        self._unitGrid[x][y] = self.imageList[playerNumber][type]
        self._grid[x][y].setAvailable(False)
        # theTag = str(x) + str(y)
        # theTag = str(theTag)
        # self._screen.itemconfig(item, theTag)

        # print(PhotoImage(self._unitGrid[x][y]["file"]))

    def checkUniGridAvailability(self, x,y):

        if self._unitGrid[x][y] != None:
            return False
        return True

    def checkTileGridAvailability(self,x,y):

        if self._grid[x][y] != None:
            return False
        return True

    #takes care of the terrain: grass, water
    def randomize(self):
        t = self.allocate(Tile)

    # 1- grass, 2- water, 3- street, 4- mountain
        for vertical in range(self._mapSize):
            for horizontal in range(self._mapSize):
                t[vertical][horizontal].setTileType(1)
                t[vertical][horizontal].setPosition(vertical,horizontal)
                # if (t[vertical][horizontal].getTileType() == 1):
                t[vertical][horizontal].setSprite(self.grass)
                    # t[vertical][horizontal].setAnimation([self.grass])
                # if (t[vertical][horizontal].getTileType() == 2):
                #     t[vertical][horizontal].setSprite(self.water1)
                    # t[vertical][horizontal].setAnimation([self.water1,self.water2,self.water3,self.water4,self.water3,self.water2,self.water1])



        return t

    def fill(self):

        '''
        get list coordinates of images in the unit grid -> should always be 2
        build three streets

        water

        W1 = random.randint(self.,5)

        '''

        #save the whales
        # W1 = random.randint(self._mapSize/5,self._mapSize-(self._mapSize/5))
        # W2 = random.randint(self._mapSize / 5, self._mapSize - (self._mapSize / 5))
        # W1 = random.randint(self._mapSize / 5, self._mapSize - (self._mapSize / 5))
        # W2 = random.randint(self._mapSize / 5, self._mapSize - (self._mapSize / 5))
        # self._grid[W1][W2] = Tile(W1,W2, 4)
        # self._grid[W1][W2].setSprite(self.mountain)
        #generate water

        # print(W1, " ", W2)
        # for y in range(0, int(self._mapSize/5)):
        #     count = 0
        #     for x in range(int(self._mapSize/4),0):
        #         self._grid[W1 + y][W2+ x - count] = Tile(W1 + y,W2 - int(self._mapSize/4) + x,2)
        #         self._grid[W1 + y][W2+ x - count].setSprite(self.water1)
        #         self._grid[W1 - y][W2- x + count] = Tile(W1 - y, W2 - int(self._mapSize / 4) + x, 2)
        #         self._grid[W1 - y][W2- x + count].setSprite(self.water1)

        unitList = []
        for x in range(0,int(self._mapSize)):
            for y in range(self._mapSize):
                if self._unitGrid[x][y] != None:
                    unitList.append([x,y])

        P1 = unitList[0] #x,y
        P2 = unitList[1]

        print(P1, P2)

        n = self._mapSize
        n = int(n)
        for x in range(0,n*3):
            W1 = random.randint(0, self._mapSize-1)
            W2 = random.randint(0, self._mapSize-1)
            while self._grid[W1][W2].getTileType() == 2 or self._grid[W1][W2].getTileType() == 4:
                W1 = random.randint(P1[0] + 1, P2[0] - 1)
                W2 = random.randint(P1[0] + 1, P2[0] - 1)

            self._grid[W1][W2] = Tile(W1, W2, 2)
            self._grid[W1][W2].setSprite(self.water1)

        for x in range(0,n):
            W1 = random.randint(P1[0] + 1, P2[0] - 1)
            W2 = random.randint(P1[0] + 1, P2[0] - 1)
            while self._grid[W1][W2].getTileType() == 2 or self._grid[W1][W2].getTileType() == 4:
                W1 = random.randint(P1[0] + 1, P2[0] - 1)
                W2 = random.randint(P1[0] + 1, P2[0] - 1)

            self._grid[W1][W2] = Tile(W1, W2, 4)
            self._grid[W1][W2].setSprite(self.mountain)

        print("P1: ", P1)
        print("P2: ",P2)

        #top L
        for x in range(P1[0],P2[0] +1):
            self._grid[x][P1[1]] = Tile(x, P1[1], 3)
            self._grid[x][P1[1]].setSprite(self.street)

        for y in range(P1[1],P2[1] +1):
            self._grid[P2[0]][y] = Tile(P2[0], y, 3)
            self._grid[P2[0]][y].setSprite(self.street)

        #bottom L
        for y in range(P1[1], P2[1] + 1):
            self._grid[P1[0]][y] = Tile(P1[0], y, 3)
            self._grid[P1[0]][y].setSprite(self.street)

        for x in range(P1[0], P2[0] + 1):
            self._grid[x][P2[1]] = Tile(x, P2[1], 3)
            self._grid[x][P2[1]].setSprite(self.street)

        #diagon - L lolz

        # while P1[0] != P2[0] and P1[1] != P2[1]:
        #
        #     if P1[0] <= P2[0]:
        #         P1[0] = P1[0] + 1
        #         self._grid[P1[0]][P1[1]] = Tile (P1[0], P1[1], 3)
        #         self._grid[P1[0]][P1[1]].setSprite(self.street)
        #     if P1[1] <= P2[1]:
        #         P1[1] = P1[1] + 1
        #         self._grid[P1[0]][P1[1]]= Tile(P1[0], P1[1], 3)
        #         self._grid[P1[0]][P1[1]].setSprite(self.street)



    def allocate(self, type):
        list = []
        for moreLists in range(self._mapSize):
            list.append([])
        for theLists in list:
            for terrain in range(self._mapSize):
                if(type == None):
                    theLists.append(None)
                else:
                    theLists.append(type())


        return tuple(list)

    def getAdjacent(self, x, y):

        adjacentList = []

        if not(x-1 <0):
           adjacentList.append(self._grid[x-1][y])
        if not (x + 1 > self._mapSize-1):
            adjacentList.append(self._grid[x + 1][y])
        if not (y - 1 < 0):
            adjacentList.append(self._grid[x][y-1])
        if not (y + 1 > self._mapSize-1):
            adjacentList.append(self._grid[x][y+1])

        return adjacentList

    def print_grid (self, tuple):

        for item in tuple:
            print(item)