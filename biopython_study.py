'''
Biopython study.py
Tasks:
======
Given a FASTA file, output the complete sequence record, its object representation,
	and length of sequence
Reference:
==========
http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec12
http://biopython.org/DIST/docs/api/Bio.SeqIO-module.html
'''
from Bio import SeqIO
for seq_record in SeqIO.parse("Input files/fasta.txt", "fasta"): # SeqIO.parse returns an iterator giving SeqRecord objects
	print "-"*200
	print "Complete sequence record = \n",seq_record,"\n"
	print "Object representation = ",repr(seq_record.seq),"\n"
	print "Length = ",len(seq_record),"\n"
	print "-"*200