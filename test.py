"""
Carlos Barona
my_test_code
"""

# install pylint in out virtual environment
# use it, correct errors and warnings
# acheive a score of 7.5 or higher with pylint

# import pdb

# 1
# import my_module and pprint
# add breakpoint to test your data
# view the data in your variables to ensure they are correct

# breakpoint()
import pprint
from pprint import pprint
import my_module
from my_module import my_json_data as my_data


# 2
# use the greeting method from my_module to print put your name
# add breakpoint to test your data
# view the data in your variables to ensure they are correct

# breakpoint()
print(my_module.greeting('Carlos'))

# 3
# use the letter_text module to print out a string
# add breakpoint to test your data
# view the data in your variables to ensure they are correct

# breakpoint()
print(my_module.letter_text(name = 'Carlos', amount = '12', denomination = 'Dollars'))


# 4
# use the my_module.my_json_data and print it out
# add breakpoint to test your data
# view the data in your variables to ensure they are correct

# breakpoint()
print(my_module.my_json_data)

# 5
# import the my_json_data as my_data and print out the my_json_data using pprint
# add breakpoint to test your data
# view the data in your variables to ensure they are correct

# breakpoint()
# from my_module import my_json_data as my_data

pprint(my_data)
