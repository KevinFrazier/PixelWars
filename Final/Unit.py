

class Unit(object):
    # type, health, damage, movement, range, x, y
    def __init__(self, type=0, health=0, damage=0, movement=0, range=0, x=0, y=0):
        # 0:base, 1:camp, 2:infantry, 3:tank, 4:helicopter
        self._type = type
        self._health = health
        self._damage = damage
        self._movement = movement
        self._range = range
        self._x = x
        self._y = y
        self._remainingMove = movement
        # image

    def getType(self):
        return self._type

    def setType(self, type):
        self._type = type

    def getHealth(self):
        return self._health

    def setHealth(self, health):
        self._health = health

    def getDamage(self):
        return self._damage

    def setDamage(self, damage):
        self._damage = damage

    def getMovement(self):
        return self._movement

    def setMovement(self, movement):
        self._movement = movement

    def getRange(self):
        return self._range

    def setRange(self, range):
        self._range = range

    def getX(self):
        return self._x

    def setX(self, x):
        self._x = x

    def getY(self):
        return self._y

    def setY(self, y):
        self._y = y

    def getRemainingMoves(self):
        return self._remainingMove

    def setRemainingMoves(self, moves):
        self._remainingMove = moves

    def canMove(self):
        if self._remainingMove > 0:
            return True
        else:
            return False

    def resetMoves(self):
        self._remainingMove = self._movement

    # 0:base, 1:camp, 2:infantry, 3:tank, 4:helicopter
    def calcAdvantage(self, otherUnit):
        if (self._type == 2 and otherUnit.getType() == 4) or \
           (self._type == 3 and otherUnit.getType() == 2) or \
           (self._type == 4 and otherUnit.getType() == 3):
            return True
        return False

    #check if tile is empty
    #if so, place on map and return true, otherwise, return false
    def placeOnMap(self, map):
        print()

    #die function
    #remove unit from map
    #remove unit from player unit array
