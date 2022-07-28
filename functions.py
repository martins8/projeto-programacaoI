from time import time
from random import randint


# FUNÇÃO QUE REGISTRA O USUÁRIO PARA DEPOIS, NO FIM, DO QUIZ ARMAZENAR SEU NOME E SEU SCORE EM UM ARQUIVO DE TEXTO.
def user_register():
    global username
    print(f'\n\033[33mOlá seja BEM VINDO AO QUIZ DE MATEMÁTICA, vejo que é\n'
          f'sua primeira vez nesse QUIZ. Logo, registre um '
          f'nome de\nusuário para que você consiga visualizar seu score depois.\033[m\n')
    username = str(input('USERNAME: ')).strip()


# FUNÇÃO DO MENU PRINCIPAL
def menu():
    print(f'{"-" * 56}\n'
          f'\033[33m{" QUIZ DE MATEMÁTICA".center(56)}\033[m\n'
          f'{"-" * 56}\n'
          f'{"escolha alguma opção digitando o número referente a ela:".center(56)}\n\n'
          f' [1] INICIAR QUIZ\t\t\t\t\t[2] FINALIZAR PROGRAMA\n\n'
          f' [3] SCORES\t\t\t\t\t\t\t[4] SAIBA MAIS\n')


# FUNÇÃO DA INTERATIVIDADE DO USUÁRIO COM O MENU
def options(number):
    if number == 1:
        print(f'\033[33mQUIZ INICIADO, TENHA UMA BOA JOGATINA!\n'
              f'Responda as questõs em, no máximo, 10 segundos para obter pontuação.\n'
              f'Caso erre, perderá uma vida\033[m\n'
              f'{"-" * 56}')
        game()

    elif number == 2:
        print(f'{"-" * 56}')
        print(f'\033[33mPROGRAMA FINALIZADO, VOLTE SEMPRE!\033[m\n')
        quit()

    elif number == 3:
        print(f'{"-" * 56}\n'
              f'\033[33m{"SCORES".center(56)}\033[m')
        userscorestxt = open("userScores.txt", "r")
        print(userscorestxt.read())
        userscorestxt.close()

        print(f'[1] VOLTAR AO MENU PRINCIPAL      [2] FINALIZAR PROGRAMA')
        option3 = int(input('Sua opção: '))
        if option3 == 1:
            menu()
            your_option3 = int(input('Sua opção: '))
            print(f'{"-" * 56}')
            options(your_option3)
        else:
            print(f'QUIZ FINALIZADO, VOLTE SEMPRE!')

    elif number == 4:
        print(f'\n\033[33m Esse QUIZ DE MATEMÁTICA, irá lhe desafiar com cálculos\n básicos, os quais deverão ser'
              f' resolvidos em um intervalo\n de 10 SEGUNDOS, senão, a questão será desconsiderada e\n você perderá '
              f'uma vida. Quando você acertar alguma questão\n você receberá uma pontuação e ao errar, perderá uma '
              f'vida. \n O jogador terá 3 vidas, ao perdê-las, o\n quiz será finalizado e sua pontuação será'
              f' registrada\033[m\n\n'
              f'[1] VOLTAR AO MENU PRINCIPAL      [2] FINALIZAR PROGRAMA')
        option4 = int(input('Sua opção: '))
        if option4 == 1:
            menu()
            your_option4 = int(input('Sua opção: '))
            options(your_option4)
        else:
            print(f'QUIZ FINALIZADO, VOLTE SEMPRE!')


# FUNÇÃO DO JOGO
def game():
    # CRIAÇÃO DE UMA LISTA A PARTIR DO ARQUIVO DE TEXTO QUE CONTÉM TODAS AS RESPOSTAS
    answerstxt = open("answers.txt", "r")
    answers = answerstxt.readlines()
    answerstxt.close()

    # CRIAÇÃO DE UMA LISTA A PARTIR DO ARQUIVO DE TEXTO QUE CONTÉM TODAS AS PERGUNTAS
    questionstxt = open("questions.txt", "r")
    questions = questionstxt.readlines()
    questionstxt.close()

    # VARIÁVEIS DE VIDA, SCORE E QUANTIDADE DE QUESTÕES
    score = 0
    life = 3
    amount_of_questions = 19

    # LOOP DO JOGO
    while life > 0 and amount_of_questions > 0:

        # VARIÁVEL QUE ARMAZENA UM NÚMERO ALEATÓRIO QUE SERÁ USADO PARA BUSCAR A PERGUNTA E SUA RESPECTIVA RESPOSTA
        # AS QUAIS ESTARÃO ARMAZENADAS EM UMA LISTA
        indice = randint(0, 18)

        # TRECHO DE CÓDIGO RESPONSÁVEL PELA IMPRESSÃO DA PERGUNTA E TAMBÉM DA BARRAGEM DE PERGUNTAS REPETIDAS
        while questions[indice] == "":
            indice = randint(0, 18)
        # VARIÁVEL DE TEMPO
        start = time()
        print(f'\033[32mVIDAS: {life}{" "*6}PLAYER: {username}\n\033'
              f'[mNº QUESTÕES REALIZADAS: {19-amount_of_questions}\n')
        print(f'\033[34m {questions[indice]}\033[m')
        your_answer = str(input(' Sua resposta: ')).strip()
        questions[indice] = ""
        amount_of_questions -= 1

        # CONDICIONAL DE ACERTO/ERRO DO USUÁRIO
        if your_answer == answers[indice].replace("\n", ""):
            end = time()
            if end - start > 10:
                life -= 1
                print(f'\n\033[31m Você acertou a questão, porém, ultrapassou o limite de\n tempo. Logo você '
                      f'não será pontuado por essa questão e perderá uma vida'
                      f'\n Tempo de resposta: {end - start:.2f} segundos.\033[m')
                print(f'{"-" * 56}')
            elif end - start <= 10:
                print(f'\n Parabéns, você acertou a questão!\n'
                      f'\033[31m Tempo de resposta: {end - start:.2f} segundos.\033[m')
                score += 1
                print(f'{"-" * 56}')
        elif your_answer != answers[indice].replace("\n", ""):
            print(f'\nInfelizmente, você errou :(!\n')
            life -= 1
            print(f'{"-" * 56}')

        # MENSAGEM DE FINALIZAÇÃO DO JOGO
        if life == 0:
            print(f'\033[31mGAME OVER\033[m')
        if amount_of_questions == 0:
            print(f'\033[32mVOCÊ ATINGIU O LIMITE DE QUESTÕES, PARABÉNS\033[m')

    # CÓDIGO PARA REGISTRAR O USUÁRIO E SEU RESPECTIVO SCORE
    userscorestxt = open("userScores.txt", "a")
    userscorestxt.write(f'{username} - {score}\n')
    userscorestxt.close()

    # RETORNO AO MENU
    menu()
    your_option_game = int(input('Sua opção: '))
    options(your_option_game)
