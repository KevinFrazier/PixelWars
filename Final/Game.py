from tkinter import *
from theMap import Map
from Player import Player
from Unit import Unit
from Infantry import Infantry
from Tank import Tank
from Helicopter import Helicopter
from Base import Base
from threading import Timer
import math
'''
6.6.2017

document
randomization -> streets, mountains, lake, random base position -> still needs work
tank attack -> takes list of units
add currency check and display ong (update)
tank gets extra move
spawning check terrain types
kill unit for currency

'''


root = Tk()

class Game(Frame):

    def __init__(self):

        self.titleMenu()

    def currencyUpdate(self):
        self.moneyLabel.configure(text = "Player " + str((self.currentPlayer.playerNumber + 1)) + " cash: " + str(self.currentPlayer.getCurrency()))

        for player in self.listOfPlayers:
            player.setCurrency(player.getCurrency() + 500)

    def updateMap(self):
        for player in self.listOfPlayers:
            for unit in player.unitList:
                self.map.drawImage(player.playerNumber, unit.getX(), unit.getY(), unit.getType())

    def UserButtons(self):
        buttonFrame = Frame(self)
        buttonFrame.grid()
        self.upButton = Button(buttonFrame, text=" ^ ", command=self.up)
        self.upButton.grid(row=0, column=1)
        self.downButton = Button(buttonFrame, text=" v ", command=self.down)
        self.downButton.grid(row=2, column=1)
        self.leftButton = Button(buttonFrame, text=" < ", command=self.left)
        self.leftButton.grid(row=1, column=0)
        self.rightButton = Button(buttonFrame, text=" > ", command=self.right)
        self.rightButton.grid(row=1, column=2)

        self.spawnButton = Button(buttonFrame, text="Spawn Unit", command=self.spawn)
        self.spawnButton.grid(row=0, column=5)
        self.infantryRdo = Radiobutton(buttonFrame, text="Infantry", variable=self.spawnUnitType, value=2)
        self.infantryRdo.grid(row=1, column=5)
        self.tankRdo = Radiobutton(buttonFrame, text="Tank", variable=self.spawnUnitType, value=3)
        self.tankRdo.grid(row=2, column=5)
        self.helicopterRdo = Radiobutton(buttonFrame, text="Helicopter", variable=self.spawnUnitType, value=4)
        self.helicopterRdo.grid(row=3, column=5)


        self.attackButton = Button(buttonFrame, text = "Attack", command = self.attack)
        self.attackButton.grid(row = 1,column =6)
        cancelButton = Button(buttonFrame, text="Cancel", command=self.cancel)
        cancelButton.grid(row=2, column=6)
        skipButton = Button(buttonFrame, text="Skip", command=self.skip)
        skipButton.grid(row=3, column=6)

        self.moneyLabel = Label(buttonFrame, text = "Player " + str((self.currentPlayer.playerNumber + 1)) + " cash: " + str(self.currentPlayer.getCurrency()))
        self.moneyLabel.grid(row=0, column = 7)


    def enableDisableButtons(self):

        u = self.currentPlayer.getCurrentUnit()
        print(u.getType())
        if(u.getType() == 0 or u.getType() == 1): #camp or base
            self.upButton.configure(state = DISABLED)
            self.downButton.configure(state = DISABLED)
            self.rightButton.configure(state = DISABLED)
            self.leftButton.configure(state = DISABLED)
            self.attackButton.configure(state = DISABLED)
            self.spawnButton.configure(state = NORMAL)
            self.infantryRdo.configure(state = NORMAL)
            self.tankRdo.configure(state=NORMAL)
            self.helicopterRdo.configure(state=NORMAL)
        else: #infantry, tank, helicopter
            self.upButton.configure(state=NORMAL)
            self.downButton.configure(state=NORMAL)
            self.rightButton.configure(state=NORMAL)
            self.leftButton.configure(state=NORMAL)
            self.attackButton.configure(state = NORMAL)
            self.spawnButton.configure(state=DISABLED)
            self.infantryRdo.configure(state=DISABLED)
            self.tankRdo.configure(state=DISABLED)
            self.helicopterRdo.configure(state=DISABLED)

    def skip(self):
        try:
            u = self.currentPlayer.getCurrentUnit()
            self.currentPlayer.nextUnit()
        except IndexError:
            self.switchPlayers()
            self.currentPlayer.newTurn()
    def getPlayer_getUnit(self, x, y):
        for player in self.listOfPlayers:
                for u in player.unitList:
                    if u.getX() == x and u.getY() == y:
                        return u,player

        return None

    def attack(self):
        '''

        '''
        if self.currentPlayer.getCurrentUnit().getType() != 0 and self.currentPlayer.getCurrentUnit().getType() != 1:

            if not(self.attackButtonPressed):

                u = self.currentPlayer.getCurrentUnit()
                self.cursorPositionX = u.getX()
                self.cursorPositionY = u.getY()
                self.redrawCursor()
                self.upButton.configure(command = self.attackUp)
                self.downButton.configure(command = self.attackDown)
                self.rightButton.configure(command = self.attackRight)
                self.leftButton.configure(command = self.attackLeft)

                self.attackButtonPressed = True

            else:
                try:
                    u,p = self.getPlayer_getUnit(self.cursorPositionX,self.cursorPositionY)
                # if u != None:
                    #change button commands


                    #calculate damage

                    #identify unit being attacked, and attack, then check the life if it is zero then delete image

                    #when the attacked unit is dead
                    s = self.currentPlayer.getCurrentUnit()
                    distance = int( abs(s.getX() - u.getX()) + abs(s.getY() - u.getY()))
                    print("distance: ", distance)
                    print("s range: ", s.getRange())
                    if s.getRange() >= distance:
                        print("u health: ", u.getHealth())
                        if s.attack(u):
                            if u.getType() == 0:
                                #win
                                print("win")
                            else:
                                self.map._unitGrid[u.getX()][u.getY()] = None
                                p.removeUnit(u)

                        else:
                            print("u health: ", u.getHealth())

                        self.upButton.configure(command=self.up)
                        self.downButton.configure(command=self.down)
                        self.rightButton.configure(command=self.right)
                        self.leftButton.configure(command=self.left)
                        self.attackButtonPressed = False

                    else:
                        print("invalid target, target is at distance of: ", distance, " and range is: ", s.getRange())
                        return


                except:
                    print("No Unit selected")
                    self.attackButtonPressed = False
                    self.attack()
                    return

                self.map.draw_grid()

                #end Unit's turn
                try:
                    self.currentPlayer.nextUnit()
                except IndexError:
                    self.switchPlayers()
                    self.currentPlayer.newTurn()
            # else:
            #     print("No Unit!")
            #
            #     self.self.attackButtonPressed = False
            #     c = self.map._screen
            #     c.delete("cursor")
                # change self.attackButton state and delete Cursor


                # self.currentPlayer.getCurrentUnit().

    def cancel(self):
        self.upButton.configure(command=self.up)
        self.downButton.configure(command=self.down)
        self.rightButton.configure(command=self.right)
        self.leftButton.configure(command=self.left)

        # change self.attackButton state and delete Cursor
        self.self.attackButtonPressed = False
        c = self.map._screen
        c.delete("cursor")

    def redrawCursor(self):
        c = self.map._screen
        # print(c.find_withtag( "cursor" ))
        c.delete("cursor")
        item = c.create_image((self.cursorPositionX * self.map.spriteDimension, self.cursorPositionY * self.map.spriteDimension),
                       anchor = NW , image = self.cursor)
        c.itemconfig(item, tags = "cursor")

    def attackUp(self):
        self.cursorPositionY =  self.cursorPositionY - 1
        self.redrawCursor()
    def attackRight(self):
        self.cursorPositionX = self.cursorPositionX + 1
        self.redrawCursor()
    def attackDown(self):
        self.cursorPositionY = self.cursorPositionY + 1
        self.redrawCursor()
    def attackLeft(self):
        self.cursorPositionX = self.cursorPositionX - 1
        self.redrawCursor()

    def up(self):
        try:
            u = self.currentPlayer.getCurrentUnit()
            if u.canMove():
                if u.getType() != 0 and u.getType() != 1:
                    # print(self.map._grid[u.getX()][u.getY() - 1].isAvailable())
                    if self.map._grid[u.getX()][u.getY() - 1].isAvailable():
                        if (self.map._grid[u.getX()][u.getY() - 1].getTileType() == 2 or self.map._grid[u.getX() + 1][
                            u.getY()].getTileType() == 4) and u.getType() == 4:
                            self.map._unitGrid[u.getX()][u.getY() - 1] = self.map._unitGrid[u.getX()][u.getY()]
                            self.map._unitGrid[u.getX()][u.getY()] = None
                            self.map._grid[u.getX()][u.getY()].setAvailable(True)
                            u.move(u.getX(), u.getY() - 1)
                            self.map.draw_grid()
                        else:
                            self.map._unitGrid[u.getX()][u.getY() - 1] = self.map._unitGrid[u.getX()][u.getY()]
                            self.map._unitGrid[u.getX()][u.getY()] = None
                            self.map._grid[u.getX()][u.getY()].setAvailable(True)
                            u.move(u.getX(), u.getY() - 1)
                            self.map.draw_grid()
                    else:
                        print("not available")
            else:
                self.currentPlayer.nextUnit()
                self.up()
        except IndexError:
            self.switchPlayers()
            self.currentPlayer.newTurn()
            self.up()

    def down(self):
        try:
            u = self.currentPlayer.getCurrentUnit()
            if u.canMove():
                if u.getType() != 0 and u.getType() != 1:
                    # print(self.map._grid[u.getX()][u.getY() + 1].isAvailable())
                    if self.map._grid[u.getX()][u.getY() + 1].isAvailable():
                        if (self.map._grid[u.getX()][u.getY() + 1].getTileType() == 2 or self.map._grid[u.getX() + 1][
                            u.getY()].getTileType() == 4) and u.getType() == 4:
                            self.map._unitGrid[u.getX()][u.getY() + 1] = self.map._unitGrid[u.getX()][u.getY()]
                            self.map._unitGrid[u.getX()][u.getY()] = None
                            self.map._grid[u.getX()][u.getY()].setAvailable(True)
                            u.move(u.getX(), u.getY() + 1)
                            self.map.draw_grid()
                        else:
                            self.map._unitGrid[u.getX()][u.getY() + 1] = self.map._unitGrid[u.getX()][u.getY()]
                            self.map._unitGrid[u.getX()][u.getY()] = None
                            self.map._grid[u.getX()][u.getY()].setAvailable(True)
                            u.move(u.getX(), u.getY() + 1)
                            self.map.draw_grid()
                    else:
                        print("not available")
            else:
                self.currentPlayer.nextUnit()
                self.down()
        except IndexError:
            self.switchPlayers()
            self.currentPlayer.newTurn()
            self.down()

    def left(self):
        try:
            u = self.currentPlayer.getCurrentUnit()
            if u.canMove():
                if u.getType() != 0 and u.getType() != 1:
                    # print(self.map._grid[u.getX() - 1][u.getY()].isAvailable())
                    if self.map._grid[u.getX() - 1][u.getY()].isAvailable():
                        if (self.map._grid[u.getX() - 1][u.getY()].getTileType() == 2 or self.map._grid[u.getX() + 1][
                            u.getY()].getTileType() == 4) and u.getType() == 4:
                            self.map._unitGrid[u.getX() - 1][u.getY()] = self.map._unitGrid[u.getX()][u.getY()]
                            self.map._unitGrid[u.getX()][u.getY()] = None
                            self.map._grid[u.getX()][u.getY()].setAvailable(True)
                            u.move(u.getX() - 1, u.getY())
                            self.map.draw_grid()
                        else:
                            self.map._unitGrid[u.getX() - 1][u.getY()] = self.map._unitGrid[u.getX()][u.getY()]
                            self.map._unitGrid[u.getX()][u.getY()] = None
                            self.map._grid[u.getX()][u.getY()].setAvailable(True)
                            u.move(u.getX() - 1, u.getY())
                            self.map.draw_grid()
                    else:
                        print("not available")
            else:
                self.currentPlayer.nextUnit()
                self.left()
        except IndexError:
            self.switchPlayers()
            self.currentPlayer.newTurn()
            self.left()

    def right(self):
        try:
            u = self.currentPlayer.getCurrentUnit()
            if u.canMove():
                if u.getType() != 0 and u.getType() != 1:
                    # print(self.map._grid[u.getX() + 1][u.getY()].isAvailable())
                    if self.map._grid[u.getX() + 1][u.getY()].isAvailable():
                        if (self.map._grid[u.getX() + 1][u.getY()].getTileType() == 2 or self.map._grid[u.getX() + 1][
                            u.getY()].getTileType() == 4) and u.getType() == 4:
                            self.map._unitGrid[u.getX() + 1][u.getY()] = self.map._unitGrid[u.getX()][u.getY()]
                            self.map._unitGrid[u.getX()][u.getY()] = None
                            self.map._grid[u.getX()][u.getY()].setAvailable(True)
                            u.move(u.getX() + 1, u.getY())
                            self.map.draw_grid()
                        else:
                            self.map._unitGrid[u.getX() + 1][u.getY()] = self.map._unitGrid[u.getX()][u.getY()]
                            self.map._unitGrid[u.getX()][u.getY()] = None
                            self.map._grid[u.getX()][u.getY()].setAvailable(True)
                            u.move(u.getX() + 1, u.getY())
                            self.map.draw_grid()
                    else:
                        print("not available")
            else:
                self.currentPlayer.nextUnit()
                self.right()
        except IndexError:
            self.switchPlayers()
            self.currentPlayer.newTurn()
            self.right()

    def switchPlayers(self):
        if self.currentPlayer == self.listOfPlayers[0]:
            self.currentPlayer = self.listOfPlayers[1]
        else:
            self.currentPlayer = self.listOfPlayers[0]
        # self.enableDisableButtons()

    def titleMenu(self):

        Frame.__init__(self)
        self.pack()
        self.menuFrame = Frame(self)
        self.menuFrame.pack()

        titleLabel = Label(self.menuFrame, text = "Pixel Wars")
        titleLabel.pack(anchor = CENTER)

        playerFrame = Frame(self, borderwidth = 10)
        playerFrame.pack(anchor = CENTER)

        # self.var = IntVar()
        # playerLabel = Label(playerFrame, text = "Players")
        # R1 = Radiobutton(playerFrame, text="1", variable=self.var, value=1, command = self.sel)
        # R1.pack(anchor=W)
        # R2 = Radiobutton(playerFrame, text="2", variable=self.var, value=2, command = self.sel)
        # R2.pack(anchor=W)
        # R3 = Radiobutton(playerFrame, text="3", variable=self.var, value=3, command = self.sel)
        # R3.pack(anchor=W)
        # R4 = Radiobutton(playerFrame, text="4", variable=self.var, value=4, command=self.sel)
        # R4.pack(anchor=W)
        MapFrame = Frame(self.menuFrame)
        MapFrame.pack()

        self.mapLabel = Label(MapFrame, text = "Map")
        self.mapLabel.pack()
        self.var3 = IntVar()
        R42 = Radiobutton(MapFrame, text="S", variable=self.var3, value=10, command=self.sel2)
        R42.pack(anchor=W, side = LEFT)
        R52 = Radiobutton(MapFrame, text="M", variable=self.var3, value=20, command=self.sel2)
        R52.pack(anchor=W, side = LEFT)
        R62 = Radiobutton(MapFrame, text="L", variable=self.var3, value=30, command=self.sel2)
        R62.pack(anchor=W, side = LEFT)

        startFrame = Frame(self)
        startFrame.pack()

        startButton = Button(startFrame, text = "Start", command = self.start)
        startButton.pack()
        exitButton = Button(startFrame, text = "Exit", command = self.exit)
        exitButton.pack()

    def start(self):
        # self.titleMenu()
        # self.gameFrame = Frame(self.)
        print(self.var3.get())
        if self.var3.get() != 0:
            self.master.destroy()
            Frame.__init__(self)
            self.pack()

            self.listOfPlayers = [Player(0), Player(1)]
            self.currentPlayer = self.listOfPlayers[0]

            self.map = Map(self.var3.get())

            self.cursor = PhotoImage(file="cursor.gif")
            c = self.map._screen
            self.cursorPositionX = 0
            self.cursorPositionY = 0
            self.attackButtonPressed = False

            #random function
            self.aUnit = Base(1, 1, 1)
            self.bUnit = Base(self.var3.get()-2, self.var3.get()- 2, 1)
            self.listOfPlayers[0].addUnit(self.aUnit)
            self.listOfPlayers[1].addUnit(self.bUnit)
            # self.aUnit2 = Tank(3,4)
            # self.bUnit2 = Tank(3,6)
            # self.listOfPlayers[0].addUnit(self.aUnit2)
            # self.listOfPlayers[1].addUnit(self.bUnit2)

            self.spawnUnitType = IntVar()
            self.UserButtons()
            # self.enableDisableButtons()
            self.updateMap()  # for units only
            self.map.fill()
            self.map.draw_grid()

    def exit(self):
        self.master.destroy()
        return

    def sel(self):

        print("You have selected Player:" + str(self.var.get()))

    def sel2(self):
        print("You have selected Map: " + str(self.var3.get()))

    def spawn(self):
        try:
            u = self.currentPlayer.getCurrentUnit()
            if u.canMove():
                if u.getType() == 0 or u.getType() == 1:
                    for tile in self.map.getAdjacent(self.currentPlayer.getCurrentUnit().getX(),
                                                     self.currentPlayer.getCurrentUnit().getY()):
                        if tile.isAvailable():
                            unit = u.spawnUnit(self.spawnUnitType.get(), tile.getX(), tile.getY())
                            # if self.spawnUnitType.get() == 2:
                            #     unit = Infantry(tile.getX(), tile.getY())
                            # elif self.spawnUnitType.get() == 3:
                            #     unit = Tank(tile.getX(), tile.getY())
                            # else:
                            #     unit = Helicopter(tile.getX(), tile.getY())
                            unit.setRemainingMoves(0)
                            self.currentPlayer.addUnit(unit)
                            # self.map._unitGrid[[tile.getX()][tile.getY()]] = unit
                            self.updateMap()
                            self.currentPlayer.getCurrentUnit().setRemainingMoves(
                                self.currentPlayer.getCurrentUnit().getRemainingMoves() - 1)
                            return True
                elif u.getType() == 2:
                    for tile in self.map.getAdjacent(self.currentPlayer.getCurrentUnit().getX(),
                                                     self.currentPlayer.getCurrentUnit().getY()):
                        if tile.isAvailable():
                            unitX, unitY, unitType = u.buildCamp(tile.getX(), tile.getY())
                            unit = Base(unitX, unitY, unitType)
                            unit.setRemainingMoves(0)
                            self.currentPlayer.addUnit(unit)
                            # self.map._unitGrid[[tile.getX()][tile.getY()]] = unit
                            self.updateMap()
                            self.currentPlayer.getCurrentUnit().setRemainingMoves(
                                self.currentPlayer.getCurrentUnit().getRemainingMoves() - 1)
                            return True
            else:
                self.currentPlayer.nextUnit()
                self.spawn()
                # self.enableDisableButtons()
        except IndexError:
            self.switchPlayers()
            self.currentPlayer.newTurn()
            # self.enableDisableButtons()
            self.spawn()

def main():
    PixelWars = Game()
    # root.after(1000,Game.updateMap)
    root.mainloop() # forever loop

main()