import numpy as np

list = [1, 2, 3]
print(type(list))

np_list = np.array(list)
print(type(np_list))
print(np_list.dtype)

""" 
Create an Array with all zeros

"""

zeros_np_array = np.zeros(shape= (5,))
print(zeros_np_array.dtype)
print(zeros_np_array)

""" 
Create an Array with all ones

"""

ones_np_array = np.ones(shape= (10, 2), dtype= 'int')
print(ones_np_array.dtype)
print(ones_np_array)

""" 
Create an Array assigned with a specific value

"""

np_array_assign_with_specific_values = np.full(
    shape= (5,),
    dtype= int,
    fill_value= 15
    )

print(np_array_assign_with_specific_values.dtype)

print(np_array_assign_with_specific_values)

"""
Create an empty array
"""

np_empty_array = np.empty(
    shape= (5,)
)
print(np_empty_array)

"""Type Cast
Conversion from one data type to another compatible data type
"""
print(np_empty_array.dtype)
np_empty_array_int = np_empty_array.astype('int')
print(np_empty_array_int)
print(np_empty_array_int.dtype)

"""Create Sequential array
"""
np_seq_array = np.arange(start= 1, stop= 10, step= 2)
print(np_seq_array)