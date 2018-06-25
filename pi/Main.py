from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
from sklearn.metrics import classification_report, confusion_matrix
import Gaitmate
import Learner
import State
import sys
import os
import time
import SaveFileHelper
import LoadFileHelper


def main():
    controller = Gaitmate.Gaitmate(0x68, 17, 27, 6, 5, 25)
    controller.execute()
