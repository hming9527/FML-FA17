import os, sys, traceback, getpass, time, re
from threading import Thread
from subprocess import *
import numpy as np


# LIBSVM_PATH = "/home/hming/Downloads/libsvm-3.22/"
# TOOLS_PATH = "/home/hming/Downloads/libsvm-3.22/tools/"

# DATASET_PATH = TOOLS_PATH + "partitions/"
# MODEL_PATH = DATASET_PATH + "models/"

C_START = -2
C_STEP = 0.5
C_END = 2 + C_STEP #By default np.arange doesn't include the c_stop

KERNEL_DEGREE = 1

ACCURACY_REGEX = re.compile("Accuracy = ([\d]+\.[\d]+)")

cross_validation_pairs = {
    1:'split10',
    2:'split1',
    3:'split2',
    4:'split3',
    5:'split4',
    6:'split5',
    7:'split6',
    8:'split7',
    9:'split8',
    10:'split9'
}

for c in np.arange(C_START, C_END, C_STEP):
    for training_id, holdout_set in sorted(cross_validation_pairs.items()):
        training_set = "train" + str(training_id)

        accuracy = 0;

        pattern = 'c_{0}_d_{1}.{2}'.format(c if c >=0 else "_"+str(abs(c)), KERNEL_DEGREE, training_set)

        model_file = "{0}.model".format(pattern)
        out_file = '{0}.out'.format(pattern)

        cmd = 'svm-train -t 1 -c {0} -d {1} {2} {3}'.format(2**c, KERNEL_DEGREE, training_set, model_file)
        #cmd = 'svm-train -t 1 -c {0} -d {1} {2} {3}'.format(2**c, KERNEL_DEGREE, training_set, MODEL_PATH+model_file)

        result = Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE,stdin=PIPE).stdout
        for line in result.readlines():
            print(line),

        predict_cmd = 'svm-predict {0} {1} {2}'.format(holdout_set, model_file, out_file)
        #predict_cmd = 'svm-predict {0} {1} {2}'.format(holdout_set, MODEL_PATH+model_file, MODEL_PATH+out_file)

        predict_result = Popen(predict_cmd,shell=True,stdout=PIPE,stderr=PIPE,stdin=PIPE).stdout
        for line in predict_result.readlines():
            print(line),
            # if(len(ACCURACY_REGEX.match(line).groups())):
            #     accuracy = float(ACCURACY_REGEX.match(line).groups()[0])

        print "OURRESULT {0} {1} {2} {3} {4}".format(KERNEL_DEGREE, c, training_set, holdout_set, accuracy)