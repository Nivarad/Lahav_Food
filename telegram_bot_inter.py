from abc import abstractmethod


class TelegramBotInterface:

    @abstractmethod
    def order_pizza(self, update, context):
        pass

    @abstractmethod
    def order_toast(self, update, context):
        pass

    @abstractmethod
    def order_falafel(self, update, context):
        pass
