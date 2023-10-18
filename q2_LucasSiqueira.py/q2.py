write_credentials = lambda username, password: open('C:\\Users\\lukas\\Documents\\Ciência-da-Computação\\Programacao-Funcional\\functional-programming\\credenciais.txt', 'a').write(username + " " + password + "\n")

check_credentials = lambda username, password: (username + " " + password + "\n") in open('credenciais.txt', 'r').readlines()

sign_up = lambda: (lambda x: write_credentials(input("Insira o usuário: "), input("Insira a senha: ")))("Usuário registrado com sucesso!")

sign_in = lambda: print("SUCESSO") if check_credentials(input("Insira o usuário: "), input("Insira a senha: ")) else print("FRACASSO")

process_choice = lambda choice: {
    "cadastrar": sign_up,
    "logar": sign_in,
    "sair": lambda: "exit",
    "default": lambda: print("Opção inválida, escreva uma das opções: cadastrar/logar/sair")
}.get(choice, lambda: print("Opção inválida, escreva uma das opções: cadastrar/logar/sair"))()

main_loop = (
    lambda f: f(f)
)(
    lambda f:
    None if process_choice(input("Você quer se logar ou se cadastrar? (logar/cadastrar/sair)\n")) == "exit" else f(f)
)
