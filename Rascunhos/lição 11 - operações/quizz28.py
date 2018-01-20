# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list, element):
    result = -1
    count = 0
    for a in list:
        count = count + 1
        if a == element:
            result = count-1
            return result



print find_element(['CS101', 'CS373', 'CS212', 'CS101', 'CS373', 'CS262'], 'CS101')

#print find_element([1,2,3],3)
#>>> 2

#print find_element(['alpha','beta'],'gamma')
#>>> -1
