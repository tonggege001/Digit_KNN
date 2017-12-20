from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt



def classify0(intX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(intX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDisIndex = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDisIndex[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def main():
    dataSet ,labels = createDataSet()
    print(classify0([3,3],dataSet,labels,3))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataSet[:,0],dataSet[:,1])
    plt.show()



if __name__ == '__main__':
  main()


