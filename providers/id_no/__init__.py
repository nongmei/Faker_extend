# coding=utf-8

from .. import BaseProvider
import datetime
from faker.generator import random

class Provider(BaseProvider):
    address_str = ['110108', '120114', '130283', '130304', '130423', '211201', '230702', '330106', '440402', '450305']

    @classmethod
    def id_number(cls, sex=None):
        """ Returns an valid id number. """
        addr_code = cls.random_element(cls.address_str)
        birth_code = cls._get_random_birthday()
        SEX = ["F", "M"]
        if sex not in SEX:
            sex = cls.random_element(SEX)
        order_code = cls._get_order_code(sex)
        id_no = addr_code + birth_code + order_code
        check_code = cls._get_check_code(id_no)
        id_no += check_code
        return id_no

    @classmethod
    def _get_check_code(cls, number):
        multi_list =  [ 7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10 ,5 ,8 ,4 ,2]
        check_list = [ '1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        sum = 0
        i = 0
        for n in list(number):
            sum += int(n)*multi_list[i]
            i += 1
        return  check_list[sum%11]

    @classmethod
    def _get_order_code(cls, sex):
        code = int(random.uniform(1, 998))
        SEX_FIX = {'F':0, 'M':1}
        if code%2 != SEX_FIX[sex]:
            code += 1
        return str(code).zfill(3)

    @classmethod
    def _get_random_birthday(cls):
        now = datetime.datetime.now()
        days = random.uniform(-7300, -21900)
        delta = datetime.timedelta(days=days)
        n_days = now+delta
        return n_days.strftime('%Y%m%d')



