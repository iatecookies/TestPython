import time

# TEST CLASS -------------------------------------------------------------------
# import menu
class Test ():
    def __init__ (self):
        self.framerate = 10
        self.status = 'b'

    def start (self):
        self.gameLoop()

    def game (self):
        self.framerate = 10
        print('Playing the game')

    def startMenu (self):
        self.framerate = 1
        menu = Menu('Start Menu')
        cont = menu.addButton('Continue game')

        if cont.setColor('ret'):
            print('Color changed')
        else:
            print('Color not changed')

        hs = menu.addButton('Highscores')
        quit = menu.addButton('Quit game')

        def aFunction ():
            self.status = 'b'

        cont.click(aFunction)

    def highscoreMenu (self):
        self.framerate = 1
        print('Highscore menu')



    def gameLoop (self):
        while True:
            # Timing van de framerate
            time.sleep(1 / self.framerate)
            # Speel het spel
            if self.status == 'a':
                self.game()
            # Het start menu
            elif self.status == 'b':
                self.startMenu()
            # Het highscore menu
            elif self.status == 'c':
                self.highscoreMenu()
            else:
                print("Something else...")

# MENU CLASS -------------------------------------------------------------------
# import button
class Menu ():
    def __init__ (self, title='No title'):
        self.title = title
        self.buttons = []

    def addButton (self, title):
        button = Button(title)
        self.buttons.append(button)
        return button



# BUTTON CLASS -----------------------------------------------------------------

class Button ():
    def __init__ (self, title):
        self.title = title
        self.color = 'green'
        self.colorsAllowed = ['red', 'green', 'blue']

    def click (self, callback=None):
        # Standard action might be logging the button click
        print('You pressed the button: \'' + self.title + '\'.')
        if callback != None:
            callback()

    def setColor (self, value):
        if value in self.colorsAllowed:
            self.color = value
            return True
        return False

    def getColor (self):
        return self.color




# TESTING ----------------------------------------------------------------------

game = Test()
#game.status = 'Dikke aap'
game.start()
