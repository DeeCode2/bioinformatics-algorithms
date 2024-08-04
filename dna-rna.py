"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

def dna_to_rna(str):
    rna = ""
    for nucleotide in str:
        if nucleotide == "T":
            rna = rna + "U"
        else:
            rna = rna + nucleotide
    
    print(rna)

dna_to_rna("GATGGAACTTGACTACGTAAATT")

