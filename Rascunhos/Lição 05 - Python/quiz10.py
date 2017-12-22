# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = 'Zip is a file format used for data compression and archiving. A zip file contains one or more files that have been compressed, to reduce file size, or stored as is. The zip file format permits a number of compression algorithms.'

# ENTER CODE BELOW HERE
primeira_ocorrencia = text.find("zip")
segunda_ocorrencia = text.find("zip", primeira_ocorrencia + 1)

print segunda_ocorrencia

# IMPORTANT BEFORE SUBMITTING:
# You should only have one print command in your function
