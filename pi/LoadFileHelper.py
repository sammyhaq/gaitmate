class LoadFileHelper():

    def __init__(self, filename):
        self.filename = filename;
        self.file = open(filename, "r"); 
        self.x = [];
        self.y = [];
        self.z = [];


    def returnRawFile(self):
        return self.file.read

    def parseData(self):
        for line in self.file.readlines():
            parsedLine = line.split(",");

            print(parsedLine[0]);
            
            self.x.append(float(parsedLine[0]));
            self.y.append(float(parsedLine[1]));
            self.z.append(float(parsedLine[2]));

    def getData_X(self):
        return self.x;

    def getData_Y(self):
        return self.y;

    def getData_Z(self):
        return self.z;

    def getData(self):
        data = [];
        data.append(self.x);
        data.append(self.y);
        data.append(self.z);

        return data;
