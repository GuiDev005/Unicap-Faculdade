def f(x): 
    return x**3 - x - 2 # Função escolhida

def metodo_bissecao(a, b, max_iter=30): # Método da bisseção
    imagem_a = f(a) # Aqui armazena a imagem da substituição de x na função pelo valor inicial do intervalo
    imagem_b = f(b) # Aqui armazena a imagem da substituição de x na função pelo valor final do intervalo

    if imagem_a * imagem_b > 0:
# A imagem com o valor A multiplicado pela imagem com o valor B, na função, tem que ser menor ou igual 0 para ter raiz no intervalo selecionado.
        print("O intervalo não contém raiz.") # Sendo maior que 0, não tem raiz e o programa mostra essa mensagem 
        return None

    for i in range(max_iter): # Aqui começa um looping de no máximo 30 repetições para achar a raiz, seja ela aproximada ou não
        
        raiz = (a + b) / 2 # A partir dessa operação, é obtido o intervalo exato entre o número de A e número de B
        imagem_raiz = f(raiz) # O valor obtido em raiz vai ser jogado na função e o resultado da função vai ser armazenado em outra variável para verificação
        
        if imagem_raiz == 0:  # Condição que encontra a raiz exata, para o programa e exibe resposta
            return raiz

        if imagem_a * imagem_raiz < 0: # Imagem de f(a) multiplicado pela imagem de f(raiz)(raiz = intervalo de A e B) for negativo
            b = raiz # B assume o valor do intervalo
            imagem_b = imagem_raiz # Atualiza a imagem de f(b) para a f(raiz)
        else: # Caso contrário a "if imagem_a * imagem_raiz < 0:" ele:
            a = raiz # Atualiza o valor de a para raiz
            imagem_a = imagem_raiz # Atualiza a imagem de f(a) para a f(raiz)

    
    return (a + b) / 2

# Programa para entrada do usuário
try:
    # Entrada de usuário
    print("x**3 - x - 2 ")
    a = float(input("Digite o primeiro número do intervalo: "))
    b = float(input("Digite o segundo número do intervalo: "))
    
    if a >= b: # Não aceita a primeira entrada sendo menor que a segunda
        print("Intervalo inválido: o primeiro número deve ser menor que o segundo.")

    else:

        raiz = metodo_bissecao(a, b) # Chama o método da Bisseção
        if raiz is not None:
            print(f"A raiz aproximada é: {raiz:.6f}")

except ValueError:
    print("Digite apenas números válidos!")

