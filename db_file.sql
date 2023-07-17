CREATE DATABASE `db_teste`;

-- Criando usuário
CREATE USER 'usr_teste'@'%' IDENTIFIED BY 'teste';
 
-- Adicionando permissões
GRANT ALL PRIVILEGES ON *.* TO 'usr_teste'@'%';

-- Criação das tabelas 
CREATE TABLE `fornecedor` (
    `cod_fornecedor` INT AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(255)
);

CREATE TABLE `estado` (
    `cod_uf` INT AUTO_INCREMENT PRIMARY KEY,
    `uf` VARCHAR(2),
    `cod_fornecedor` INT,
    `nome` VARCHAR(255),
    FOREIGN KEY (`cod_fornecedor`) REFERENCES `fornecedor` (`cod_fornecedor`)
);

CREATE TABLE `funcionario` (
    `cod_funcionario` INT AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(255)
);

CREATE TABLE `lote` (
    `cod_lote` INT AUTO_INCREMENT PRIMARY KEY,
    `cod_lote_prazo` INT,
    `data_criacao` DATETIME,
    `cod_funcionario` INT,
    `tipo` VARCHAR(255),
    `prioridade` VARCHAR(255),
    FOREIGN KEY (`cod_funcionario`) REFERENCES `funcionario` (`cod_funcionario`)
);

CREATE TABLE `lote_pesquisa` (
    `cod_lote_pesquisa` INT AUTO_INCREMENT PRIMARY KEY,
    `cod_lote` INT,
    `cod_pesquisa` INT,
    `cod_funcionario` INT,
    `cod_funcionario_conclusao` INT,
    `cod_fornecedor` INT,
    `data_entrada` DATETIME,
    `data_conclusao` DATETIME,
    `cod_uf` INT,
    `obs` TEXT,
    FOREIGN KEY (`cod_lote`) REFERENCES `lote` (`cod_lote`),
    FOREIGN KEY (`cod_funcionario`) REFERENCES `funcionario` (`cod_funcionario`),
    FOREIGN KEY (`cod_funcionario_conclusao`) REFERENCES `funcionario` (`cod_funcionario`),
    FOREIGN KEY (`cod_fornecedor`) REFERENCES `fornecedor` (`cod_fornecedor`),
    FOREIGN KEY (`cod_uf`) REFERENCES `estado` (`cod_uf`)
);

CREATE TABLE `servico` (
    `cod_servico` INT PRIMARY KEY,
    `civel` VARCHAR(255),
    `criminal` VARCHAR(255)
);

CREATE TABLE `pesquisa` (
    `cod_pesquisa` INT AUTO_INCREMENT PRIMARY KEY,
    `cod_cliente` INT,
    `cod_uf` INT,
    `cod_servico` INT,
    `tipo` TEXT,
    `cpf` VARCHAR(11),
    `cod_uf_nascimento` INT,
    `cod_uf_rg` INT,
    `data_entrada` DATETIME,
    `data_conclusao` DATETIME,
    `nome` VARCHAR(255),
    `nome_corrigido` VARCHAR(255),
    `rg` VARCHAR(10),
    `rg_corrigido` VARCHAR(10),
    `nascimento` DATETIME,
    `mae` VARCHAR(255),
    `mae_corrigido` VARCHAR(255),
    `anexo` TEXT
);

CREATE TABLE `pesquisa_spv` (
    `cod_pesquisa` INT AUTO_INCREMENT PRIMARY KEY,
    `cod_spv` INT,
    `cod_spv_computador` INT,
    `cod_spv_tipo` INT,
    `cod_funcionario` INT,
    `filtro` INT,
    `website_id` INT,
    `resultado` VARCHAR(255)
);
