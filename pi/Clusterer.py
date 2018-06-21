from sklearn.cluster import KMeans
import numpy as np
import LoadFileHelper
import os


class Clusterer:

    def __init__(self, filenames):
        self.rawVariance = []

        for i in range(len(filenames)):
            loader = LoadFileHelper.LoadFileHelper(filenames[i])

            # Checking to see if file was incorrectly saved, before parsing.
            # Prevents blank files from being parsed and ruining clustering.
            if (loader.isBlank()):
                continue
            else:
                loader.parseData()  # parsing data

            self.rawVariance.append([loader.getDataVariance_X(),
                                     loader.getDataVariance_Y(),
                                     loader.getDataVariance_Z()])

        self.results = KMeans(n_clusters=3,
                              random_state=0).fit(np.array(self.rawVariance))


def ClusterInterface():
    print("\n####################")
    print("# Gathering files: #")
    print("####################\n")

    print("\tpulling from 'logs/walkingData..'")
    walkingFileList = os.listdir("logs/walkingData")
    print("\t\t"+str(len(walkingFileList))+" data points found.")
    print("\t\t..done.")

    print("\tpulling from 'logs/standingData..'")
    standingFileList = os.listdir("logs/standingData")
    print("\t\t"+str(len(standingFileList))+" data points found.")
    print("\t\t..done.")

    print("\tpulling from 'logs/shufflingData..'")
    shufflingFileList = os.listdir("logs/shufflingData")
    print("\t\t"+str(len(shufflingFileList))+" data points found.")
    print("\t\t..done.")

    print("\t..done.")

    fileList = []
    print("\n###################################")
    print("# Appending file lists together.. #")
    print("###################################\n")
    for i in range(len(walkingFileList)):
        fileList.append("logs/walkingData/" + walkingFileList[i])
    for i in range(len(standingFileList)):
        fileList.append("logs/standingData/" + standingFileList[i])
    for i in range(len(shufflingFileList)):
        fileList.append("logs/shufflingData/" + shufflingFileList[i])
    print("\t..done.\n")

    print("Total amount of data points: " + str(len(fileList)) + "\n")

    print("\n###########################")
    print("# Attempting to cluster.. #")
    print("###########################\n")
    clusterer = Clusterer(fileList)
    print("\t..done.\n")

    print("\n#####################")
    print("# Printing results: #")
    print("#####################\n")

    print("\n\t************************")
    print("\t* Walking Data labels: *")
    print("\t************************\n")
    print("\t\tData#\tFilename\tLabel")
    print("\t\t-----------------------------")
    for i in range(len(walkingFileList)):
        print("\t\t" + str(i+1) + "\t" +
              walkingFileList[i] + "\t" +
              str(clusterer.results.labels_[i]))

    print("\n\t*************************")
    print("\t* Standing Data labels: *")
    print("\t*************************\n")
    print("\t\tData#\tFilename\tLabel")
    print("\t\t-----------------------------")
    for i in range(len(standingFileList)):
        print("\t\t" + str(i+1) + "\t" +
              standingFileList[i] + "\t" +
              str(clusterer.results.labels_[i + len(walkingFileList)]))

    print("\n\t**************************")
    print("\t* Shuffling Data labels: *")
    print("\t**************************\n")
    print("\t\tData#\tFilename\tLabel")
    print("\t\t-----------------------------")
    for i in range(len(shufflingFileList)):
        print("\t\t" + str(i+1) + "\t" +
              shufflingFileList[i] + "\t" +
              str(clusterer.results.labels_[i + len(walkingFileList) +
                  len(shufflingFileList) - 1]))


ClusterInterface()


