from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    # return True if answer == 2 else False      #remove this
    return True if question["answer"] == answer else False


def lifeLine(ques, quesNum):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    num = ques["answer"]
    lis = [' ', ques["option1"], ques["option2"], ques["option3"], ques["option4"]]
    x = 4 if num - 1 == 0 else num - 1
    y = 1 if num + 1 == 5 else num + 1

    print(f'\tQuestion {quesNum}: {ques["name"]}' )
    print(f'\t\tOptions:')
    for i in range(1, 5):
        if i == x or i == y:
            print('\t\t\t')
        else:
            print(f'\t\t\tOption {i}: {lis[i]}')


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print("\n\n                        WELCOME TO KE BHAIL CROREPATI !!", end = '\n\n')
    print("------------------------------------------------------------------------------------------", end = '\n')
    print("------------------------------------------------------------------------------------------", end = '\n\n')

    money = 0
    flag = 1
    won = 1
    for i in range(15):

        if i == 0:
            print("First Level!! -> Minimum Money: 0", end = '\n\n')
        elif i == 5:
            print("Second Level!! -> Minimum Money: 10,000", end = '\n\n')
        elif i == 10:
            print("Third Level!! -> Minimum Money: 3,20,000", end = '\n\n')

        print(f'\tQuestion {i + 1}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')

        ans = input('Your choice ( 1-4 ) : ')

        while ans not in ['1', '2', '3', '4', 'lifeline', 'LIFELINE', 'quit', 'QUIT']:
            print("Invalid input!!\n")
            ans = input('Your choice ( 1-4 ) : ')


        if ans == "quit" or ans == "QUIT":
            print('You chose to quit!\n')
            print(f'\t Money Won: {money}')
            inp = input('What you would have chosen if you did not quit\n')
            res = isAnswerCorrect(QUESTIONS[i], int(inp))
            if res == True:
                print(f'\t {inp} would have been the right option!!\n')
            else:
                print('\tYou would have chosen the wrong option\n')
                print(f'\tThe correct option is {QUESTIONS[i]["answer"]}\n',)
            won = 0
            quit()

        if (ans == "lifeline" or ans == "LIFELINE") and flag == True and i != 14:
            flag = False
            lifeLine(QUESTIONS[i], i + 1)
            life = input('Your choice again: ')
            while life not in ['1', '2', '3', '4', 'lifeline', 'LIFELINE', 'quit', 'QUIT']:
                print("Invalid input!!\n")
                ans = input('Your choice again : ')
            ans = life

        # check for the input validations

        if isAnswerCorrect(QUESTIONS[i], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            money += QUESTIONS[i]["money"]
            print('\nMoney in Hand: {}'.format(money))

        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            print('\nThe correct answer was {}'.format(QUESTIONS[i]["answer"]))
            if i <= 4:
                print('\t Money Won: 0}')
            elif i <= 9:
                print('\t Money Won: 10,000')
            else:
                print('\t Money Won: 3,20,000')
            won = 0
            quit()
        
        print(end = '\n\n')
    
    if won == 1:
        print('Congrats!! You answered all the questions correctly!!\n')
        print(f'Total Money Won: {money}\n\n')

        # print the total money won in the end.


kbc()
