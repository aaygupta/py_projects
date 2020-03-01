import pyperclip, re
# pip install pyperclip

# +91 95959 59595
phone_regex = re.compile(r'''(
    (\+91)?                                     # country code
    (\s|-|\.)?                                  # seperator
    (\d{5})                                     # 5 digits
    (\s|-|\.)?                                  # seperator
    (\d{5})                                     # 5 digits
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
phone_num = ''

for groups in phone_regex.findall(text):
    phone_num = ''.join([groups[3], groups[5]])
    matches.append(phone_num)

if len(matches) > 0:
    distinct_matches = list(dict.fromkeys(matches))

    if len(matches)!=len(distinct_matches):
        print('Duplicates Removed')
    else:
        print('No duplicates found!')

    pyperclip.copy('\n'.join(distinct_matches))
    print('Copied to clipboard')
else:
    print('No Phone No. was found!!')