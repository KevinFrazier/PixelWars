from tkinter import *
from Unit import Unit


class Helicopter(Unit):
    # type, health, damage, movement, range, x, y
    def __init__(self, x, y):
        Unit.__init__(self, 4, 5, 3, 2, 1, x, y)
        self.cost = 900

    def getCost(self):
        return self.cost

    #attack (C&P from infantry)

    #move
    #more general since no need to check for tile type
    #still check for validity
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
                self.setRemainingMoves(self.getRemainingMoves() - reqMoves)
                return True

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