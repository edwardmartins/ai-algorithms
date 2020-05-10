import numpy as np
from scipy.stats import entropy

def calculate_entropy(attribute, data):
    print((1/3)*entropy([1,0], base=2)+(2/3)*entropy([1/2,1/2], base=2))


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

#def id3(attributes, values):
# Sacar los atributos unicos por cada columna, menos de la columna final
# Por cada atributo unico sacar el numero de veces que se repite, el numero de (+) y el numero de (-)

data = read_data()
print(data)
print(read_attributes())
print(np.shape(data)[1]) # number of columns

for i in range(np.shape(data)[1]): # for each column
    print(find_unique_vals(data,i)) # print unique values

print(np.sum(data == 'caluroso'))

