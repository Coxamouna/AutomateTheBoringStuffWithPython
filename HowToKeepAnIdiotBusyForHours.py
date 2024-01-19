import pyinputplus as pyip

def howToKeepAnIdiotBusy():
    while True:
        prompt = "Want to know how to keep an idiot busy for hours?\n"
        response = pyip.inputYesNo(prompt)
        if response in ['no', 'n']:
            return "Thank you. Have a nice day."
         
print(howToKeepAnIdiotBusy())
    