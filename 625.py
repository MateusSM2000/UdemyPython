from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def broadcast(self, msg: str): pass

    @abstractmethod
    def direct_msg(self,msg: str): pass


class LoggedInUser(User):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str, mediator):


    def direct_msg(self,msg: str):
        print(msg)
