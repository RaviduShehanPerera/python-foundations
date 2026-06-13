score = 0


question1 = input("what is the capital of sri lanka?")
question1 = question1.lower()

if question1 == 'colombo':
    score += 1
    print ('you are correct')
else:
    print('wrong the answer is colombo')

question2 = input('what is the biggest export of sri lanka?')
question2 = question2.lower()

if question2 == 'tea':
    score += 1
    print ('you are correct')
else:
    print('wrong, the answer is tea')

question3 = input('which year did sri lanka get freedom?')
question3 = int(question3)
if question3 == 1948:
    score += 1
    print (f'you are correct')
else:  
    print('wrong the answer is 1948')

print (f'you scored :{score}/3 points')