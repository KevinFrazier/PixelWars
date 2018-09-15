from Unit import Unit

class Infantry(Unit):
    # type, health, damage, movement, range, x, y
    # pass in a map to be placed in
    def __init__(self, x, y):
        Unit.__init__(self, 2, 4, 3, 1, 1, x, y)
        self.cost = 300

    def getCost(self):
        return self.cost

    # replace with x, y
    def attack(self, otherUnit):
        if self.getRemainingMoves() > 0:
            if self.calcAdvantage(otherUnit):
                dmg = self.getDamage() * 1.5
            else:
                dmg = self.getDamage()
            if otherUnit.getHealth() <= dmg:
                return True
            else:
                otherUnit.setHealth(otherUnit.getHealth() - dmg)
                return False

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
                self.setRemainingMoves(self.getRemainingMoves() - reqMoves)
                return True

    def buildCamp(self, x, y):
        return x, y, 0

    # check in range function
    def inRange(self, x, y):
        difX = abs(self.getX() - x)
        difY = abs(self.getY() - y)
        reqRange = difX + difY
        if self.getRange() >= reqRange:
            return True
        else:
            return False
