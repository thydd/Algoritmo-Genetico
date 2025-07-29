def ler_distancias():
    file = open(r"Algoritmo Genético\edgesbrasil58.tsp")
    distancias = {}
    for i in range(1, 58): 
        linha = file.readline()
        lista = linha.split()
        for j in range(i+1, 59): 
            if len(lista) > 0:
                peso = int(lista.pop(0))
            else:
                print(f"Erro! linha {i} do arquivo não possui elementos suficientes")
                exit()
            distancias[(i, j)] = peso
            distancias[(j, i)] = peso
    file.close()
    return distancias

def custo_distancia(permutacao, dicDistancias):
    soma = 0
    for i in range(len(permutacao)-1):
        a = permutacao[i]
        b = permutacao[i+1]
        if (a,b) in dicDistancias:
            soma += dicDistancias[(a,b)]
        else:
            print(f"Erro! ({a},{b}) não existe no dicionario!")
            exit()
    soma += dicDistancias[(permutacao[-1],permutacao[0])]
    return soma

def inicializaPopulacao(tamanho, qtdeCidades):
	import random
	lista = []
	for i in range(tamanho):
		individuo = list(range(1, qtdeCidades+1))
		random.shuffle(individuo)
		lista.append(individuo)
	return lista

def calculaAptidao(populacao, distancias):
	listaAptidao = []
	for elem in populacao:
		listaAptidao.append(custo_distancia(elem, distancias))
	listaAptidao = [1/i for i in listaAptidao]
	return listaAptidao

def crossover(populacao, listaAptidao):
    from random import choices, randint
    pai1, pai2 = choices(populacao, weights=listaAptidao, k=2)
    n = len(pai1)
    start = randint(0, n - 2)
    end = randint(start + 1, n - 1)

    filho = [None] * n
    filho[start:end] = pai1[start:end]

    ptr = 0
    for gene in pai2:
        if gene not in filho:
            while filho[ptr] is not None:
                ptr += 1
            filho[ptr] = gene

    return filho

def inversion_mutation(individuo):
    from random import sample
    idx1, idx2 = sorted(sample(range(len(individuo)), 2))
    fatia = individuo[idx1:idx2+1]
    fatia.reverse()
    individuo[idx1:idx2+1] = fatia
    return individuo

def normalizar_caminho(caminho, cidade_inicial=1):
    if cidade_inicial not in caminho:
        return caminho 

    indice = caminho.index(cidade_inicial)
    caminho_normalizado = caminho[indice:] + caminho[:indice]
    return caminho_normalizado

def main():
    from random import randint, random

    TAXA_MUTACAO = 0.05 #taxa de mutaçao 1% a 5% 
    MAX_GERACOES = 5000
    LIMITE_ESTAGNACAO = 200
    ELITISMO = 5

    TAM_POP = 50
    DISTANCIAS = ler_distancias()

    melhor_custo_global = float('inf')
    melhor_caminho_global = None
    sem_melhora = 0

    pop = inicializaPopulacao(TAM_POP, 58)
    
    for geracao in range(MAX_GERACOES):
        custos = [custo_distancia(ind, DISTANCIAS) for ind in pop]
        aptidoes = calculaAptidao(pop, DISTANCIAS)

        melhor_custo_geracao = min(custos)

        if melhor_custo_geracao < melhor_custo_global:
            melhor_custo_global = melhor_custo_geracao
            melhor_caminho_global = pop[custos.index(melhor_custo_geracao)]
            sem_melhora = 0
            print(f'Geraçao {geracao}: Novo melhor custo = {melhor_custo_global}')
        else:
            sem_melhora += 1

        if sem_melhora >= LIMITE_ESTAGNACAO:
            print(f"\nParando por estagnação na Geraçao: {geracao}")
            print(f"Melhor custo final encontrado: {melhor_custo_global}")
            caminho_formatado = normalizar_caminho(melhor_caminho_global, 1)
            print(f"Melhor caminho final encontrado: {caminho_formatado}")
            break

        nova_pop = []
        pop_ordenada = [individuo for _, individuo in sorted(zip(custos, pop))]
        elite = pop_ordenada[:ELITISMO]
        nova_pop.extend(elite)

        for _ in range(TAM_POP - 1):
            filho = crossover(pop, aptidoes)

            if random() < TAXA_MUTACAO:
                filho = inversion_mutation(filho)
        
            nova_pop.append(filho)
        pop = nova_pop

    if geracao == MAX_GERACOES - 1:
        print(f'\nFim das {MAX_GERACOES} geraçoes.')     
        print(f'Melhor custo fina encontrado: {melhor_custo_global}')

if __name__ == "__main__":
	main()
