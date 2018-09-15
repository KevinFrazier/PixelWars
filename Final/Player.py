
from tkinter import *
class Player(object):
    def __init__(self, playerNumber):

        self.playerNumber = playerNumber
        self.unitList = []
        self.currency = 1000
        self.isTurn = False
        self.current = 0

        #cursor

    def moveCursor(self,x,y):
        self.cursorPositionX = x
        self.cursorPositionY = y

    def getCursor(self):
        return self.cursor
    def getCursorPositionX(self):
        return self.cursorPositionX
    def getCursorPositionY(self):
        return self.cursorPositionY

    def changeTurn(self):
        if self.isTurn:
            self.isTurn = False
        else:
            self.isTurn = True

    def getCurrency(self):
        return self.currency

    def setCurrency(self, currency):
        self.currency = currency

    def getNumUnits(self):
        return len(self.unitList)

    def addUnit(self, unit):
        self.unitList.append(unit)

    def removeUnit(self, unit):
        self.unitList.remove(unit)

    def getCurrentUnit(self):
        return self.unitList[self.current]

    def nextUnit(self):
        self.current += 1

    def newTurn(self):
        for unit in self.unitList:
            unit.resetMoves()
        self.current = 0
