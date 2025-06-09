from abc import ABC, abstractmethod

class Commands(ABC):
    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class Lights:
    def __init__(self, name:str, room_name:str):
        self.name = name
        self.room_name = room_name

    def turn_on(self) -> None:
        print(f'{self.name} in {self.room_name} has been turned on!')

    def turn_off(self) -> None:
        print(f'{self.name} in {self.room_name} has been turned off!')


class LightsOnOffCommand(Commands):
    def __init__(self, lights:Lights):
        self.lights = lights

    def execute(self) -> None:
        self.lights.turn_on()

    def undo(self) -> None:
        self.lights.turn_off()


class SmartApp:
    def __init__(self):
        self.hotkeys : dict[str, Commands] = {}

    def add_button_command(self, name:str, command:Commands) -> None:
        self.hotkeys[name] = command

    def execute_button(self, name:str) -> None:
        if name in self.hotkeys:
            self.hotkeys[name].execute()

    def undo_button(self, name:str) -> None:
        if name in self.hotkeys:
            self.hotkeys[name].undo()



smart_app = SmartApp()
smart_app.add_button_command('First Button', LightsOnOffCommand(Lights('Light1', 'Living Room')))
smart_app.execute_button('First Button')
smart_app.undo_button('First Button')