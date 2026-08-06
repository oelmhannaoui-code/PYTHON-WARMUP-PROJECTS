# QUIZ GAME
answers = []
def welcome():
    print('Welcome to the Quiz GAME')
    print('Provide the right answers')
def quiz1():
    print('what martial art is known as the art of 8 limbs?')
    print('1. Aikido.')
    print('2. Sambo.')
    print('3. Muay thai.')
    choice = int(input('Enter your choice: '))
    if choice == 3:
        answers.append(1)
        print('CORRECT')
    else:
        print('WRONG ANSWER!')
def quiz2():
    print('what do we call a friendly technical combat in training?')
    print('1. Scar.')
    print('2. Spar.')
    print('3. Star.')
    choice = int(input('Enter your choice: '))
    if choice == 2:
        answers.append(1)
        print('CORRECT')
    else:
        print('WRONG ANSWER!')
def quiz3():
    print('where do we use the suplex?')
    print('1. Tai chi.')
    print('2. Sanda.')
    print('3. Wrestling.')
    choice = int(input('Enter your choice: '))
    if choice == 3:
        answers.append(1)
        print('CORRECT')
    else:
        print('WRONG ANSWER!')
def quiz4():
    print('what do we call deformed fighters ears ?')
    print('1. brussels sprouts ears.')
    print('2. tomato ears.')
    print('3. cauliflowers ears.')
    choice = int(input('Enter your choice: '))
    if choice == 3:
        answers.append(1)
        print('CORRECT')
    else:
        print('WRONG ANSWER!')
def quiz5():
    print('what does mean MMA ?')
    print('1. Mexican Martial Arts.')
    print('2. Mixed Martial Arts.')
    print('3. Mystery Made Abstract .')
    choice = int(input('Enter your choice: '))
    if choice == 2:
        answers.append(1)
        print('CORRECT')
    else:
        print('WRONG ANSWER!')
def results():
    score = sum(answers)
    print('Your score is :', score,'/5')
    if score >= 5:
        print('OUTSTANDING !!')
    elif score >= 4:
        print('Excellent !!')
    elif score >= 3:
        print('You can do better !.')
    elif score >= 2:
        print('are you even trying ')
    elif score >= 1:
        print('eat your vegetables bro :/')
welcome()
quiz1()
quiz2()
quiz3()
quiz4()
quiz5()
results()
