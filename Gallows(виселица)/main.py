from random import randint

game_status = True
dictionary = open('dictionary', 'r', encoding='utf-8').read().split()

number = randint(0, len(dictionary))

# выбор рандомного слова из словаря
word = dictionary[number].lower()
print(word, len(word))

# как видит пользователь слово
secret_word = ['_'] * len(list(word))


def difficult():
    print("Выберите уровень сложности:\n-1\n-2\n-3")
    q = int(input())
    hp = 0
    if q == 1:
        hp = 10
    elif q == 2:
        hp = 5
    elif q == 3:
        hp = 3
    else:
        print("Недопустимый уровень сложности")
    return hp


def logic():
    global game_status

    new_lives = difficult()
    print('Оставшиеся жизни', new_lives)

    while game_status:

        if new_lives == 0:
            game_status = False
            print("Вы проиграли")
            break

        letter = input("Введите новую букву: ")

        if letter in word:
            print('Вы угадали букву!')
            for i in range(len(word)):
                if letter == word[i]:
                    secret_word[i] = letter
            # secret_word[word.index(letter)] = letter
            print(secret_word)

        else:
            new_lives -= 1
            print(f"Вы не угадали букву! Ваше здоровье: {new_lives}")
        if word == ''.join(secret_word):
            game_status = False
            print("Поздравляю, Вы выиграли!!!")
            break


while game_status:
    logic()
