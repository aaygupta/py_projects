# pip install pyinputplus 
import pyinputplus as pyip
import random, time

num_of_ques = 5
correct_ans = 0
for ques_no in range(num_of_ques):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (ques_no+1, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out off tries!')
    else:
        print('Correct!')
        correct_ans += 1

    time.sleep(1)

print('Score: %s / %s' % (correct_ans, num_of_ques))