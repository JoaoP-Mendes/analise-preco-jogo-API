# Análise de Preço de Jogos — Steam API

Projeto pessoal em Python + MySQL, com consumo de API externa e análise
de dados com Pandas.

## Objetivo

Esse projeto foi criado com três objetivos principais:

- Começar a trabalhar com consumo de APIs externas
- Enviar dados de uma API pública para um banco de dados relacional
- Realizar análise de preço de jogos com base no tempo (histórico)

## Estrutura

```
analise preco jogo API/
├── api/
│   └── steam.py           # Consome a API pública da Steam (appdetails)
├── bancodados/
│   └── banco.py            # Classe bancoDados: conexão e execução de queries
├── config/
│   └── config.py            # Dados de conexão com o MySQL
├── layout/
│   └── layout.py             # Funções auxiliares de terminal (cores, carregamento)
├── modelos/
│   ├── jogo.py                # Classe Jogo: cadastro, exclusão e listagem
│   └── historico.py           # Classe Historico: registro e consulta de preços
├── banco.sql                   # Script SQL: cria o banco e as 2 tabelas
├── menu.py                      # Fluxo de menus (jogo, histórico)
└── main.py                       # Ponto de entrada do programa
```

## Como funciona

A [Steam Storefront API](https://store.steampowered.com/api/appdetails)
não mantém histórico de preços — ela sempre devolve apenas o preço
**atual** de um jogo. Para construir um histórico de verdade, o próprio
sistema precisa consultar a API repetidamente ao longo do tempo e salvar
um "retrato" (snapshot) de cada consulta.

O fluxo é:

1. Cadastra-se um jogo pelo `appid` da Steam — a classe `Jogo` consulta
   a API, extrai nome, desenvolvedora, publicadora, gênero e se é
   gratuito, e salva na tabela `jogos`
2. A classe `Historico` lê (via Pandas) todos os `appid` já cadastrados
   em `jogos`, consulta o preço atual de cada um na API, e insere um
   novo registro na tabela `historico`, com a data da consulta
3. Repetindo o passo 2 ao longo de vários dias, forma-se um histórico
   real de preços e promoções, possível de analisar depois com Pandas

## Como rodar

### 1. Instalar as dependências
```
pip install pymysql requests pandas
```

### 2. Criar o banco de dados
Execute o conteúdo de `banco.sql` no MySQL. Isso cria o banco
`analise_jogos` e as tabelas `jogos` e `historico`.

### 3. Configurar a conexão
Edite `config/config.py` com o usuário/senha do seu MySQL local:
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "passwd": "sua_senha_aqui",
    "database": "analise_jogos"
}
```

### 4. Rodar o programa
A partir da pasta raiz do projeto:
```
python -m main
```

## Arquitetura

- **`config/config.py`** — guarda os dados de conexão.
- **`bancodados/banco.py`** (classe `bancoDados`) — conecta, desconecta
  e executa queries com parâmetros preparados (`%s` + tupla de valores),
  prevenindo SQL Injection.
- **`api/steam.py`** — isolado do resto do sistema: só sabe conversar
  com a API da Steam e devolver um dicionário já tratado. Não conhece
  nada sobre o banco de dados.
- **`modelos/jogo.py`, `modelos/historico.py`** — usam a API (via
  `api/steam.py`) e o banco (via `bancodados/banco.py`) para cadastrar
  jogos e manter o histórico de preços. `historico.py` usa
  `pandas.read_sql` para ler todos os jogos cadastrados e iterar sobre
  eles, atualizando o preço de cada um automaticamente.
- **`menu.py` / `main.py`** — interface de terminal, sem lógica de
  negócio própria.

## Tabelas (banco.sql)

- **`jogos`**: appid (PK), nome, tipo, desenvolvedora, publicadora,
  genero, gratuito (ENUM)
- **`historico`**: id (PK), appid (FK), data_analise, preco

## Limitações conhecidas / próximos passos

- **Automação diária pendente**: o objetivo inicial incluía rodar a
  atualização do histórico automaticamente todo dia (via GitHub Actions
  + banco de dados em nuvem), sem depender do computador ligado. A
  migração do banco para um provedor gratuito (Aiven) foi tentada, mas
  a conexão remota não foi estabelecida com sucesso nas ferramentas
  testadas (phpMyAdmin, MySQL Workbench). Por ora, a atualização do
  histórico é feita manualmente, rodando o programa quando necessário.
- Próxima iteração possível: resolver a conexão com o banco em nuvem
  e configurar o agendamento automático via GitHub Actions.
