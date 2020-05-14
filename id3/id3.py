import numpy as np
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
    data = np.loadtxt('data.txt', dtype=str, delimiter=',')
    return data

# returns the frequency of the values in a column
def get_frequency(attribue_data):
    values, frequencies = np.unique(attribue_data, return_counts=True)
    return values, frequencies

# gets the entropy of the entire dataset
def get_dataset_entropy(data):
    labels, counts = get_frequency(data[:,-1])
    probs = counts / float(np.shape(data)[0])
    entropy =- np.sum(probs * np.log2(probs))
    return entropy

def get_attribute_entropy(data,col):
    labels, counts = get_frequency(data[:,col]) # label of each example
    ri = counts / float(np.shape(data)[0]) # frequency of each example
    print(labels)
    print(ri)

    dic = {} # create a dictionary with {label,[ri,pi,ni]}
    count  = 0

    # for each label
    for label in labels:
        labels_target = data[data[:,col] == label][:,-1] # take the positives and negatives of a label
        fr_target = get_frequency(labels_target)
        pi,ni = 0,0

        # cuando hay solo un si o solo un no
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

    total = 0
    for value in dic.values():
        total += value[0] * entropy([value[1],value[2]], base=2)

    print(total)


# def id3(attributes, values):
data = read_data()
print(read_attributes())
print(data)
print(get_attribute_entropy(data,0))
print(get_attribute_entropy(data,1))
print(get_attribute_entropy(data,2))
print(get_attribute_entropy(data,3))

