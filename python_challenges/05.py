class InputOutputString:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


str_obj = InputOutputString()
str_obj.getString()
str_obj.printString()
