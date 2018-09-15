'''
#difference between UML diagram and this .py:
-getHealth might be redundant
-getAdjacentTiles should be in the mapClass

'''
class Tile:

    def __init__(self, x = -1, y= -1, type = -1):

        self.x = x
        self.y = y #(x,y)
        self.image = None
        self._type = type
        self.animation = None
        self.animationIndex = -1
        self._available = True #checks if there is a unit there or not
        # dimensions = (image.height,image.width) #this is found from image
        # self._dimensions = dimensions
        #this is manually checked depending on the image content

    def setAvailable(self, bool):
        self._available = bool

    def isAvailable(self):
        return self._available

    def getTileType(self):
        return self._type

    def setTileType(self,string):
        self._type = string

    def getSprite(self):
        return self.image

    #sets the image of the terrain tile
    def setSprite(self, sprite):
        self.image = sprite

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def setAnimation(self, listofAnimations):

        #you want the beginning image to also be the 0 index image
        if(self.image == listofAnimations[0]):
            self.animation = listofAnimations
            self.animationIndex = 0
            return True
        return False

    def Animate(self):
        print("animation index: ", self.animationIndex)
        self.animatonIndex = (self.animationIndex + 1)
        print("animation index2: ", self.animationIndex)
        if self.animationIndex >= len(self.animation):
            self.animationIndex = self.animation - len(self.animation)

        self.image = self.animation[self.animationIndex]

    def __str__(self):
        return "[position: " + str(self.getX()) + " " + str(self.getY()) + " , type: " + str(self._type) + ", animationIndex: " + str(self.animationIndex)
    #this should be in map class
    # def getAdjacent(self):