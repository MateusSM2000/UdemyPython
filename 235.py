#podemos adicionar notas quando levantamos alguma exceção

class MeuError(Exception):
    pass



erro = MeuError('Algum erro ocorreu.')
erro.add_note('Este erro ocorreu por conta de tal coisa')
erro.add_note('Descrevendo tal coisa...')
print(erro.__notes__)
raise erro        #n dá pra colocoar .add_note() no proprio raise, tem q colocar uma variavel com o erro e dai usar o .add_note() nessa variavel e dps dar raise nessa variavel