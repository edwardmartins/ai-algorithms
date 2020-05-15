import numpy as np
import pandas as pd
import pprint
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

        if(len(fr_target[0]) > 1):
            ni = fr_target[1][0]/len(labels_target) # negative frequency
            pi = fr_target[1][1]/len(labels_target) # positive frequency
        else: # there is just one label
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

# gets a subtable of a particular label
def get_subtable(data,attribute,label):
    return data[data[attribute] == label].reset_index(drop=True)

# finds the winner attribute, maximize information
def find_winner(data):
    entropies = []
    for attribute in data.keys()[:-1]:
        entropies.append(get_attribute_entropy(data,attribute))
    return data.keys()[:-1][np.argmin(entropies)]

# builds decision tree
def build_tree(data,tree=None): 
    Class = data.keys()[-1]   
    attribute = find_winner(data)
    att_values = np.unique(data[attribute])
    
    # create an empty dictionary to create tree    
    if tree is None:                    
        tree={}
        tree[attribute] = {} 
    
    for value in att_values:
        
        subtable = get_subtable(data,attribute,value)
        class_value,counts = np.unique(subtable[Class],return_counts=True)                        
        
        if len(counts)==1: # checking purity of subset
            tree[attribute][value] = class_value[0]                                                    
        else:        
            tree[attribute][value] = build_tree(subtable) # calling the function recursively 
                   
    return tree

tree = build_tree(read_data())
pprint.pprint(tree)
