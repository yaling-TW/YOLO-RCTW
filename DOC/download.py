import subprocess
import pandas as pd

#change testOz.txt/trainOz.txt
fileNameDataFrame = pd.read_csv('testOz.txt', header=None)

base_url = 'https://data.pawsey.org.au/download/FDFML/frames/'

for filename in fileNameDataFrame[0]:
    url = base_url + filename

    #change OzFish_test/OzFish_train
    subprocess.run(['wget', '-P', 'images/OzFish_test', url])
    print(url)
