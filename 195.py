import os.path
import time, json


def clear():
    print('\n' * 12)


def desfazer():
    global TarefasRefazer, tarefas
    if not tarefas:
        print('\033[31mNão há o que desfazer.\033[m')
        time.sleep(2)
        return
    TarefasRefazer.append(tarefas[-1])
    tarefas.pop()


def refazer():
    global tarefas, TarefasRefazer
    if not TarefasRefazer:
        print('\033[31mNão há o que refazer.\033[m')
        time.sleep(2)
        return
    tarefas.append(TarefasRefazer[-1])
    TarefasRefazer.pop()


def load_list(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
            arquivo.write('[]')
            arquivo.seek(0,0)
            return json.load(arquivo)
    else:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            return json.load(arquivo)


def salvar(caminho_arquivo, lista):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)


comandos = {'desfazer': desfazer,
            'refazer': refazer
            }


tarefas = load_list('195tarefas.json')
TarefasRefazer = load_list('195TarefasRefazer.json')

while True:
    print('----------LISTA DE TAREFAS----------')
    for tarefa in tarefas:
        print(f'{tarefa:^38}')
    print()
    print('Comandos: desfazer, refazer, sair')
    comando = input('Digite uma tarefa para adicionar ou comando: ').strip().lower()
    if comando in 'sair':
        break
    if not comando in comandos.keys():
        tarefas.append(comando)
    else:
        executar = comandos.get(comando)
        executar()
    clear()

    salvar('195tarefas.json', tarefas)
    salvar('195TarefasRefazer.json', TarefasRefazer)
    continue