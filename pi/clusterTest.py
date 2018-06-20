from sklearn.cluster import KMeans
import numpy as np
import LoadFileHelper
import os

class Clusterer:

    def __init__(self, filenames):
        self.rawVariance = [];

        for i in range(len(filenames)):
            l = LoadFileHelper.LoadFileHelper(filenames[i])
            l.parseData()

            self.rawVariance.append([l.getDataVariance_X(), l.getDataVariance_Y(), l.getDataVariance_Z()])
    
        self.results = KMeans(n_clusters=2, random_state=0).fit(np.array(self.rawVariance))

def main():
    print("Gathering files:")
    print("  pulling from 'logs/walkingData..'")
    walkingFileList = os.listdir("logs/walkingData")
    print("    ..done.")
    print("  pulling from 'logs/standingData..'")
    standingFileList = os.listdir("logs/standingData")
    print("    ..done.")
    print("  ..done.\n")

    fileList = []
    print("Appending file lists together..")
    for i in range(len(walkingFileList)):
        fileList.append("logs/walkingData/" + walkingFileList[i])
    for i in range(len(standingFileList)):
        fileList.append("logs/standingData/" + standingFileList[i])
    print("  ..done.\n")

    for i in range(len(fileList)):
        print(fileList[i] + "\n")

    print("Attempting to cluster..")
    clusterer = Clusterer(fileList)
    print(" ..done.\n")

    print("Printing results:")
    print(clusterer.results.labels_)

main()


