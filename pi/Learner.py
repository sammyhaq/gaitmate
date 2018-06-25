from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import LoadFileHelper
import matplotlib.pyplot as plt
import os


class Learner:

    def __init__(self):
        self.X = []  # samples
        self.Y = []  # labels
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        self.y_pred = None
        self.clf = None

    def checkDataIntegrity(self, filename):
        foundBlankFiles = False

        loader = LoadFileHelper.LoadFileHelper(filename)
        if (loader.isBlank()):
            foundBlankFiles = True

            print("\t'" + filename + "' found to be blank/corrupted!")
            print("\t\tmoving to " + "'logs/blank" + filename + "'..")
            os.rename(filename, "logs/blank" + filename)
            print("\t\t\t..done.\n")

        if (foundBlankFiles):
            print("\tFound corrupted file, moved offender to" +
                  " 'logs/blanklogs/'\n")
            return False

        else:
            return True

    def addSample(self, filepath, label):
        if (self.checkDataIntegrity(filepath)):
            loader = LoadFileHelper.LoadFileHelper(filepath)
            loader.parseData()
            self.X.append([loader.getDataVariance_X(),
                           loader.getDataVariance_Y(),
                           loader.getDataVariance_Z()])
            self.Y.append(label)
            return True
        else:
            return False

    def addSampleFolder(self, folderpath, label):
        print("\tPulling from "+folderpath+"..")
        fileList = os.listdir(folderpath)
        print("\t\t"+str(len(fileList))+" data points found.")
        print("\t\t..done.")

        print("\tAdding data found in " + folderpath + " to dataset as " +
              label + " data..")
        for i in range(len(fileList)):
            self.addSample(folderpath+fileList[i], label)
        print("\t\t..done.")

    def doDecisionTree(self, splitSize):
        [self.x_train,
         self.x_test,
         self.y_train,
         self.y_test] = train_test_split(self.X, self.Y, test_size=splitSize)

        self.clf = DecisionTreeClassifier()
        self.clf.fit(self.x_train, self.y_train)

        self.y_pred = self.clf.predict(self.x_test)

    def showResults(self):
        print(confusion_matrix(self.y_test, self.y_pred))
        print(classification_report(self.y_test, self.y_pred))


def main():
    learner = Learner()
    learner.addSampleFolder("logs/shufflingData/", "shuffling")
    learner.addSampleFolder("logs/standingData/", "standing")
    learner.addSampleFolder("logs/walkingData/", "walking")

    learner.doDecisionTree(0.10)
    learner.showResults()
main()
