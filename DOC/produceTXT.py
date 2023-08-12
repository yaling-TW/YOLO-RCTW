import os

path = './images/TWFDB_test'                   #modify either 'test' or 'train'

with open('TWFDB_test.txt', 'w') as f:         #modify either 'test' or 'train'
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):  
            f.write(f'mydatasets{path[1:]}/{filename}\n')
