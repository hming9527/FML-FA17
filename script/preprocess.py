numLine = 0
rawdata = open('rawdata', 'r')
lines = rawdata.readlines()
with open('formattedData.txt', 'w') as formattedData:
	while numLine < len(lines):
		splitted = lines[numLine].split(',')
		reformat = []
		feature = 1
		value = splitted[57].strip(' \t\n\r')
		if value == '1':
			reformat.append('+1')
		elif value == '0':
			reformat.append('-1')
		while feature <= 57:
			item = str(feature) + ':' + splitted[feature - 1]
			reformat.append(item)
			feature += 1
		for item in reformat:
			formattedData.write("%s " % item)
		formattedData.write("\n")
		numLine += 1
