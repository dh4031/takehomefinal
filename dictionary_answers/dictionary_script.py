import csv #required library to open csv files

#function to create a dictionary from a csv file
def dictionary(filename):
#opens up file and need to rU otherwise, I get this unicode error
	with open(filename, "rU") as csvfile:
#reading the csv file and stating where the delimiter is
		reader = csv.reader(csvfile, delimiter = ',')
		dictionary = {}
		for row in reader:
			dictionary[row[0]]=row[1:]

#created it out of the function for testing purposes
out_dict = {}
#opens up file and need to rU otherwise, I get this unicode error
with open('../dictionaries_and_flow/richness_fishbase_family.csv', "rU") as csvfile:
#reading the csv file and stating where the delimiter is
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader:
#gets the rows of the csv file and turns them into a dictionary		
		out_dict[row[0]]=row[1:]

#create a minimum value
current_min = out_dict[out_dict.keys()[0]]
#empty list of where all the values will go
min_keys = []
#for loop for printing out 1 species
for key1, key2 in out_dict.iteritems():
#comparing key1 and key2 to see which values are smaller
    if key2 < current_min:
        current_min = key2
        min_keys = [key1]
    elif key2 == current_min:
#creates the value and
        min_keys.append(key1)
        for sentence in min_keys:
        	print (sentence + " has 1 species.") 
        	#print sentence +" has 1 species."
        	with open('1_species_output.txt', 'w') as outfile:
        		for sentence2 in min_keys: #prevents overwriting of output file
        			outfile.write(sentence2 + " has 1 species." + "\n")

print "Output file has been created"

#cannot get it working
#creating a user input where they will send a string through and make into an argument
#threshold = raw_input("Type in a threshold species number: ")
#current_min2 = threshold
#current_min2 = out_dict[out_dict.keys()[0]]
#raw input of the user putting in a number
#threshold = int(raw_input("Type in a threshold species number: "))
#for values in out_dict.values():
#comparing threshold values and if it's smaller than the values in the dictionary, it will save
#	if threshold <= out_dict.values():
#		if out_dict[values] <= out_dict.values():
#			for sentence2 in threshold: #to prevent overwriting of output file
#				print("Family XX has ", out_dict.values()) 
