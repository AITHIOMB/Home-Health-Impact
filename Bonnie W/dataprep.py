import csv
import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
import seaborn as sns

### Declaring known value sets ### 

#Empty Columns & Non Valueble columns 
    #(Dropping health concerns because all entries are yes)
emptyColumns = ['Unnamed: 42', 'Unnamed: 43','Health Concerns?'] 

#Location Columns
locationColumns = ['City','State','Zip']

#Syptom Columns (Columns that need to be one-hot encoded)
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

#Health Information 
healthInfoColumns = [
        'Sum of the Logs (Group I)',
        'Sum of the Logs (Group II)',
        'ERMI Score (Group I - Group II)']

#Molds 
moldColumns = ['Aspergillus flavus/oryzae',
       'Aspergillus fumigatus', 'Aspergillus niger', 'Aspergillus ochraceus',
       'Aspergillus penicillioides', 'Aspergillus restrictus*',
       'Aspergillus sclerotiorum', 'Aspergillus sydowii', 'Aspergillus unguis',
       'Aspergillus versicolor', 'Aureobasidium pullulans',
       'Chaetomium globosum', 'Cladosporium sphaerospermum',
       'Eurotium (Asp.) amstelodami*', 'Paecilomyces variotii',
       'Penicillium brevicompactum', 'Penicillium corylophilum',
       'Penicillium crustosum*', 'Penicillium purpurogenum',
       'Penicillium spinulosum*', 'Penicillium variabile',
       'Scopulariopsis brevicaulis/fusca', 'Scopulariopsis chartarum',
       'Stachybotrys chartarum', 'Trichoderma viride*', 'Wallemia sebi','Acremonium strictum',
       'Alternaria alternata', 'Aspergillus ustus',
       'Cladosporium cladosporioides 1', 'Cladosporium cladosporioides 2',
       'Cladosporium herbarum', 'Epicoccum nigrum', 'Mucor amphibiorum*',
       'Penicillium chrysogenum', 'Rhizopus stolonifer']

# 0 Values 
zeroValues = ['ND','<1','nd','N/D','N D','Nd', 'Hhh', 'nan', 
               'Hh', 'ND, <1','NDNDND', 'na','Ne','NF','<','n/d',
               'o', 'BD','NaN', 'N d','ND,<2','1<']

def oneHotEncodeSymptoms(symptomDF):
    # For every column in symptom DF columns, find all unique comma separated symptoms and add them to a list 
    for column in symptomDF.columns:
        systemSymptomList = (df[column].dropna()   # Drop any remaining NaNs (though there shouldn't be any after fillna)
                        .replace('', '0')    # Replace empty strings with '0'
                        .str.lower()         # Convert to lowercase
                        .str.replace(" ", "") # Remove spaces
                        .str.split(',')      # Split by commas
                        .explode()           # Explode lists to rows
                        .loc[lambda x: x != '0'] # Filter out '0' values
                        .dropna()            # Drop any remaining NaNs (though there shouldn't be any after fillna)
                        .unique())           # Get unique values
            
        for j in systemSymptomList:
            newColumn = str(i) + "_" + str(j)
            df[newColumn] = df[i].apply(lambda x: 1 if j in str(x).lower().replace(" ", "") else 0)
        systemSymptomList = []
    return df


# Read the Original WeInspect B CSV Data file 
df = pd.read_csv('WeInspectB.csv')

#### Splitting Dataframe into parts 

# Dropping Useless Columns 
print("Inital Columns Count: ", len(df.columns))
df = df.drop(emptyColumns,axis=1)
print("Count after dropping useless Columns: ", len(df.columns))
print("_____________________________________")

# Drop all rows where Zip , City, and State are missing 
print("Initial Rows before City/State/Zip Drop: ", len(df))
df = df.dropna(subset=['Zip', 'City', 'State'])
print("Rows after Dropping:" ,len(df))
print("_____________________________________")


# Creating a dataframe only handling symptom columns 
symptomDF = df[symptomColumns]
print("Symptom Dataframe Columns: ", len(symptomDF.columns))
print(symptomDF.columns)
print("_____________________________________")


# Creating dataframe handling location Data 
locationDF = df[locationColumns]
print("Location Dataframe Columns: ", len(locationDF.columns) )
print(locationDF.columns)
print("_____________________________________")


# Creating dataframe handling health information columns 
healthInfoDF = df[healthInfoColumns]
print("Health Information Dataframe Columns: ", len(healthInfoDF.columns))
print(healthInfoDF.columns)
print("_____________________________________")


# Creating dataframe handling mold
moldDF = df[moldColumns]
print("Mold Dataframe Columns: ", len(moldDF.columns))
print(moldDF.columns)
print("_____________________________________")


# One Hot Encoding Symptoms 
print("One Hot Encoding Symptom DF, Inital Columns: ", len(symptomDF.columns))
#symptomDF = oneHotEncodeSymptoms(symptomDF)
print("One Hot Encoded Columns: ", len(symptomDF.columns))
print("_____________________________________")



