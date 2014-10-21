'''
Biopyth on study.py
Based on http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec12
Given: Fasta file
Output: Complete sequence record, its object representation, and length of sequence
'''
from Bio import SeqIO
for seq_record in SeqIO.parse("Input files/fasta.txt", "fasta"):
	print "-"*200
	print "Complete sequence record = \n",seq_record,"\n"
	print "Object representation = ",repr(seq_record.seq),"\n"
	print "Length = ",len(seq_record),"\n"
	print "-"*200

