"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s , then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
"""

def reverse_complement(str):
    complements = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }

    result = ""

    for nucleotide in str:
        result = complements[nucleotide] + result

    return result