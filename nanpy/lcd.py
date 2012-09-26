from nanpy.arduinoboard import ArduinoObject

class Lcd(ArduinoObject):

    def __init__(self, pins, begin):
        ArduinoObject.__init__(self, "Lcd")
        self.call('new', pins, begin)
        self.id = self.return_value()

    def printString(self, value):
        self.call('print', value)
        return self.return_value()

    def setCursor(self, col, row):
        self.call('setCursor', col, row)
        return self.return_value()
