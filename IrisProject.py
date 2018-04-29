#Stephen Hammel
#Data analysis of Iris Fischer Data
#References included in ReadMe file

import pandas as pd
import numpy as np


data = pd.read_csv("Iris Project/iris.csv", sep = "\t", header = 0)

data.head()
print(data.head())

species_list = list(data["Species"].unique())
print("Data Analysis:")

print("The species in this data include: %s\n" % species_list)
print("Sepal length range: [%s, %s]" % (min(data["SepalLengthCm"]), max(data["SepalLengthCm"])))
print("Sepal width range:  [%s, %s]" % (min(data["SepalWidthCm"]), max(data["SepalLengthCm"])))
print("Petal length range: [%s, %s]" % (min(data["PetalLengthCm"]), max(data["PetalLengthCm"])))
print("Petal width range:  [%s, %s]\n" % (min(data["PetalWidthCm"]), max(data["PetalWidthCm"])))

print("Sepal length stddev:\t %f" % np.std(data["SepalLengthCm"]))
print("Sepal width stddev: \t %f" % np.std(data["SepalWidthCm"]))
print("Petal length stddev:\t %f" % np.std(data["PetalLengthCm"]))
print("Petal width stddev: \t %f\n" % np.std(data["PetalWidthCm"]))

print("Data summary:\n")
print(data[data.columns[2:]].describe())
#This section groups species and gives their mean value under each 
print("Species Summary:\n")

print(data.groupby('Species').mean())

