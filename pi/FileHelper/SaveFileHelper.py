"""
SaveFileHelper.py
Code by Sammy Haq
https://github.com/sammyhaq

Class for saving x,y,z data from a .csv-like file.
The functionality of this program is shown in saveFileTester.py

"""


class SaveFileHelper():

    # Constructor
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "w")
        self.buffer = []

    # Writes a line to the file.
    def writeToFile(self, line):
        self.file.write(line)

    # Writes given float variables to the line.
    def writeData(self, x, y, z):
        self.writeToFile("%.3f,%.3f,%.3f\n" % (float(x), float(y), float(z)))

    # appends the data to write to the file to a buffer (list).
    def appendToBuffer(self, x, y, z):
        self.buffer.append("%.3f,%.3f,%.3f\n" % (float(x), float(y), float(z)))

    # Dumps all data stored in the buffer to the file.
    def dumpBuffer(self):
        for item in self.buffer:
            self.writeToFile(item)

        self.buffer = []  # resetting buffer after dump

    # Good practice to close the writer after one is done with it.
    def closeWriter(self):
        self.file.close()

    def isClosed(self):
        return self.file.closed
