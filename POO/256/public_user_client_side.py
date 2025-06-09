from re import fullmatch
from secrets import SystemRandom as Sr
from dateutil.relativedelta import relativedelta
from os.path import exists
from os import system as os_system
from platform import system as pf_system
from pathlib import Path
from readchar import readchar
from dotenv import load_dotenv
from os import getenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from aiosmtplib import send
from typing import Any
import classes, string, datetime, csv, uuid, asyncio

async def enviar_email(cpf:str, nome_arquivo_msg_email:str, assunto_email:str, **key_value_template:Any) -> None:
    async def aguarde() -> None:
        nonlocal i
        print('Aguarde', end='', flush=True)
        while True:
            i = 0
            await asyncio.sleep(0.5)
            print('.', end='', flush=True)
            i = 1
            await asyncio.sleep(0.5)
            print('.', end='', flush=True)
            i = 2
            await asyncio.sleep(0.5)
            print('.', end='', flush=True)
            i = 3
            await asyncio.sleep(0.5)
            print('\b\b\b   \b\b\b', end='', flush=True)

    i = None
    task_aguarde = asyncio.create_task(aguarde())
    await asyncio.sleep(0)

    load_dotenv()
    remetente = getenv('FROM_EMAIL')
    for cliente_ in classes.Banco().clientes:
        if cliente_.get(cpf):
            to_email = cliente_[cpf]['email']
            break
    destinatario = to_email
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = remetente
    smtp_password = getenv('EMAIL_PASSWORD')
    CAMINHO_MENSAGEM_HTML = Path(__file__).parent / nome_arquivo_msg_email
    with open(CAMINHO_MENSAGEM_HTML, 'r', encoding='utf_8') as file:
        mensagem_arquivo = file.read()
        template = string.Template(mensagem_arquivo)
        mensagem_texto = template.substitute(**key_value_template)
    mime_multipart = MIMEMultipart()
    mime_multipart['from'] = remetente
    mime_multipart['to'] = destinatario
    mime_multipart['subject'] = assunto_email
    corpo_email = MIMEText(mensagem_texto, 'html', 'utf-8')
    mime_multipart.attach(corpo_email)
    await send(mime_multipart, hostname=smtp_server, port=smtp_port, start_tls=True, username=smtp_username,
               password=smtp_password)

    task_aguarde.cancel()
    print('\b' * (7 + i) + ' ' * (7 + i))

def get_mac_address() -> str:
    try:
        mac_address = uuid.getnode()
        mac_address_formatado = ':'.join(f'{(mac_address >> i) & 0xff:02x}' for i in range(40, -1, -8))
        return mac_address_formatado
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

def login() -> bool:
    cadastrado = input('Já é nosso cliente? [S/N]\n').lower().strip()[:3]
    print()
    santander = classes.Banco()
    if cadastrado in 'sim':

        cpf = input('CPF: ')
        if not fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf):
            print('\033[1;31mCPF inválido...\033[m')
            try_again()
            return False
        if fullmatch(r'^\d{11}$', cpf):
            cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
        cpf_nao_encontrado = True
        for dicionario in santander.clientes:
            if dicionario.get(cpf) is not None:
                nome = dicionario[cpf]['nome']
                to_email = dicionario[cpf]['email']
                cpf_nao_encontrado = False
                break
        if cpf_nao_encontrado:
            print('\033[1;31mCPF não cadastrado...\033[m')
            try_again()
            return False


        senha = ''
        print('Senha (0 - Esqueci minha senha): ', end='', flush=True)

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
            while True:
                nova_senha = ''.join(
                    Sr().choices(string.ascii_letters + string.digits + "!#$%&'()*+,-./:;<=>?@[]^_`{|}~", k=Sr().randint(8, 20)))
                if fullmatch(
                        r'^(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~])[A-Za-z\d!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]{8,}$',
                        nova_senha):
                    break

            asyncio.run(enviar_email(cpf, 'esqueci_senha.html', 'Nova senha solicitada', nome=nome, senha=nova_senha))

            for cliente_ in santander.clientes:
                if cliente_.get(cpf):
                    cliente_['senha'] = nova_senha
                    break
            santander.dump_santander_json(santander.clientes)

            with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
                log_writer = csv.writer(log)
                log_writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                     cpf, 'MUDANÇA DE SENHA', '-', get_mac_address()])

            print(f'\033[1;32mUma nova senha foi enviada ao seu e-mail {to_email}\033[m')
            print('Pressione ENTER para voltar à tela de login.', end='', flush=True)
            while True:
                caractere = readchar()
                if caractere == '\r' or caractere == '\n':
                    return False

        for dicionario in santander.clientes:
            if dicionario.get(cpf) is not None:
                if dicionario.get('senha') == senha:
                    global cliente
                    cliente = dicionario
                    return True
                else:
                    print('\033[1;31mSenha incorreta...\033[m')
                    try_again()
                    return False



    else:
        limpar_tela()
        while True:

            print('--------------- CADASTRO DE NOVA CONTA ---------------')
            print('\nInsira seus dados...\n')
            while True:
                cpf = input('Cpf (0 - voltar): ')
                if cpf == '0':
                    return False
                if not fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf):
                    print('\033[1;31mCpf inválido...\033[m')
                    try_again()
                    continue
                if fullmatch(r'^\d{11}$', cpf):
                    cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
                if not cpf_digitos_verificadores(cpf):
                    print('\033[1;31mCpf inválido...\033[m')
                    try_again()
                    continue
                cpf_cadastrado = False
                for dicionario in santander.clientes:
                    if dicionario.get(cpf) is not None:
                        print('\033[1;31mCpf já cadastrado...\033[m')
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
                    return False
                if not nome.replace(' ', '').isalpha():
                    print('\033[1;31mNome digitado incorretamente...\033[m')
                    try_again()
                    continue
                break

            while True:

                data_nascimento = input('Data de nascimento [dd/mm/aaaa] (0 - voltar): ')
                if fullmatch(r'^(0|((0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/\d{4}))$', data_nascimento):
                    if data_nascimento == '0':
                        return False
                else:
                    print('\033[1;31mInsira uma data válida...\033[m')
                    try_again()
                    continue
                try:
                    data_nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
                except ValueError:
                    print('\033[1;31mData inválida...\033[m')
                    try_again()
                    continue
                data_atual = datetime.datetime.now()
                if data_atual - relativedelta(years=91) > data_nascimento:
                    print('\033[1;31mUsuário deve ter até 90 anos...\033[m')
                    try_again()
                    continue
                if data_atual - relativedelta(years=18) < data_nascimento:
                    print('\033[1;31mUsuário deve ter no mínimo 18 anos...\033[m')
                    try_again()
                    continue
                if data_atual < data_nascimento:
                    print('\033[1;31mEsta é uma data futura...\033[m')
                    try_again()
                    continue

                data_nascimento = datetime.datetime.strftime(data_nascimento, '%d/%m/%Y')
                break

            while True:
                numero_telefone = input('Insira o número de contato do seu celular (0 - voltar): ')
                if numero_telefone == '0':
                    return False
                if not fullmatch(r'^\(?\d{2}\)?\s?9\s?\d{4}([-\s]?)\d{4}$', numero_telefone):
                    print('\033[1;31mNúmero de telefone inválido...\033[m')
                    try_again()
                    continue
                if numero_telefone.count('(') != numero_telefone.count(')'):
                    print('\033[1;31mNúmero de telefone inválido...\033[m')
                    try_again()
                    continue
                numero_telefone = numero_telefone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
                ddds = (
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33',
                '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55',
                '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82',
                '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99')
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
                    return False
                if not fullmatch(r"^[^@.]+@[^@.]+\.[^.]+(\.[^.]+)?$", email):
                    print('\033[1;31mE-mail inválido...\033[m')
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

                senha_opcao = input('Deseja que o sistema crie uma senha forte para você (0 - voltar)? [S/N]\n').lower().strip()[:3]
                if senha_opcao == '0':
                    return False
                if senha_opcao in 'sim':
                    while True:
                        senha = ''.join(Sr().choices(string.ascii_letters + string.digits + "!#$%&'()*+,-./:;<=>?@[]^_`{|}~", k=Sr().randint(8, 20)))
                        if fullmatch(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~])[A-Za-z\d!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]{8,}$', senha):
                            break
                    break

                else:
                    print("Sua senha deve conter um mínimo de 8 caracteres, contendo pelo menos um número, letra maiúscula e caractere especial !#$%&'()*+,-./:;<=>?@[]^_`{|}~")
                    senha = ''
                    print('Insira uma senha (0 - voltar): ', end='', flush=True)

                    while True:
                        caractere = readchar()
                        if caractere == '\r' or caractere == '\n':
                            print()
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
                        return False
                    if not fullmatch(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~])[A-Za-z\d!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]{8,}$', senha):
                        print('\033[1;31mSenha inválida. Insira os requisitos mínimos...\033[m')
                        try_again()
                        continue
                    break

            print('\nConfira os dados da sua conta:\n')
            print(f'CPF: {cpf}')
            print(f'Nome: {nome}')
            print(f'Data de nascimento: {data_nascimento}')
            print(f'Número de telefone: {numero_telefone}')
            print(f'E-mail: {email}')
            print(f'Senha: {senha}\n' if senha_opcao in 'sim' else f'Senha: {'*' * len(senha)}\n')

            while True:
                senha_confirmacao = ''
                print('Insira sua senha para confirmar seus dados e criar sua conta (0 - reinserir dados): ', end='', flush=True)

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

        print('\nSeus dados da conta:')
        print(f'CPF: {cpf}')
        print(f'Nome: {nome}')
        print(f'Data de nascimento: {data_nascimento}')
        print(f'Número de telefone: {numero_telefone}')
        print(f'E-mail: {email}')
        print(f'Agência: {agencia}')
        print(f'Número da conta: {numero_conta}')
        print(f'Senha: {senha}\n' if senha_opcao in 'sim' else f'Senha: {'*' * len(senha)}\n')

        data_criacao_conta = datetime.datetime.now()

        santander.clientes.append({cpf: {'nome': nome, 'data_nascimento': data_nascimento,
                                         'numero_telefone': numero_telefone, 'email': email, 'agencia': agencia,
                                         'numero_conta': numero_conta, 'saldo_corrente': 0, 'saldo_poupanca': 0,
                                         'data_criacao_conta': datetime.datetime.strftime(data_criacao_conta, '%d/%m/%Y')},
                                   'senha': senha})

        santander.dump_santander_json(santander.clientes)
        with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
            csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                      cpf, 'CONTA CRIADA', '-', get_mac_address()])

        print('\033[1;32mCadastrado com sucesso!\n\033[m')
        back_main_menu()

        return False

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

    global santander
    valor = None

    if menu_ == '1':
        santander.cliente.conta_corrente = classes.ContaCorrente(santander.cliente.cpf)
        print(f'Saldo Corrente: R${santander.cliente.saldo_corrente:.2f}')
        if menu == '1':
            informe_valor_saque()
            if santander.cliente.conta_corrente.sacar(valor):
                if valor != 0:
                    with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
                        csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y %H:%M:%S'),
                                                  santander.cliente.cpf, 'SAQUE C/C', str(valor).replace('.',','),
                                                  get_mac_address()])
                print(f'\033[1;32mSaque de R${valor:.2f} efetuado com sucesso!\033[m')
                back_main_menu()
            else:
                print(
                    '\033[1;31mSaque negado pois ultrapassa o limite: saldo da conta corrente + R$1000.00\033[m')
                back_main_menu()
        if menu == '2':
            informe_valor_deposito()
            if santander.cliente.conta_corrente.depositar(valor):
                if valor != 0:
                    with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
                        csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y %H:%M:%S'),
                                                  santander.cliente.cpf, 'DEPÓSITO C/C', str(valor).replace('.',','),
                                                  get_mac_address()])
                print(f'\033[1;32mDepósito de R${valor:.2f} efetuado com sucesso!\033[m')
                back_main_menu()
            else:
                print('\033[1;31mHouve algum erro.\033[m')
                back_main_menu()

    if menu_ == '2':
        santander.cliente.conta_poupanca = classes.ContaPoupanca(santander.cliente.cpf)
        print(f'Saldo Poupança: R${santander.cliente.saldo_poupanca:.2f}')
        if menu == '1':
            informe_valor_saque()
            if santander.cliente.conta_poupanca.sacar(valor):
                if valor != 0:
                    with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
                        csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y %H:%M:%S'),
                                                  santander.cliente.cpf, 'SAQUE C/P', str(valor).replace('.',','),
                                                  get_mac_address()])
                print(f'\033[1;32mValor de R${valor:.2f} movido para a conta corrente com sucesso!\033[m')
                back_main_menu()
            else:
                print('\033[1;31mSaque negado pois ultrapassa o saldo da conta.\033[m')
                back_main_menu()
        if menu == '2':
            informe_valor_deposito()
            if santander.cliente.conta_poupanca.depositar(valor):
                if valor != 0:
                    with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
                        csv.writer(log).writerow([datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y %H:%M:%S'),
                                                  santander.cliente.cpf, 'DEPÓSITO C/P', str(valor).replace('.',','),
                                                  get_mac_address()])
                print(f'\033[1;32mDepósito de R${valor:.2f} efetuado com sucesso!\033[m')
                back_main_menu()
            else:
                print(
                    '\033[1;31mDepósito negado pois ultrapassa o limite: saldo da conta corrente + R$1000.00\033[m')
                back_main_menu()

def menu_visualizar_dados_cadastrais() -> None:
    global santander
    print(f'\nNome: {santander.cliente.nome}')
    print(f'Data de nascimento: {santander.cliente.data_nascimento}')
    print(f'Telefone: {'(' + santander.cliente.numero_telefone[:2] + ') 9 ' + santander.cliente.numero_telefone[3:7] + 
          '-' + santander.cliente.numero_telefone[7:]}')
    print(f'E-mail: {santander.cliente.email}')
    print(f'Agência: {santander.cliente.agencia}')
    print(f'Número da conta: {santander.cliente.numero_conta}\n')
    back_main_menu()

def menu_alterar_dados_cadastrais() -> None:
    print('\nQual dado cadastral deseja alterar?\n')
    print('1 - E-mail')
    print('2 - Telefone')
    print('3 - Senha')
    print('4 - Voltar\n')
    while True:
        menu = input('Opção: ')
        if menu not in ('1', '2', '3', '4'):
            print('\033[1;31mInsira uma opção válida...\033[m')
            try_again()
            continue
        break
    if menu == '4':
        return

    codigo = ''.join(Sr().choices(string.ascii_letters + string.digits, k=6))

    global santander

    print()
    asyncio.run(enviar_email(santander.cliente.cpf, 'codigo_alterar_dados.html',
                             'Código para alterar dados cadastrais', nome=santander.cliente.nome,
                             codigo=codigo))

    while True:
        codigo_input = input(f'\nInsira o código enviado ao seu e-mail {santander.cliente.email} (0 - voltar): ')
        if codigo_input == '0':
            return
        if codigo_input != codigo:
            print('\033[1;31mCódigo inválido...\033[m')
            try_again()
            continue
        break

    if menu == '1':
        while True:
            novo_email = input('Insira seu novo e-mail (0 - voltar): ')
            if novo_email == '0':
                return
            if not fullmatch(r"^[^@.]+@[^@.]+\.[^.]+(\.[^.]+)?$", novo_email):
                print('\033[1;31mE-mail inválido...\033[m')
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

        while True:
            confirmacao_email = input('Reinsira novamente seu novo e-mail para confirmar (0 - voltar): ')
            if confirmacao_email == '0':
                return
            if confirmacao_email == novo_email:
                break
            print('\033[1;31mE-mail inválido...\033[m')
            try_again()
            continue

        for cliente in santander.clientes:
            if cliente.get(santander.cliente.cpf):
                antigo_email = cliente[santander.cliente.cpf]['email']
                cliente[santander.cliente.cpf]['email'] = novo_email
                santander.dump_santander_json(santander.clientes)
                break

        with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
            log_writer = csv.writer(log)
            log_writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                 santander.cliente.cpf, 'MUDANÇA DE EMAIL', f'DE {antigo_email} PARA {novo_email}',
                                 get_mac_address()])

        print('\033[1;32mE-mail alterado com sucesso!\033[m')
        back_main_menu()


    if menu == '2':
        while True:
            novo_telefone = input('Insira o seu novo número de contato do celular (0 - voltar): ')
            if novo_telefone == '0':
                return
            if not fullmatch(r'^\(?\d{2}\)?\s?9\s?\d{4}([-\s]?)\d{4}$', novo_telefone):
                print('\033[1;31mNúmero de telefone inválido...\033[m')
                try_again()
                continue
            if novo_telefone.count('(') != novo_telefone.count(')'):
                print('\033[1;31mNúmero de telefone inválido...\033[m')
                try_again()
                continue
            novo_telefone = novo_telefone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
            ddds = (
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28', '31', '32', '33',
                '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55',
                '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82',
                '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99')
            if novo_telefone[:2] not in ddds:
                print('\033[1;31mNúmero de telefone inválido...\033[m\n')
                try_again()
                continue
            telefone_duplicado = False
            for cliente in santander.clientes:
                for cliente_ in cliente.values():
                    if isinstance(cliente_, dict):
                        if novo_telefone == cliente_.get('numero_telefone'):
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
                antigo_telefone = cliente[santander.cliente.cpf]['numero_telefone']
                cliente[santander.cliente.cpf]['numero_telefone'] = novo_telefone
                santander.dump_santander_json(santander.clientes)
                break

        with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
            log_writer = csv.writer(log)
            log_writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                 santander.cliente.cpf, 'MUDANÇA DE TELEFONE', f'DE {antigo_telefone} PARA {novo_telefone}',
                                 get_mac_address()])

        print('\033[1;32mNúmero de telefone alterado com sucesso!\033[m')
        back_main_menu()


    if menu == '3':
        while True:
            senha_opcao = input(
                'Deseja que o sistema crie uma nova senha forte para você (0 - voltar)? [S/N]\n').lower().strip()[:3]
            if senha_opcao == '0':
                return
            if senha_opcao in 'sim':
                while True:
                    nova_senha = ''.join(
                        Sr().choices(string.ascii_letters + string.digits + "!#$%&'()*+,-./:;<=>?@[]^_`{|}~", k=Sr().randint(8, 20)))
                    if fullmatch(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~])[A-Za-z\d!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]{8,}$', nova_senha):
                        break
                break

            else:
                print("Sua senha deve conter um mínimo de 8 caracteres, contendo pelo menos um número, letra maiúscula e caractere especial !#$%&'()*+,-./:;<=>?@[]^_`{|}~")
                nova_senha = ''
                print('Insira sua nova senha (0 - voltar): ', end='', flush=True)

                while True:
                    caractere = readchar()
                    if caractere == '\r' or caractere == '\n':
                        print()
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
                    return
                if not fullmatch(
                        r'^(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~])[A-Za-z\d!#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~]{8,}$',
                        nova_senha):
                    print('\033[1;31mSenha inválida. Insira os requisitos mínimos...\033[m')
                    try_again()
                    continue
                break

        print(f'Sua nova senha é: {nova_senha}' if senha_opcao in 'sim' else f'Sua nova senha é: {'*' * len(nova_senha)}')

        while True:
            print('\nInsira novamente sua nova senha para confirmação (0 - voltar): ', end='', flush=True)
            senha_confirmacao = ''
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

            if senha_confirmacao == '0':
                return
            if not senha_confirmacao == nova_senha:
                print('\033[1;31mSenha incorreta...\033[m')
                try_again()
                continue

            break

        for cliente in santander.clientes:
            if cliente.get(santander.cliente.cpf):
                cliente['senha'] = nova_senha
                santander.dump_santander_json(santander.clientes)
                break

        with open(Path(__file__).parent / 'log.csv', 'a', encoding='utf_8', newline='') as log:
            log_writer = csv.writer(log)
            log_writer.writerow([datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y %H:%M:%S'),
                                 santander.cliente.cpf, 'MUDANÇA DE SENHA', '-', get_mac_address()])

        print('\033[1;32mSenha alterada com sucesso!\033[m')
        back_main_menu()








#------------------------------------------MAIN------------------------------------------------------







if not exists(Path(__file__).parent / 'log.csv'):
    with open(Path(__file__).parent/ 'log.csv', 'w', encoding='utf_8', newline='') as log:
        colunas = ['Data', 'CPF da conta', 'Tipo de Movimentação', 'Valor', 'MAC Address / IP local']
        csv.writer(log).writerow(colunas)

if not exists(Path(__file__).parent / 'santander.json'):
    with open(Path(__file__).parent / 'santander.json', 'w', encoding='utf_8') as clientes_db:
        clientes_db.write('[]')

while True:

    cliente = None
    limpar_tela()

    print('''
     Bem-Vindo ao Santander!
           
------------ LOGIN ------------
    ''')
    if login():
        while True:
            santander = classes.Banco()
            santander.cliente = classes.Cliente(cliente)
            limpar_tela()
            print(f'Bem-vindo novamente, {santander.cliente.nome}!\n')
            print(f'Limite da conta corrente: saldo + R$1000.00')
            print(f'Saldo conta corrente: R${santander.cliente.saldo_corrente}')
            print(f'Saldo conta poupança: R${santander.cliente.saldo_poupanca}\n')
            print('~~~~~~~~~~ MENU INICIAL ~~~~~~~~~~')
            print('1 - Sacar')
            print('2 - Depositar')
            print('3 - Visualizar dados cadastrais')
            print('4 - Alterar dados cadastrais')
            print('5 - Sair\n')
            menu = input('Opção: ')
            if menu not in ('1', '2', '3', '4', '5'):
                print('\033[1;31mInsira uma opção válida...\033[m')
                try_again()
                continue
            if menu == '1' or menu == '2':
                menu_sacar_depositar()
            if menu == '3':
                menu_visualizar_dados_cadastrais()
            if menu == '4':
                menu_alterar_dados_cadastrais()
            if menu == '5':
                break
            continue
    else:
        limpar_tela()
        continue