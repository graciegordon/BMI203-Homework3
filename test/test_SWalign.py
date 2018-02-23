from functions import swalign

def test_alignscore():
    seq1='TGTTACGG'
    seq2='GGTTGACTA'
    mat='scoringTables/BLOSUM50'
    gapscore=-2
    extend=0
    scoring_matrix,scorelabels=swalign.create_score_mat(mat)
    labels={'A':0, 'R':1, 'N':2, 'D':3, 'C':4, 'Q':5, 'E':6, 'G':7, 'H':8, 'I':9, 'L':10, 'K':11, 'M':12, 'F':13, 'P':14, 'S':15, 'T':16, 'W':17, 'Y':18, 'V':19, 'B':20, 'Z':21, 'X':22, '*':23}
    temp = swalign.local_align(seq1, seq2, scoring_matrix, labels, gapscore,extend)    
    assert temp[0] == 34



