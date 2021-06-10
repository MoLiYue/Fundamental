# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
import jieba

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print(__doc__)

    temString = 'the dalian univercity of technology'
    print(temString.title())
    print(temString[0:-1])
    print(temString[0:])
    print(temString * 2)
    print(hex(44)+hex(20))
    print(eval("2+3"))
    print(jieba.lcut("中国是⼀个伟⼤的国家"))

while 1:
    try:
        num = eval(input("请输入整数："))
        if isinstance(num, int):
            break
    except:
        print("请输入整数")
    else:
        break

a = 3
name_saved = "hyl"
password_saved = "123"
while a:
    name = input("用户名：")
    password = input("密码：")
    if (name == name_saved and password == password_saved):
        break
    else:
        print("用户名或密码错误")
    a -= 1


"""

#--------------------------------------------------------------------------------------
from math import log
import operator
import sys
for i in range(len(sys.path)):
    print(sys.path[i])
def calcShannonEnt(dataSet):  # 计算数据的熵(entropy)
    numEntries=len(dataSet)  # 数据条数
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1] # 每行数据的最后一个字（类别）
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1  # 统计有多少个类以及每个类的数量
    shannonEnt=0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries # 计算单个类的熵值
        shannonEnt-=prob*log(prob,2) # 累加每个类的熵值
    return shannonEnt

def createDataSet1():    # 创造示例数据
    dataSet =[["不均匀","中等","分明","清亮","普通猫"],
     ["不均匀","中等","分明","中等","普通猫"],
     ["不均匀","中等","分明","不清亮","普通猫"],
     ["不均匀","中等","不分明","中等","普通猫"],
     ["不均匀","中等","不分明","清亮","普通猫"],
     ["不均匀","中等","不分明","不清亮","普通猫"],

     ["不均匀","优良","不分明","不清亮","普通猫"],
     ["不均匀","优良","不分明","中等","普通猫"],
     ["不均匀","优良","不分明","清亮","普通猫"],
     ["不均匀","优良","分明","清亮","普通猫"],
     ["不均匀","优良","分明","中等","普通猫"],
     ["不均匀","优良","分明","不清亮","普通猫"],

     ["不均匀","劣质","不分明","不清亮","普通猫"],
     ["不均匀","劣质","不分明","中等","普通猫"],
     ["不均匀","劣质","不分明","清亮","普通猫"],
     ["不均匀","劣质","分明","清亮","普通猫"],
     ["不均匀","劣质","分明","中等","普通猫"],
     ["不均匀","劣质","分明","不清亮","普通猫"],

     ["均匀","中等","分明","清亮","良种猫"],
     ["均匀","中等","分明","中等","良种猫"],
     ["均匀","中等","分明","不清亮","普通猫"],
     ["均匀","中等","不分明","中等","普通猫"],
     ["均匀","中等","不分明","清亮","良种猫"],
     ["均匀","中等","不分明","不清亮","普通猫"],

     ["均匀","优良","不分明","不清亮","良种猫"],
     ["均匀","优良","不分明","中等","良种猫"],
     ["均匀","优良","不分明","清亮","良种猫"],
     ["均匀","优良","分明","清亮","良种猫"],
     ["均匀","优良","分明","中等","良种猫"],
     ["均匀","优良","分明","不清亮","良种猫"],

     ["均匀","劣质","不分明","不清亮","普通猫"],
     ["均匀","劣质","不分明","中等","普通猫"],
     ["均匀","劣质","不分明","清亮","普通猫"],
     ["均匀","劣质","分明","清亮","普通猫"],
     ["均匀","劣质","分明","中等","普通猫"],
     ["均匀","劣质","分明","不清亮","普通猫"],

     ["中等","劣质","分明","中等","良种猫"],
     ["中等","劣质","分明","清亮","良种猫"],
     ["中等","劣质","不分明","不清亮","普通猫"]

     ]
    labels = ["色泽","毛发质地","瞳色","声音"]  #两个特征
    return dataSet,labels

def splitDataSet(dataSet,axis,value): # 按某个特征分类后的数据
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec =featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):  # 选择最优的分类特征
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)  # 原始的熵
    bestInfoGain = 0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob =len(subDataSet)/float(len(dataSet))
            newEntropy +=prob*calcShannonEnt(subDataSet)  # 按特征分类后的熵
        infoGain = baseEntropy - newEntropy  # 原始熵与按特征分类后的熵的差值
        if (infoGain>bestInfoGain):   # 若按某特征划分后，熵值减少的最大，则次特征为最优分类特征
            bestInfoGain=infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):    #按分类后类别数量排序，比如：最后分类为2男1女，则判定为男；
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    print(sortedClassCount[0][0],"/n")
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]  # 类别：男或女
    if classList.count(classList[0])==len(classList):
        print("2")
        return classList[0]
    if len(dataSet[0])==1:
        print("1")
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet) #选择最优特征
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}} #分类结果以字典形式保存
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet\
                            (dataSet,bestFeat,value),subLabels)
    return myTree


if __name__=='__main__':
    dataSet, labels=createDataSet1()  # 创造示列数据
    print(createTree(dataSet, labels))  # 输出决策树模型结果
