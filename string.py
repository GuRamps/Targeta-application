# 5. Inversão de uma string sem usar funções prontas

def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

# Exemplo de uso
string = input("Informe uma string: ")
resultado = inverter_string(string)
print(f"String invertida: {resultado}")
