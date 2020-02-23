import pyperclip, re
# pip install pyperclip

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                          # area code
    (\s|-|\.)?                                  # seperator
    (\d{3})                                     # 3 digits
    (\s|-|\.)?                                  # seperator
    (\d{4})                                     # last 4 digits
    (\s*(ext|x|ext.|Ext|Ext.)\s*(\d{2,5}))?     # extension
)''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                           # username
    @                                           # @ symbol
    [a-zA-Z0-9.-]+                              # username
    (\.[a-zA-Z]{2,4})                           # dot something
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
phone_num = ''

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No Email or Phone No. was found!!')