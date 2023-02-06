import pandas as pd

def disjoint(firstArray,secondArray):
    return list(set(firstArray).symmetric_difference(set(secondArray)))

df = pd.read_csv('first_file.txt', header=None, dtype=str)

firstArray = list(df[0])

df1 = pd.read_csv('second_file.txt', header=None, dtype=str)

secondArray = list(df1[0])

nonMatchedList = disjoint(firstArray, secondArray)

print(nonMatchedList)
