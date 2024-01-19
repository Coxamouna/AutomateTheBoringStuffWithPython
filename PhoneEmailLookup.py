# finds phone numbers and email addresses on the clipboard.
import pyperclip, re

# phone regex:
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # groups[1]: area code
    (\s|-|\.)?                        # groups[2]: separator
    (\d{3})                           # groups[3]: first 3 digits
    (\s|-|\.)                         # groups[4]: separator
    (\d{4})                           # groups[5]: last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # groups[6]: extension
    )''', re.VERBOSE)                 # groups[0] = all

# email regex:
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                 # groups[1]: username
    @                                 # groups[2]: @ symbol
    [a-zA-Z0-9.-]+                    # groups[3]: domain name
    (\.[a-zA-Z]{2,4})                 # groups[4]: dot-something
    )''', re.VERBOSE)                 # groups[0] = all

# find matches in clipboard text:
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
# copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied results to clipboard: ")
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')