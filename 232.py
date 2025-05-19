from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg):
        self.msg = msg

    @abstractmethod
    def _enviar(self) -> bool:  # -> bool apenas mostra (n tem nenhum efeito no codigo em si, é como se estivesse comentado com #) aos desenvolvedores do código qual tipo de classe este
        pass                   # metodo deve retornar como valor. No caso é booleano, ou seja, True ou False. Mas poderia ser str, int, float, ou até msm uma classe criada por vc
                                # mt util para metodos polimorficos pq as vezes eles devem retornar valores de apenas uma classe, como neste caso True ou False
    def notificar(self):
        if self._enviar():
            print('Enviado com sucesso!!')
        else:
            print('Erro: mensagem não enviada.')



class SMS(Notificacao):
    def __init__(self, msg):
        super().__init__(msg)

    def _enviar(self):
        print(f"Enviando SMS com a mensagem '{self.msg}'...")
        return True




class Email(Notificacao):
    def __init__(self, msg):
        super().__init__(msg)

    def _enviar(self):
        print(f"Enviando e-mail com a mensagem '{self.msg}'...")
        return True




email = Email('Oi como ce ta?')
email.notificar()
sms = SMS('to entendendo essa porra cada vez melhor caralhooooooo')
sms.notificar()