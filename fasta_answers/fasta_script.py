import re #import regular expressions library
import glob #import glob module to read multiple file pathnames

#creates one output from multiple files
def parse_fasta2(filename):#
	with open('single_output_fasta.fa','w') as outfile: #creates a new file ready to write
		for fasta in path_names: #each path name into fasta
			with open(fasta) as infile: #opens up seq file
				for line in infile: #prevents from overwriting 
					if line.startswith(">"):
						outfile.write(line)
					else:
						outfile.write(line.lower().strip()) #writes the output of each file
	
print 'A single output file called single_output_fasta.fa has successfully created.'

path_names = glob.glob('../fasta_problem/FEC[0-9][0-9][0-9][0-9][0-9]_[0-9].seq')
parse_fasta2(path_names)

def log_file(filename):
	with open('log_file.txt','w') as outfile:
		outfile.write("sequence_header" + "," +  "length" + "\n")
		for fasta in path_names:
			with open(fasta) as infile:
				for line in infile:
					if line.startswith(">"):
						outfile.write(line.strip() + ",")
					else:
						hi = line.strip()
						outfile.write(hi)

def parse_fasta(filename):
	for fasta in path_names:
		with open(fasta) as seqfile:
			name = ""
			seqs = ""
			for line in seqfile:
				line = line.strip()
				if line.startswith(">"):
					if name != "":
						yield name, seqs
						seqs = ""
					name = line.lstrip(">")
				else: 
					seqs = seqs + line

for name, sequence in parse_fasta(path_names):
    print "{} is {} base pairs long".format(name, len(sequence))

parse_fasta(path_names)


