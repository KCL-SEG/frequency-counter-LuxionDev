"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    freq = {}
    if len(items) > 0:
        if len(freq) == 0:
            freq[str(items[0])] = 0
        for item in items:
            print(str(item))
            if str(item) in freq.keys():
                freq[str(item)] += 1
            else:
                freq[str(item)] = 1

    print(freq)    
    return freq