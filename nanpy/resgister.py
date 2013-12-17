from nanpy.arduinoboard import arduinoclassmethod, returns
from nanpy.memo import memoized


class _Registers(object):

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def count(cls):
        pass

    @classmethod
    @returns(int)
    @arduinoclassmethod
    def read(cls, index):
        pass

    @classmethod
    @arduinoclassmethod
    def write(cls, index, value):
        pass

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def address(cls, index):
        pass

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def size(cls, index):
        pass

    @classmethod
    @memoized
    @arduinoclassmethod
    def name(cls, index):
        pass

    @classmethod
    @memoized
    def name_index_dict(cls):
        d = dict()
        for i in range(cls.count()):
            d[cls.name(i)] = i
        return d


class Register(object):

    @classmethod
    @memoized
    def names(cls):
        return sorted(_Registers.name_index_dict().keys())

    def __init__(self, name):
        try:
            self.index = _Registers.name_index_dict()[name]
        except KeyError:
            raise ValueError('Unknown register: %s' % name)

    def read_value(self):
        return _Registers.read(self.index)

    def write_value(self, value):
        return _Registers.write(self.index, value)

    value = property(read_value, write_value)

    @property
    def name(self):
        return _Registers.name(self.index)

    @property
    def address(self):
        return _Registers.address(self.index)

    @property
    def size(self):
        return _Registers.size(self.index)
