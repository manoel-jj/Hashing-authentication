Sistema de Autenticação com Hashing
Descrição
Este projeto é um sistema de autenticação simples desenvolvido em Python que permite o registro e login de usuários com armazenamento seguro de senhas utilizando o algoritmo de hashing bcrypt. As credenciais dos usuários são salvas em um arquivo JSON (users.json) para persistência de dados. O sistema inclui funcionalidades para registrar novos usuários, verificar credenciais durante o login e gerenciar erros de entrada.
Funcionalidades

Registro de Usuários: Cria um novo usuário com uma senha hasheada usando bcrypt. Após o registro, um arquivo users.json é criado (ou atualizado) contendo o nome de usuário e o hash da senha.
Login de Usuários: Verifica as credenciais do usuário comparando a senha fornecida com o hash armazenado.
Armazenamento Seguro: As senhas são armazenadas de forma segura em um arquivo JSON.
Interface de Linha de Comando: Menu interativo para registro, login e saída.

Pré-requisitos

Python 3.6 ou superior
Biblioteca bcrypt instalada

Instalação

Clone ou baixe este repositório para sua máquina local.
Certifique-se de ter o Python instalado. Você pode verificar com:python --version


Instale a biblioteca bcrypt usando pip:pip install bcrypt


Coloque o arquivo auth_system.py (contendo o código fornecido) no diretório do projeto.

Como Usar

Execute o script principal:python auth_system.py


Um menu será exibido com as seguintes opções:
1. Registrar: Insira um nome de usuário e senha para criar uma nova conta.
2. Login: Insira um nome de usuário e senha para autenticar.
3. Sair: Encerra o programa.


Siga as instruções no terminal para interagir com o sistema.

Exemplo de Uso
Sistema de Autenticação
1. Registrar
2. Login
3. Sair
Escolha uma opção (1-3): 1
Digite o nome de usuário: joao
Digite a senha: senha123
Usuário registrado com sucesso!

Sistema de Autenticação
1. Registrar
2. Login
3. Sair
Escolha uma opção (1-3): 2
Digite o nome de usuário: joao
Digite a senha: senha123
Login bem-sucedido!

Estrutura do Projeto

auth_system.py: Script principal contendo o sistema de autenticação.
users.json: Arquivo gerado automaticamente para armazenar os dados dos usuários (nome de usuário e senha hasheada).

Dependências

bcrypt: Biblioteca para hashing de senhas.
json: Biblioteca padrão do Python para manipulação de arquivos JSON.
os: Biblioteca padrão do Python para verificação de arquivos.

Notas

As senhas são armazenadas de forma segura usando o algoritmo bcrypt, que adiciona um salt único para proteger contra ataques de força bruta.
O arquivo users.json será criado automaticamente no diretório do projeto ao registrar o primeiro usuário.
O sistema valida entradas para evitar nomes de usuário ou senhas vazias e verifica se o usuário já existe durante o registro.

Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

