import re #import regular expressions library
import glob #import glob module to read multiple file pathnames
import fileinput

#this is to get the header and sequences from the file name
def parse_fasta(filename):#opens and closes the file when it is done
#lists multiple pathnames of all the files
	path_names = glob.glob('../fasta_problem/FEC[0-9][0-9][0-9][0-9][0-9]_[0-9].seq')
	for fasta in filename:
		with open(fasta) as seqfile:
			for line in seqfile:
				line = line.strip() #removes newline
				if line.startswith(">"): #creates header
					name = line
					print name
				else:
					seqs = line.lower() #creates the sequences and puts them into lowercase
					print seqs
					seqs_output = open("single_file_fasta_format.fa", "w")
					seqs_output.write(seqs)
					seqs_output.close()

def parse_fasta2(filename):#opens and closes the file when it is done
#lists multiple pathnames of all the files
	path_names = glob.glob('../fasta_problem/FEC[0-9][0-9][0-9][0-9][0-9]_[0-9].seq')
	with open('output_test.fa','w') as outfile:
		for fasta in path_names:
			with open(fasta) as infile:
				for line in infile:
					outfile.write(line)

path_names = glob.glob('../fasta_problem/FEC[0-9][0-9][0-9][0-9][0-9]_[0-9].seq') #lists multiple pathnames of all the files
for output in path_names:
	print output

def output_fasta():
	path_names = glob.glob('../fasta_problem/FEC[0-9][0-9][0-9][0-9][0-9]_[0-9].seq') #lists multiple pathnames of all the files
	parse_fasta(path_names)
	for output in fileinput.input(path_names):
		print output
