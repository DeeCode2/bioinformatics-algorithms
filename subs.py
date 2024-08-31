"""
Finding a Motif in DNA

Given: Two DNA strings s and t (each of length at most 1 kbp)
Return: All locations of t as a substring of s.
"""

def subs(s, t):
    k = len(t)
    locations = []

    for i in range(len(s)):
        if s[i:i+k] == None:
            break
        if s[i:i+k] == t:
            locations.append(i)
    
    return locations