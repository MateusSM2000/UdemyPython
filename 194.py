import time

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


comandos = {'desfazer': desfazer,
            'refazer': refazer
            }
tarefas = []
TarefasRefazer = []
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
    continue