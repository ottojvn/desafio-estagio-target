str = input("Digite uma string qualquer: ")

def inverte_string(str):
    if str == "" or len(str) == 1:
        return str
    
    str_invertida = ""
    for i in range(len(str) - 1, -1, -1):
        str_invertida += str[i]

    return str_invertida

print(inverte_string(str))
