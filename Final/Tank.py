from tkinter import *
from Unit import Unit


class Tank(Unit):
    # type, health, damage, movement, range, tile
    def __init__(self, x, y):
        Unit.__init__(self, 3, 6, 3, 2, 2, x, y)
        self.cost = 500

    def getCost(self):
        return self.cost

    def attack(self, otherUnit):
        if self.getRemainingMoves() > 0:
            if self.calcAdvantage(otherUnit):
                dmg = self.getDamage() * 2
            else:
                dmg = self.getDamage()
            if otherUnit.getHealth() <= dmg:
                return True
            else:
                otherUnit.setHealth(otherUnit.getHealth() - dmg)
                return False

    #basic attack (C&P from infantry)

    #splash attack
    #get target tile within range
    #check tile for unit
    #apply attack
    #check each adjacent tile for unit
    #apply attack to each

    #move function (C&P from infantry)
    # click unit, click destination, if too far: show dialogue box, else: move to destination?
    # check for tile type as well to make sure not water
    def move(self, x, y):
        if self.getRemainingMoves() > 0:
            difX = abs(self.getX() - x)
            difY = abs(self.getY() - y)
            reqMoves = difX + difY
            if reqMoves > self.getRemainingMoves():
                return False
            else:
                self.setX(x)
                self.setY(y)
                self.setRemainingMoves(self.getRemainingMoves()-reqMoves)
                return True
