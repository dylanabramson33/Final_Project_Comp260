#!/usr/bin/env python3
import sys
import subprocess as sp
import re
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


if(len(sys.argv) == 1):
    raise RuntimeError('Pass in .dat file')

with open(sys.argv[1],'r') as file:
    text = file.read()


split_text = text.split('\n')
split_text.pop()

data = [re.findall('\d\.\d+',text)[0] if len(re.findall('\d\.\d+',text)) > 0 else None for text in split_text]
data = list(filter(lambda x: x != None,data))
data = np.array([float(val) for val in data])

df1 = pd.DataFrame(data)

df1.plot()

plt.show()
