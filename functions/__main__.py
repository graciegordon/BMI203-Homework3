###This script will call the functions in SW_align and aligh all positive and 
###negative pairs in the files 
###CMD: python __main__.py scoringmatrix gappenalty file_of_sequences_to_compare outfile 


import sys
import SW_align as sw  

#path to seqs
path='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/'

#outfile
outfile=open(sys.argv[4],'r')
#define gap
gap=float(sys.argv[2])
#read in scoring matrix
mat=sys.argv[1]
scoremat,scorelabels=sw.create_score_mat(mat)
#read in sequences of interest
answers=[]
seqA=''
seqB=''
with open(sys.argv[3],'r') as seqs:
    for line in seqs:
        print(line)
        cur=line.split()
        with open(path+cur[0],'r') as seq1:
            for a in seq1:
                a=a.strip()
                if a[0]!='>':
                    seqA=seqA+a 
        #print('seqA',seqA) 
        with open(path+cur[1],'r') as seq2:
            for b in seq2:
                b=b.strip()
                if b[0]!='>':
                    seqB=seqB+b 
        #print('seqB',seqB)

        seqA=str(seqA)
        seqB=str(seqB)

        #print(scoremat)
        #print(scorelabels)

        answers.append(sw.local_align(seqA,seqB,scoremat,scorelabels,gap))

outfile.write(answers)
outfile.close()

