__author__ = 'PLNech'


class Named(object):
    @classmethod
    def class_name(cls):
        return cls.__name__
