import logging
import csv


# Configuração de Logging
logging.basicConfig(
    filename='login.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


# Função para realizar login
def realizar_login(user, password):
    """
    Função que realiza o login verificando credenciais.
    :param user: Nome de usuário.
    :param password: Senha.
    :return: True se login for bem-sucedido, False caso contrário.
    """
    if user == "main" and password == "123456":
        logging.info(f"Login bem-sucedido para o utilizador: {user}")
        return True
    else:
        logging.info(f"Tentativa de login falhou para o utilizador: {user}")
        return False


# Função para identificar a companhia com mais tweets negativos
def companhia_com_mais_tweets_negativos(dados):
    """
    Retorna a companhia com mais tweets negativos.
    :param dados: Lista de dicionários representando os dados.
    :return: Nome da companhia com maior número de tweets negativos.
    """
    negativos = {}
    for item in dados:
        if item['airline_sentiment'] == 'negative':
            companhia = item['airline']
            negativos[companhia] = negativos.get(companhia, 0) + 1

    if negativos:
        return max(negativos, key=negativos.get)
    return None


# Função para contar o total de tweets por companhia
def total_tweets_por_companhia(dados):
    """
    Conta o número total de tweets por companhia.
    :param dados: Lista de dicionários representando os dados.
    :return: Dicionário com contagem de tweets por companhia.
    """
    contagem = {}
    for item in dados:
        companhia = item['airline']
        contagem[companhia] = contagem.get(companhia, 0) + 1
    return contagem


# Função para listar as companhias únicas
def listar_companhias(dados):
    """
    Lista todas as companhias únicas presentes nos dados.
    :param dados: Lista de dicionários representando os dados.
    :return: Lista de companhias únicas.
    """
    companhias = set()
    for item in dados:
        companhias.add(item['airline'])
    return list(companhias)


# Função para filtrar tweets por uma companhia específica
def filtrar_tweets_por_companhia(dados, companhia):
    """
    Filtra os dados de tweets de acordo com a companhia.
    :param dados: Lista de dicionários representando os dados.
    :param companhia: Nome da companhia para filtrar.
    :return: Lista de dados filtrados pela companhia.
    """
    return [item for item in dados if item['airline'] == companhia]
