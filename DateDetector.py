import re, pyperclip

# date regex:
dateRegex = "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
clipboard = str(pyperclip.paste())
print(re.findall(dateRegex, clipboard))

# import datevalid
# # find matches in clipboard text:
# clipboard = str(pyperclip.paste())
# matches = []

# for match in dateRegex.findall(clipboard):
#     day, month, year = match
#     if datevalid.isValidDate(int(day), int(month), int(year)):
#         matches.append('/'.join([day, month, year]))

# Debugging output
# print("Clipboard text:")
# print(clipboard)
# print("Extracted matches:")
# print(matches)

# # copy results to clipboard:
# if len(matches) > 0:
#     pyperclip.copy('\n'.join(matches))
#     print("Copied results to clipboard:")
#     print('\n'.join(matches))
# else:
#     print('No valid date found.')