def some_function(one_parameter, another_parameter, a_third_parameter):
    print "The parameter 'one_parameter' is equal to:", one_parameter
    print "The parameter 'another_parameter' is equal to:", another_parameter
    print "The parameter 'a_third_parameter' is equal to:", a_third_parameter

#print 'Unnamed parameters'
#some_function(1,2,3)

#print 'Named parameters - the order doesnt import'
#some_function(another_parameter = "another parameter", one_parameter = "1_plaalarameter", a_third_parameter = "param 3")

# some_list = [1,2,3]
# some_function(*some_list)
#
# some_dictionary = {"another_parameter" : "another parameter", "one_parameter" : "1_parameter", "a_third_parameter" : "param 3"}
# some_function(**some_dictionary)

# def some_function(param1, param2):
#     print param1, param2
#
# some_function(1,2)
#
# some_function(param2 = 1, param1 = 2)
#
# some_list = [1,2]
# some_function(*some_list)
#
# some_dict = {"param1" : 38, "param2": "40deg 2"}
# some_function(**some_dict)
#>>>parameter 1 parameter 2

def some_other_function(*args, **kwargs):
    for arg in args:  #args is like a list
        print arg
    for kwarg in kwargs:  #kwargs is like a dictionary
        print kwarg, kwargs[kwarg]
x = 1
y = 2
z = ['a', 'b']
a_dict = {'hello': 'World!'}
a_tuple = (1,2,3,4,5)

some_other_function(x, y, z, some_dictionary = a_dict, some_tuple = a_tuple)     
