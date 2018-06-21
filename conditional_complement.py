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
        dtype={'#CHROM': str,
               'POS': int,
               'ID': str,
               'REF' : str,
               'ALT' : str}
        ).filter({'#CHROM','POS','ID','REF','ALT'}).rename(columns={'#CHROM':'CHROM'})

""" Creating a merger between the two files to match variants (concordant)
"""

d1 = read_vcf(1)
d2 = read_vcf(2)
d12 = pd.merge(d1[['CHROM','POS','ID']],
               d2,
               how='inner',
               on=['CHROM','POS','ID'],
               sort=False)
d12 = d12.set_index('ID')

#print("The SNVs in concordance w/ and w/o different STRAND GT:\n")
#print(d12.index)


""" Using concordant hits to flip allele (swap strand) for both REF an ALT
"""

for record1 in IN_VCF1:
    if (str(record1.ID) in d12.index.tolist()):
        if (str(record1.REF) != d12.loc[str(record1.ID)]['REF']):
            record1.REF=Seq(str(record1.REF)).complement()
        #redundant check
        #if (str(record1.ALT) != d12.loc[str(record1.ID)]['ALT']):
            record1.ALT=Seq(str(record1.ALT)).complement()[1]
            record1.ALT=[N.replace("N",".") for N in record1.ALT]
    OUT_VCF.write_record(record1)

  
""" Clean up
"""
OUT_VCF.close()
