##This code will perform a Smith-Waterman (local) alignment
import numpy as np
import pandas as pd
import sys

def make_matrix(sizeX,sizeY):
    #create matrix filled with zeros 
    #np.zeros(sizeX,sizeY)
    return np.zeros((sizeY,sizeX))
    #return [[0]]*sizeB for i in xrange(sizeA)]

def get_score(seqB,seqA,i,j,label,matrix):
    #get letter of current position in both strings
    #converted back to 0 numbering
    curCharA=seqA[j-1]
    curCharB=seqB[i-1]
    
    #get score between two characters
    posA=label[curCharA]
    posB=label[curCharB]

    
    score=matrix[posA][posB]
    #print(seqA,seqB,i,j)
    #print(curCharA,curCharB)
    #print('score',score)
    return score

def local_align(seqA, seqB, scoring_matrix, labels, gapscore):
    
    #print('test score')
    #print(scoring_matrix)

    #initialize matrix
    H=make_matrix(len(seqA)+1,len(seqB)+1)
    #print('H')
    #print(H) 
    best=0
    bestloc=(0,0)

    # fill in H in the right order
    for i in range(1, len(seqB)):
        for j in range(1,len(seqA)):
            #print('idx A,B:',i,j)
            
            #define local alignment recurrance rule
            matchscore=get_score(seqB,seqA,i,j,labels,scoring_matrix)
            #print(matchscore)
            H[i][j]=max(
                    H[i][j-1]+gapscore,
                    H[i-1][j]+gapscore,
                    H[i-1][j-1]+matchscore,
                    0
            )
            #print(H[i][j])

            #keep track of cell with the largest score
            if H[i][j] >= best:
                best=H[i][j]
                bestloc=(i,j)

    #print(H)
    return best, bestloc

def create_score_mat(matrix):
    #define score matrix
    with open(matrix,'r') as smat:
        iter=0 
        for line in smat:
            line=line.rstrip()
            if line[0]!='#':
                #print(line)
                if iter==0:
                    #header=np.fromstring(line,dtype=str, sep=' ')
                    #line.replace(' ',',')
                    header=list(np.array(line.split()))
                    #print('header',header)
                    scorelabels={}
                    for i in range(len(header)):
                        scorelabels[header[i]]=i
                    print(scorelabels)
                    iter+=1
                else:
                    line=list(np.fromstring(line, dtype=int, sep=' '))
                    scoremat.append(line)
                    #temp=pd.DataFrame(line)
                    #scoremat.append(temp,ignore_index=True)
    
    return scoremat, scorelabels

        

#define gap
gap=float(sys.argv[2])
scoremat=[]
mat=sys.argv[1]
scoremat,scorelabels=create_score_mat(mat)

print(scoremat)
print(scorelabels)

print(local_align('AACCCMMMS','CCCCAAATTMMA',scoremat,scorelabels,gap))
