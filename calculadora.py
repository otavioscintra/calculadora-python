import os
import time

def int_or_float(x):
    num1 = float(x)
    if num1.is_integer():
        num1 = int(num1)
    return num1
    
def add(x,y):
    return x + y 

def subtract(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

def potentiation(x,y):
    return x ** y

def rest_of_division(x,y):
    return x % y

def square_root(x):
    return x ** 0.5

list_of_counts = []

print('Calculadora')

while True:
    print('Escolha a operação desejada',
                            '1- Soma','2- Subtração','3- Multiplicação','4- Divisão',
                            '5- Potenciação','6- Resto de divisão','7- Raiz quadrada',
                            'H- Ver histórico','S- Sair', sep='\n')

    chosen_operation = input('Número da operação desejada: ')

    if chosen_operation == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        first_digit = input('Primeiro número da soma: ')
        second_digit = input('Segunda número da soma: ')
        try:
            num1 = int_or_float(first_digit)
            num2 = int_or_float(second_digit)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Você não digitou um número. Tente novamente.')
            time.sleep(1.5)
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        result = add(num1,num2)
        count = f'{num1} + {num2} = {result}'
        list_of_counts.append(count)
        print(count)
        time.sleep(2.2)

    elif chosen_operation == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        first_digit = input('Primeiro número da subtração: ')
        second_digit = input('Segunda número da subtração: ')
        try:
            num1 = int_or_float(first_digit)
            num2 = int_or_float(second_digit)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Você não digitou um número. Tente novamente.')
            time.sleep(1.5)
            continue
        
        os.system('cls' if os.name == 'nt' else 'clear')
        result = subtract(num1,num2)
        count = f'{num1} - {num2} = {result}'
        list_of_counts.append(count)
        print(count)
        time.sleep(2.2)

    elif chosen_operation == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        first_digit = input('Primeiro número da multiplicação: ')
        second_digit = input('Segunda número da multiplicação: ')
        try:
            num1 = int_or_float(first_digit)
            num2 = int_or_float(second_digit)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Você não digitou um número. Tente novamente.')
            time.sleep(1.5)
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        result = multiplication(num1,num2)
        count = f'{num1} * {num2} = {result}'
        list_of_counts.append(count)
        print(count)
        time.sleep(2.2)

    elif chosen_operation == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        first_digit = input('Primeiro número da divisão: ')
        second_digit = input('Segunda número da divisão: ')
        try:
            num1 = int_or_float(first_digit)
            num2 = int_or_float(second_digit)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Você não digitou um número. Tente novamente.')
            time.sleep(1.5)
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            result = division(num1,num2)
            count = f'{num1} / {num2} = {result}'
            list_of_counts.append(count)
            print(count)
            time.sleep(2.2)
        except ZeroDivisionError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Não é possível dividir por Zero. Tente novamente.')
            time.sleep(1.5)
            continue


    elif chosen_operation == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        first_digit = input('Base da pontenciação: ')
        second_digit = input('Expoente da potenciação: ')
        try:
            num1 = int_or_float(first_digit)
            num2 = int_or_float(second_digit)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Você não digitou um número. Tente novamente.')
            time.sleep(1.5)
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        result = potentiation(num1,num2)
        count = f'{num1} ** {num2} = {result}'
        list_of_counts.append(count)
        print(count)
        time.sleep(2.2)

    elif chosen_operation == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        first_digit = input('Primeiro número da divisão: ')
        second_digit = input('Segunda número da divisão: ')
        try:
            num1 = int_or_float(first_digit)
            num2 = int_or_float(second_digit) 
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Você não digitou um número. Tente novamente.')
            time.sleep(1.5)
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            result = rest_of_division(num1,num2)
            count = f'{num1} % {num2} = {result}'
            list_of_counts.append(count)
            print(count)
            time.sleep(2.2)
        except ZeroDivisionError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Não é possível dividir por Zero. Tente novamente.')
            time.sleep(1.5)
            continue

    elif chosen_operation == '7':
        os.system('cls' if os.name == 'nt' else 'clear')
        first_digit = input('Radicando da raiz quadrada: ')
        
        try:
            num1 = int_or_float(first_digit)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Você não digitou um número. Tente novamente.')
            time.sleep(1.5)
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        result = square_root(num1)
        count = f'√{num1} = {result:.2f}'
        list_of_counts.append(count)
        print(count)
        time.sleep(2.2)

    elif chosen_operation.lower() == 'h':
        os.system('cls' if os.name == 'nt' else 'clear')

        if list_of_counts == []:
           print('Histórico vazio')

        i = 0
        for count in list_of_counts:
            i += 1
            print(f'{i}. {count}')

        option_chosen = input('[V]oltar ao inicio | [S]air : ')
        if option_chosen.lower() == 'v':
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(0.5)
            continue

        elif option_chosen.lower() == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(0.5)
            break

                

    elif chosen_operation.lower() == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        break


    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Você não escolheu uma das opções abaixo. Tente novamente.')
        time.sleep(1.5)
        continue

print('Você saiu.')



        