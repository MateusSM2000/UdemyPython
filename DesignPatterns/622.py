#desse jeito uma classe consegue alterar um atributo de outra classe

from abc import ABC, abstractmethod

class Order:
    def __init__(self):
        self.state: OrderState = PaymentPending(self)
        print(self)

    def pending(self):
        self.state.pending()

    def approve(self):
        self.state.approve()

    def reject(self):
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order: Order):
        self.order = order

    @abstractmethod
    def pending(self): pass

    @abstractmethod
    def approve(self): pass

    @abstractmethod
    def reject(self): pass


class PaymentPending(OrderState):
    def __init__(self, order: Order):
        super().__init__(order)

    def pending(self):
        print(f'Order is already on pending state...')

    def approve(self):
        self.order.state = PaymentApproved(self.order)
        print(f'Order has been approved! (order.state: {self.__class__.__name__} -> {self.order.state.__class__.__name__}')

    def reject(self):
        self.order.state = PaymentRejected(self.order)
        print(f'Order has been rejected! (order.state: {self.__class__.__name__} -> {self.order.state.__class__.__name__}')


class PaymentApproved(OrderState):
    def __init__(self, order: Order):
        super().__init__(order)

    def pending(self):
        self.order.state = PaymentPending(self.order)
        print(f'Order has been moved back to pending state! (order.state: {self.__class__.__name__} -> {self.order.state.__class__.__name__}')

    def approve(self):
        print(f'Order is already approved...')

    def reject(self):
        print(f'Order has been moved to rejected state! (order.state: {self.__class__.__name__} -> {self.order.state.__class__.__name__}')


class PaymentRejected(OrderState):
    def __init__(self, order: Order):
        super().__init__(order)

    def pending(self):
        print('Order has already been rejected...')

    def approve(self):
        print('Order has already been rejected...')

    def reject(self):
        print('Order has already been rejected...')



order = Order()
order.pending()
order.approve()
order.approve()
order.pending()
order.reject()
order.approve()