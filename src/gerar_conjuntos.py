import random

def gerar_dataset(nome_arquivo, qtd):
    print(f"Gerando {nome_arquivo} com {qtd} registros...")
    with open(nome_arquivo, 'w') as f:
        for _ in range(qtd):
            f.write(f"{random.randint(1, qtd*10)}\n")
    print("Concluído.")

if __name__ == "__main__":

    gerar_dataset("conjunto_pequeno.txt", 100_000)
    gerar_dataset("conjunto_medio.txt", 5_000_000) 
    # O conjunto grande pode demorar até mesmo para ser construído.
    gerar_dataset("conjunto_grande.txt", 30_000_000)