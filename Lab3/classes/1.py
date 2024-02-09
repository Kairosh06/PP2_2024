class StringManipulator:
    def __init__(self):
        self.user_string = ""

    def getString(self):
        """
        Gets a string from console input and stores it in the class.
        """
        self.user_string = input("Enter a string: ")

    def printString(self):
        """
        Prints the stored string in upper case.
        """
        print("Uppercase String:", self.user_string.upper())