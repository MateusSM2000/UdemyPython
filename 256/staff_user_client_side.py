from os.path import exists
from secrets import SystemRandom as Sr
from re import fullmatch
from dateutil.relativedelta import relativedelta
from readchar import readchar
from os import system as os_system
from platform import system as pf_system
from pathlib import Path
import classes, string, datetime, csv, socket

def get_local_ip() -> str:
    try:
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        return local_ip
    except Exception as e:
        return f'{e}'

def cpf_digitos_verificadores(cpf: str) -> bool:
    digitos_e_fatores = [(int(cpf[0]), 10), (int(cpf[1]), 9), (int(cpf[2]), 8), (int(cpf[4]), 7), (int(cpf[5]), 6),
               (int(cpf[6]), 5), (int(cpf[8]), 4), (int(cpf[9]), 3), (int(cpf[10]), 2)]
    soma = 0
    for n, f in digitos_e_fatores:
        soma += n * f
    if soma % 11 < 2:
        digito_1o = 0
    else:
        digito_1o = 11 - soma % 11

    digitos_e_fatores = [(int(cpf[0]), 11), (int(cpf[1]), 10), (int(cpf[2]), 9), (int(cpf[4]), 8), (int(cpf[5]), 7),
                         (int(cpf[6]), 6), (int(cpf[8]), 5), (int(cpf[9]), 4), (int(cpf[10]), 3), (digito_1o, 2)]
    soma = 0
    for n, f in digitos_e_fatores:
        soma += n * f
    if soma % 11 < 2:
        digito_2o = 0
    else:
        digito_2o = 11 - soma % 11

    digitos_verificadores = str(digito_1o) + str(digito_2o)

    if cpf[-2:] == digitos_verificadores:
        return True
    else:
        return False

def try_again() -> None:
    print('\033[1;31mPressione ENTER para tentar novamente.\033[m', end='', flush=True)
    while True:
        char = readchar()
        if char == '\r' or char == '\n':
            print('\n')
            break

def back_main_menu() -> None:
    print('Pressione ENTER para voltar ao menu inicial.', end='', flush=True)
    while True:
        char = readchar()
        if char == '\r' or char == '\n':
            break
    limpar_tela()

def limpar_tela() -> None:
    if pf_system() == 'Windows':
        os_system('cls')
    else:
        os_system('clear')

def menu_cadastrar_cliente() -> None:
    santander = classes.Banco()
    while True:
        print('\nInsira os dados do cliente...\n')

        while True:
            cpf = input('Cpf (0 - voltar): ')
            if cpf == '0':
                limpar_tela()
                return
            if not fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf):
                print('\033[1;31mCpf inválido...\033[m\n')
                try_again()
                continue
            if fullmatch(r'^\d{11}$', cpf):
                cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
            if not cpf_digitos_verificadores(cpf):
                print('\033[1;31mCpf inválido...\033[m\n')
                try_again()
                continue
            cpf_cadastrado = False
            for dicionario in santander.clientes:
                if dicionario.get(cpf) is not None:
                    print('\033[1;31mCpf já cadastrado...\033[m\n')
                    try_again()
                    cpf_cadastrado = True
                    break
            if cpf_cadastrado:
                continue
            else:
                break

        while True:
            nome = input('Nome (0 - voltar): ').title().strip()
            if nome == '0':
                limpar_tela()
                return
            if not nome.replace(' ', '').isalpha():
                print('\033[1;31mNome digitado incorretamente...\033[m\n')
                try_again()
                continue
            break

        while True:

            data_nascimento = input('Data de nascimento [dd/mm/aaaa] (0 - voltar): ')
            if fullmatch(r'^(0|((0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/\d{4}))$', data_nascimento):
                if data_nascimento == '0':
                    limpar_tela()
                    return
            else:
                print('\033[1;31mInsira uma data válida...\033[m\n')
                try_again()
                continue
            try:
                data_nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
            except ValueError:
                print('\033[1;31mData inválida...\033[m\n')
                try_again()
                continue
            data_atual = datetime.datetime.now()
            if data_atual - relativedelta(years=91) > data_nascimento:
                print('\033[1;31mUsuário deve ter até 90 anos...\033[m\n')
                try_again()
                continue
            if data_atual - relativedelta(years=18) < data_nascimento:
                print('\033[1;31mUsuário deve ter no mínimo 18 anos...\033[m\n')
                try_again()
                continue
            if data_atual < data_nascimento:
                print('\033[1;31mEsta é uma data futura...\033[m\n')
                try_again()
                continue

            data_nascimento = datetime.datetime.strftime(data_nascimento, '%d/%m/%Y')

            break

        while True:
            numero_telefone = input('Número de contato do celular (0 - voltar): ')
            if numero_telefone == '0':
                limpar_tela()
                return
            if not fullmatch(r'^\(?\d{2}\)?\s?9\s?\d{4}([-\s]?)\d{4}$', numero_telefone):
                print('\033[1;31mNúmero de telefone inválido...\033[m\n')
                try_again()
                continue
            if numero_telefone.count('(') != numero_telefone.count(')'):
                print('\033[1;31mNúmero de telefone inválido...\033[m\n')
                try_again()
                continue
            numero_telefone = numero_telefone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
            ddds = (
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33', '34',
            '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62',
            '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85',
            '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99')
            if numero_telefone[:2] not in ddds:
                print('\033[1;31mNúmero de telefone inválido...\033[m\n')
                try_again()
                continue
            telefone_duplicado = False
            for cliente in santander.clientes:
                for cliente_ in cliente.values():
                    if isinstance(cliente_, dict):
                        if numero_telefone == cliente_.get('numero_telefone'):
                            print('\033[1;31mNúmero de telefone já cadastrado...\033[m\n')
                            telefone_duplicado = True
                            try_again()
                            break
                if telefone_duplicado:
                    break
            if telefone_duplicado:
                continue

            break

        while True:
            email = input('Insira seu e-mail (0 - voltar): ')
            if email == '0':
                limpar_tela()
                return
            if not fullmatch(r"^[^@.]+@[^@.]+\.[^.]+(\.[^.]+)?$", email):
                print('\033[1;31mE-mail inválido...\033[m\n')
                try_again()
                continue

            email_duplicado = False
            for cliente in santander.clientes:
                for cliente_ in cliente.values():
                    if isinstance(cliente_, dict):
                        if email == cliente_.get('email'):
                            email_duplicado = True
                            break
                if email_duplicado:
                    break
            if email_duplicado:
                print('\033[1;31mE-mail já cadastrado...\033[m\n')
                try_again()
                continue

            break

        while True:

            print("Sua senha deve conter um mínimo de 8 caracteres, contendo pelo menos um número, letra maiúscula e caractere especial !#$%&'()*+,-./:;<=>?@[]^_`{|}~")
            senha = ''
            print('Dê o segundo teclado ao cliente para ele digitar a senha (0 - voltar): ', end='', flush=True)

            while True:
                caractere = readchar()
                if caractere == '\r' or caractere == '\n':
                    print('\n')
                    break
                elif caractere == '\x7f' or caractere == '\b':
                    if senha:
                        senha = senha[:-1]
                        print('\b \b', end='', flush=True)
                    continue
                else:
                    senha += caractere
                    print('*', end='', flush=True)
                    continue

            if senha == '0':
                limpar_tela()
                return
            if not fullmatch(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~])[A-Za-z\d!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]{8,}$', senha):
                print('\033[1;31mSenha inválida. Insira os requisitos mínimos...\033[m')
                try_again()
                continue
            break

        print('\nRepita os dados ao cliente para confirmação:\n')
        print(f'CPF: {cpf}')
        print(f'Nome: {nome}')
        print(f'Data de nascimento: {data_nascimento}')
        print(f'Número de telefone: {numero_telefone}')
        print(f'E-mail: {email}')

        while True:
            senha_confirmacao = ''
            print('Dê o segundo teclado novamente ao cliente para o mesmo inserir sua senha e criar sua conta (0 - reinserir dados): ', end='', flush=True)

            while True:
                caractere = readchar()
                if caractere == '\r' or caractere == '\n':
                    print()
                    break
                elif caractere == '\x7f' or caractere == '\b':
                    if senha_confirmacao:
                        senha_confirmacao = senha_confirmacao[:-1]
                        print('\b \b', end='', flush=True)
                    continue
                else:
                    senha_confirmacao += caractere
                    print('*', end='', flush=True)
                    continue

            reinserir_dados = False
            if senha_confirmacao == '0':
                reinserir_dados = True
                break

            if not senha_confirmacao == senha:
                print('\033[1;31mSenha incorreta...\033[m')
                try_again()
                continue

            break

        if reinserir_dados:
            limpar_tela()
            continue
        else:
            break

    agencia = f'{Sr().randint(0, 9)}{Sr().randint(0, 9)}{Sr().randint(0, 9)}{Sr().randint(0, 9)}'

    while True:
        numero_conta = f'{Sr().randint(0, 9)}{Sr().randint(0, 9)}{Sr().randint(0, 9)}{Sr().randint(0, 9)}{Sr().randint(0, 9)}{Sr().randint(0, 9)}{Sr().randint(0, 9)}{Sr().randint(0, 9)}-{Sr().randint(0, 9)}'
        numero_conta_duplicado = False
        for cliente in santander.clientes:
            for cliente_ in cliente.values():
                if isinstance(cliente_, dict):
                    if cliente_.get('numero_conta') == numero_conta:
                        numero_conta_duplicado = True
                        break
            if numero_conta_duplicado:
                break
        if numero_conta_duplicado:
            continue
        else:
            break

    print('\nDados da conta:')
    print(f'CPF: {cpf}')
    print(f'Nome: {nome}')
    print(f'Data de nascimento: {data_nascimento}')
    print(f'Número de telefone: {numero_telefone}')
    print(f'E-mail: {email}')
    print(f'Agência: {agencia}')
    print(f'Número da conta: {numero_conta}')

    data_criacao_conta = datetime.datetime.now()

    santander.clientes.append({cpf: {'nome': nome, 'data_nascimento': data_nascimento,
                                     'numero_telefone': numero_telefone, 'email': email, 'agencia': agencia,
                                     'numero_conta': numero_conta, 'saldo_corrente': 0, 'saldo_poupanca': 0,
                                     'data_criacao_conta': datetime.datetime.strftime(data_criacao_conta, '%d/%m/%Y')},
                               'senha': senha})

    santander.dump_santander_json(santander.clientes)
    with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
        csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                  cpf, 'CONTA CRIADA', '-', get_local_ip()])

    print('\033[1;32mCadastrado com sucesso!\n\033[m')
    back_main_menu()

def menu_sacar_depositar() -> None:
    def informe_valor_saque() -> None:
        nonlocal valor
        while True:
            try:
                valor = float(input('Informe o valor do saque: R$'))
                if valor < 0:
                    print('\033[1;31mValor inválido...\033[m')
                    try_again()
                    continue
            except ValueError:
                print('\033[1;31mValor inválido...\033[m')
                try_again()
                continue
            break

    def informe_valor_deposito() -> None:
        nonlocal valor
        while True:
            try:
                valor = float(input('Informe o valor do depósito: R$'))
                if valor < 0:
                    print('\033[1;31mValor inválido...\033[m')
                    try_again()
                    continue
            except ValueError:
                print('\033[1;31mValor inválido...\033[m')
                try_again()
                continue
            break


    global menu
    print('\n1 - Conta Corrente\n2 - Conta Poupança')
    while True:
        menu_ = input('\nOpção (0 - Voltar): ')
        print()
        if menu_ == '0':
            limpar_tela()
            return
        if menu_ != '1' and menu_ != '2':
            print('\033[1;31mInsira uma opção válida...\033[m')
            try_again()
            continue
        break

    santander = classes.Banco()
    while True:
        cpf = None
        numero_conta = None
        cpf_ou_numeroconta = input('\nInsira o cpf ou número da conta do cliente (0 - Voltar): ')
        if cpf_ou_numeroconta == '0':
            limpar_tela()
            return
        if not fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf_ou_numeroconta) and not fullmatch(r'^\d{8}-?\d$', cpf_ou_numeroconta):
            print('\033[1;31mCpf ou número da conta inválido...\033[m')
            try_again()
            continue
        if fullmatch(r'^\d{11}$', cpf_ou_numeroconta):
            cpf_ou_numeroconta = cpf_ou_numeroconta[:3] + '.' + cpf_ou_numeroconta[3:6] + '.' + cpf_ou_numeroconta[6:9] + '-' + cpf_ou_numeroconta[9:]
        if fullmatch(r'^\d{9}$', cpf_ou_numeroconta):
            cpf_ou_numeroconta = cpf_ou_numeroconta[:8] + '-' + cpf_ou_numeroconta[8]
        if fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf_ou_numeroconta):
            cpf = cpf_ou_numeroconta
        if fullmatch(r'^\d{8}-?\d$', cpf_ou_numeroconta):
            numero_conta = cpf_ou_numeroconta

        if cpf:
            cpf_nao_encontrado = True
            for cliente in santander.clientes:
                if cliente.get(cpf) is not None:
                    cpf_nao_encontrado = False
                    santander.cliente = classes.Cliente(cliente)
                    break
            if cpf_nao_encontrado:
                print('\033[1;31mEste cpf não se encontra na base de dados...\033[m')
                try_again()
                continue

        if numero_conta:
            numero_conta_nao_encontrado = True
            for cliente in santander.clientes:
                for cliente_ in cliente.values():
                    if isinstance(cliente_, dict):
                        if cliente_.get('numero_conta') == numero_conta:
                            numero_conta_nao_encontrado = False
                            santander.cliente = classes.Cliente(cliente)
                            break
                if numero_conta_nao_encontrado is False:
                    break
            if numero_conta_nao_encontrado:
                print('\033[1;31mEsta conta não se encontra na base de dados...\033[m')
                try_again()
                continue

        break

    valor = None

    if menu_ == '1':
        santander.cliente.conta_corrente = classes.ContaCorrente(santander.cliente.cpf)
        print(f'Saldo Corrente: R${santander.cliente.saldo_corrente:.2f}')
        if menu == '2':
            informe_valor_saque()
            if santander.cliente.conta_corrente.sacar(valor):
                if valor != 0:
                    with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
                        csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y %H:%M:%S'),
                                                  santander.cliente.cpf, 'SAQUE C/C', str(valor).replace('.',','),
                                                  get_local_ip()])
                print(f'\033[1;32mSaque de R${valor:.2f} efetuado com sucesso!\033[m')
                back_main_menu()
            else:
                print('\033[1;31mSaque negado pois ultrapassa o limite: saldo da conta corrente + R$1000.00\033[m')
                back_main_menu()
        if menu == '3':
            informe_valor_deposito()
            if santander.cliente.conta_corrente.depositar(valor):
                if valor != 0:
                    with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
                        csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y %H:%M:%S'),
                                                  santander.cliente.cpf, 'DEPÓSITO C/C', str(valor).replace('.',','),
                                                  get_local_ip()])
                print(f'\033[1;32mDepósito de R${valor:.2f} efetuado com sucesso!\033[m')
                back_main_menu()
            else:
                print('\033[1;31mHouve algum erro.\033[m')
                back_main_menu()

    if menu_ == '2':
        santander.cliente.conta_poupanca = classes.ContaPoupanca(santander.cliente.cpf)
        print(f'Saldo Poupança: R${santander.cliente.saldo_poupanca:.2f}')
        if menu == '2':
            informe_valor_saque()
            if santander.cliente.conta_poupanca.sacar(valor):
                if valor != 0:
                    with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
                        csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y %H:%M:%S'),
                                                  santander.cliente.cpf, 'SAQUE C/P', str(valor).replace('.',','),
                                                  get_local_ip()])
                print(f'\033[1;32mValor de R${valor:.2f} movido para a conta corrente com sucesso!\033[m')
                back_main_menu()
            else:
                print('\033[1;31mSaque negado pois ultrapassa o saldo da conta.\033[m')
                back_main_menu()
        if menu == '3':
            informe_valor_deposito()
            if santander.cliente.conta_poupanca.depositar(valor):
                if valor != 0:
                    with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
                        csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y %H:%M:%S'),
                                                  santander.cliente.cpf, 'DEPÓSITO C/P', str(valor).replace('.',','),
                                                  get_local_ip()])
                print(f'\033[1;32mDepósito de R${valor:.2f} efetuado com sucesso!\033[m')
                back_main_menu()
            else:
                print('\033[1;31mDepósito negado pois ultrapassa o limite: saldo da conta corrente + R$1000.00\033[m')
                back_main_menu()

    limpar_tela()

def menu_remover_cliente() -> None:
    santander = classes.Banco()
    while True:
        cpf = input('\nInsira o cpf do cliente a ser removido (0 - Voltar): ')
        if cpf == '0':
            limpar_tela()
            break
        if not fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf):
            print('\033[1;31mCpf inválido...\033[m')
            try_again()
            continue
        if fullmatch(r'^\d{11}$', cpf):
            cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        for cliente in santander.clientes:
            if cliente.get(cpf) is not None:
                if cliente[cpf]['saldo_corrente'] or cliente[cpf]['saldo_poupanca'] > 0:
                    print('\033[1;31mEsta conta ainda possui saldo positivo. Peça ao cliente para retirar seu dinheiro antes de deletar sua conta.\033[m')
                    back_main_menu()
                    return
                santander.clientes.remove(cliente)
                santander.dump_santander_json(santander.clientes)
                with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
                    csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                              cpf, 'CONTA DELETADA', '-', get_local_ip()])
                print(f'\033[1;32mUsuário {cpf} removido com sucesso!\033[m')
                print()
                back_main_menu()
                return
        print('\033[1;31mEste cpf não se encontra cadastrado...\033[m')
        try_again()
        continue

def mostrar_dados_clientes():
    santander = classes.Banco()
    print()
    for cliente in santander.clientes:
        for cpf in cliente.keys():
            if cpf != 'senha':
                print(f"{cpf}: {cliente[cpf]}\n")

    print(f'Total de cadastros: {len(santander.clientes)}\n')
    back_main_menu()

def mostrar_dados_cliente():
    santander = classes.Banco()
    while True:
        cpf = None
        numero_conta = None
        cpf_ou_numeroconta = input('\nInsira o cpf ou número da conta do cliente (0 - Voltar): ')
        if cpf_ou_numeroconta == '0':
            limpar_tela()
            return
        if not fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf_ou_numeroconta) and not fullmatch(r'^\d{8}-?\d$', cpf_ou_numeroconta):
            print('\033[1;31mCpf ou número da conta inválido...\033[m')
            try_again()
            continue
        if fullmatch(r'^\d{11}$', cpf_ou_numeroconta):
            cpf_ou_numeroconta = cpf_ou_numeroconta[:3] + '.' + cpf_ou_numeroconta[3:6] + '.' + cpf_ou_numeroconta[6:9] + '-' + cpf_ou_numeroconta[9:]
        if fullmatch(r'^\d{9}$', cpf_ou_numeroconta):
            cpf_ou_numeroconta = cpf_ou_numeroconta[:8] + '-' + cpf_ou_numeroconta[8]
        if fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf_ou_numeroconta):
            cpf = cpf_ou_numeroconta
        if fullmatch(r'^\d{8}-?\d$', cpf_ou_numeroconta):
            numero_conta = cpf_ou_numeroconta

        if cpf:
            cpf_nao_encontrado = True
            for cliente in santander.clientes:
                if cliente.get(cpf) is not None:
                    cpf_nao_encontrado = False
                    santander.cliente = classes.Cliente(cliente)
                    break
            if cpf_nao_encontrado:
                print('\033[1;31mEste cpf não se encontra na base de dados...\033[m')
                try_again()
                continue

        if numero_conta:
            numero_conta_nao_encontrado = True
            for cliente in santander.clientes:
                for cliente_ in cliente.values():
                    if isinstance(cliente_, dict):
                        if cliente_.get('numero_conta') == numero_conta:
                            numero_conta_nao_encontrado = False
                            santander.cliente = classes.Cliente(cliente)
                            break
                if numero_conta_nao_encontrado is False:
                    break
            if numero_conta_nao_encontrado:
                print('\033[1;31mEsta conta não se encontra na base de dados...\033[m')
                try_again()
                continue

        break

    print()
    print(f'CPF: {santander.cliente.cpf}')
    print(f'Nome: {santander.cliente.nome}')
    print(f'Data de nascimento: {santander.cliente.data_nascimento}')
    print(f'E-mail: {santander.cliente.email}')
    print(f'Número de telefone: {santander.cliente.numero_telefone}')
    print(f'Data de criação da conta: {santander.cliente.data_criacao_conta}')
    print(f'Agência: {santander.cliente.agencia}')
    print(f'Número da conta: {santander.cliente.numero_conta}')
    print(f'Saldo Conta Corrente: R${santander.cliente.saldo_corrente:.2f}')
    print(f'Saldo Conta Poupança: R${santander.cliente.saldo_poupanca:.2f}\n')
    back_main_menu()

def menu_alterar_dados_cadastrais() -> None:
    santander = classes.Banco()
    while True:
        cpf = None
        numero_conta = None
        cpf_ou_numeroconta = input('\nInsira o cpf ou número da conta do cliente (0 - Voltar): ')
        if cpf_ou_numeroconta == '0':
            limpar_tela()
            return
        if not fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf_ou_numeroconta) and not fullmatch(r'^\d{8}-?\d$',
                                                                                                        cpf_ou_numeroconta):
            print('\033[1;31mCpf ou número da conta inválido...\033[m')
            try_again()
            continue
        if fullmatch(r'^\d{11}$', cpf_ou_numeroconta):
            cpf_ou_numeroconta = cpf_ou_numeroconta[:3] + '.' + cpf_ou_numeroconta[3:6] + '.' + cpf_ou_numeroconta[
                                                                                                6:9] + '-' + cpf_ou_numeroconta[
                                                                                                             9:]
        if fullmatch(r'^\d{9}$', cpf_ou_numeroconta):
            cpf_ou_numeroconta = cpf_ou_numeroconta[:8] + '-' + cpf_ou_numeroconta[8]
        if fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf_ou_numeroconta):
            cpf = cpf_ou_numeroconta
        if fullmatch(r'^\d{8}-?\d$', cpf_ou_numeroconta):
            numero_conta = cpf_ou_numeroconta

        if cpf:
            cpf_nao_encontrado = True
            for cliente in santander.clientes:
                if cliente.get(cpf) is not None:
                    cpf_nao_encontrado = False
                    santander.cliente = classes.Cliente(cliente)
                    break
            if cpf_nao_encontrado:
                print('\033[1;31mEste cpf não se encontra na base de dados...\033[m')
                try_again()
                continue

        if numero_conta:
            numero_conta_nao_encontrado = True
            for cliente in santander.clientes:
                for cliente_ in cliente.values():
                    if isinstance(cliente_, dict):
                        if cliente_.get('numero_conta') == numero_conta:
                            numero_conta_nao_encontrado = False
                            santander.cliente = classes.Cliente(cliente)
                            break
                if numero_conta_nao_encontrado is False:
                    break
            if numero_conta_nao_encontrado:
                print('\033[1;31mEsta conta não se encontra na base de dados...\033[m')
                try_again()
                continue

        break

    print(f'\nCPF: {santander.cliente.cpf}')
    print(f'1 - Nome: {santander.cliente.nome}')
    print(f'2 - Data de nascimento: {santander.cliente.data_nascimento}')
    print(f'3 - E-mail: {santander.cliente.email}')
    print(f'4 - Número de telefone: {santander.cliente.numero_telefone}')
    print(f'5 - Agência: {santander.cliente.agencia}')
    print(f'6 - Senha: {len(cliente['senha']) * '*'}\n')

    while True:
        opcao = input('Qual dado o cliente deseja alterar (0 - voltar)? ')
        if opcao == '0':
            return
        if opcao not in ('1', '2', '3', '4', '5', '6'):
            print('\033[1;31mInsira uma opção válida...\033[m')
            try_again()
            continue
        print()
        break

    if opcao == '1':
        while True:
            novo_nome = input('Novo nome: (0 - voltar): ').title().strip()
            if novo_nome == '0':
                limpar_tela()
                return
            if not novo_nome.replace(' ', '').isalpha():
                print('\033[1;31mNome digitado incorretamente...\033[m\n')
                try_again()
                continue
            break

        for cliente in santander.clientes:
            if cliente.get(santander.cliente.cpf):
                antigo_nome = cliente[santander.cliente.cpf]['nome']
                cliente[santander.cliente.cpf]['nome'] = novo_nome
                santander.dump_santander_json(santander.clientes)
                break

        with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
            log_writer = csv.writer(log)
            log_writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                 santander.cliente.cpf, 'MUDANÇA DE NOME', f'DE {antigo_nome} PARA {novo_nome}',
                                 get_local_ip()])

        print('\033[1;32mNome alterado com sucesso!\033[m')
        back_main_menu()


    if opcao == '2':
        while True:
            nova_data_nascimento = input('Data de nascimento [dd/mm/aaaa] (0 - voltar): ')
            if fullmatch(r'^(0|((0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/\d{4}))$', nova_data_nascimento):
                if nova_data_nascimento == '0':
                    limpar_tela()
                    return
            else:
                print('\033[1;31mInsira uma data válida...\033[m\n')
                try_again()
                continue
            try:
                nova_data_nascimento = datetime.datetime.strptime(nova_data_nascimento, '%d/%m/%Y')
            except ValueError:
                print('\033[1;31mData inválida...\033[m\n')
                try_again()
                continue
            data_atual = datetime.datetime.now()
            if data_atual - relativedelta(years=91) > nova_data_nascimento:
                print('\033[1;31mUsuário deve ter até 90 anos...\033[m\n')
                try_again()
                continue
            if data_atual - relativedelta(years=18) < nova_data_nascimento:
                print('\033[1;31mUsuário deve ter no mínimo 18 anos...\033[m\n')
                try_again()
                continue
            if data_atual < nova_data_nascimento:
                print('\033[1;31mEsta é uma data futura...\033[m\n')
                try_again()
                continue

            nova_data_nascimento = datetime.datetime.strftime(nova_data_nascimento, '%d/%m/%Y')

            break

        for cliente in santander.clientes:
            if cliente.get(santander.cliente.cpf):
                antiga_data_nascimento = cliente[santander.cliente.cpf]['data_nascimento']
                cliente[santander.cliente.cpf]['data_nascimento'] = nova_data_nascimento
                break

        santander.dump_santander_json(santander.clientes)

        with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
            log_writer = csv.writer(log)
            log_writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                 santander.cliente.cpf, 'MUDANÇA DE DATA DE NASCIMENTO', f'DE {antiga_data_nascimento} PARA {nova_data_nascimento}',
                                 get_local_ip()])

        print('\033[1;32mData de nascimento alterada com sucesso!\033[m')
        back_main_menu()


    if opcao == '3':
        while True:
            novo_email = input('Insira o novo e-mail (0 - voltar): ')
            if novo_email == '0':
                limpar_tela()
                return
            if not fullmatch(r"^[^@.]+@[^@.]+\.[^.]+(\.[^.]+)?$", novo_email):
                print('\033[1;31mE-mail inválido...\033[m\n')
                try_again()
                continue

            email_duplicado = False
            for cliente in santander.clientes:
                for cliente_ in cliente.values():
                    if isinstance(cliente_, dict):
                        if novo_email == cliente_.get('email'):
                            email_duplicado = True
                            break
                if email_duplicado:
                    break
            if email_duplicado:
                print('\033[1;31mE-mail já cadastrado...\033[m\n')
                try_again()
                continue

            break

        for cliente in santander.clientes:
            if cliente.get(santander.cliente.cpf):
                antigo_email = cliente[santander.cliente.cpf]['email']
                cliente[santander.cliente.cpf]['email'] = novo_email
                break

        santander.dump_santander_json(santander.clientes)

        with open(Path(__file__).parent / 'log.csv' , 'a', encoding='utf_8', newline='') as log:
            log_writer = csv.writer(log)
            log_writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                 santander.cliente.cpf, 'MUDANÇA DE EMAIL', f'DE {antigo_email} PARA {novo_email}',
                                 get_local_ip()])

        print('\033[1;32mE-mail alterado com sucesso!\033[m')
        back_main_menu()


    if opcao == '4':
        while True:
            novo_numero_telefone = input('Novo número de contato do celular (0 - voltar): ')
            if novo_numero_telefone == '0':
                limpar_tela()
                return
            if not fullmatch(r'^\(?\d{2}\)?\s?9\s?\d{4}([-\s]?)\d{4}$', novo_numero_telefone):
                print('\033[1;31mNúmero de telefone inválido...\033[m\n')
                try_again()
                continue
            if novo_numero_telefone.count('(') != novo_numero_telefone.count(')'):
                print('\033[1;31mNúmero de telefone inválido...\033[m\n')
                try_again()
                continue
            novo_numero_telefone = novo_numero_telefone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
            ddds = (
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33', '34',
            '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62',
            '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85',
            '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99')
            if novo_numero_telefone[:2] not in ddds:
                print('\033[1;31mNúmero de telefone inválido...\033[m\n')
                try_again()
                continue
            telefone_duplicado = False
            for cliente in santander.clientes:
                for cliente_ in cliente.values():
                    if isinstance(cliente_, dict):
                        if novo_numero_telefone == cliente_.get('numero_telefone'):
                            print('\033[1;31mNúmero de telefone já cadastrado...\033[m\n')
                            telefone_duplicado = True
                            try_again()
                            break
                if telefone_duplicado:
                    break
            if telefone_duplicado:
                continue

            break

        for cliente in santander.clientes:
            if cliente.get(santander.cliente.cpf):
                antigo_numero_telefone = cliente[santander.cliente.cpf]['numero_telefone']
                cliente[santander.cliente.cpf]['numero_telefone'] = novo_numero_telefone
                break

        santander.dump_santander_json(santander.clientes)

        with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
            log_writer = csv.writer(log)
            log_writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                 santander.cliente.cpf, 'MUDANÇA DE TELEFONE', f'DE {antigo_numero_telefone} PARA {novo_numero_telefone}',
                                 get_local_ip()])

        print('\033[1;32mNúmero de telefone alterado com sucesso!\033[m')
        back_main_menu()


    if opcao == '5':
        while True:
            nova_agencia = input('Insira a nova agência (0 - voltar): ')
            if nova_agencia == '0':
                limpar_tela()
                return
            if not fullmatch(r"^\d{4}$", nova_agencia):
                print('\033[1;31mAgência inválida...\033[m\n')
                try_again()
                continue
            break

        for cliente in santander.clientes:
            if cliente.get(santander.cliente.cpf):
                antiga_agencia = cliente[santander.cliente.cpf]['agencia']
                cliente[santander.cliente.cpf]['agencia'] = nova_agencia
                break

        santander.dump_santander_json(santander.clientes)

        with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
            log_writer = csv.writer(log)
            log_writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                 santander.cliente.cpf, 'MUDANÇA DE AGÊNCIA', f'DE {antiga_agencia} PARA {nova_agencia}',
                                 get_local_ip()])

        print('\033[1;32mAgência alterada com sucesso!\033[m')
        back_main_menu()


    if opcao == '6':
        while True:
            print("Sua senha deve conter um mínimo de 8 caracteres, contendo pelo menos um número, letra maiúscula e caractere especial !#$%&'()*+,-./:;<=>?@[]^_`{|}~")
            nova_senha = ''
            print('Dê o segundo teclado ao cliente para ele digitar sua nova senha (0 - voltar): ', end='', flush=True)

            while True:
                caractere = readchar()
                if caractere == '\r' or caractere == '\n':
                    print('\n')
                    break
                elif caractere == '\x7f' or caractere == '\b':
                    if nova_senha:
                        nova_senha = nova_senha[:-1]
                        print('\b \b', end='', flush=True)
                    continue
                else:
                    nova_senha += caractere
                    print('*', end='', flush=True)
                    continue

            if nova_senha == '0':
                limpar_tela()
                return
            if not fullmatch(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~])[A-Za-z\d!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]{8,}$', nova_senha):
                print('\033[1;31mSenha inválida. Insira os requisitos mínimos...\033[m')
                try_again()
                continue
            break

        for cliente in santander.clientes:
            if cliente.get(santander.cliente.cpf):
                cliente['senha'] = nova_senha
                break

        santander.dump_santander_json(santander.clientes)

        with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
            log_writer = csv.writer(log)
            log_writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                 santander.cliente.cpf, 'MUDANÇA DE SENHA', '-', get_local_ip()])

        print('\033[1;32mSenha alterada com sucesso!\033[m')
        back_main_menu()







#------------------------------------------MAIN-----------------------------------------------------






if not exists(Path(__file__).parent / 'log.csv'):
    with open(Path(__file__).parent/ 'log.csv', 'w', encoding='utf_8', newline='') as log:
        colunas = ['Data', 'CPF da conta', 'Tipo de Movimentação', 'Valor', 'MAC Address / IP local']
        csv.writer(log).writerow(colunas)

if not exists(Path(__file__).parent / 'santander.json'):
    with open(Path(__file__).parent / 'santander.json', 'w', encoding='utf_8') as clientes_db:
        clientes_db.write('[]')


while True:
    print(' SISTEMA BANCÁRIO SANTANDER '.center(50, '~'))
    print('\nMenu de opções:\n\n1 - Cadastrar cliente\n2 - Sacar\n3 - Depositar\n4 - Remover cliente do sistema\n'
          '5 - Mostrar todos os clientes\n6 - Mostrar dados de um cliente\n7 - Alterar dados cadastrais')
    while True:
        menu = input('\nOpção: ')
        if menu not in ('1', '2', '3', '4', '5', '6', '7'):
            print('\033[1;31mInsira uma opção válida...\033[m')
            try_again()
            continue
        break

    if menu == '1':
        menu_cadastrar_cliente()

    if menu == '2' or menu == '3':
        menu_sacar_depositar()

    if menu == '4':
        menu_remover_cliente()

    if menu == '5':
        mostrar_dados_clientes()

    if menu == '6':
        mostrar_dados_cliente()

    if menu == '7':
        menu_alterar_dados_cadastrais()

    limpar_tela()

    continue