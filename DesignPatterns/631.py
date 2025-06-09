#esse padrao de projeto bridge faz com q um objeto de uma classe seja alterado seu estado pelo objeto de outra classe

from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None: pass

    @abstractmethod
    def decrease_volume(self) -> None: pass

    @abstractmethod
    def power(self) -> None: pass


class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice):
        self._device = device

    def increase_volume(self) -> None:
        self._device.volume += 10

    def decrease_volume(self) -> None:
        self._device.volume -= 10


    def power(self) -> None:
        self._device.power = not self._device.power


class IDevice(ABC):
    _volume: int
    _power: bool

    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter
    def volume(self, volume: int) -> None: pass

    @property
    @abstractmethod
    def power(self) -> bool: pass

    @power.setter
    def power(self, power: bool) -> None: pass



class TV(IDevice):
    def __init__(self, power: bool = False, volume: int = 10):
        self._power = power
        self._volume = volume

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self._power:
            print('Cannot change volume because the TV is off. Please turn the TV on.')
            return
        self._volume = volume
        if self._volume < 0:
            self._volume = 0
            print('Cannot set volume below 0. Volume has been set to 0.')
            return
        if self._volume > 100:
            self._volume = 100
            print('Cannot set volume above 100. Volume has been set to 100.')
            return
        print(f'Volume is now set to {self._volume}.')

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power




tv = TV()
remote_control = RemoteControl(tv)
remote_control.increase_volume()
remote_control.power()
remote_control.decrease_volume()
remote_control.decrease_volume()
for i in range(11):
    remote_control.increase_volume()
remote_control.power()
remote_control.decrease_volume()
remote_control.power()
remote_control.decrease_volume()