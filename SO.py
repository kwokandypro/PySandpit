from math import sqrt
import numpy as np
import warnings
from collections import Counter 
from collections import defaultdict
import pandas as pd
import random

def k_nearest_neighbors(data,predict, k =3):
 if len(data) >= k:
  warnings.warn('K is set to a value less than total voting groups')
 distances = []
 for group in data:
  for features in data[group]:
   eucliden_distance = np.linalg.norm(np.array(features)-np.array(predict))
   distances.append([eucliden_distance,group])
 votes = [i[1] for i in sorted(distances)[:k]]
 print(Counter(votes).most_common(1))
 vote_result = Counter(votes).most_common(1)[0][0]
 return vote_result

df = pd.read_csv('bc2.txt')
df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace = True)
full_data = df.astype(float).values.tolist()

random.shuffle(full_data)
test_size = 0.2
train_set = defaultdict(list)
test_set = defaultdict(list)
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]



for i in train_data:
 train_set[i[-1]].append(i[:-1])

 for i in train_data:
  test_set[i[-1]].append(i[:-1])


correct = 0
total = 0

for group in test_set:
 for data in test_set[group]:
  vote = k_nearest_neighbors(train_set,data, k=5)
  if group == vote:
   correct += 1
  total += 1

print ('Accuracy:',correct/total)