import sys, pygame, random
from pygame import *
from pygame.locals import *
from pygame.sprite import *

# some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGRAY = (47, 79, 79)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 155, 255)
BROWN = (150, 75, 0)
YELLOW = (255, 255, 0)

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 60
HOLESWIDTH = 4
HOLESHEIGHT = 4

XMARGIN = int((WINDOWWIDTH - (BOXSIZE * HOLESWIDTH + (HOLESWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOXSIZE * HOLESHEIGHT + (HOLESHEIGHT - 1))) / 2)


# Farmer sprite object
class Ace(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("Ace.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Two(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("2.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Three(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("3.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Four(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("4.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Five(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("5.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))

class Six(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("6.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Seven(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("7.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Eight(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("8.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Nine(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("9.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Ten(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("10.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Jack(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("Jack.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Queen(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("Queen.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class King(pygame.sprite.Sprite):

    # "Constructor" of the Ace sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("King.png")
        imageSized = pygame.transform.scale(image, (62, 88))
        self.image = imageSized
        self.rect = self.image.get_rect(topleft=(x, y))


class Tomato(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tomato_image.png").convert_alpha()
        self.rect = self.image.get_rect()

    # did the shovel hit the mole?
    def hit(self, target):
        return self.rect.colliderect(target)

    # follows the mouse cursor
    def update(self, pt):
        self.rect.center = pt

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def centerImage(DISPLAYSURF, im):
    scrWidth, scrHeight = DISPLAYSURF.get_size()
    x = (scrWidth - im.get_width()) / 2
    y = (scrHeight - im.get_height()) / 2
    DISPLAYSURF.blit(im, (x, y))


def addPoints():
    global scoreNum
    # method to add points with every "successful" click
    scoreNum = scoreNum + 1


start_ticks = pygame.time.get_ticks()


def main():
    global scoreNum
    pygame.display.set_caption('WhackACard')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 30)
    DISPLAYSURF = pygame.display.set_mode((640, 480))
    DISPLAYSURF.fill(GREEN)
    clock = pygame.time.Clock()
    timer = 60  # 1 means one second; 60 means sixty seconds or one minute
    timerDecrement = 1  # 1 means one second; Should be used for counting down

    # Score stuff
    scoreNum = 0

    # Makes it so that only one dot exists on the tile at a time
    haveSetTile = False
    theX = None
    theY = None
    dotLocation = pygame.draw.rect(DISPLAYSURF, BROWN, (400, 400, 1, 1))

    # Board starts with an Ace
    current_card = Ace(200, 195)
    randX = 1
    randY = 1

    # Starting temp to indicate card type
    temp = 1

    # Determinant booleans for which types of cards can be selected
    faceCardOnly = False
    numberCardOnly = False
    evenCardOnly = False
    oddCardOnly = True

    # Determinant boolean for the current card on board
    isFaceCard = False
    isNumberCard = True
    isEvenCard = False
    isOddCard = True

    # Saves the timestep at a certain point so that 3 second cycles can be maintained
    savedTime = 0

    gameOver = False
    gameOverTime = False

    while True:
        scoreText = "Score: "
        timeText = "Time: "
        theScoreText = BASICFONT.render(scoreText, True, WHITE)
        theTimeText = BASICFONT.render(timeText, True, WHITE)
        DISPLAYSURF.blit(theScoreText, (20, 20))
        DISPLAYSURF.blit(theTimeText, (20, 60))

        pointString = str(scoreNum)
        theScoreNumText = BASICFONT.render(pointString, True, WHITE)
        pygame.draw.rect(DISPLAYSURF, GREEN, (120, 20, 80, 25))
        DISPLAYSURF.blit(theScoreNumText, (120, 20))

        onlyClickText = "Only Click On:"
        theOnlyClickText = BASICFONT.render(onlyClickText, True, WHITE)
        pygame.draw.rect(DISPLAYSURF, GREEN, (220, 20, 200, 25))
        DISPLAYSURF.blit(theOnlyClickText, (220, 20))

        if faceCardOnly is True:
            onlyText = "FACE CARDS"
            theOnlyText = BASICFONT.render(onlyText, True, RED)
            pygame.draw.rect(DISPLAYSURF, GREEN, (220, 50, 450, 25))
            DISPLAYSURF.blit(theOnlyText, (250, 50))
        elif numberCardOnly is True:
            onlyText = "NUMBERED CARDS"
            theOnlyText = BASICFONT.render(onlyText, True, BLUE)
            pygame.draw.rect(DISPLAYSURF, GREEN, (220, 50, 450, 25))
            DISPLAYSURF.blit(theOnlyText, (250, 50))
        elif evenCardOnly is True:
            onlyText = "EVEN NUMBERED CARDS"
            theOnlyText = BASICFONT.render(onlyText, True, BLACK)
            pygame.draw.rect(DISPLAYSURF, GREEN, (220, 50, 450, 25))
            DISPLAYSURF.blit(theOnlyText, (250, 50))
        elif oddCardOnly is True:
            onlyText = "ODD NUMBERED CARDS"
            theOnlyText = BASICFONT.render(onlyText, True, DARKGRAY)
            pygame.draw.rect(DISPLAYSURF, GREEN, (220, 50, 450, 25))
            DISPLAYSURF.blit(theOnlyText, (250, 50))

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
        # if seconds > 30:  # if more than 30 seconds close the game
        # print(seconds)  # print how many seconds
        secondsString = str(seconds)
        theSecondsText = BASICFONT.render(secondsString, True, WHITE)
        pygame.draw.rect(DISPLAYSURF, GREEN, (140, 60, 100, 100))
        DISPLAYSURF.blit(theSecondsText, (140, 60))

        if int(seconds) == 30:
            gameOverTime = True

        x = 0
        y = 0

        holeArray1 = []
        holeArray2 = []
        holeArray3 = []
        holeArray4 = []
        # placeholder for dotLocation

        # all this just draws the 8 brown squares
        hole11 = pygame.draw.rect(DISPLAYSURF, BROWN, (100, 100, 62, 88))
        holeArray1.append(hole11)
        hole12 = pygame.draw.rect(DISPLAYSURF, BROWN, (100, 195, 62, 88))
        holeArray1.append(hole12)
        hole13 = pygame.draw.rect(DISPLAYSURF, BROWN, (100, 290, 62, 88))
        holeArray1.append(hole13)
        hole14 = pygame.draw.rect(DISPLAYSURF, BROWN, (100, 385, 62, 88))
        holeArray1.append(hole14)

        hole21 = pygame.draw.rect(DISPLAYSURF, BROWN, (200, 100, 62, 88))
        holeArray2.append(hole21)
        hole22 = pygame.draw.rect(DISPLAYSURF, BROWN, (200, 195, 62, 88))
        holeArray2.append(hole22)
        hole23 = pygame.draw.rect(DISPLAYSURF, BROWN, (200, 290, 62, 88))
        holeArray2.append(hole23)
        hole24 = pygame.draw.rect(DISPLAYSURF, BROWN, (200, 385, 62, 88))
        holeArray2.append(hole24)

        hole31 = pygame.draw.rect(DISPLAYSURF, BROWN, (300, 100, 62, 88))
        holeArray3.append(hole31)
        hole32 = pygame.draw.rect(DISPLAYSURF, BROWN, (300, 195, 62, 88))
        holeArray3.append(hole32)
        hole33 = pygame.draw.rect(DISPLAYSURF, BROWN, (300, 290, 62, 88))
        holeArray3.append(hole33)
        hole34 = pygame.draw.rect(DISPLAYSURF, BROWN, (300, 385, 62, 88))
        holeArray3.append(hole34)

        hole41 = pygame.draw.rect(DISPLAYSURF, BROWN, (400, 100, 62, 88))
        holeArray4.append(hole41)
        hole42 = pygame.draw.rect(DISPLAYSURF, BROWN, (400, 195, 62, 88))
        holeArray4.append(hole42)
        hole43 = pygame.draw.rect(DISPLAYSURF, BROWN, (400, 290, 62, 88))
        holeArray4.append(hole43)
        hole44 = pygame.draw.rect(DISPLAYSURF, BROWN, (400, 385, 62, 88))
        holeArray4.append(hole44)

        timeStep = (pygame.time.get_ticks() - start_ticks) / 1000
        # timeStep is the timer for determining when to move the dot; Might implement a decrementing factor later

        if gameOver is True:
            pygame.draw.rect(DISPLAYSURF, DARKGRAY, (0, 0, 640, 480))
            wrongChoiceText = "BAD CHOICE"
            gameOverText = "GAME OVER"
            theWrongChoiceText = BASICFONT.render(wrongChoiceText, True, YELLOW)
            theGameOverText = BASICFONT.render(gameOverText, True, YELLOW)
            DISPLAYSURF.blit(theWrongChoiceText, (300, 200))
            DISPLAYSURF.blit(theGameOverText, (300, 240))
            savedTime = 100000000

        if gameOverTime is True:
            pygame.draw.rect(DISPLAYSURF, DARKGRAY, (0, 0, 640, 480))
            timeUpText = "TIME'S UP"
            finalScoreText = "YOUR FINAL SCORE:"
            scoreText = str(scoreNum)
            theTimeUpText = BASICFONT.render(timeUpText, True, YELLOW)
            theFinalScoreText = BASICFONT.render(finalScoreText, True, YELLOW)
            theScoreText = BASICFONT.render(scoreText, True, YELLOW)
            DISPLAYSURF.blit(theTimeUpText, (300, 200))
            DISPLAYSURF.blit(theFinalScoreText, (300, 240))
            DISPLAYSURF.blit(theScoreText, (580, 300))
            savedTime = 100000000

        # Setup for card displayed on board
        cardLocation = pygame.draw.rect(DISPLAYSURF, WHITE, (100 + (randX * 100), 100 + (randY * 95), 62, 88))
        cardSpriteGroup = Group(current_card)
        cardSpriteGroup.draw(DISPLAYSURF)
        if int(timeStep - savedTime) == 3:
            savedTime = timeStep
            cardTypeTemp = random.randint(0, 3)
            if cardTypeTemp == 0:
                faceCardOnly = True
                numberCardOnly = False
                evenCardOnly = False
                oddCardOnly = False
            elif cardTypeTemp == 1:
                faceCardOnly = False
                numberCardOnly = True
                evenCardOnly = False
                oddCardOnly = False
            elif cardTypeTemp == 2:
                faceCardOnly = False
                numberCardOnly = False
                evenCardOnly = True
                oddCardOnly = False
            elif cardTypeTemp == 3:
                faceCardOnly = False
                numberCardOnly = False
                evenCardOnly = False
                oddCardOnly = True

            temp = random.randint(1, 14)
            randX = random.randint(0, 3)
            randY = random.randint(0, 3)

            if temp == 1:
                current_card = Ace(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = False
                isNumberCard = True
                isEvenCard = False
                isOddCard = True
            elif temp == 2:
                current_card = Two(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = False
                isNumberCard = True
                isEvenCard = True
                isOddCard = False
            elif temp == 3:
                current_card = Three(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = False
                isNumberCard = True
                isEvenCard = False
                isOddCard = True
            elif temp == 4:
                current_card = Four(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = False
                isNumberCard = True
                isEvenCard = True
                isOddCard = False
            elif temp == 5:
                current_card = Five(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = False
                isNumberCard = True
                isEvenCard = False
                isOddCard = True
            elif temp == 6:
                current_card = Six(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = False
                isNumberCard = True
                isEvenCard = True
                isOddCard = False
            elif temp == 7:
                current_card = Seven(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = False
                isNumberCard = True
                isEvenCard = False
                isOddCard = True
            elif temp == 8:
                current_card = Eight(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = False
                isNumberCard = True
                isEvenCard = True
                isOddCard = False
            elif temp == 9:
                current_card = Nine(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = False
                isNumberCard = True
                isEvenCard = False
                isOddCard = True
            elif temp == 10:
                current_card = Ten(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = False
                isNumberCard = True
                isEvenCard = True
                isOddCard = False
            elif temp == 11:
                current_card = Jack(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = True
                isNumberCard = False
                isEvenCard = False
                isOddCard = False
            elif temp == 12:
                current_card = Queen(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = True
                isNumberCard = False
                isEvenCard = False
                isOddCard = False
            elif temp == 13:
                current_card = King(100 + (randX * 100), 100 + (randY * 95))
                isFaceCard = True
                isNumberCard = False
                isEvenCard = False
                isOddCard = False

        # handle events
        for event in pygame.event.get():

            mousePos = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0] and cardLocation.collidepoint(pygame.mouse.get_pos()):
                if isFaceCard is True and faceCardOnly is True:
                    print("You have hit THE object!")
                    addPoints()
                    cardLocation = pygame.draw.rect(DISPLAYSURF, BROWN,
                                                    (100 + (randX * 100), 100 + (randY * 95), 62, 88))
                    cardSpriteGroup.draw(DISPLAYSURF)
                    temp = random.randint(1, 14)
                    randX = random.randint(0, 3)
                    randY = random.randint(0, 3)

                    if temp == 1:
                        current_card = Ace(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 2:
                        current_card = Two(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 3:
                        current_card = Three(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 4:
                        current_card = Four(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 5:
                        current_card = Five(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 6:
                        current_card = Six(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 7:
                        current_card = Seven(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 8:
                        current_card = Eight(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 9:
                        current_card = Nine(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 10:
                        current_card = Ten(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 11:
                        current_card = Jack(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False
                    elif temp == 12:
                        current_card = Queen(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False
                    elif temp == 13:
                        current_card = King(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False

                elif isNumberCard is True and numberCardOnly is True:
                    print("You have hit THE object!")
                    addPoints()
                    cardLocation = pygame.draw.rect(DISPLAYSURF, BROWN,
                                                    (100 + (randX * 100), 100 + (randY * 95), 62, 88))
                    cardSpriteGroup.draw(DISPLAYSURF)

                    temp = random.randint(1, 14)
                    randX = random.randint(0, 3)
                    randY = random.randint(0, 3)

                    if temp == 1:
                        current_card = Ace(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 2:
                        current_card = Two(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 3:
                        current_card = Three(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 4:
                        current_card = Four(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 5:
                        current_card = Five(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 6:
                        current_card = Six(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 7:
                        current_card = Seven(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 8:
                        current_card = Eight(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 9:
                        current_card = Nine(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 10:
                        current_card = Ten(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 11:
                        current_card = Jack(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False
                    elif temp == 12:
                        current_card = Queen(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False
                    elif temp == 13:
                        current_card = King(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False

                elif isEvenCard is True and evenCardOnly is True:
                    print("You have hit THE object!")
                    addPoints()
                    cardLocation = pygame.draw.rect(DISPLAYSURF, BROWN,
                                                    (100 + (randX * 100), 100 + (randY * 95), 62, 88))
                    cardSpriteGroup.draw(DISPLAYSURF)

                    temp = random.randint(1, 14)
                    randX = random.randint(0, 3)
                    randY = random.randint(0, 3)

                    if temp == 1:
                        current_card = Ace(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 2:
                        current_card = Two(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 3:
                        current_card = Three(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 4:
                        current_card = Four(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 5:
                        current_card = Five(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 6:
                        current_card = Six(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 7:
                        current_card = Seven(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 8:
                        current_card = Eight(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 9:
                        current_card = Nine(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 10:
                        current_card = Ten(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 11:
                        current_card = Jack(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False
                    elif temp == 12:
                        current_card = Queen(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False
                    elif temp == 13:
                        current_card = King(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False

                elif isOddCard is True and oddCardOnly is True:
                    print("You have hit THE object!")
                    addPoints()
                    cardLocation = pygame.draw.rect(DISPLAYSURF, BROWN,
                                                    (100 + (randX * 100), 100 + (randY * 95), 62, 88))
                    cardSpriteGroup.draw(DISPLAYSURF)

                    temp = random.randint(1, 14)
                    randX = random.randint(0, 3)
                    randY = random.randint(0, 3)

                    if temp == 1:
                        current_card = Ace(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 2:
                        current_card = Two(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 3:
                        current_card = Three(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 4:
                        current_card = Four(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 5:
                        current_card = Five(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 6:
                        current_card = Six(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 7:
                        current_card = Seven(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 8:
                        current_card = Eight(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 9:
                        current_card = Nine(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = False
                        isOddCard = True
                    elif temp == 10:
                        current_card = Ten(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = False
                        isNumberCard = True
                        isEvenCard = True
                        isOddCard = False
                    elif temp == 11:
                        current_card = Jack(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False
                    elif temp == 12:
                        current_card = Queen(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False
                    elif temp == 13:
                        current_card = King(100 + (randX * 100), 100 + (randY * 95))
                        isFaceCard = True
                        isNumberCard = False
                        isEvenCard = False
                        isOddCard = False
                else:
                    gameOver = True

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()

        # It should be triggered either by the passing of a certain amount of time (which removes points too),
        # Or  by clicking on the correct tile

        pygame.display.update()
        clock.tick(100)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
    sys.exit()
