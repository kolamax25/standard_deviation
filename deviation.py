import csv
import pandas as pd
import plotly.express as px
import math
#class 1
with open('deviation.csv', newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]


def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean


# sqr(xi - mean(x))
squared_list = []

for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)



#getting sum

sum = 0
for i in squared_list:
    sum = sum + i

#dividing the sum by the total values
result = sum /(len(data)- 1)
standard_deviation = math.sqrt(result)
print(standard_deviation)