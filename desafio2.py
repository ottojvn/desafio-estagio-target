fibonacci = [0, 1]


def pertence(n):
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return n in fibonacci


def print_sequencia():
    print(fibonacci)


while (i := int(input("Digite um numero positivo ou -1 para sair: "))) != -1:
    if pertence(i):
        print(f"{i} pertence à sequencia de Fibonacci\n")
    else:
        print(f"{i} não pertence à sequencia de Fibonacci\n")