## Problem C

### 1.

Download software.

### 2.

First use a python script to format raw data into standard libsvm data format and split data into two parts. Then use libsvm command line tool to scale data.

`python preprocess.py`

`svm-scale -l -1 -u 1 -s scale.txt train.txt > train.scale.txt`

`svm-scale -r scale.txt test.txt > test.scale.txt`

### 3.

Use the libsvm python script to randomly split data into ten parts.

Then generate a training sample from 9 splits, and use the left 1 as testing sample. Use each split file as a testing sample, so 10 such training samples will be genereated.

Then use a python script to train and generate outputs.

Finally, reformat outputs and plot.

Output plots:

![degree=1](https://github.com/hming9527/FML-FA17/blob/master/figure/deg1.png)
![degree=2](https://github.com/hming9527/FML-FA17/blob/master/figure/deg2.png)
![degree=3](https://github.com/hming9527/FML-FA17/blob/master/figure/deg3.png)
![degree=4](https://github.com/hming9527/FML-FA17/blob/master/figure/deg4.png)

From the figure above we can see that the performances are very close, I would choose C to be 2^10 and degree to be 4 since it's the smoothest choice.

### 4.

Compare of cross-validation error and test error:

![error](https://github.com/hming9527/FML-FA17/blob/master/figure/error_compare.png)

We can see that as degree increases, both error decreases, but somehow my test error is better than cross-validation error.

Number of support vector machines:

![nsv](https://github.com/hming9527/FML-FA17/blob/master/figure/numSV.png)

We can see that the average number of total support vectors decreases while the average number of marginal support vectors increases as degree increases.
