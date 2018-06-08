class SaveFileHelper():

    def __init__(self, filename):
        self.filename = filename;
        self.file = open(filename, "w");

    def writeToFile(self, line):
        self.file.write(line);

    def writeData(self, x, y, z ):
        self.writeToFile("%.3f,%.3f,%.3f\n" %(float(x), float(y), float(z)));

    def closeHelper(self):
        self.file.close();


