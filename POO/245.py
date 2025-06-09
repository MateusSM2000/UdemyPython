#__call__ habilita dar call na propria instancia, executando os codigos escrito no dunder call

class PhoneCall:
    def __init__(self, number):
        self.phone_number = number

    def __call__(self, person_name):
        print(f'{person_name} is calling {self.phone_number}...')


s23 = PhoneCall('34411490')
s23('Mateus')