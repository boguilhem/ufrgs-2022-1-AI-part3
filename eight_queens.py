import random
from typing import Tuple, List

PLOT_GRAPH = False


def evaluate(individual: List[int]) -> int:
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    hits = 0

    for i in range(7):
        queen_looking = individual[i]
        for j in range(i + 1, 8):
            queen_conflicting = individual[j]
            if (
                (queen_looking == queen_conflicting)
                or (queen_looking == queen_conflicting + (j - i))
                or (queen_looking == queen_conflicting - (j - i))
            ):
                hits += 1
    return hits


def tournament(participants: List[List[int]]) -> List[int]:
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    participants_conflict_list = [evaluate(individual) for individual in participants]
    min_conflict_value = min(participants_conflict_list)
    min_conflict_index = participants_conflict_list.index(min_conflict_value)

    return participants[min_conflict_index]


def crossover(parent1: List[int], parent2: List[int], index: int) -> Tuple[List[int], List[int]]:
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """

    descendant1 = parent1[0:index] + parent2[index:]

    descendant2 = parent2[0:index] + parent1[index:]

    return descendant1, descendant2


def mutate(individual: List[int], m: float) -> List[int]:
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:float - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    pos_ind = random.randint(0, 7)
    mutation = random.randint(1, 8)

    if random.random() < m:
        individual[pos_ind] = mutation

    return individual


def run_ga(g: int, n: int, k: int, m: float, e: int) -> List[int]:
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo
    :return:list - melhor individuo encontrado
    """

    curr_population = [[random.randint(1, 8) for i in range(8)] for individual in range(n)]
    if PLOT_GRAPH == True:
        populations = []
    for generation in range(g):
        if e > 0:
            new_population = [tournament(curr_population)]
        else:
            new_population = []
        while len(new_population) < n:
            parent1 = tournament(random.sample(curr_population, k))
            parent2 = tournament(random.sample(curr_population, k))

            descendant1, descendant2 = crossover(parent1, parent2, random.randint(0, 7))
            descendant1 = mutate(descendant1, m)
            descendant2 = mutate(descendant2, m)
            new_population.extend([descendant1, descendant2])

        curr_population = new_population
        if PLOT_GRAPH == True:
            populations.append(curr_population)
    if PLOT_GRAPH == True:
        return tournament(curr_population), populations
    else:
        return tournament(curr_population)
