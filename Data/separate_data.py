# Purpose:
# This script will seperate (or split) brain data in 'train' folder to either 'train' or 'val' folders
#
# Requirement:
# This script should be placed under 'Data' folder
# This script requires two .csv files (train.csv & val.csv) in same folder
#
# Usage:
# Modify 'train.csv' and 'val.csv' and run this script
#
# After running:
# List of data represented in 'train.csv' will remain in 'train' folder
# List of data represented in 'val.csv' will be moved to 'val' folder
# Data which are not represented in both 'train.csv' and 'val.csv' will be noticed as errors
#
# Author:
# Dongmyung Shin, Seoul National University, http://list.snu.ac.kr/

import os
import glob
import pandas as pd
import shutil

# First, remove any data in 'val' folder
files = glob.glob('./val/*')
for f in files:
    os.remove(f)

# Second, load .csv files
train_files = pd.read_csv('./train.csv', header=None)
train_files = train_files.values.tolist()
train_files = [name[0] for name in train_files]
val_files = pd.read_csv('./val.csv', header=None)
val_files = val_files.values.tolist()
val_files = [name[0] for name in val_files]

# Third, separate data
files = glob.glob('./train/*.h5')
for f in files:
    fname = os.path.basename(f)
    if fname in train_files:
        pass
    elif fname in val_files:
        shutil.move('./train/' + fname, './val/' + fname)
    else:
        print(fname + ' is not represented in both train.csv and val.csv, please check!')