import matplotlib.pyplot as plt
import string
import sys

def GetRates(actives, scores):

    tpr = [0.0]  # true positive rate
    fpr = [0.0]  # false positive rate
    nractives = len(actives)
    nrdecoys = len(scores) - len(actives)

    foundactives = 0.0
    founddecoys = 0.0
    for idx, (id, score) in enumerate(scores):
        if id in actives:
            foundactives += 1.0
        else:
            founddecoys += 1.0

        tpr.append(foundactives / float(nractives))
        fpr.append(founddecoys / float(nrdecoys))

    return tpr, fpr

def DepictROCCurve(actives, scores, label, color, fname, randomline):

    plt.figure(figsize=(4, 4), dpi=80)

    SetupROCCurvePlot(plt)
    AddROCCurve(plt, actives, scores, color, label)
    SaveROCCurvePlot(plt, fname, randomline)

def SetupROCCurvePlot(plt):

    plt.xlabel("FPR", fontsize=14)
    plt.ylabel("TPR", fontsize=14)
    plt.title("MATIO Optimized", fontsize=14)

def AddROCCurve(plt, actives, scores, color, label):

    tpr, fpr = GetRates(actives, scores)

    plt.plot(fpr, tpr, color=color, linewidth=2, label=label)

def SaveROCCurvePlot(plt, fname, randomline=True):

    if randomline:
        x = [0.0, 1.0]
        plt.plot(x, x, linestyle='dashed', color='red', linewidth=2, label='random')

    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.legend(fontsize=10, loc='best')
    plt.tight_layout()
    plt.savefig(fname)

def Create_IDs(pos,neg):
    poslen=len(pos)
    neglen=len(neg)
    letters=list(string.ascii_lowercase)
    letters.extend([i+b for i in letters for b in letters])
    #print(letters)
    posID=letters[:poslen]
    negID=letters[poslen:poslen+neglen]
    scores=[]
    for i in range(poslen):
        scores.append((posID[i],pos[i]))
    for i in range(neglen):
        scores.append((negID[i],neg[i]))

    scores=sorted(scores,key=lambda x: x[1],reverse=True)
    return scores,posID

def Normalize_Score_Len(rawscore,alignlist):
    
    path='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/'
    with open(alignlist,'r') as posPairs:
        seqA=''
        seqB=''
        lenPosPairs=[]
        for line in posPairs:
            cur=line.split()
            with open(path+cur[0],'r') as seq1:
                for a in seq1:
                    a=a.strip()
                    if a[0]!='>':
                        seqA=seqA+a
            with open(path+cur[1],'r') as seq2:
                for b in seq2:
                    b=b.strip()
                    if b[0]!='>':
                        seqB=seqB+b

            if len(seqB)>len(seqA):
                lenPosPairs.append(len(seqA))
            else:
                lenPosPairs.append(len(seqB))
    #print('length',lenPosPairs)
    normalizedscore=[]
    for s, l in zip(rawscore,lenPosPairs):
        #print(s,l)
        normalizedscore.append(float(s)/l)

    return normalizedscore

#negscores,negID=Create_IDs(rawnegscores)
#scores=posscores+negscores
#rawscores=[80,70,40,60,77,65,76,88,99,33,31,22,11,2,1,9,5,14,23,23]
#rawposscores=[60,77,65,76,88,99,33,31,22,11]
#rawnegscores=[80,70,40,2,1,9,5,14,23,23]
with open(sys.argv[1],'r') as posPairs:
    rawpos=[]
    for line in posPairs:
        cur=line.split()
        rawpos.append(cur[0])

with open(sys.argv[2],'r') as negPairs:
    rawneg=[]
    for line in negPairs:
        cur=line.split()
        rawneg.append(cur[0])
posAlPath='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/Pospairs.txt'
negAlPath='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/Negpairs.txt'

#print(rawpos)

#print(rawneg)

#uncomment below to normalize
'''
npos=Normalize_Score_Len(rawpos,posAlPath)
nneg=Normalize_Score_Len(rawneg,negAlPath)
scores,posID=Create_IDs(npos,nneg)
'''
scores,posID=Create_IDs(rawpos,rawneg)


#scores=sorted(scores,key=lambda x: x[1],reverse=True)
#print(scores)
#print(posID)



DepictROCCurve(posID,scores,'alignment','b','roc.png',True)

