#IMPORT LIBRARIES
import pandas as pd
import numpy as np
import re
import itertools
from itertools import repeat
from tkinter import *


df = pd.read_csv('data/Result.csv')

#FUNCTION TO TEST IF OBJECT FITS INPUT DIMENSIONS
def does_it_fit(object_id, dimensions):
    #FILTER FOR THE OBJECT
    rez = df[df['Object ID']==object_id]['Dimensions in cm'].tolist()
    rez = re.findall(r'[\d\.\d]+', str(rez))
    #IF OBJECT NOT FOUND, RETURN INFO
    if rez == []:
        return 'Object dimension info unavailable'
    #CHAIN ITEMS INTO ONE LIST
    #rez = list(itertools.chain(*rez))
    #TRANSFER DATATYPE TO FLOAT
    rez = [float(i) for i in rez]
    #FILL THE REST OF THE DIMENSIONS WITH 0
    a = 3 - len(rez)
    rez.extend(repeat(0, a))
    #UNPACK LISTS
    object_height, object_length, object_width = rez
    storage_height, storage_length, storage_width = dimensions
    #CHECK IF OBJECT FITS INTO STORAGE
    if (object_height<=storage_height) and (object_length<=storage_length) and (object_width<=storage_width):
        return True
    else:
        return False

def main():
	#INPUTS
	object_id = int(input("Enter object ID:  "))
	height_input = float(input("Enter height:  "))
	length_input = float(input("Enter length:  "))
	width_input = float(input("Enter width:  "))
	#OUTPUT
	print(does_it_fit(object_id, [height_input,length_input,width_input]))

if __name__ == "__main__":
	#ALWAYS RUN THE MAIN FUNCTION 
	while True:
		main()