import csv

def dictionary(filename):
	out_dict = {}
	with open(filename, "rU") as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		dictionary = {}
		for row in reader:
			dictionary[row[0]]=row[1:]

out_dict = {}
with open('../dictionaries_and_flow/richness_fishbase_family.csv', "rU") as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader:
		out_dict[row[0]]=row[1:]

current_min = out_dict[out_dict.keys()[0]]
min_keys = []
for k, v in out_dict.iteritems():
    if v < current_min:
        current_min = v
        min_keys = [k]
    elif v == current_min:
        min_keys.append(k)
        for sentence in min_keys:
        	print sentence +" has 1 species."

current_min2 = out_dict[out_dict.keys()[0]]
threshold = int(raw_input("Type in a threshold species number: "))
for bob in out_dict.values():
	if threshold <= out_dict.values():
		if out_dict[bob] <= out_dict.values():
			for sentence2 + "has " 
			print("Family XX has ", out_dict.values())



