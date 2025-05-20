import bcrypt
import json
import os

# Caminho para o arquivo de banco de dados (JSON)
DB_FILE = "users.json"


def load_users():
    """Carrega os usuários do arquivo JSON."""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_users(users):
    """Salva os usuários no arquivo JSON."""
    with open(DB_FILE, 'w') as f:
        json.dump(users, f, indent=4)


def register_user(username, password):
    """Registra um novo usuário com senha hasheada."""
    if not username or not password:
        return "Erro: Nome de usuário e senha são obrigatórios."

    users = load_users()

    if username in users:
        return "Erro: Nome de usuário já existe."

    # Gera o hash da senha com bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Armazena o usuário com a senha hasheada (convertida para string para JSON)
    users[username] = hashed_password.decode('utf-8')
    save_users(users)
    return "Usuário registrado com sucesso!"


def login_user(username, password):
    """Verifica as credenciais do usuário para login."""
    if not username or not password:
        return "Erro: Nome de usuário e senha são obrigatórios."

    users = load_users()

    if username not in users:
        return "Erro: Usuário não encontrado."

    # Verifica se a senha fornecida corresponde ao hash armazenado
    if bcrypt.checkpw(password.encode('utf-8'), users[username].encode('utf-8')):
        return "Login bem-sucedido!"
    return "Erro: Senha incorreta."


def main():
    """Função principal para interagir com o sistema."""
    while True:
        print("\nSistema de Autenticação")
        print("1. Registrar")
        print("2. Login")
        print("3. Sair")
        try:
            choice = input("Escolha uma opção (1-3): ")
        except EOFError:
            print("Entrada encerrada. Saindo...")
            break

        if choice == '1':
            try:
                username = input("Digite o nome de usuário: ")
                password = input("Digite a senha: ")
                print(register_user(username, password))
            except EOFError:
                print("Entrada encerrada. Saindo...")
                break

        elif choice == '2':
            try:
                username = input("Digite o nome de usuário: ")
                password = input("Digite a senha: ")
                print(login_user(username, password))
            except EOFError:
                print("Entrada encerrada. Saindo...")
                break

        elif choice == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()