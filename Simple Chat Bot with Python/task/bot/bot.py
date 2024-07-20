def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test(questions, option_list, correct_answers_list):
    print("Let's test your programming knowledge.")

    # write your code here
    print(questions)

    for i in option_list:
        print(i)

    # check if input is correct
    while len(correct_answers_list) != 0:

        print('Pick a number: ')
        answer = int(input())

        if answer in correct_answers_list:
            print('Congratulations!')
            correct_answers_list.remove(answer)

        else:
            print('Please, try again.')

    return print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()

question = 'Which properties are true for lists?'
option1 = '1. Lists are iterable.'
option2 = '2. Lists cannot be duplicated.'
option3 = '3. Lists can contain objects of different types.'
option4 = '4. Lists cannot be empty.'

option = [option1, option2, option3, option4]
correct_answers = [1, 3]

test(question, option, correct_answers)
# ...
end()
