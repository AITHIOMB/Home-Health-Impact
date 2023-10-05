import csv
import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
import seaborn as sns



def cleanValues(): 
    weirdValues = ""

# Main Script 


# Read the Original WeInspect B CSV Data file 
df = pd.read_csv('WeInspectB.csv')

nullCheck = df.isnull().sum()
print(nullCheck)

#Checking Column Names for initial State 
#print(df.columns)

#Extracting symptom columns and rows from dataframe 
symptomColumns = ['Diagnoses', 
                'Eyes, Ears, Nose, & Throat',
                'Resipiratory', 'Digestive',
                'Circulatory', 
                'Skin', 
                'Brain', 
                'Nervous', 
                'Urinary', 
                'Immune', 
                'Reproductive']
symptomDataframe = df[symptomColumns]




