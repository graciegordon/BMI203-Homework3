# BMI203-Homework3: Alignment

[![Build
Status](https://travis-ci.org/graciegordon/BMI203-Homework3.svg?branch=master)](https://travis-ci.org/graciegordon/BMI203-Homework3)

##What does this repo contain?
1. Main function to run alignment of a list of pairs given gap and gap extension penalties
2. 

##To run alignment
python -m functions /pathto/scoringmatrix /pathto/Pospairs.txt -10 -4 PosScoreTest10_4.txt PosAlignTest10_4.txt
##To test
Testing is as simple as running

```
python -m pytest
```

from the root directory of this project.
