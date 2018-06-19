#!/usr/bin/python

"""
 This is the script for VCF strand conditional swapping 

"""
import sys
import io
import os
import vcf
import vcf.utils
import pandas as pd
import itertools as it
from Bio.Seq import Seq

"""Parsing the vcf files using sys.argv
"""


if len(sys.argv) < 3:
        print("\ne.g: ./complement.py [INPUT_WORK_ON.vcf] [INPUT_MATCH_TO.vcf] [OUTPUT.vcf]")
        print("\nThe inputs and output file names should be passed",
              "as 1st (work on), 2nd (match to) and 3rd argument ",
              "respectively \n\n\n\n")

"""Reading the sys.argv except the python script itself [0]
"""

IN_VCF1 = vcf.Reader(open(sys.argv[1] ,'r'))
IN_VCF2 = vcf.Reader(open(sys.argv[2] ,'r'))
OUT_VCF = vcf.Writer(open(sys.argv[3] ,'w'), IN_VCF1)


""" https://gist.github.com/dceoy/99d976a2c01e7f0ba1c813778f9db744
"""

def read_vcf(tally):
    with open(sys.argv[tally],'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_table(
        io.StringIO(str.join(os.linesep, lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str}
        ).filter({'#CHROM','POS','ID'}).rename(columns={'#CHROM':'CHROM'})

""" Creating a merger between the two files to match variants (concordant)
"""

d1 = read_vcf(1)
d2 = read_vcf(2)
d12 = pd.merge(d1,d2,how='inner',on=['CHROM','POS','ID'])
#d12_set = d12.loc[:,['CHROM','POS']]
d12_set = tuple(d12.loc[:,['CHROM','POS']])

""" Using concordant hits to flip allele (swap strand) for both REF an ALT
"""

for (record1,record2) in zip(IN_VCF1,IN_VCF2):
    #Casting Tally as list (tupple) for finding hits
    tally = tuple([record1.CHROM, record1.POS])
    #hit = [list(filter(lambda x: x in tally, sublist)) for sublist in d12_set]
    #bool(set(tally).intersection(d12_set))
    if (bool(set(tally).intersection(d12_set))):
        if(record1.REF != record2.REF):
            record1.REF=Seq(str(record1.REF)).complement()
        elif(record1.ALT != record2.ALT):
            record1.ALT=Seq(str(record1.ALT)).complement()[1]
            #lamba for fixing the N (None)
            record1.ALT=[N.replace("N",".") for N in record1.ALT]
        else:
            print("No variant was found in concordance")
    #Writing it out
    OUT_VCF.write_record(record1)
   
""" Clean up
"""

OUT_VCF.close()
