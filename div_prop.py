def dividir_proporcionalmente(numero, *proporcionais):
    # Calcula a soma dos números proporcionais
    soma_proporcionais = sum(proporcionais)
    
    # Lista para armazenar os resultados
    resultados = []
    
    # Calcula a parcela proporcional para cada número
    for proporcional in proporcionais:
        resultado = numero * (proporcional / soma_proporcionais)
        resultados.append(resultado)
    
    return resultados

# Número a ser dividido
numero = 180

# Dividir 180 diretamente proporcional a 2, 3 e 4
resultados = dividir_proporcionalmente(numero, 2, 3, 4)

# Imprimir os resultados
print("Os resultados da divisão proporcional são:")
for i, resultado in enumerate(resultados, 1):
    print(f"Parcela {i}: {resultado}")
