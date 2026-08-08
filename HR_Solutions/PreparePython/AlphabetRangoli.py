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

#size 10

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------

# 

def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase

    # Create the rangoli pattern
    lines = []
    for i in range(size):
        # Create the line with the appropriate letters and dashes
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        # Center the line and add it to the list of lines
        lines.append((s).center(size * 4 - 3, '-'))

    # Print the rangoli pattern
    print('\n'.join(lines[::-1] + lines[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)