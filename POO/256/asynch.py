import asyncio

async def enviar_email():
    async def aguarde():
        nonlocal i
        print('Aguarde', end='')
        while True:
            i = 0
            await asyncio.sleep(0.5)
            print('.', end='')
            i = 1
            await asyncio.sleep(0.5)
            print('.', end='')
            i = 2
            await asyncio.sleep(0.5)
            print('.', end='')
            i = 3
            await asyncio.sleep(0.5)
            print('\b\b\b   \b\b\b', end='')
    print('Enviando e-mail.')
    i = None
    task_aguarde = asyncio.create_task(aguarde())
    await asyncio.sleep(5)  #simula o envio de e-mail
    task_aguarde.cancel()
    print('\b' * (7+i) + ' ' * (7+i))
    print('E-mail enviado!')



asyncio.run(enviar_email())