#IMPORT LIBRARIES
import pandas as pd
import numpy as np
import re
import itertools
from itertools import repeat

#READ THE DATA
df = pd.read_excel('data/MetObjects.xlsx')
#EXTRACT NEEDED FEATURES
df = df[['Object ID','Dimensions']]
#DROP N/A ROWS
df = df[df['Object ID'].notna()]
# FUNCTION FOR EXTRACTING THE DIMENSIONS IN CM
def extract_cm(string):
    s = str(string)
    #FIND THE BEGINNING INDEX OF CM DIMENSIONS
    start = s.find(" in. (")
    len_start = len(" in. (")
    end = s.find(" cm)")
    a = s[start+len_start:end]
    #IF SUBSTRING NOT FOUND, RETURN FALSE
    if start == -1 or a is None:
        return False
    else:
        #EXTRACT FLOATS FROM SUBSTRING
        c = re.findall(r'[\d\.\d]+', str(a))
        if c == []:
            #IF NO NUMBER IS FOUND INSIDE PARENTHESIS RETURN FALSE
            return False
        else:
            return c
#APPLY FUNCTION TO CREATE COLUMN
df['Dimensions in cm'] = df['Dimensions'].apply(extract_cm)
#FILTER OUT ROWS WITHOUT DIMENSION INFORMATION WHICH WAS PREVIOUSLY BRANDED AS FALSE
df = df[df['Dimensions in cm'] != False]
#DROP DIMENSIONS
df.drop('Dimensions', axis = 1, inplace = True)

df = df[['Object ID','Dimensions in cm']]
#WRITE TO CSV
df.to_csv(r"data/Result.csv")