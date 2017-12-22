# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

print s[0:5] + t[6:]

# Insert the proper slicing indices for the substring variable
# so that the slice is a string that contains everything after "A NOUN".
# For example, if we wanted to store everything after "went", the returned
# string would be equal to sentence[11:].

sentence = "A NOUN went on a walk."
substring = sentence[6:]
print substring

# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB"
# in substring3.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]


# Set noun_replacement and verb_replacement to your own noun and verb strings.
# Then, concatenate the variables substring1-3, noun_replacement, and
# verb_replacement and assign the result to the variable new_sentence so that
# it's in the same order as the variable sentence.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "Louis" # your noun here
verb_replacement = "run" # your verb here

new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3
# your code here
print new_sentence
