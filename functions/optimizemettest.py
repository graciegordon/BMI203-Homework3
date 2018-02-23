#this script will randomly permute a value in the matrix 

import sys
import numpy as np
#import SW_align as sw
from functions import swalign
from random import *

def Permute_mat(matrix):
    #for line in matrix:
        #print(line)
    #print(matrix)
    #print(len(matrix))
    
    #spot to change
    i= randint(0,len(matrix)-1)
    j= randint(0,len(matrix)-1)
    #spot to swap with
    
    x=randint(0,len(matrix)-1)
    y=randint(0,len(matrix)-1)

    while (x==i and j==y) or (x==j and y==i):
        x=randint(0,len(matrix)-1)
        y=randint(0,len(matrix)-1)

    pos1=matrix[i][j]
    pos2=matrix[x][y]

    pos1a=matrix[j][i]
    pos2a=matrix[y][x]
    
    print('first pos',i,j)
    print(pos1,pos1a)
    print('second pos',x,y)
    print(pos2,pos2a)
    
    matrix[i][j]=pos2
    matrix[j][i]=pos2
    matrix[x][y]=pos1
    matrix[y][x]=pos1
    
    #for line in matrix:
        #print(line)
    #print(matrix)
    return matrix

def out_TPR(allscores,fpr):
    
    countf=0.0
    pos_count=0
    neg_count=0
    counter=0
    totneg=0
    totpos=0
    truepos=0

    for i in allscores:
        if i[0]=='neg':
            totneg+=1
        if i[0]=='pos':
            totpos+=1
    for item in allscores:
        if fpr==0:
            if item[0]=='pos':
                pos_count+=1

            if item[0]=='neg':
                neg_count+=1

            counter+=1
            countf=float(neg_count)/totneg
            truepos=float(pos_count)/counter
            #print(truepos)
            break
        if float(countf) < float(fpr):
            if item[0]=='pos':
                pos_count+=1

            if item[0]=='neg':
                neg_count+=1
            
            counter+=1
            countf=float(neg_count)/totneg
            truepos=float(pos_count)/totpos
            #print('fpr',countf)
    #print('tp',truepos)
    
    return truepos
        

def Calc_TP(pos,neg):
    #accept 2 tuples ('pos',score) ('neg',score)
    allscores=pos+neg

    allscores=sorted(allscores,key=lambda x: x[1],reverse=True)
    #print(allscores)    
    sumTP=0

    #calculate TP when FP is 0
    sumTP+=out_TPR(allscores,0.0)
    #calculate TP when FP is 0.1
    sumTP+=out_TPR(allscores,0.1)
    #calculate TP when FP is 0.2
    sumTP+=out_TPR(allscores,0.2)
    #calculate TP when FP is 0.3
    sumTP+=out_TPR(allscores,0.3)

    #print("sumTP",sumTP)
    return sumTP


'''
#############
##run program
#############


#path to seqs
path='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/'
pospath='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/Pospairs.txt'
negpath='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/Negpairs.txt'
tests=[pospath,negpath]
gap=float(-10)
extend=float(-4)

#read in scoring matrix
originalmat=sys.argv[1]
scoremat,scorelabels=sw.create_score_mat(originalmat)

cost=0
#iterate
for i in range(20):
    mat=Permute_mat(scoremat)
    pos=[]
    neg=[]
    for test in tests:
        with open(test,'r') as seqs:
            for line in seqs:
                print(line)
                cur=line.split()
                #with open(path+cur[0],'r') as seq1:
                    #data=seq1.read()

                seqA=''
                seqB=''
                with open(path+cur[0],'r') as seq1:
                    for a in seq1:
                        a=a.strip()
                        a=a.upper()
                        if a[0]!='>':
                            seqA=seqA+a
                #print('seqA',seqA) 
                with open(path+cur[1],'r') as seq2:
                    for b in seq2:
                        b=b.upper()
                        b=b.strip()
                        if b[0]!='>':
                            seqB=seqB+b

                seqA=str(seqA)
                seqB=str(seqB)

                temp=sw.local_align(seqA,seqB,mat,scorelabels,gap,extend)
                
                if test == pospath:
                    pos.append(('pos',temp[0]))
                elif test == negpath:
                    neg.append(('neg',temp[0]))

    #print(pos)
    #print(neg)
    curcost=Calc_TP(pos,neg)
    if cost < curcost:
        cost=curcost
        bestmat=mat
        scores=pos+neg
print('best score',cost)

print('best matrix')
for line in bestmat:
        print(line)
'''
