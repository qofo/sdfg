import abc


class Base_UNIT(abc.ABC):
    @abc.abstractmethod
    def __init__(self):

        pass

    @abc.abstractmethod
    def damage(self):

        pass

    @abc.abstractmethod
    def health(self):

        pass

    @abc.abstractmethod
    def speed(self):

        pass

    @abc.abstractmethod
    def name(self):

        pass

    @abc.abstractmethod
    def image(self):

        pass
