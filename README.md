# PyStrand
Python scripts for changing strand orientation of a VCF file (non-Illumina format [ACGT]) containing bi-allelic SNVs only:

1. Complementer (complement.py) will swap the VCF strand based on it self (Complementing the REF/ALT).
2. Conditional complementer (conditional_comeplement.py) will swap strand to match another vcf file. 

NB. This script only works for BiAllelic SNVs (for INDEL or multi allelic might need adjustment)
NB. Feed the files to the script in an increasing order of VCF length. (small match to large)

Extensive use of the following libraries: 

1. PyVCF https://pyvcf.readthedocs.io/en/latest/INTRO.html#
2. BioPython https://biopython.org/
3. Pandas http://pandas.pydata.org/
