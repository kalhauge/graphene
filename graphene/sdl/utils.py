from enum import Enum


class Flags(Enum):

    @classmethod
    def from_names(cls, names):
        return {cls[name] for name in names}

    @classmethod
    def encode(cls, flags):
        flag = 0
        for f in flags:
            flag |= f.value
        return flag

    @classmethod
    def decode(cls, flag):
        flags = set()
        for f in cls:
            if flag & f.value != 0:
                flags.add(f)
        return flags

    @classmethod
    def process(cls, names):
        return cls.encode(cls.from_names(names))
