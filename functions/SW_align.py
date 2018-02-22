##This code will perform a Smith-Waterman (local) alignment
import numpy as np
import pandas as pd
import sys


def get_score(seqB,seqA,i,j,label,matrix):

    #get letter of current position in both strings
    #converted back to 0 numbering
     
    #score=matrix[posA][posB]
    score=matrix[label[seqA[i-1]]][label[seqB[j-1]]]
    return score

def local_align(seqA, seqB, scoring_matrix, labels, gapscore,extend):
    
    #initialize matrix
    H=np.zeros((len(seqA)+1,len(seqB)+1))
    state = [['x' for x in range(len(seqB)+1)] for y in range(len(seqA)+1)]
    
    best=0
    bestloc=(0,0)
    curstat=''
    # fill in H in the right order
    for i in range(1, len(seqA)):
        #print('row')
        for j in range(1,len(seqB)):
            #print('innerloop')
            #print('idx A,B:',i,j)
            curmax=0        
            #print('calc match') 
            diag=H[i-1][j-1]
            #west=H[i][j-1]
            #north=H[i-1][j]

            matchscore=diag+get_score(seqB,seqA,i,j,labels,scoring_matrix)
            
            #print('matchscore',matchscore) 
            #print('compare cells')
            #compare west cell
            if state[i][j-1] == 'match':
                westscore=H[i][j-1]+gapscore
                curstat='west'
            else:
                westscore=H[i][j-1]+extend
                curstat='west'

            #compare north cell
            if state[i-1][j] == 'match': 
                northscore=H[i-1][j]+gapscore
                if northscore>westscore:
                    curstat='north'
                    #print('north open',curmax)
            else:
                northscore=H[i-1][j]+extend
                if northscore>westscore:
                    curstat='north'
                    #print('north ext',curmax)
            #print('north',curstat,curmax)

            #score=H[i-1][j-1]
            #print('determine max')
            #alignmentScore=max(0,matchscore,northscore,westscore)

            if matchscore == max(matchscore,northscore,westscore):
                curstat='match'
            
            ##update current matrix
            H[i][j]=max(0,matchscore,northscore,westscore)
            
            state[i][j]=str(curstat)
            #print('score',alignmentScore)
            #if this is the new best score take note
            
            #print('save best')            
            if H[i][j] >= best:
                best=H[i][j]
                bestloc=(i,j)

    #print(H)
    #print(state)
            

    ###TRACEBACK
    i=bestloc[0]
    j=bestloc[1]
    align=''
    #trace back until you run out of numbers
    while state[i][j] != 'x':
        if state[i][j] == 'match':
            #add to sequence
            align=seqA[i-1]+align
            #print(seqA[i-1])
            #print(align)
            i=i-1
            j=j-1

        elif state[i][j] == 'north':
            align='-'+align
            j=j-1

        elif state[i][j] == 'west':
            align='-'+align
            i=i-1
    #print('align',align)

    return best, bestloc, align

def TraceBack(seqA,seqB,best, bestloc, state):
    #find optimal alignment
    
    #start at best loc in state matrix

    i=bestloc[0]
    j=bestloc[1]
    align=''

    #trace back until you run out of numbers
    while state[i][j] != 'x':
        if state[i][j] == 'match':
            #add to sequence
            #print(seqA[i])
            align=seqA[i]+align
            #print(align)
            i=i-1
            j=j-1

        elif state[i][j] == 'north':
            align='-'+align
            j=j-1
        
        elif state[i][j] == 'west':
            align='-'+align
            i=i-1
    print('align',align)

def create_score_mat(matrix):
    #define score matrix
    with open(matrix,'r') as smat:
        iter=0
        scoremat=[]
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

'''        
#define gap
gap=float(sys.argv[2])
extend=float(sys.argv[3])
scoremat=[]
mat=sys.argv[1]
scoremat,scorelabels=create_score_mat(mat)

print(scoremat)
print(scorelabels)

print(local_align('ACCTGG','ACTGGGGG',scoremat,scorelabels,gap,extend))
'''
