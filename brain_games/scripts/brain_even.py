import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name ? ')

    return name


def check_answer(name):
    print('Answer "yes" if the number is even, otherwise answer "no". ')
    gen_num = random.randrange(1, 1000, 1)
    print("Question: " + gen_num.__str__())
    answer = prompt.string()
    print("Your answer:" + answer)

    if gen_num % 2 == 0 and answer == "yes":
        print("Correct!")
        return 1
    elif gen_num % 2 == 0 and "yes" != answer:
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        print("Let's try again, " + name)
        return 0
    elif gen_num % 2 != 0 and "yes" == answer:
        print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
        print("Let's try again, " + name)
        return 0
    elif gen_num % 2 != 0 and "no" == answer:
        print("Correct!")
        return 1
    else:
        print("Let's try again, " + name)
        return 0


def main():
    print('Welcome to the Brain Games')
    name = welcome_user()
    i = 0
    while i < 3:

        if check_answer(name):
            i += 1
        else:
            i += 3
    if i == 3:
        print("Congratulations, " + name)


if __name__ == '__main__':
    main()
