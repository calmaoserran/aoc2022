#!/usr/bin/python3

def find_marker(signal: str,marker_len: int) -> int:
    """
    Looks for the first occurence of N characters that are all different in a string
    Arguments:
        signal: string to be parsed
        marker_len: length of the marker
    Returns:
        String index of the marker's first character
    """
    # Start iterating from marker_len to avoid iterating over smaller than marker_len strings
    for idx in range(marker_len,len(signal)):
        # Use a set to find duplicates. If len is marker_len there is no dupes
        if len(set(signal[idx-marker_len:idx])) == marker_len:
            return idx
    
if __name__ == "__main__":
    # Read file into string
    file_name = 'input'
    signal = [line.rstrip() for line in open(file_name)][0]
    print(f'Challenge 1 solution: {find_marker(signal,4)}')
    print(f'Challenge 2 solution: {find_marker(signal,14)}')
