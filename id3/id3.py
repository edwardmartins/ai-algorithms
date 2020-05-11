import numpy as np
from scipy.stats import entropy

def calculate_entropy(data,col):
    labels, counts = class_counts(data,col)
    probs = counts/ float(np.shape(data)[0]) # number of rows
    entropy = - np.sum(probs * np.log2(probs))
    return entropy

def read_data():
    with open('data.txt', 'r') as f:
        data = np.loadtxt('data.txt', dtype=str ,delimiter =',')
        return data

def read_attributes():
    with open('attributes.txt', 'r') as f:
        attr = np.loadtxt('attributes.txt', dtype=str ,delimiter =',')
        return attr

def find_unique_vals(data, col):
    return np.unique(data[:,col]) # row,column

def class_counts(df,col):
    return np.unique(df[:,col], return_counts=True)

# def id3(attributes, values):


data = read_data()
print(data)
print(read_attributes())
print(calculate_entropy(data,-1))


"""
print(np.shape(data)[1]) # number of columns
labels, counts = class_counts(data, -1)
print(labels)
print(counts/np.shape(data)[0]) # number of rows

for i in range(np.shape(data)[1]): # for each column
    print(find_unique_vals(data,i)) # print unique values

print(np.sum(data == 'caluroso'))
"""
