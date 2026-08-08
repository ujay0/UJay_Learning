# !/bin/python3
# The center of the rangoli has the first alphabet letter a, 
# and the boundary has the Nth alphabet letter (in alphabetical order).
# Starting by first incresing the size to then decreasing it.
#
# Input Format
# A single line containing the integer N.

# Output Format
# Print the alphabet rangoli in the format explained above.
# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
#size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase

    # Create the rangoli pattern
    lines = []
    for i in range(size):
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append((s).center(size * 4 - 3, '-'))

    # Print the rangoli pattern
    print('\n'.join(lines[::-1] + lines[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)