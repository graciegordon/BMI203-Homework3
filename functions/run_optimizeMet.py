import sys
import numpy as np
import SW_align as sw
from random import *
import optimizeMet as om

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
#mat=scoremat
cost=0
#iterate
for i in range(100):
    mat=om.Permute_mat(scoremat)
    pos=[]
    neg=[]
    for test in tests:
        with open(test,'r') as seqs:
            for line in seqs:
                #print(line)
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
    curcost=om.Calc_TP(pos,neg)
    if cost < curcost:
        cost=curcost
        bestmat=mat
print('best score',cost)


print('best matrix')
for line in bestmat:
        print(line)


outfile=open(sys.argv[2],'w')
outfile2=open(sys.argv[3],'w')
for p in pos:
    outfile.write(str(p[1])+'\n')
for n in neg:
    outfile2.write(str(n[1])+'\n')

outfile.close()
outfile2.close()



