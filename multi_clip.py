import sys, pyperclip
# pip install pyperclip

TEXT = {
    'agree': """Agreed! Sounds good.""",
    'busy': """Sorry, busy schedule.""",
    'upsell': """Monthly Donation?"""
}

if len(sys.argv) < 2:
    print('Usage: py multi_clip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)