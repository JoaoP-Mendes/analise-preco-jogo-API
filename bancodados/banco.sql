CREATE DATABASE IF NOT EXISTS analise_jogos;
USE analise_jogos;

CREATE TABLE IF NOT EXISTS jogos (
    appid INT PRIMARY KEY, 
    nome VARCHAR (255) NOT NULL,
    tipo VARCHAR (255) NOT NULL DEFAULT 'game',
    desenvolvedora VARCHAR (255) NOT NULL,
    publicadora VARCHAR(255) NOT NULL,
    genero VARCHAR(255) NOT NULL, 
    gratuito boolean NOT NULL DEFAULT True
) DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS historico(
    id INT PRIMARY KEY AUTO_INCREMENT,
    appid INT NOT NULL,
    data_analise DATE NOT NULL,
    preco FLOAT(5, 2) NOT NULL DEFAULT 0.00,
    CONSTRAINT appid_jogo FOREIGN KEY (appid) REFERENCES jogos(appid)
) DEFAULT CHARSET = utf8mb4;