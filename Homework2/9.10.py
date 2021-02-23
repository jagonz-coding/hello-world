#Name: Juan Gonzalez
#ID: 1808943

import csv

fileName = input()
freq = {}

with open(fileName, 'r') as file:
    read = csv.reader(file)
    for text in read:
        for word in text:
            if word not in freq.keys():
                freq[word] = 1
            else:
                freq[word] += 1

for key in freq.keys():
    print(key + " " + str(freq[key]))