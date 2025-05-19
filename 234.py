#exceções são classes. Podemos criar nossa propria exceção criando uma classe q herda de Exception
#por covenção, classes q herdam de Exception tem como sua ultima parte do nome escrito 'Error'
#se escrever raise e deixar vazio durante a tratação de um erro, o erro q tá sendo tratado é levantado novamente

class MeuError(Exception):
    @staticmethod
    def levantar_erro():
        raise MeuError('Algum erro ocorreu.')



try:
    raise MeuError('Algum erro ocorreu')
except MeuError as error:
    print(error)
    print()

#caso n apareça de qual classe está ocorrendo o erro, podemos fazer o seguinte para descobrir:

class OutroError(Exception):
    @staticmethod
    def levantar_erro():
        raise OutroError('Outro erro ocorreu.')


try:
    MeuError.levantar_erro()
    OutroError.levantar_erro()
except (OutroError, MeuError) as error:
    print(error.__class__.__name__)


#tbm podemos fazer com q o traceback nos diga q um erro foi levantado a partir do tratamento de outro erro, como no caso a seguir:

try:
    MeuError.levantar_erro()
except MeuError as error:
    raise OutroError('Outro erro ocorreu') from error