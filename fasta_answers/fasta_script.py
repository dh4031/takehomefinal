import re #import regular expressions library
import glob #import glob module to read multiple file pathnames
import fileinput

#this is to get the header and sequences from the file name
def parse_fasta(filename):#opens and closes the file when it is done
	for hi in filename:
		with open(hi) as seqfile:
			for line in seqfile:
				line = line.strip() #removes newline
				if line.startswith(">"): #creates header
					name = line
					print name
				else:
					seqs = line #creates the sequences
					print seqs

def parse_fasta2(filename):#opens and closes the file when it is done
	for line in filename:
		line = line.strip() #removes newline
		if line.startswith(">"): #creates header
			name = line
			print name
		else:
			seqs = line #creates the sequences
			print seqs1



path_names = glob.glob('../fasta_problem/FEC[0-9][0-9][0-9][0-9][0-9]_[0-9].seq') #lists multiple pathnames of all the files
for output in path_names:
	print output

def output_fasta():
	path_names = glob.glob('../fasta_problem/FEC[0-9][0-9][0-9][0-9][0-9]_[0-9].seq') #lists multiple pathnames of all the files
	parse_fasta(path_names)
	for output in fileinput.input(path_names):
		print output
