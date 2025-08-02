# 🧬 Algoritmo Genético para o Problema do Caixeiro Viajante (TSP)

Este projeto implementa um algoritmo genético simples para resolver uma instância do **Problema do Caixeiro Viajante (TSP)** com 58 cidades no Brasil. O objetivo é encontrar o menor caminho possível que visita cada cidade exatamente uma vez e retorna à cidade de origem.

## 🗺️ Arquivo de Entrada

O algoritmo espera um arquivo chamado `edgesbrasil58.tsp` no diretório `Algoritmo Genético`, contendo uma matriz triangular superior com as distâncias entre as cidades. As distâncias devem estar organizadas linha por linha, como em arquivos `.tsp` típicos.

## 📦 Funcionalidades

- Leitura eficiente das distâncias a partir do arquivo `.tsp`.
- Inicialização de uma população com indivíduos (rotas) aleatórios.
- Avaliação por aptidão com base na soma das distâncias.
- Operador de crossover parcialmente ordenado (Order Crossover - OX).
- Mutação por inversão de fatias da rota.
- Elitismo: os melhores indivíduos são preservados a cada geração.
- Critério de parada por estagnação ou número máximo de gerações.

## 🧠 Como funciona

O processo evolutivo segue estes passos:

1. Gera uma população inicial aleatória.
2. Calcula o custo (distância total) de cada indivíduo.
3. Aplica seleção probabilística baseada em aptidão (1/custo).
4. Realiza o crossover entre pais selecionados para gerar novos filhos.
5. Aplica mutação aleatória em parte dos indivíduos.
6. Repete o processo por até 5000 gerações ou até 200 gerações sem melhora.

## ⚙️ Parâmetros

Você pode ajustar os seguintes parâmetros no início da função `main()`:

```python
TAXA_MUTACAO = 0.05          # Taxa de mutação (5%)
MAX_GERACOES = 5000          # Número máximo de gerações
LIMITE_ESTAGNACAO = 200      # Gerações sem melhora para parar
ELITISMO = 5                 # Quantos indivíduos melhores permanecem
TAM_POP = 50                 # Tamanho da população
```

## 📈 Saída

Durante a execução, o programa imprime:

- O custo do melhor indivíduo de cada geração (quando há melhora).
- Quando atinge o critério de estagnação, imprime o melhor caminho e seu custo.

### Exemplo de saída:

```
Geraçao 0: Novo melhor custo = 9213
Geraçao 3: Novo melhor custo = 9051
...
Parando por estagnação na Geraçao: 412
Melhor custo final encontrado: 8432
Melhor caminho final encontrado: [1, 34, 17, 8, 45, ..., 1]
```

## ▶️ Como executar

Certifique-se de ter o Python instalado (versão 3.6 ou superior) e o arquivo de distâncias `edgesbrasil58.tsp` no caminho correto.

```bash
python nome_do_arquivo.py
```

## 📁 Estrutura esperada do arquivo `.tsp`

Um exemplo ilustrativo de como deve estar o arquivo `edgesbrasil58.tsp`:

```
234 543 234 ...
123 432 ...
...
```

Cada linha representa as distâncias da cidade `i` para as cidades `j > i`.

## 🧪 Possíveis melhorias

- Implementar outros operadores de crossover (ex: PMX, CX).
- Adicionar visualização gráfica do melhor caminho.
- Permitir diferentes cidades iniciais ou rotas assimétricas.
- Carregar o número de cidades automaticamente do arquivo.

## 📄 Licença

Este projeto é de uso livre para fins educacionais e acadêmicos. Nenhuma garantia é oferecida quanto à performance.