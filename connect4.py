from cmu_graphics import *

# game state variables
gameOn = False
bgColor = "white"
playerOneColor = "red"
playerTwoColor = "yellow"
app.color = bgColor

winner = ""

player = 1
rows = 6
cols = 7

# board storage
holes = []
hoverHoles = []

board = Group(Rect(40, 80, 320, 280, fill="blue"), Rect(40, 360, 15, 100, fill="blue"),
              Rect(345, 360, 15, 100, fill="blue"))
board.visible = False

# UI elements
winLabel = Label("", 0, 0, visible=False)
restartLabel = Group()
restartLabel.visible = False

# drop animation
fallingPiece = None
fallingRow = None
fallingCol = None

fallDelay = 0
fallDelayMax = 4
targetRow = None

# title screen components
title = Label("Connect 4 Game", 204, 80, size=40, font="monospace", visible=False)
startButton = Rect(80, 200, 240, 80, fill="black", visible=False)
startText = Group(Label("Press Start", 200, 240, size=32, fill="white", font="sans-serif", bold=True, visible=False),
                  Label("Press Start", 201, 241, size=32, fill="white", font="sans-serif", bold=True, visible=False))

# decorative stick figures for title screen
person = Group(Circle(80, 320, 15), Line(80, 320, 80, 375), Line(80, 375, 85, 400), Line(80, 375, 75, 400),
               Line(80, 362, 100, 340), Line(80, 362, 60, 340))
person.visible = False
person2 = Group(Circle(320, 320, 15), Line(320, 320, 320, 375), Line(320, 375, 325, 400), Line(320, 375, 315, 400),
                Line(320, 362, 340, 350), Line(340, 350, 340, 335), Line(320, 362, 300, 340))
person2.visible = False


def titleScreen():
    global gameOn

    gameOn = False
    title.visible = True
    startButton.visible = True
    startText.visible = True
    person.visible = True
    person2.visible = True


titleScreen()


def setup():
    global gameOn, rows, cols, holes, hoverHoles

    gameOn = True
    board.visible = True

    holes = [[None for _ in range(cols)] for _ in range(rows)]

    # setup coins
    for col in range(cols):
        for row in range(rows):
            circle = Circle(80 + 40 * col, 120 + 40 * row, 15, fill=bgColor)
            holes[row][col] = circle

    # setup hover coins
    for col in range(cols):
        circle = Circle(80 + 40 * col, 60, 20, fill="gray")
        circle.visible = False
        hoverHoles.append(circle)


def onMouseMove(mouseX, mouseY):
    playerCol = getCol(mouseX)

    # show preview pieces for each column
    if gameOn:
        for col in range(cols):
            if playerCol == col and not isColFull(col):
                hoverHoles[col].visible = True
            else:
                hoverHoles[col].visible = False


def drop(playerCol):
    global fallingPiece, fallingRow, fallingCol, fallDelay, targetRow

    # starts falling animation for each piece
    if gameOn and fallingPiece == None:
        fallingRow = -1
        fallingCol = playerCol
        fallDelay = 0
        fallingPiece = getCurrentColor()

        for row in range(rows - 1, -1, -1):
            if holes[row][playerCol].fill == bgColor:
                targetRow = row
                break


def isBoardFull():
    # returns false if one hole is not filled else true
    for row in range(rows):
        for col in range(cols):
            if holes[row][col].fill == bgColor:
                return False
    return True


def isColFull(col):
    # checks if top column is full to determine if filled
    return not holes[0][col].fill == bgColor


def getCurrentColor():
    # returns the color string of current player
    global player

    if player == 1:
        return playerOneColor
    elif player == 2:
        return playerTwoColor


def onMousePress(mouseX, mouseY):
    global player, gameOn, board, winLabel, restartLabel

    playerCol = getCol(mouseX)

    # start game
    if not gameOn and title.visible and startButton.hits(mouseX, mouseY):
        title.visible = False
        startButton.visible = False
        startText.visible = False
        person.visible = False
        person2.visible = False
        setup()
        return

    # drop piece
    if gameOn and fallingPiece == None and playerCol != -1 and not isColFull(playerCol):
        drop(playerCol)


def onKeyPress(key):
    # reset
    if not gameOn:
        if key == 'n' or key == 'N':
            reset()


def getCol(mouseX):
    # converts mouse position to column index
    col = (mouseX - 60) // 40
    if 0 <= col <= 6:
        return col
    return -1


def playerWon():
    global winner

    # check vertical | win condition
    for row in range(rows - 3):
        for col in range(cols):
            color = holes[row][col].fill
            if color != bgColor and color == holes[row + 1][col].fill == holes[row + 2][col].fill == holes[row + 3][
                col].fill:
                winner = color
                return True

    # check horizontal - win condition
    for row in range(rows):
        for col in range(cols - 3):
            color = holes[row][col].fill
            if color != bgColor and color == holes[row][col + 1].fill == holes[row][col + 2].fill == holes[row][
                col + 3].fill:
                winner = color
                return True

    # check diagonal \ win condition
    for row in range(rows - 3):
        for col in range(cols - 3):
            color = holes[row][col].fill
            if color != bgColor and color == holes[row + 1][col + 1].fill == holes[row + 2][col + 2].fill == \
                    holes[row + 3][col + 3].fill:
                winner = color
                return True

    # check diagonal / win condition
    for row in range(3, rows):
        for col in range(cols - 3):
            color = holes[row][col].fill
            if color != bgColor and color == holes[row - 1][col + 1].fill == holes[row - 2][col + 2].fill == \
                    holes[row - 3][col + 3].fill:
                winner = color
                return True

    return False


def reset():
    global gameOn, winner, player, holes, hoverHoles, board, winLabel, restartLabel, fallingPiece, fallingRow, fallingCol

    # resets the global variables
    gameOn = False
    player = 1
    winner = ""

    winLabel.visible = False
    restartLabel.visible = False

    fallingPiece = None
    fallingRow = None
    fallingCol = None

    board.visible = False

    # clear hover holes
    for circle in hoverHoles:
        circle.visible = False
    hoverHoles = []

    # clear board holes
    for row in holes:
        for circle in row:
            circle.visible = False
    holes = []

    # sends user back to title screen
    titleScreen()


def onStep():
    global fallingPiece, fallingRow, fallingCol, fallDelay, targetRow, winLabel, restartLabel, player, gameOn, holes, hoverHoles, rows, cols

    # switches color for hover holes
    if gameOn:
        for col in range(len(hoverHoles)):
            if hoverHoles[col].visible:
                hoverHoles[col].fill = getCurrentColor()

    # piece drop logic
    if fallingPiece != None:
        fallDelay += 1

        if fallDelay >= fallDelayMax:
            fallDelay = 0

            # clear previous hole
            if fallingRow >= 0:
                holes[fallingRow][fallingCol].fill = bgColor

            fallingRow += 1

            # fill current hole
            holes[fallingRow][fallingCol].fill = fallingPiece

            if fallingRow == targetRow:

                # check win
                if playerWon():
                    gameOn = False
                    if (winner == playerOneColor):
                        winLabel = Label("Player 1 Won!", 100, 40, size=25)
                    elif (winner == playerTwoColor):
                        winLabel = Label("Player 2 Won!", 100, 40, size=25)
                    else:
                        winLabel = Label(winner + " Won!", 100, 40, size=25)

                    restartLabel = Group(Label("Press N", 320, 35, size=25), Label("to restart:", 320, 55, size=25))

                    for circle in hoverHoles:
                        circle.visible = False

                # check draw
                elif isBoardFull():
                    gameOn = False
                    winLabel = Label("It's a Draw!", 100, 40, size=25)
                    restartLabel = Group(Label("Press N", 320, 35, size=25), Label("to restart:", 320, 55, size=25))
                    for circle in hoverHoles:
                        circle.visible = False

                # switch players
                if gameOn:
                    if player == 1:
                        player = 2
                    elif player == 2:
                        player = 1

                # clear pieces
                fallingPiece = None

                return

cmu_graphics.run()
