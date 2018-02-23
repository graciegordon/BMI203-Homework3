# BMI203-Homework3: Alignment

[![Build
Status](https://travis-ci.org/graciegordon/BMI203-Homework3.svg?branch=master)](https://travis-ci.org/graciegordon/BMI203-Homework3)

##What does this repo contain?
1. __main__.py: function to run alignment of a list of pairs given gap and gap extension penalties
2. submit_all_gaps.py: function to submit all  20 gap opening and 5 extension penalties
3. swalign.py/SW_align.py: funtions to complete Smith Waterman Alignment (duplicated)
4. run_optimizeMet.py: function that runs many iterations of optimization of a matrix
5. optimizeMet.py: function that permutes a given matrix and calculates sum of true positives at false positive rates of 0, 0.1, 0.2, 0.3
6. calcRates: calcultes false positive rate given true positive rate of 0.7
7. rocPlot.py: function to plot ROC curve given positive and negative scores

##To run alignment
python -m functions /pathto/scoringmatrix /pathto/Pospairs.txt -10 -4 PosScoreTest10_4.txt PosAlignTest10_4.txt
##To test
Testing is as simple as running

```
python -m pytest
```

from the root directory of this project.
