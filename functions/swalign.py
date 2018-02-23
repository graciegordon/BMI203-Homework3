##This code will perform a Smith-Waterman (local) alignment
##This naming can be imported by the test set in main
import numpy as np
import pandas as pd
import sys


def get_score(seqB,seqA,i,j,label,matrix):

    #get letter of current position in both strings
    #converted back to 0 numbering
     
    score=matrix[label[seqA[i-1]]][label[seqB[j-1]]]
    return score

def local_align(seqA, seqB, scoring_matrix, labels, gapscore,extend):
    
    #initialize score and state matrix
    H=np.zeros((len(seqA)+1,len(seqB)+1))
    state = [['x' for x in range(len(seqB)+1)] for y in range(len(seqA)+1)]
    
    best=0
    bestloc=(0,0)
    curstat=''

    ################################
    # fill in score and state matrix
    ################################

    for i in range(1, len(seqA)):
        for j in range(1,len(seqB)):
            
            curmax=0        
            diag=H[i-1][j-1]
            #calc score
            matchscore=diag+get_score(seqB,seqA,i,j,labels,scoring_matrix)
            
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

            #compare diagnal cell
            if matchscore == max(matchscore,northscore,westscore):
                curstat='match'
            
            ##update current matrix with best score and the state 
            ##matrix with the best state

            H[i][j]=max(0,matchscore,northscore,westscore)
            state[i][j]=str(curstat)
            
            #if this is the new best score take note
            if H[i][j] >= best:
                best=H[i][j]
                bestloc=(i,j)

    ############
    ###TRACEBACK
    ############

    i=bestloc[0]
    j=bestloc[1]
    align=''
    
    #trace back until you run out of numbers
    #given state of where that cell came from
    #to to that cell and get the letter it came
    #from

    while state[i][j] != 'x':
        if state[i][j] == 'match':
            #add to sequence
            align=seqA[i-1]+align
            i=i-1
            j=j-1

        elif state[i][j] == 'north':
            align='-'+align
            j=j-1

        elif state[i][j] == 'west':
            align='-'+align
            i=i-1

    return best, bestloc, align


def create_score_mat(matrix):
    #define score matrix
    with open(matrix,'r') as smat:
        iter=0
        scoremat=[]
        for line in smat:
            line=line.rstrip()
            if line[0]!='#':
                if iter==0:
                    header=list(np.array(line.split()))
                    scorelabels={}
                    for i in range(len(header)):
                        scorelabels[header[i]]=i
                    iter+=1
                else:
                    line=list(np.fromstring(line, dtype=int, sep=' '))
                    scoremat.append(line)
    return scoremat, scorelabels

'''        
##code to test functions
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
