from sklearn.cluster import KMeans
import numpy as np
import LoadFileHelper
import os

class Clusterer:

    def __init__(self, filenames):
        self.rawVariance = [];

        for i in range(len(filenames)):
            l = LoadFileHelper.LoadFileHelper(filenames[i])
            
            # Checking to see if file was incorrectly saved, before parsing. Prevents blank files from being parsed and ruining clustering.
            if (l.isBlank()):
                continue
            else:
                l.parseData()  # parsing data

            self.rawVariance.append([l.getDataVariance_X(), l.getDataVariance_Y(), l.getDataVariance_Z()])
    
        self.results = KMeans(n_clusters=3, random_state=0).fit(np.array(self.rawVariance))

def main():
    print("Gathering files:")
    print("\tpulling from 'logs/walkingData..'")
    walkingFileList = os.listdir("logs/walkingData")
    print("\t\t..done.")
    print("\tpulling from 'logs/standingData..'")
    standingFileList = os.listdir("logs/standingData")
    print("\t\t..done.")
    print("\tpulling from 'logs/shufflingData..'")
    shufflingFileList = os.listdir("logs/shufflingData")
    print("\t\t..done.")
    print("\t..done.")

    fileList = []
    print("Appending file lists together..")
    for i in range(len(walkingFileList)):
        fileList.append("logs/walkingData/" + walkingFileList[i])
    for i in range(len(standingFileList)):
        fileList.append("logs/standingData/" + standingFileList[i])
    for i in range(len(shufflingFileList)):
        fileList.append("logs/shufflingData/" + shufflingFileList[i])
    print("\t..done.\n")

    for i in range(len(fileList)):
        print(fileList[i] + "\n")
    print("Amount of points: " + str(len(fileList)) + "\n")

    print("Attempting to cluster..")
    clusterer = Clusterer(fileList)
    print("\t..done.\n")

    print("Printing results:")
    print("\tWalking Data labels:")
    print("\t\t" + str(clusterer.results.labels_[:len(walkingFileList)]))
    print("\tStanding Data labels:")
    print("\t\t" + str(clusterer.results.labels_[len(walkingFileList):(len(standingFileList)+len(walkingFileList)-1)]))
    print("\tShuffling Data labels:")
    print("\t\t" + str(clusterer.results.labels_[len(standingFileList)+len(walkingFileList):]))

main()


