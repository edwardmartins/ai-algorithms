import numpy as np
from scipy.stats import entropy


def calculate_entropy_dataset(data):
    labels, counts = class_counts(data, -1)
    probs = counts / float(np.shape(data)[0])
    entropy = - np.sum(probs * np.log2(probs))
    return entropy


"""
def calculate_entropy_attribute(data,col):
    target_variables = find_unique_vals(data, -1)
    variables, counts = class_counts(data,col) # number of times each example appears
    probs = counts/ float(np.shape(data)[0]) # probability of appareance of each example

    for var in variables: # para cada ejemplo
        entropy = 0
        for target in target_variables:
            numerator = 

"""


def read_data():
    with open('data.txt', 'r') as f:
        data = np.loadtxt('data.txt', dtype=str, delimiter=',')
        return data


def read_attributes():
    with open('attributes.txt', 'r') as f:
        attr = np.loadtxt('attributes.txt', dtype=str, delimiter=',')
        return attr


def find_unique_vals(data, col):
    return np.unique(data[:, col])  # row,column


def class_counts(data, col):
    return np.unique(data[:, col], return_counts=True)


def get_classes(data, col, value):
    return data[data[:,col] == value][:,-1]

# def id3(attributes, values):


data = read_data()
print(data)
print(read_attributes())
print(calculate_entropy_dataset(data))
print(get_classes(data,0,'lluvioso'))
print(np.unique(get_classes(data,0,'lluvioso'), return_counts=True))



"""
print(np.shape(data)[1]) # number of columns
labels, counts = class_counts(data, -1)
print(labels)
print(counts/np.shape(data)[0]) # number of rows

for i in range(np.shape(data)[1]): # for each column
    print(find_unique_vals(data,i)) # print unique values

print(np.sum(data == 'caluroso'))
"""
