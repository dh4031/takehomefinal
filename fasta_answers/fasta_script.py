import re #import regular expressions library
import glob #import glob module to read multiple file pathnames
import time #import time

#creates one output from multiple files
def parse_fasta2(filename):#
	with open('single_output_fasta.fa','w') as outfile: #creates a new file ready to write
		for fasta in path_names: #each path name into fasta
			with open(fasta) as infile: #opens up seq file
				for line in infile: #prevents from overwriting 
					if line.startswith(">"):
						outfile.write(line)
					else:
						outfile.write(line.lower()) #writes the output of each file
	
print 'A single output file called single_output_fasta.fa has successfully created.'

#getting the list of all pathfile names
path_names = glob.glob('../fasta_problem/FEC[0-9][0-9][0-9][0-9][0-9]_[0-9].seq')
parse_fasta2(path_names) #running te list of path file names to parse_fasta2 function

#log file function
def log_file(filename):
	with open('log_file.txt','w') as outfile: #opens up file for writing
#creates the title for sequence header and length
		outfile.write("sequence_header" + "," +  "length" + "\n")
		for fasta in path_names: 
			with open(fasta) as infile:
				for line in infile: #prevents from overwriting output file
					if line.startswith(">"): #gets the list of the names
						outfile.write(line.strip() + ",") #creates a comma after the sequence name
					else:
#gets sequence, however, cannot insert a new line because it just breaks apart all the DNA sequence
						sequence = line.strip() 
						outfile.write(sequence) #writes the sequence out to the output file
#printing what time and date the analysis was done on
		outfile.write("\n" + "Analysis was done on " + time.strftime("%c")) 

log_file(path_names) #testing the functino with path_names

#beta testing function to better seperate the sequence with a comma
#since the original fasta format file has a lot of newlines which breaks up the DNA sequences
#when appending the DNA sequences, the names of the sequencs gets mixed up with the sequence
def parse_fasta(filename):
	for fasta in path_names:
		with open(fasta) as seqfile: #opens up the file and closes it when it's done
			name = "" #create an empty list for names
			seqs = "" #create an empty list for sequences
			for line in seqfile:
				line = line.strip() #gets rid of newlines to turn into a list
				if line.startswith(">"): #gets the name
					if name != "":
						yield name, seqs
						seqs = ""
					name = line.lstrip(">") 
				else: 
					seqs = seqs + line #gets the sequence with the names in a list

parse_fasta(path_names) #testing function


