#encode = utf-8
from os import listdir

from numpy import *
import operator

def image2vector(filename):
    returnVec = zeros((1,900))
    fr = open(filename,'r')
    for i in range(30):
        lineStr = fr.readline()
        for j in range(30):
            returnVec[0,30*i+j] = int(lineStr[j])
    return returnVec


def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    difMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = difMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]



def handWritingClassTest():
    hwLable = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,900))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLable.append(classNumStr)
        trainingMat[i,:] = image2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = image2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest,trainingMat,hwLable,5)
        print('the Classifier came back with : %d,the real answer is :%d'%(classifierResult,classNumStr))
        if(classNumStr!=classifierResult) : errorCount += 0.1
    print('\n the total number of errors is : %d'% errorCount)
    print('the total error rate is : %f'%(errorCount/float(mTest)))

if __name__ == '__main__':
    handWritingClassTest()
