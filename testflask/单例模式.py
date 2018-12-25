# coding=utf-8


class Single(object):
    isinstance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance:
            cls.isinstance = object.__new__(cls)
        return cls.isinstance


a = Single()
b = Single()
print(id(a))
print(id(b))
