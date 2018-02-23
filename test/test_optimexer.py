from functions import optimizeMet
from functions import swalign
import numpy as np
def test_Calc_TP():
    positiveScores=[('pos',90),('pos',78),('pos',88),('pos',13),('pos',99),('pos',86),('pos',66),('pos',3),('pos',33),('pos',10)]
    negativeScores=[('neg',55),('neg',3),('neg',8),('neg',16),('neg',2),('neg',7),('neg',4),('neg',20),('neg',1),('neg',12)]
    temp=optimizeMet.Calc_TP(positiveScores,negativeScores)
    print(temp)
    assert temp == 3

def test_edit_matrix():
    
    matrix='/scoringTables/BLOSUM50'
    matrix, label=swalign.create_score_mat(matrix)
    newmat=optimizeMet.Permute_mat(matrix)
    flatMat = lambda matrix: [item for sublist in l for item in sublist]
    flatNewMat = lambda newmat: [item for sublist in l for item in sublist]
    assert np.not_equal(flatNewMat, flatMat)

