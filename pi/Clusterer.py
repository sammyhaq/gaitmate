from sklearn.cluster import KMeans
from sklearn import svm
import numpy as np
import LoadFileHelper
import os
import sys


class Clusterer:

    def __init__(self, filenames):
        self.X = []

        for i in range(len(filenames)):
            loader = LoadFileHelper.LoadFileHelper(filenames[i])

            # Checking to see if file was incorrectly saved, before parsing.
            # Prevents blank files from being parsed and ruining clustering.
            if (loader.isBlank()):
                continue
            else:
                loader.parseData()  # parsing data

            self.X.append([loader.getDataVariance_X(),
                           loader.getDataVariance_Y(),
                           loader.getDataVariance_Z()])

    def doKMeansCluster(self):
        return KMeans(n_clusters=3, random_state=0).fit(np.array(self.X))

    def trainSVC(self):
        self.Y = ["Standing", "Sitting", "Shuffling"]

        self.clf = svm.SVC()
        self.clf.fit(self.X, self.Y)

    def predictSVC(self, feature):
        return str(self.clf.predict(feature).item(0))


def execute():

    print("\n####################################")
    print("# Cluster Tester for Gaitmate Data #")
    print("# Code by Sammy Haq                #")
    print("# https://github.com/sammyhaq      #")
    print("####################################\n")

    runSVC = False
    runKMeans = False

    if (len(sys.argv) == 1):
        runSVC = True
        runKMeans = True
    if ("SVC" in sys.argv):
        runSVC = True
    if ("KMeans" in sys.argv):
        runKMeans = True

    print("\n\t************************")
    print("\t* Command Line Options *")
    print("\t************************\n")
    if (runSVC):
        print("\t\tSVC Test: ENABLED")
    else:
        print("\t\tSVC Test: DISABLED")
    if (runKMeans):
        print("\t\tKMeans Test: ENABLED")
    else:
        print("\t\tKMeans Test: DISABLED")

    print("\n####################")
    print("# Gathering files: #")
    print("####################\n")

    print("\tpulling from 'logs/trainData/walkingData..'")
    walkingFileList = os.listdir("logs/trainData/walkingData")
    print("\t\t"+str(len(walkingFileList))+" data points found.")
    print("\t\t..done.")

    print("\tpulling from 'logs/trainData/standingData..'")
    standingFileList = os.listdir("logs/trainData/standingData")
    print("\t\t"+str(len(standingFileList))+" data points found.")
    print("\t\t..done.")

    print("\tpulling from 'logs/trainData/shufflingData..'")
    shufflingFileList = os.listdir("logs/trainData/shufflingData")
    print("\t\t"+str(len(shufflingFileList))+" data points found.")
    print("\t\t..done.")

    print("\t..done.")

    fileList = []
    print("\n###################################")
    print("# Appending file lists together.. #")
    print("###################################\n")
    for i in range(len(walkingFileList)):
        fileList.append("logs/trainData/walkingData/" + walkingFileList[i])
    for i in range(len(standingFileList)):
        fileList.append("logs/trainData/standingData/" + standingFileList[i])
    for i in range(len(shufflingFileList)):
        fileList.append("logs/trainData/shufflingData/" + shufflingFileList[i])
    print("\t..done.\n")

    print("Total amount of data points: " + str(len(fileList)) + "\n")

    print("\n###########################")
    print("# Attempting to cluster.. #")
    print("###########################\n")
    clusterer = Clusterer(fileList)
    print("\t..done.\n")

    if (runKMeans):

        print("\n############################")
        print("# Printing KMeans Results: #")
        print("############################\n")

        print("\n\t************************")
        print("\t* Walking Data labels: *")
        print("\t************************\n")
        print("\t\tData#\tFilename\tLabel")
        print("\t\t-----------------------------")
        for i in range(len(walkingFileList)):
            print("\t\t" + str(i+1) + "\t" +
                  walkingFileList[i] + "\t" +
                  str(clusterer.doKMeansCluster().labels_[i]))

        print("\n\t*************************")
        print("\t* Standing Data labels: *")
        print("\t*************************\n")
        print("\t\tData#\tFilename\tLabel")
        print("\t\t-----------------------------")
        for i in range(len(standingFileList)):
            print("\t\t" + str(i+1) + "\t" +
                  standingFileList[i] + "\t" +
                  str(clusterer.doKMeansCluster().labels_[i +
                      len(walkingFileList)]))

        print("\n\t**************************")
        print("\t* Shuffling Data labels: *")
        print("\t**************************\n")
        print("\t\tData#\tFilename\tLabel")
        print("\t\t-----------------------------")
        for i in range(len(shufflingFileList)):
            print("\t\t" + str(i+1) + "\t" +
                  shufflingFileList[i] + "\t" +
                  str(clusterer.doKMeansCluster().labels_[i +
                      len(walkingFileList) +
                      len(shufflingFileList) - 1]))

    if (runSVC): 
        print("\n#########################")
        print("# Printing SVC Results: #")
        print("#########################\n")
        
        clusterer.trainSVC()

        walkingTestFileList = os.listdir("logs/testData/walkingData")
        standingTestFileList = os.listdir("logs/testData/standingData")
        shufflingTestFileList = os.listdir("logs/testData/shufflingData")

        walkingTestData = []
        for file in range(len(walkingTestFileList)):
            loader = LoadFileHelper.LoadFileHelper(
                    "logs/testData/walkingData/"+walkingTestFileList[i])

            # Checking to see if file was incorrectly saved, before parsing.
            # Prevents blank files from being parsed and ruining clustering.
            if (loader.isBlank()):
                continue
            else:
                loader.parseData()  # parsing data

            walkingTestData.append([loader.getDataVariance_X(),
                                    loader.getDataVariance_Y(),
                                    loader.getDataVariance_Z()])

        standingTestData = []
        for file in range(len(standingTestFileList)):
            loader = LoadFileHelper.LoadFileHelper(
                    "logs/testData/standingData/"+standingTestFileList[i])

            if (loader.isBlank()):
                continue
            else:
                loader.parseData()  # parsing data

            standingTestData.append([loader.getDataVariance_X(),
                                     loader.getDataVariance_Y(),
                                     loader.getDataVariance_Z()])

        shufflingTestData = []
        for file in range(len(shufflingTestFileList)):
            loader = LoadFileHelper.LoadFileHelper(
                    "logs/testData/shufflingData/"+shufflingTestFileList[i])

            if (loader.isBlank()):
                continue
            else:
                loader.parseData()  # parsing data

            standingTestData.append([loader.getDataVariance_X(),
                                     loader.getDataVariance_Y(),
                                     loader.getDataVariance_Z()])

        print("\n\t*****************************")
        print("\t* Walking Test Data Results *")
        print("\t*****************************\n")
        print("\t\tData#\tFilename\tLabel")
        print("\t\t-----------------------------")
        for i in range(len(walkingTestFileList)):
            print("\t\t" + str(i+1) + "\t" +
                  walkingTestFileList[i] + "\t" +
                  str(clusterer.predictSVC(walkingTestData[i])))

        print("\n\t******************************")
        print("\t* Standing Test Data Results *")
        print("\t******************************\n")
        print("\t\tData#\tFilename\tLabel")
        print("\t\t-----------------------------")
        for i in range(len(standingTestFileList)):
            print("\t\t" + str(i+1) + "\t" +
                  standingTestFileList[i] + "\t" +
                  str(clusterer.predictSVC(standingTestData[i])))

        print("\n\t*******************************")
        print("\t* Shuffling Test Data Results *")
        print("\t*******************************\n")
        print("\t\tData#\tFilename\tLabel")
        print("\t\t-----------------------------")
        for i in range(len(shufflingTestFileList)):
            print("\t\t" + str(i+1) + "\t" +
                  shufflingTestFileList[i] + "\t" +
                  str(clusterer.predictSVC(standingTestData[i])))


execute()
