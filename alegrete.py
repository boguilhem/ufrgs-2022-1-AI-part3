import numpy as np
from typing import Tuple, List


def compute_mse(theta_0: float, theta_1: float, data: np.array) -> float:
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    data_x = data[:, 0]
    data_y = data[:, 1]

    hypothesis = theta_0 + theta_1 * data_x
    square_error = np.square(hypothesis - data_y)
    mse = np.mean(square_error)

    return mse


def step_gradient(theta_0: float, theta_1: float, data: np.array, alpha: float) -> Tuple[float, float]:
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """

    data_x = data[:, 0]
    data_y = data[:, 1]

    derivative_theta_0 = np.mean(2 * ((theta_0 + theta_1 * data_x) - data_y))
    derivative_theta_1 = np.mean(2 * ((theta_0 + theta_1 * data_x) - data_y) * data_x)

    updated_theta_0 = theta_0 - alpha * derivative_theta_0
    updated_theta_1 = theta_1 - alpha * derivative_theta_1

    return updated_theta_0, updated_theta_1


def fit(
    data: np.array, theta_0: float, theta_1: float, alpha: float, num_iterations: int
) -> Tuple[List[float], List[float]]:
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """

    list_theta_0 = []
    list_theta_1 = []
    curr_theta_0 = theta_0
    curr_theta_1 = theta_1

    for iteration in range(num_iterations):
        curr_theta_0, curr_theta_1 = step_gradient(curr_theta_0, curr_theta_1, data, alpha)
        list_theta_0.append(curr_theta_0)
        list_theta_1.append(curr_theta_1)

    return list_theta_0, list_theta_1
