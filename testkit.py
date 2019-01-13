from kit import Kit

print("Kits are : ",Kit.kits)
board = Kit("s2441")
board.addComponent("wr21","55581")
board.addComponent("TA 125","CFG5148")
board.addComponent("Tbrt 47","tfr444")
board.addComponent("tf d2","noshit154")
board.addComponent("SIM VZ","422222222",True,"55581")

anotherBoard = Kit("s2331")
anotherBoard.addComponent("wr21","3333")
anotherBoard.addComponent("TA 125","CF8455")
anotherBoard.addComponent("Tbrt 47","14S55")
anotherBoard.addComponent("tf d2","lsladjsk")
anotherBoard.addComponent("SIM VZ","855655655",True,"3333")

print(board)
print(anotherBoard)
print("The two Boards are Equal ? : ", board == anotherBoard)
print("Kits are : ",Kit.kits)
