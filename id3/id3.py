import numpy as np
from scipy.stats import entropy

def calculate_entropy(attribute, data):
    print((1/3)*entropy([1,0], base=2)+(2/3)*entropy([1/2,1/2], base=2))


def read_data():
    with open('Juego.txt', 'r') as f:
        data = [[str(word) for word in line.split(',')[:-1]] for line in f]
        return np.array(data[:-1]) # skip last new line


def find_unique_vals(data, col):
    return np.unique(data[:,col]) # row,column

#def id3(attributes, values):


data = read_data()
print(data)

print(find_unique_vals(data,0))