import random
import time
import os

# CONFIGURAÇÕES
EXECUTAR_TESTE_GRANDE = False

ARQUIVO_PEQUENO = "conjunto_pequeno.txt"
ARQUIVO_MEDIO = "conjunto_medio.txt"
ARQUIVO_GRANDE = "conjunto_grande.txt"

# Classes necessárias para os testes e questões
class Node:
    """Representa um nó na Árvore Binária."""
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    """
    Implementação de uma Árvore Binária de Busca (BST).
    Otimizada para buscas, mas com custo maior de inserção se não balanceada.
    """
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
            return

        # Se existir uma raiz, o nó atual recebe o valor da raiz
        no_atual = self.raiz

        while True:
            # Se valor for menor que atual, olha para a esquerda do no_atual
            if valor < no_atual.valor:
                if no_atual.esquerda is None:
                    no_atual.esquerda = Node(valor)
                    break
                else:
                    no_atual = no_atual.esquerda

            # Se valor for maior que atual, olha para a direita do no_atual
            elif valor > no_atual.valor:
                if no_atual.direita is None:
                    no_atual.direita = Node(valor)
                    break
                else:
                    no_atual = no_atual.direita
            else:
                break # Valor duplicado, Ignorar

    def buscar(self, valor):
        no_atual = self.raiz

        # Se não existe raiz
        if no_atual is None:
            return False

        while no_atual is not None:
            # Existe o valor na árvore
            if valor == no_atual.valor:
                return True
            # Valor é menor
            elif valor < no_atual.valor:
                no_atual = no_atual.esquerda
            # Valor é maior
            else:
                no_atual = no_atual.direita
        # Valor não existe na árvore
        return False

class Lista:
    """Implementação padrão de lista sequencial (Wrapper para list do Python)."""
    
    def __init__(self):
      self.items = []
      
    def inserir(self, valor):
        """
        Insere um valor ao final da lista.
        
        Parâmetros:
        - valor: valor a ser inserido.
        """
        self.items.append(valor)
    
    def inserirVarios(self, valores):
        """
        Insere múltiplos valores ao final da lista.
        
        Parâmetros:
        - valores: lista de valores a ser inserido.
        """
        self.items.extend(valores) # extend é mais rápido que um loop for append
    
    def buscar(self, valor):
        # Busca Linear: O(n)
        for item in self.items:
            if item == valor:
                return True
        return False

class ListaOtimizada:
    """
    Lista que mantém os dados ordenados para permitir Busca Binária.
    Custo alto de construção (Ordenação), mas custo baixo de busca (O(log n)).
    """
    
    def __init__(self):
        self.items = []
        
    def inserir(self, valor):
        """
        Insere um valor ao final da lista.
        
        Parâmetros:
        - valor: valor a ser inserido.
        """
        self.items.append(valor)
    
    def inserirVarios(self, valores):
        """
        Insere múltiplos valores ao final da lista.
        
        Parâmetros:
        - valores: lista de valores a ser inserido.
        """
        self.items.extend(valores) # extend é mais rápido que um loop for append
    
    def merge_sort(self, lista):
    
        """
        Método recursivo que implementa o algoritmo de ordenação Merge Sort
        
        Parâmetros:
        - lista: recebe uma lista, ordena e a retorna.
        """
        if len(lista) > 1:
            meio = len(lista) // 2  # meio
            metade_esquerda = lista[:meio]  # divide na metade esquerda
            metade_direita = lista[meio:]   # divide na metade direita
            
            # recursivamente ordena as duas metades
            self.merge_sort(metade_esquerda)
            self.merge_sort(metade_direita)
            
            ponteiro_e = ponteiro_d = ponteiro_r = 0
            
            # mescla as metades ordenadas
            while ponteiro_e< len(metade_esquerda) and ponteiro_d < len(metade_direita):
                if metade_esquerda[ponteiro_e] < metade_direita[ponteiro_d]:
                    lista[ponteiro_r] = metade_esquerda[ponteiro_e]
                    ponteiro_e+=1
                else:
                    lista[ponteiro_r] = metade_direita[ponteiro_d]
                    ponteiro_d += 1
                ponteiro_r += 1
            
            # verifica elementos restantes    
            while ponteiro_e < len(metade_esquerda):
                lista[ponteiro_r] = metade_esquerda[ponteiro_e]
                ponteiro_e += 1
                ponteiro_r += 1
            
            while ponteiro_d < len(metade_direita):
                lista[ponteiro_r] = metade_direita[ponteiro_d]
                ponteiro_d += 1
                ponteiro_r += 1
                
        return lista
                
    def ordenar(self):
        """
        Método que faz o processo de ordenação do objeto.
        ele chama o método merge_sort e atualiza a lista interna com o resultado
        """
        
        # chama o merge sort e armazena
        lista_ordenada = self.merge_sort(self.items)
        
        # atualiza lista interna
        self.items = lista_ordenada

    def busca_binaria(self, valor):
        esquerda = 0
        direita = len(self.items) - 1
        
        while esquerda <= direita:
            meio = esquerda + (direita - esquerda) // 2
            
            if self.items[meio] == valor:
                return True # achou
            elif self.items[meio] < valor:
                esquerda = meio + 1 # metade direita
            else:
                direita = meio - 1 # metade esquerda
        return False # não achou

#  === FUNÇÕES AUXILIARES ===

def ler_arquivo(arquivo):
    """
    Lê um arquivo txt e retorna os valores como uma lista de inteiros.
    
    Parâmetros:
    - arquivo: nome do arquivo txt a ser lido
    
    Retorna:
    - lista com os valores inteiros do arquivo
    """
    

    pasta_do_script = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(pasta_do_script, arquivo)
    

    
    if not os.path.exists(caminho_completo):
        print(f"\nArquivo '{arquivo}' não encontrado. Pulando testes relacionados.")
        return []
    
    try:
        valores = []
        with open(caminho_completo, "r") as arq:
            for linha in arq:
                valor = int(linha.strip())
                valores.append(valor)
            return valores
    except Exception as e:
        print(f"\nFalha ao ler {arquivo}: {e}")
        return




def gerar_valores_busca(valores, qtd, existente=True):
    """
    Gera valores para teste de busca em uma lista de dados selecionada.

    Parâmetros:
    - valores: A lista inteira de onde tirar a amostra.
    - quantidade: O número de valores a serem gerados.
    - existente: boolean que define se gera valores existentes ou não existentes na estrutura alvo

    Retorna:
    - Uma lista com a amostra de valores na lista passada como parâmetro (padrão: existentes).
    """
    
    if not valores: return []
    
    resultado = []
    if existente:
        # calcula um intervalo pra fazer o incremento nos indices de acordo com a quantidade passada
        intervalo = len(valores) // qtd
        
        # gera valores existentes na lista, pegando eles da propria lista por indice
        for i in range(qtd):
            indice = i * intervalo
            resultado.append(valores[indice])

    else:
        maior = max(valores)
        for x in range(maior + 1, (maior + (qtd + 1))):
            resultado.append(x)
    
    return resultado


def imprimir_separador(titulo):
    print(f"\n{'='*60}")
    print(f"{titulo.center(60)}")
    print(f"{'='*60}")


#  === FUNÇÕES PARA TESTES DO PONTO DE VIRADA ===
def encontrar_ponto_virada_busca():
    """
    Testa incrementalmente tamanhos de N para descobrir quando a 
    Árvore supera a Lista na busca de dados existentes e não existentes
    (considerando apenas tempo de busca).
    """
    dados = ler_arquivo("conjunto_pequeno.txt")

    quantidade = 10
    
    ponto_virada_inexistentes = None
    ponto_virada_existentes = None
    
    print("--> Executando testes incrementais...", end="", flush=True)
    while True:
        # gera quantidade inicial de dados para teste
        dados_teste = gerar_valores_busca(dados, quantidade)
        n = len(dados_teste)
        
        # verificação se ja achou os dois pontos de virada pra terminar a função
        if n <= 0 or (ponto_virada_inexistentes and ponto_virada_existentes):
            print(" Concluído!")
            break
        
        # instancia os objetos pros testes
        lista_ponto = Lista()
        arvore_ponto = Arvore()
        
        # insere os dados nos objetos
        lista_ponto.inserirVarios(dados_teste)
        for valor in dados_teste:
            arvore_ponto.inserir(valor)
            
        # gera os valores necessarios pra realizar as buscas    
        qtd_busca = quantidade // 2
        busca_inexistentes = gerar_valores_busca(dados_teste, qtd_busca, existente=False)
        busca_existentes = gerar_valores_busca(dados_teste, qtd_busca) 
        
        # inexistentes
        inicio_lista_inex = time.perf_counter()
        for v in busca_inexistentes: lista_ponto.buscar(v)
        tempo_lista_inex = time.perf_counter() - inicio_lista_inex
        
        inicio_arvore_inex = time.perf_counter()
        for v in busca_inexistentes: arvore_ponto.buscar(v)
        tempo_arvore_inex = time.perf_counter() - inicio_arvore_inex
        
        # Existentes
        inicio_lista_ex = time.perf_counter()
        for v in busca_existentes: lista_ponto.buscar(v)
        tempo_lista_ex = time.perf_counter() - inicio_lista_ex

        inicio_arvore_ex = time.perf_counter()
        for v in busca_existentes: arvore_ponto.buscar(v)
        tempo_arvore_ex = time.perf_counter() - inicio_arvore_ex
        

        if ponto_virada_inexistentes is None and tempo_arvore_inex < tempo_lista_inex:
            ponto_virada_inexistentes = n
        if ponto_virada_existentes is None and tempo_arvore_ex < tempo_lista_ex:
            ponto_virada_existentes = n
  
    
        quantidade += 10 
    
    if ponto_virada_inexistentes:
        print(f"[.] Buscas INEXISTENTES : Árvore supera Lista em N = {ponto_virada_inexistentes}")
    else:
        print(f"[x] Buscas INEXISTENTES : Ponto de virada não encontrado neste dataset.")
        
    if ponto_virada_existentes:
        print(f"[.] Buscas EXISTENTES   : Árvore supera Lista em N = {ponto_virada_existentes}")
    else:
        print(f"[x] Buscas EXISTENTES   : Ponto de virada não encontrado neste dataset.")
    print("-" * 60)
            
def encontrar_ponto_virada_total(tamanho):
    # ... configurações iniciais ...
    if tamanho == "pequeno":
        dados = ler_arquivo("conjunto_pequeno.txt")
        quantidade = 100
    elif tamanho == "medio":
        dados = ler_arquivo("conjunto_medio.txt")
        quantidade = 500000
    
    ponto_virada_inexistentes = None
    ponto_virada_existentes = None
    
    stats_inexistentes = {}
    stats_existentes = {}
    
    print(f"--> Iniciando Testes Incrementais ({tamanho.upper()})")
    while True:
        dados_teste = gerar_valores_busca(dados, quantidade)
        n = len(dados_teste)
        
        if n <= 0 or (ponto_virada_inexistentes and ponto_virada_existentes):
            break
            
        # ... instanciação e construção ...
        lista_ponto_total = Lista()
        arvore_ponto = Arvore()
        
        inicio_build_lista = time.perf_counter()
        lista_ponto_total.inserirVarios(dados_teste)
        tempo_build_lista = time.perf_counter() - inicio_build_lista
        
        inicio_build_arvore = time.perf_counter()
        for valor in dados_teste:
            arvore_ponto.inserir(valor)
        tempo_build_arvore = time.perf_counter() - inicio_build_arvore
        
        # ... preparação das buscas ...
        if tamanho == 'pequeno':
            qtd_busca = quantidade // 2
        elif tamanho == 'medio':
            qtd_busca = 1000

        busca_inexistentes = gerar_valores_busca(dados_teste, qtd_busca, existente=False)
        busca_existentes = gerar_valores_busca(dados_teste, qtd_busca)
        
        # ... execução das buscas ...
        inicio_lista_inex = time.perf_counter()
        for v in busca_inexistentes: lista_ponto_total.buscar(v)
        tempo_lista_inex = time.perf_counter() - inicio_lista_inex
        
        inicio_arvore_inex = time.perf_counter()
        for v in busca_inexistentes: arvore_ponto.buscar(v)
        tempo_arvore_inex = time.perf_counter() - inicio_arvore_inex
        
        inicio_lista_ex = time.perf_counter()
        for v in busca_existentes: lista_ponto_total.buscar(v)
        tempo_lista_ex = time.perf_counter() - inicio_lista_ex

        inicio_arvore_ex = time.perf_counter()
        for v in busca_existentes: arvore_ponto.buscar(v)
        tempo_arvore_ex = time.perf_counter() - inicio_arvore_ex
        
        # Totais
        tempo_total_lista_inex = tempo_build_lista + tempo_lista_inex
        tempo_total_arvore_inex = tempo_build_arvore + tempo_arvore_inex
        tempo_total_lista_ex = tempo_build_lista + tempo_lista_ex
        tempo_total_arvore_ex = tempo_build_arvore + tempo_arvore_ex

        # --- DETECÇÃO ---

        # Para INEXISTENTES
        if ponto_virada_inexistentes is None and tempo_total_arvore_inex < tempo_total_lista_inex:
            ponto_virada_inexistentes = n
            stats_inexistentes = {'arv': tempo_total_arvore_inex, 'lst': tempo_total_lista_inex}
            # O \t dá um tab para indentar, fica bonito
            print(f"[!] Virada (INEXISTENTES) detectada em N = {n}")
            
        # Para EXISTENTES
        if ponto_virada_existentes is None and tempo_total_arvore_ex < tempo_total_lista_ex:
            ponto_virada_existentes = n
            stats_existentes = {'arv': tempo_total_arvore_ex, 'lst': tempo_total_lista_ex}
            print(f"[!] Virada (EXISTENTES)   detectada em N = {n}")
        
        # Incremento
        if tamanho == 'pequeno':
            quantidade += 10
        elif tamanho == 'medio':
            quantidade += 1000

    # --- RELATÓRIO FINAL ---

    print(f"\n{'RELATÓRIO FINAL DE PERFORMANCE':^60}\n") # Centraliza o texto
    print("-"*60)

    
    if ponto_virada_inexistentes:
        t_arv = stats_inexistentes['arv']
        t_lst = stats_inexistentes['lst']
        diff = (t_lst - t_arv) / t_lst * 100 # Calcula % de melhoria só pra mostrar
        
        print("\n>>> CENÁRIO 1: BUSCA POR VALORES INEXISTENTES")
        print(f"    A Árvore supera a Lista (incluindo tempo de construção) a partir de:")
        print(f"    N = {ponto_virada_inexistentes} elementos")
        print(f"    --------------------------------------------------")
        print(f"    Tempo Árvore : {t_arv:.6f}s")
        print(f"    Tempo Lista  : {t_lst:.6f}s")
        print(f"    Vantagem     : A árvore foi {diff:.1f}% mais rápida neste ponto.")

    if ponto_virada_existentes:
        t_arv = stats_existentes['arv']
        t_lst = stats_existentes['lst']
        diff = (t_lst - t_arv) / t_lst * 100
        
        print("\n>>> CENÁRIO 2: BUSCA POR VALORES EXISTENTES")
        print(f"    A Árvore supera a Lista (incluindo tempo de construção) a partir de:")
        print(f"    N = {ponto_virada_existentes} elementos")
        print(f"    --------------------------------------------------")
        print(f"    Tempo Árvore : {t_arv:.6f}s")
        print(f"    Tempo Lista  : {t_lst:.6f}s")
        print(f"    Vantagem     : A árvore foi {diff:.1f}% mais rápida neste ponto.")
    
   

        
        
    
        
        
if __name__ == "__main__":

    random.seed(42)  # Reprodutibilidade
    
    print(f"=== 1 ===\n")
    imprimir_separador("Ponto de virada (somente tempo de busca)")
    encontrar_ponto_virada_busca()
    imprimir_separador("Ponto de virada (tempo de busca + construcao)")
    encontrar_ponto_virada_total('pequeno')
    
    # com muitos dados a lista já não 'compensa' independente da quantidade, mesmo com o tempo de construção da arvore maior, a diferença na busca é ainda mais bruta, fazendo
    # qualquer teste com praticamente qualquer quantidade dar como ponto de virada pra árvore na 1° rodada.
    # então comentado.
        # print(f"Considerando tempo de construção + busca para MUITOS DADOS:\n")
        # encontrar_ponto_virada_total('medio')
    
    
    # Armazenando valores dos arquivos disponibilizados
    imprimir_separador("2 - 4 Análise de tempo (construcao, busca)")
    valores_pequeno = ler_arquivo("conjunto_pequeno.txt")
    valores_medio = ler_arquivo("conjunto_medio.txt")
    # valores_grande = ler_arquivo("conjunto_grande.txt")


    # Instanciar as Árvores Binárias
    arvore_p = Arvore()
    arvore_m = Arvore()
    arvore_g = Arvore()
    
    # Instanciar as Listas
    lista_p = Lista()
    lista_m = Lista()
    lista_g = Lista()
    
    # Instanciar as Listas Otimizadas ( QUESTÃO 4 )
    lista_otimizada_p = ListaOtimizada()
    lista_otimizada_m = ListaOtimizada()
    lista_otimizada_g = ListaOtimizada()
    
    
    # **2** -- ANÁLISE TEMPORAL DETALHADA (Testes do conjunto grande estão comentados, devido ao tempo para execução)
    
    
    # ====INSERINDO valores====
    print(f"\nTempos de Construcao - ARVORE")
    print("="*60)
    
    # Inserir valores pequenos na Árvore
    inicio_arvore_p = time.perf_counter()
    for valor in valores_pequeno:
        arvore_p.inserir(valor)
    print(f"tempo conjunto PEQUENO {time.perf_counter() - inicio_arvore_p:.6f}")
    
    # Inserir valores medios na Árvore
    inicio_arvore_m = time.perf_counter()
    for valor in valores_medio:
        arvore_m.inserir(valor)
    print(f"tempo conjunto MEDIO {time.perf_counter() - inicio_arvore_m:.6f}")
    
    # # Inserir valores grandes na Árvore
    # inicio_arvore_g = time.perf_counter()
    # for valor in valores_grande:
    #     arvore_g.inserir(valor)
    # print(f"tempo conjunto GRANDE {time.perf_counter() - inicio_arvore_g:.6f}")
    
    
    print(f"\nTempos de Construcao - LISTA")
    print("="*60)
    
    # Inserir valores pequenos na Lista
    inicio_lista_p =  time.perf_counter()
    lista_p.inserirVarios(valores_pequeno)
    print(f"tempo conjunto PEQUENO {time.perf_counter() - inicio_lista_p:.6f}")
    
    # Inserir valores medios na Lista
    inicio_lista_m =  time.perf_counter()
    lista_m.inserirVarios(valores_medio)
    print(f"tempo conjunto MEDIO {time.perf_counter() - inicio_lista_m:.6f}")
    
    # # Inserir valores grandes na Lista
    # inicio_lista_g =  time.perf_counter()
    # lista_g.inserirVarios(valores_grande)
    # print(f"tempo conjunto GRANDE {time.perf_counter() - inicio_lista_g:.6f}")
    
    
    print(f"\nTempos de Construcao + Ordenacao - LISTA OTIMIZADA")
    print("="*60)
    
    # Inserir conjunto PEQUENO na Lista otimizada e depois ORDENAR
    inicio_insercao_p = time.perf_counter()
    lista_otimizada_p.inserirVarios(valores_pequeno)
    tempo_insercao_p = time.perf_counter() - inicio_insercao_p
    
    inicio_ordenacao_p = time.perf_counter()
    lista_otimizada_p.ordenar()
    tempo_ordenacao_p = time.perf_counter() - inicio_ordenacao_p
    tempo_total_build_p = tempo_insercao_p + tempo_ordenacao_p
    print(f"tempo conjunto PEQUENO {tempo_total_build_p:.6f} (Insercao: {tempo_insercao_p:.6f}s + Ordenacao: {tempo_ordenacao_p:.6f})")

    # Inserir conjunto MÉDIO na Lista otimizada e depois ORDENAR
    inicio_insercao_m = time.perf_counter()
    lista_otimizada_m.inserirVarios(valores_medio)
    tempo_insercao_m = time.perf_counter() - inicio_insercao_m

    inicio_ordenacao_m = time.perf_counter()
    lista_otimizada_m.ordenar()
    tempo_ordenacao_m = time.perf_counter() - inicio_ordenacao_m
    tempo_total_build_m = tempo_insercao_m + tempo_ordenacao_m
    print(f"tempo conjunto MEDIO {tempo_total_build_m:.6f} (Insercao: {tempo_insercao_m:.6f} + Ordenacao: {tempo_ordenacao_m:.6f})")
    
    # # Inserir conjunto GRANDE na Lista otimizada e depois ORDENAR
    # inicio_insercao_g = time.perf_counter()
    # lista_otimizada_g.inserirVarios(valores_grande)
    # tempo_insercao_g = time.perf_counter() - inicio_insercao_g

    # inicio_ordenacao_g = time.perf_counter()
    # lista_otimizada_g.ordenar()
    # tempo_ordenacao_g = time.perf_counter() - inicio_ordenacao_g
    # tempo_total_build_g = tempo_insercao_g + tempo_ordenacao_g
    # print(f"tempo conjunto GRANDE {tempo_total_build_g:.6f} (Insercao: {tempo_insercao_g:.6f} + Ordenacao: {tempo_ordenacao_g:.6f})")

    


    

    # ====Testes de BUSCA====
    
    # ==Criando valores de busca de CONJUNTO PEQUENO==
    
    
    # cria/armazena 500 valores existentes no arquivo
    valores_busca_existentes_pequeno = gerar_valores_busca(valores_pequeno, 500)
    
    
    # cria/armazena 500 valores NÃO existentes no arquivo
    valores_busca_nexistentes_pequeno = gerar_valores_busca(valores_pequeno, 500, existente=False)   
        
        
    # ==Criando valores de busca de CONJUNTO MEDIO==
    

    # cria/armazena 500 valores existentes no arquivo
    valores_busca_existentes_medio = gerar_valores_busca(valores_medio, 500)

    # cria/armazena 500 valores NÃO existentes no arquivo
    valores_busca_nexistentes_medio = gerar_valores_busca(valores_medio, 500, existente=False) 
    
    
    # ==Criando valores de busca de CONJUNTO GRANDE==
    
    # cria/armazena 500 valores existentes no arquivo
    #valores_busca_existentes_grande = gerar_valores_busca(valores_grande, 500)
    # cria/armazena 500 valores NÃO existentes no arquivo
    #valores_busca_nexistentes_grande = gerar_valores_busca(valores_grande, 500, existente=False) 


    print(f"\nTempos de Buscas - ARVORE")
    print("="*60)
    inicio_busca_e_p = time.perf_counter()
    for n in valores_busca_existentes_pequeno:
        resposta = arvore_p.buscar(n)
    print(f"Tempo Conjunto PEQUENO, valores Existentes -> {time.perf_counter() - inicio_busca_e_p:.6f}")
    
    inicio_busca_e_m = time.perf_counter()
    for n in valores_busca_existentes_medio:
        resposta = arvore_m.buscar(n)
    print(f"Tempo Conjunto MEDIO, valores Existentes -> {time.perf_counter() - inicio_busca_e_m:.6f}")
    
    # inicio_busca_e_g = time.perf_counter()
    # for n in valores_busca_existentes_grande:
    #     resposta = arvore_g.buscar(n)
    # print(f"Tempo Conjunto GRANDE, valores Existentes -> {time.perf_counter() - inicio_busca_e_g:.6f}")



    inicio_busca_ne_p = time.perf_counter()
    for n in valores_busca_nexistentes_pequeno:
        resposta = arvore_p.buscar(n)
    print(f"tempo Conjunto PEQUENO, valores NAO Existentes -> {time.perf_counter() - inicio_busca_ne_p:.6f}")
    
    inicio_busca_ne_m = time.perf_counter()
    for n in valores_busca_nexistentes_medio:
        resposta = arvore_m.buscar(n)
    print(f"tempo Conjunto MEDIO, valores NAO Existentes -> {time.perf_counter() - inicio_busca_ne_m:.6f}")
    
    # inicio_busca_ne_g = time.perf_counter()
    # for n in valores_busca_nexistentes_grande:
    #     resposta = arvore_g.buscar(n)
    # print(f"tempo Conjunto GRANDE, valores NAO Existentes -> {time.perf_counter() - inicio_busca_ne_g:.6f}")
    
    
    print(f"\nTempos de Buscas - LISTA")
    print("="*60)
    l_inicio_busca_e_p = time.perf_counter()
    for n in valores_busca_existentes_pequeno:
        resposta = lista_p.buscar(n)
    print(f"Tempo Conjunto PEQUENO, valores Existentes -> {time.perf_counter() - l_inicio_busca_e_p:.6f}")
    
    l_inicio_busca_e_m = time.perf_counter()
    for n in valores_busca_existentes_medio:
        resposta = lista_m.buscar(n)
    print(f"Tempo Conjunto MEDIO, valores Existentes -> {time.perf_counter() - l_inicio_busca_e_m:.6f}")
    
    # l_inicio_busca_e_g = time.perf_counter()
    # for n in valores_busca_existentes_grande:
    #     resposta = lista_g.buscar(n)
    # print(f"Tempo Conjunto GRANDE, valores Existentes -> {time.perf_counter() - l_inicio_busca_e_g:.6f}")



    l_inicio_busca_ne_p = time.perf_counter()
    for n in valores_busca_nexistentes_pequeno:
        resposta = lista_p.buscar(n)
    print(f"tempo Conjunto PEQUENO, valores NAO Existentes -> {time.perf_counter() - l_inicio_busca_ne_p:.6f}")
    
    l_inicio_busca_ne_m = time.perf_counter()
    for n in valores_busca_nexistentes_medio:
        resposta = lista_m.buscar(n)
    print(f"tempo Conjunto MEDIO, valores NAO Existentes -> {time.perf_counter() - l_inicio_busca_ne_m:.6f}")
    
    # l_inicio_busca_ne_g = time.perf_counter()
    # for n in valores_busca_nexistentes_grande:
    #     resposta = lista_g.buscar(n)
    # print(f"tempo Conjunto GRANDE, valores NAO Existentes -> {time.perf_counter() - l_inicio_busca_ne_g:.6f}")
    


    # ( Questão 4 )
    print(f"\nTempos de Buscas - LISTA OTIMIZADA")
    print("="*60)
    
    # Teste de busca com valores existentes
    lo_inicio_busca_e_p = time.perf_counter()
    for n in valores_busca_existentes_pequeno:
        resposta = lista_otimizada_p.busca_binaria(n)
    print(f"Tempo Conjunto PEQUENO, valores Existentes -> {time.perf_counter() - lo_inicio_busca_e_p:.6f}")
    
    lo_inicio_busca_e_m = time.perf_counter()
    for n in valores_busca_existentes_medio:
        resposta = lista_otimizada_m.busca_binaria(n)
    print(f"Tempo Conjunto MEDIO, valores Existentes -> {time.perf_counter() - lo_inicio_busca_e_m:.6f}")
    
    # lo_inicio_busca_e_g = time.perf_counter()
    # for n in valores_busca_existentes_grande:
    #     resposta = lista_otimizada_g.busca_binaria(n)
    # print(f"Tempo Conjunto GRANDE, valores Existentes -> {time.perf_counter() - lo_inicio_busca_e_g:.6f}")
    

    
    # Teste de busca com valores NÃO existentes
    lo_inicio_busca_ne_p = time.perf_counter()
    for n in valores_busca_nexistentes_pequeno:
        resposta = lista_otimizada_p.busca_binaria(n)
    print(f"tempo Conjunto PEQUENO, valores NAO Existentes -> {time.perf_counter() - lo_inicio_busca_ne_p:.6f}")
    
    lo_inicio_busca_ne_m = time.perf_counter()
    for n in valores_busca_nexistentes_medio:
        resposta = lista_otimizada_m.busca_binaria(n)
    print(f"tempo Conjunto MEDIO, valores NAO Existentes -> {time.perf_counter() - lo_inicio_busca_ne_m:.6f}")
    
    # lo_inicio_busca_ne_g = time.perf_counter()
    # for n in valores_busca_nexistentes_grande:
    #     resposta = lista_otimizada_g.busca_binaria(n)
    # print(f"tempo Conjunto GRANDE, valores NAO Existentes -> {time.perf_counter() - lo_inicio_busca_ne_g:.6f}")
    
    
