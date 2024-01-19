import pyinputplus as pyip

breadPrices = {"wheat": 1.51, "white": 1.32, "sourdough": 1.65}
proteinPrices = {"chicken": 0.75, "turkey": 1.02, "ham": 0.50, "tofu": 1.07}
cheesePrices = {"cheedar": 0.10, "swiss": 0.35, "mozzarella": 0.20}
total = 0

print("Welcome to Andreea Tonciu's Sub Van! May I take your order, please?")

bread = pyip.inputMenu(["wheat", "white", "sourdough"], prompt = "Available bread: \n", numbered = True)
total += breadPrices[bread]

protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], prompt = "Available protein: \n", numbered = True)
total += proteinPrices[protein]

prompt = "Would you like to add cheese?\n"
cheeseYesNo = pyip.inputYesNo(prompt)
if cheeseYesNo in ['y', 'yes']:
    cheese = pyip.inputMenu(["cheedar", "swiss", "mozzarella"], prompt = "Available cheese: \n", numbered = True)
    total += cheesePrices[cheese]

prompt = "Would you like to add mayo?\n"
mayoYesNo = pyip.inputYesNo(prompt)
if mayoYesNo in ['y', 'yes']:
    total += 0.01

prompt = "Would you like to add mustard?\n"
mustardYesNo = pyip.inputYesNo(prompt)
if mustardYesNo in ['y', 'yes']:
   total += 0.01

prompt = "Would you like to add lettuce?\n"
lettuceYesNo = pyip.inputYesNo(prompt)
if lettuceYesNo in ['y', 'yes']:
   total += 0.02

prompt = "Would you like to add tomatoes?\n"
tomatoYesNo = pyip.inputYesNo(prompt)
if tomatoYesNo in ['y', 'yes']:
   total += 0.02

prompt = "How many subs would you like?\n"
noOfSubs = pyip.inputInt(prompt)
total *= noOfSubs

print(f"Your total for {noOfSubs} subs is £{round(total, 2)}, zana mea! Cash or card?")

# debugging:
# print(type(bread)) # <class 'str'>
# print(type(breadPrices[bread])) # <class 'float'>
# print(type(breadPrices)) # <class 'dict'>
