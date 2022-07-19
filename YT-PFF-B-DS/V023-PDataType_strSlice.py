s = 'abcdefghijklmnopqrstuvwxyz'
print(s[3:9])  # returns string from 3 to 8
print(s[:9])  # returns string from 0 to 8
print(s[3:])  # returns string from 3 to end of string 25

print(s[3:1000])  # returns string from 3 to end of string 25 evne though the 1000 index is not present in the string

print(s[5:1])  # returns empty string as begin is greater then the end index parameter, hence no slicing
