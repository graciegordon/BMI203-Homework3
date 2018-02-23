import sys
import pandas as pd
import matplotlib.pyplot as plt

def Calc_Rates(posPair, negPair):
    numPos=len(posPair)
    numNeg=len(negPair)
    numtot=numPos+numNeg

    allscores=[]
    onlyscores=[]
    for item in posPair:
        temp=('pos',item)
        allscores.append(temp)
        onlyscores.append(item)

    for it in negPair:
        temp=('neg',it)
        allscores.append(temp)
        onlyscores.append(it)

    allscores=sorted(allscores,key=lambda x: x[1],reverse=True)

    rateTP=0.7
    pos_count=0
    neg_count=0
    thresh=0
    count=0
    iterate=0
    allpos=0
    tpr=[0.0]

    for tm in allscores:
        if pos_count < (rateTP*numPos):
            if tm[0]=='pos':
                pos_count+=1
                #if tm[0]>thresh:
                thresh=tm[1]
            count+=1
        if tm[0]=='pos':
                allpos+=1
        iterate+=1

        tpr.append(float(allpos)/iterate)
    
    allneg=0
    fpr=[0.0]
    for i in range(numtot):
        if i < count:
            if allscores[i][0]=='neg':
                neg_count+=1
        if allscores[i][0]=='neg':
            allneg+=1
        fpr.append(float(allneg)/numNeg)

    trueneg=0
    for i in range(count,len(allscores)):
        if allscores[i][0]=='neg':
            trueneg+=1
    
    FPrate=neg_count/float(numNeg)
    #FPrate=neg_count/float(neg_count+trueneg)
    print('false positive',FPrate)
    print('true positive',rateTP)
    return rateTP,FPrate,allscores

'''
###Calculate for all gap and extensions
path='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/scores/'
gaps=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]
extends=[-1,-2,-3,-4,-5]
posbase='scorePos'
negbase='scoreNeg'

for gap in gaps:
    for extend in extends:
        filepos=path+posbase+str(gap)+str(extend)+'.txt'
        
        with open(filepos,'r') as posPairs:
            pos=[]
            for line in posPairs:
                cur=line.split()
                pos.append(cur[0])

        fileneg=path+negbase+str(gap)+str(extend)+'.txt'
        with open(fileneg,'r') as negPairs:
            neg=[]
            for line in negPairs:
                cur=line.split()
                neg.append(cur[0])
    
        tpr,fpr,myscores=Calc_Rates(pos,neg)
        print("false positive rate", fpr, "gap", gap, "extend", extend)


'''
#simple comparison of two files
with open(sys.argv[1],'r') as posPairs:
    pos=[]
    for line in posPairs:
        cur=line.split()
        pos.append(cur[0])

with open(sys.argv[2],'r') as negPairs:
    neg=[]
    for line in negPairs:
        cur=line.split()
        neg.append(cur[0])

tpr,fpr,myscores=Calc_Rates(pos,neg)



