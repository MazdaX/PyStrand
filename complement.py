#!/usr/bin/python

'''

##==========================================================================##
##             		      Complementer -  PyStrand     		              ##
##             		                              					           ##
##                    Copyright (C) 2018  Dr.Mazdak Salavati                ##
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##
##  This program is free software: you can redistribute it and/or modify	##
##  it under the terms of the GNU General Public License as published by	##
##  the Free Software Foundation, either version 3 of the License, or		##
##  (at your option) any later version.						                 ##
##  This program is distributed in the hope that it will be useful,		   ##
##  but WITHOUT ANY WARRANTY; without even the implied warranty of	 	   ##
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the		       ##
##  GNU General Public License for more details.			               	##
##										                                         ##
##  You should have received a copy of the GNU General Public License		##
##  along with this program.  If not, see <http://www.gnu.org/licenses/>. 	##
##==========================================================================##
 
This is the script for VCF strand complementation.\n
The input VCF file will be complemented for REF and ALT nucleotides;\n
however the Genotypes will not be changes. This script is useful for \n
merging VCF files being produced by different technologies (strand difference).

NB. Only tested on python3.5
NB. Need to compile PyVCF and BioPython (both avialable via pip)

 
'''
import vcf #PyVCF https://pyvcf.readthedocs.io/en/latest/INTRO.html#
import sys
from Bio.Seq import Seq

"""
Reading the vcf file line by line
"""

'''
class VCFfiles(object):
    """ The input and output VCF class"""
    def __init__(self, name):
        self.name = name
    """ Garbage collector """
    def __del__(self):
        vcf_name = self.name
        print(vcf_name, "is ready!")
'''     

"""Reading the sys.argv except the python script itself [0]
"""
if len(sys.argv) < 2:
        print("\ne.g: ./complement.py [INPUT.vcf] [OUTPUT.vcf]")
        print("\nThe input and output file names should be passed",
              "as 1st and 2nd argument respectively \n\n\n\n")

"""Reading the sys.argv except the python script itself [0]
"""

IN_VCF = vcf.Reader(open(sys.argv[1] ,'r'))
OUT_VCF = vcf.Writer(open(sys.argv[2] ,'w'), IN_VCF)


""" The complementor loop
"""
  
for record in IN_VCF:
	record.REF=Seq(str(record.REF)).complement()
	#Taking the second element of the list [,A|C|G|T,] or [,None,]
	record.ALT=Seq(str(record.ALT)).complement()[1]
	#lamba for fixing the N (None)
	record.ALT=[w.replace("N",".") for w in record.ALT]
	OUT_VCF.write_record(record)


"""Clean up
"""
OUT_VCF.close()
