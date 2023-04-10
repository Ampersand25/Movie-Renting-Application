class Data:
    def __init__(self, zi, luna, an):
        self.__zi = zi
        self.__luna = luna
        self.__an = an

    def get_zi(self):
        return self.__zi

    def set_zi(self, zi_noua):
        self.__zi = zi_noua

    def get_luna(self):
        return self.__luna

    def set_luna(self, luna_noua):
        self.__luna = luna_noua

    def get_an(self):
        return self.__an

    def set_an(self, an_nou):
        self.__an = an_nou

    def __str__(self):
        if self.__luna < 10:
            strr = '0'
        else:
            strr = ''

        return str(self.__zi) + '.' + strr + str(self.__luna) + '.' + str(self.__an) + '\n'

    def __eq__(self, other):
        return self.__zi == other.__zi and self.__luna == other.__luna and self.__an == other.__an