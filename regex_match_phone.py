import re

phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
num = phone_num_regex.search('My number is 404-546-5578.')
print('Phone Number found: ' + num.group())

phone_num_regex = re.compile(r'\(\d{3}\)-\d{3}-\d{4}')
num = phone_num_regex.search('My number is (404)-546-5578.')
print('Phone Number found: ' + num.group())