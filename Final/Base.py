from Unit import Unit
from Infantry import Infantry
from Tank import Tank
from Helicopter import Helicopter

unitCost = {'infantry': 300, 'tank': 500, 'helicopter': 900}

class Base(Unit):
    def __init__(self, x, y, base):
        #if base, set health to 5
        if(base):
            Unit.__init__(self, 0, 5, 0, 1, 0, x, y)
        #if camp, set health to 3
        else:
            Unit.__init__(self, 1, 3, 0, 1, 0, x, y)
        self.isBase = base

# functions: isbase, spawn, checkfunds, checkadjacent, takedamage
    def isBase(self):
        return self.isBase

    def checkFunds(self, player, unitType):
        return player.getCurrency() == unitCost[unitType]

    # def getEmptyPosition(self):
    #

    # place on map, add to player list
    def spawnUnit(self, unitType, x, y):
        if self.isBase:
            if unitType == 2:
                unit = Infantry(x, y)
            elif unitType == 3:
                unit = Tank(x, y)
            else:
                unit = Helicopter(x, y)
        else:
            unit = Infantry(x, y)
        return unit