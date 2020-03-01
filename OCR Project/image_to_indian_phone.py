from PIL import Image
import os, pyperclip, re
from pytesseract import image_to_string

path = os.path.dirname(os.path.realpath(__file__))
input_path = path + '/Input/'

all_text = []

for root, dirs, filenames in os.walk(input_path):
    for filename in filenames:
        try:
            img = Image.open(input_path + filename)
            all_text.append(image_to_string(img))
        except:
            continue

# +91 95959 59595
phone_regex = re.compile(r'''(
    (\+91)?                                     # country code
    (\s|-|\.)?                                  # seperator
    (\d{5})                                     # 5 digits
    (\s|-|\.)?                                  # seperator
    (\d{5})                                     # 5 digits
)''', re.VERBOSE)

text = str('\n'.join(all_text))

matches = []
phone_num = ''

for groups in phone_regex.findall(text):
    phone_num = ''.join([groups[3], groups[5]])
    matches.append(phone_num)

if len(matches) > 0:
    distinct_matches = list(dict.fromkeys(matches))

    if len(matches)!=len(distinct_matches):
        print(str(len(matches)-len(distinct_matches)) + ' Duplicates Removed')
    else:
        print('No duplicates found!')

    pyperclip.copy('\n'.join(distinct_matches))
    print('Copied to clipboard')
else:
    print('No Phone no. was found!!')