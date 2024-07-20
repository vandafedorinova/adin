from collections import defaultdict

my_dict = defaultdict(lambda: None)
my_dict['key1'] = 'value1'
my_dict['key2'] = 'value2'

# Accessing a missing key will return the default value
print(my_dict['key3'])  # Output: None
