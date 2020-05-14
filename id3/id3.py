import numpy as np
import pandas as pd
from scipy.stats import entropy

# constants
NEGATIVE = 'no'
POSITIVE = 'si'

# reads attributes
def read_attributes():
    attr = np.loadtxt('attributes.txt', dtype=str, delimiter=',')
    return attr

# reads data
def read_data():
    data = pd.read_csv('data.txt', sep=',', names=read_attributes())
    return data

# returns the frequency of the values in a column
def get_frequency(attribue_data):
    values, frequencies = np.unique(attribue_data, return_counts=True)
    return values, frequencies

# gets the entropy of the entire dataset
def get_dataset_entropy(data):
    labels, counts = get_frequency(data.iloc[:,-1])
    probs = counts / float(np.shape(data)[0])
    entropy =- np.sum(probs * np.log2(probs))
    return entropy

# gets the entropy of an attribute
def get_attribute_entropy(data,attribute):
    labels, counts = get_frequency(data[attribute]) # labels of each attribute
    ri = counts / float(np.shape(data)[0]) # frequency of each label
    dic = {} # create a dictionary with {label,[ri,pi,ni]}
    count  = 0

    # for each label
    for label in labels: # positives and negatives(labels target)
        labels_target = data.loc[data[attribute] == label].iloc[:,-1] 
        fr_target = get_frequency(labels_target)
        pi,ni = 0,0

        # there are yes and no labels
        if(len(fr_target[0]) > 1):
            ni = fr_target[1][0]/len(labels_target) # negative frequency
            pi = fr_target[1][1]/len(labels_target) # positive frequency
        else:
            if fr_target[0] == POSITIVE:
                pi = fr_target[1][0]/len(labels_target) 
            else:
                ni = fr_target[1][0]/len(labels_target) 

        dic[label] = [ri[count],pi,ni]
        count+=1

    ent = 0
    for value in dic.values():
        ent += value[0] * entropy([value[1],value[2]], base=2)
    return ent 

def get_subtable(data,col,label):
    return data[data[:,col] == label][:,1:]

# check if all values are positive or negative
def check_all_equal(subtable):
    if data[-1][data[-1] == POSITIVE]:
        return POSITIVE
    else:
        return NEGATIVE


# def id3(attributes, values):
data = read_data()
attr = read_attributes()

print(data)
print(get_dataset_entropy(data))
entropies ={attribute: get_attribute_entropy(data,attribute) for attribute in data.keys()[:-1]} 
print(entropies)

"""
print(np.argmin([ent[1] for ent in entropies]))
print(min(entropies,key=lambda x:x[1]))


print(get_attribute_entropy(data,0,'TiempoExterior'))
print(get_attribute_entropy(data,1,'Temperatura'))
print(get_attribute_entropy(data,2,'Humedad'))
print(get_attribute_entropy(data,3,'Viento'))
"""

