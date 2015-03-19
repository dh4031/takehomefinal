import re #import regular expressions library
import glob #import glob module to read multiple file pathnames

#creates one output from multiple files
def parse_fasta2(filename):#
	with open('single_output_fasta.fa','w') as outfile: #creates a new file ready to write
		for fasta in path_names: #each path name into fasta
			with open(fasta) as infile: #opens up seq file
				for line in infile: 
					if line.startswith(">"):
						outfile.write(line)
					else:
						outfile.write(line.lower()) #writes the output of each file
	print 'A single output file called single_output_fasta.fa has successfully created.'

path_names = glob.glob('../fasta_problem/FEC[0-9][0-9][0-9][0-9][0-9]_[0-9].seq')
parse_fasta2(path_names)
