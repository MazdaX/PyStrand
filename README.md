# PyStrand
Python scripts for changing strand orientation of a VCF file (non-Illumina format [ACGT]):
1. Complementer (complement.py) will swap the VCF strand based on it self.
2. Conditional Complementer (conditional_comeplement.py) will swap strand to match another vcf file. (UNDER DEVELOPMENT)

NB. This script only works for BiAllelic SNVs (for INDEL or multi allelic might need adjustment)

NB. Feed the files to the script in an increasing order of VCF length. (small match to large)



Extensive use of the following libraries: 

1. PyVCF https://pyvcf.readthedocs.io/en/latest/INTRO.html#
2. BioPython https://biopython.org/
3. IterTools https://docs.python.org/3.5/library/itertools.html#module-itertools
4. NumPy http://www.numpy.org/
5. SciPy https://www.scipy.org/
6. Pandas http://pandas.pydata.org/



