def bigger(a,b):
    if a > b:
        return a
    else:
        return b

bigger(3,5)

print bigger(3,5)

print bigger(5,3)

print bigger(0,-1)
print bigger(-1,0)

def is_friend(s):
    if s[0] == 'D':
        return 'Is friend'
    else:
        return 'Not friend'

print is_friend('Carl')
print is_friend('Daniel')
print is_friend('Deborah')
print is_friend('deno')

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9

def biggest2(a,b,c):
    return bigger(bigger(a,b),c)

biggest2(3,6,9)
biggest2(6,9,3)
