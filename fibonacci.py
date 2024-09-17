# 2. Verificação de número na sequência de Fibonacci em Python
def pertence_fibonacci(numero):
    fib1, fib2 = 0, 1
    while fib1 <= numero:
        if fib1 == numero:
            return f"O número {numero} pertence à sequência de Fibonacci."
        fib1, fib2 = fib2, fib1 + fib2
    return f"O número {numero} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero)
print(resultado)
