#! /usr/bin/python
trainingSize = 3000
testingSize = 1601
numLine = 0
rawdata = open('formattedData.txt', 'r')
lines = rawdata.readlines()
with open('train.txt', 'w') as traindata:
	while numLine < 3000:
		traindata.write(lines[numLine])
		numLine = numLine + 1
with open('test.txt', 'w') as testdata:
	while numLine < 4601:
		testdata.write(lines[numLine])
		numLine = numLine + 1

