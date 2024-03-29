import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
print("Quiz Time!")

for questionNumber in range(1, numberOfQuestions + 1):
    # pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        # right answers are handled by allowRegexes
        # wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                              blockRegexes=[('.*', 'Incorrect!')],
                              timeout=12, limit=3)
    
    except pyip.TimeoutException:
        print('Out of time!')
    
    except pyip.RetryLimitException:
        print('Out of tries!')
    
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    
    time.sleep(1) # Brief pause to let user see the result.

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))