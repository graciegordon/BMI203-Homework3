###This script will call the functions in SW_align and aligh all positive and 
###negative pairs in the files 
###CMD: python __main__.py scoringmatrix gappenalty file_of_sequences_to_compare outfile 


import sys
import SW_align as sw  

#path to seqs
path='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/'
posfile='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/Pospairs.txt'
negfile='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/Negpairs.txt'
scorepath='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/scores/'
alignpath='/Users/student/Documents/Algorithms/Homework3/BMI203-Homework3/alignments/'

gaps=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]
extends=[-1,-2,-3,-4,-5]

tests=[negfile]

#read in scoring matrix
mat=sys.argv[1]
scoremat,scorelabels=sw.create_score_mat(mat)

for test in tests: 
    for gap in gaps:
        for extend in extends:
            if test==posfile:
                scorefile=scorepath+'scorePos'+str(gap)+str(extend)+'.txt'
                alignfile=alignpath+'alignPos'+str(gap)+str(extend)+'.txt' 
            if test==negfile:
                scorefile=scorepath+'scoreNeg'+str(gap)+str(extend)+'.txt'
                alignfile=alignpath+'alignNeg'+str(gap)+str(extend)+'.txt'
            #outfiles
            outfile=open(scorefile,'w')
            outfile2=open(alignfile,'w')
            #read in sequences of interest
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
                            b=b.strip()
                            b=b.upper()
                            if b[0]!='>':
                                seqB=seqB+b 
                    
                    #print('seqB',seqB)
                    #print('read file')
                    seqA=str(seqA)
                    seqB=str(seqB)

                    #print(scoremat)
                    #print(scorelabels)
                    #print('submit to align')
                    temp=sw.local_align(seqA,seqB,scoremat,scorelabels,gap,extend)
                    #print('receive answer')
                    outfile2.write(line+'\n')
                    outfile2.write(seqA+'\n')
                    outfile2.write('\n')
                    outfile2.write(seqB+'\n')
                    outfile2.write('\n')
                    outfile2.write(temp[2]+'\n')
                    outfile2.write('\n')
                    outfile.write(str(temp[0])+'\t'+str(temp[1])+'\n')
                    #answers.append(sw.local_align(seqA,seqB,scoremat,scorelabels,gap,extend))

            #outfile.write(str(answers))
            outfile.close()
            outfile2.close()

            #calc false positive rate


