import random
import time

print("Bem-vindo ao jogo de matemática!")
print("Responda o máximo que puder. Digite 'sair' para encerrar.\n")

pontos = 0
rodada = 1

while True:
    # Gera dois números e uma operação aleatória
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    operacao = random.choice(["+", "-", "*"])

    # Calcula o resultado certo
    if operacao == "+":
        resultado_certo = n1 + n2
    elif operacao == "-":
        resultado_certo = n1 - n2
    else:
        resultado_certo = n1 * n2

    # A linha abaixo foi corrigida: uso correto de f-string e o número da rodada
    print(f"Pergunta {rodada}: Quanto é {n1} {operacao} {n2}?")
    # A linha abaixo foi corrigida: chamada correta da função input
    resposta = input("→ ")

    if resposta.lower() == "sair":
        break

    # Verifica se é número (aceita números inteiros positivos ou negativos)
    # A verificação de número foi mantida, mas pode ser simplificada com um 'try-except'
    # para melhor legibilidade, mas mantive a lógica original corrigida.
    is_digit = resposta.isdigit()
    is_negative_digit = resposta.startswith("-") and resposta[1:].isdigit()

    if not is_digit and not is_negative_digit:
        print("Por favor, digite um número inteiro ou 'sair'.")
        continue

    # Converte a resposta para inteiro após a verificação
    try:
        resposta_int = int(resposta)
    except ValueError:
        # Isso não deve acontecer devido à verificação acima, mas é uma boa prática
        print("Erro interno na conversão de número.")
        continue

    # Compara a resposta
    if resposta_int == resultado_certo:
        pontos += 1
        print("Correto!")
    else:
        # A linha abaixo foi corrigida: uso correto de f-string
        print(f"Errado! A resposta certa era {resultado_certo}.")
    
    rodada += 1
    time.sleep(1)
    print("-" * 30)

# A linha abaixo foi corrigida: uso correto de f-string
print(f"\nFim do jogo! Você fez {pontos} ponto(s).")