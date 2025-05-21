#neste design pattern (mediator) temos uma classe mediadora q recebe os objetos de uma classe e as utiliza

from __future__ import annotations
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name: str, mediator: ABCMediator) -> None:
        self.name = name
        self.mediator= mediator

    @abstractmethod
    def broadcast(self, msg: str) -> None: pass

    @abstractmethod
    def direct_msg(self, msg: str, receiver: str) -> None: pass

    def __repr__(self):
        return self.name


class LoggedInUser(User):
    def __init__(self, name: str, mediator: ABCMediator) -> None:
        super().__init__(name, mediator)

    def broadcast(self, msg: str) -> None:
        print(f"Sending message '{msg}' to mediator...")
        self.mediator.broadcast(self, msg)

    def direct_msg(self,msg: str, receiver: str) -> None:
        print(f"Sending message '{msg}' to mediator...")
        self.mediator.direct_msg(self, receiver, msg)


class ABCMediator(ABC):
    def __init__(self):
        self.logged_in_users_list: list[User] = []

    @abstractmethod
    def add_user_to_list(self, user: User) -> None: pass

    @abstractmethod
    def broadcast(self, sender: User, msg: str) -> None: pass

    @abstractmethod
    def direct_msg(self, sender: User, receiver: str, msg: str) -> None: pass


class Mediator(ABCMediator):
    def __init__(self):
        super().__init__()

    def add_user_to_list(self, *user: User) -> None:
        self.logged_in_users_list.extend(user)

    def broadcast(self, sender: User, msg: str) -> None:
        if sender not in self.logged_in_users_list:
            return
        for user in self.logged_in_users_list:
            if user != sender:
                print(f"User '{user}' has received message '{msg}' from '{sender}'")

    def direct_msg(self, sender: User, receiver: str, msg: str) -> None:
        if sender not in self.logged_in_users_list:
            return
        list_ = self.logged_in_users_list[:]
        for i in range(0, len(list_)):
            list_[i] = str(list_[i])
        if receiver not in list_:
            print(f"Could not send message because there is no such user named '{receiver}'")
            return
        print(f"User {receiver} has received message '{msg}' from '{sender}'")



mediator = Mediator()
user1 = LoggedInUser('Mateus', mediator)
user2 = LoggedInUser('Gabriele', mediator)
user3 = LoggedInUser('Marcia', mediator)
user4 = LoggedInUser('Jaquinha', mediator)
user5 = LoggedInUser('Bruno', mediator)
user6 = LoggedInUser('Rodrigo', mediator)
user7 = LoggedInUser('Adilson', mediator)
mediator.add_user_to_list(user1, user2, user3, user4, user5, user6)

user7.broadcast('My message')
user7.direct_msg('Hello receiver', 'Mateus')
user1.broadcast('Hello World!')
print()
user1.direct_msg('Have you received my first message?', 'Marcia')