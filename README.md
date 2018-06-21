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


Example of output vcf file (only the first 5 columns) and the compasrion with the input files: 

```
#################################################Conditioned OUT_VCF first 20 rows minus the header:
#####################e.g. position 89725#########
#CHROM	POS	ID	REF	ALT
1	83412	BovineHD0100000027	A	G
1	89725	BovineHD0100046367	G	A
1	100260	BovineHD0100000030	A	.
#################################################The second IN_VCF2:
#CHROM	POS	ID	REF	ALT
1	1	BovineHD0100028526	G	A
1	3	BovineHD0100009498	A	G
1	5	BovineHD0100016113	G	A
1	6	BovineHD0100016967	G	A
1	16947	BovineHD0100000005	C	A
1	36337	BovineHD0100000015	A	G
1	67130	BovineHD0100000024	A	.
1	78655	BovineHD0100000026	A	G
1	83412	BovineHD0100000027	A	G
1	89725	BovineHD0100046367	G	A
1	100260	BovineHD0100000030	A	G
#################################################The first IN_VCF1:
#CHROM	POS	ID	REF	ALT
1	83412	BovineHD0100000027	A	G
1	89725	BovineHD0100046367	C	T
1	100260	BovineHD0100000030	T	.

```
