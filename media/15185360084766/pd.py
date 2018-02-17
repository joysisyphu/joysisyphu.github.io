#!/usr/bin/env python

### pandas - Python Data Analysis Library
### pandas.pydata.org

import pandas

from random import random
d = [random() for i in range(5)]
print(d)
labels = ['a','b','c','d','e']

s1 = pandas.Series(data=d, index=labels)
# print('whole series:')
print(s1)
print('\n')

# print('item by label:')
# print(s1['a'])
# print(s1[2])
# print('\n')

# print('slice:')
# print(s1[['c','a','e']])
# print('\n')

#print('(1) selection from array of booleans:')
#print(s1[[True,False,False,True,True]])
#print('\n')

#print('(2) boolean array, given a condition:')
#print(s1 > 0.2)
#print('\n')

# print('combining (1) and (2):')
# print(s1[s1 > 0.2])
# print('\n')
# print(s1)

# print('some statistics... (numpy ndarray functions)')
# print('count of non-null values: %d' % s1.count())
# print('sum: %f' % s1.sum())
# print('mean: %f' % s1.mean())
# print('median: %f' % s1.median())
# print('variance: %f' % s1.var())
# print('mean absolute deviation: %f' % s1.mad())
# print('standard deviation: %f' % s1.std())
# print('standard error of mean: %f' % s1.sem())
# print('skew: %f' % s1.skew())
# print('kurtosis: %f' % s1.kurt())
# print('max: %f' % s1.max())
# print('min: %f' % s1.min())
# print('\n')

s2 = pandas.Series(data={'a':1.0, 'b':2.0, 'c':3.0, 'd':4.0})
print('series from dictionary:')
print(s2)
# print('\n')

# print('vector sum (with NaN for missing value):')
# print(s1+s2)
# print('\n')

# print('test for NaNs...')
# sum = s1+s2
# print(sum.notnull())
# print('\n')

# print('filter out NaNs:')
# print(sum[sum.notnull()])
# print('\n')

# df = pandas.DataFrame({'col1': s1, 'col2': s2})
# print('data frame:')
# print(df)
# print('\n')

df = pandas.read_csv('in4.csv', index_col='id')
print('data frame from csv:')
print(df)  
print('\n')

# print('a column:')
# print(df['sampleName'])
# print('\n')

# print('several columns:')
# print(df[['sampleName','sampleType','value']])
# print('\n')

# print('a row:')
# print(df.loc['DEF2'])
# print('\n')

# print('several rows:')
# print(df.loc[['ABC1','GHI3','JKL4']])
# print('\n')

# print('(1) row selection from array of booleans:')
# print(df[[False,False,True,True]])
# print('\n')

# print('(2) boolean array, given a condition:')
# print(df['value'] > 0.5)
# print('\n')

# print('combining (1) and (2):')
# print(df[df['value'] > 0.5])
# print('\n')

# print('a query for particular sampleNames...')
# print(df[['Sh2' in n for n in df['sampleName']]])
# print('\n')

d1 = [[random() for i in range(4)] for j in range(4)]
rlabel = ['a','b','c','d']
clabel = ['A','B','C','D']
df1 = pandas.DataFrame(data=d1, index=rlabel, columns=clabel)

d2 = [[random() for i in range(4)] for j in range(4)]
rlabel = ['a','b','c','d']
clabel = ['A','B','C','D']
df2 = pandas.DataFrame(data=d2, index=rlabel, columns=clabel)

print('numerical data:')
print(df1)
print('\n')
print(df2)
print('\n')

# print('vector sum:')
# print(df1+df2)
# print('\n')

# print('comparison:')
# print(df1 < df2)
# print('\n')

print('describe:')
print(df1.describe())

a1 = pandas.read_csv('a1.csv', index_col='id')
a2 = pandas.read_csv('a2.csv', index_col='id')
a3 = pandas.read_csv('a3.csv', index_col='id')

print('a1:')
print(a1)
print('\n')
print('a2:')
print(a2)
print('\n')
#print('a3:')
#print(a3)
#print('\n')

a1_a2 = a1.join(a2, how='right')#inner means no NaN, ourter means join all value ,if one is missing, NaN
print('a1 join a2:')
print(a1_a2)
print('\n')

#a2_a3 = a2.join(a3, lsuffix='_a', rsuffix='_b', how='outer')
#print('a2 join a3:')
#print(a2_a3)
#print('\n')

#a1_a2_a3 = a1.join(a2, how='outer').join(a3, lsuffix='_a', rsuffix='_b', how='outer')
#print('a1 join a2 join a3 - outer')
#print(a1_a2_a3)
#print('\n')

#print('test for NaN:')
#print(a1_a2_a3.notnull())
#print('\n')

#print('all: True if all rows in a column are True (for axis=0)')
#print('     or all columns in a row are True (for axis=1)')
#print(a1_a2_a3.notnull().all(axis=1))
#print('\n')

#print('get only rows with no NaNs')
#print(a1_a2_a3[a1_a2_a3.notnull().all(axis=1)])
#print('\n')

#print('but this is much easier!')
#a1_a2_a3 = a1.join(a2, how='inner').join(a3, lsuffix='_a', rsuffix='_b', how='inner')
#print('a1 join a2 join a3 - inner')
#print(a1_a2_a3)
#print('\n')
