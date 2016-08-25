#! /usr/bin/python

##### EXEC #####
#    This keyword is used to execute other python statements
#    Try to avoid using this, because it introduces (usually) unnecessary complexity
print "-- Exec --"
list_builder = "exec_list = [1,2,3,4,5,6,7]"
exec list_builder
print "exec_list: ", exec_list

function_builder = """
def exec_function():
\tprint "This function is created within an exec block"
"""

exec function_builder
exec_function()
