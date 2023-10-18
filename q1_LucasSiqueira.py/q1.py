accounts_data = {
    '123456': 5000,
    '234567': 35000,
    '345678': 4000,
}

account_number = input("Insira o número da sua conta: ")

check_account = lambda acc_num: acc_num in accounts_data

withdrawal = lambda amount, balance: balance - amount if amount <= balance else "Saque não permitido! Saldo insuficiente."

deposit = lambda amount, balance: balance + amount

update_account_balance = lambda action, amount, balance: withdrawal(amount, balance) if action == "sacar" else deposit(amount, balance)

execute_action = (
    lambda acc_num: 
        print(f"Saldo atual: ${accounts_data[acc_num]}") or
        (lambda action:
            (lambda result:
                print(result) if isinstance(result, str) else 
                (accounts_data.update({acc_num: result}) or print(f"Saldo atualizado: ${accounts_data[acc_num]}"))
            )(update_account_balance(action, float(input("Insira o montante: ")), accounts_data[acc_num]))
        )(input("O que gostaria de fazer? (sacar/depositar): ").lower())
    if acc_num in accounts_data else 
    print("Conta não encontrada!")
)

execute_action(account_number)
