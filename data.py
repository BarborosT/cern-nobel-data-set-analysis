from __future__ import print_function
from __future__ import division

import warnings
warnings.filterwarnings('ignore')

import pandas
import math
from ipywidgets import interact

pandas.options.mode.chained_assignment = None
data = pandas.read_csv('Data/nobel.csv', ',')

rcParams['image.cmap'] = 'Blues' # change default color

def parse_year(s):
    try:
        if s[-3] == '-':
            return int('19'+ s[-2:])
        elif s[-4:] == 'Data': # if there is a value
            return 1000
        else:
            return int(s[-4:])
    except Exception:
        return 10000

data['BirthYear'] = data['Birthdate'].apply(parse_year)
data  = data.query('BirthYear > 1000')