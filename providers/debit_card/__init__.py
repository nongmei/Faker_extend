# coding=utf-8
from __future__ import unicode_literals
from collections import OrderedDict

from faker.providers.date_time import Provider as DateTimeProvider
from .. import BaseProvider
import redis

localized = True

class DebitCard(object):

    def __init__(self, name, prefixes, length=19):
        self.name = name
        self.prefixes = prefixes
        self.length = length


class Provider(BaseProvider):

    # 大陆信用卡
    prefix_cmbc = ["472067", "427570", "421393", "621692", "623683", "622620", "622622", "900003", "622615", "622619"]
    prefix_cmb = ["410062", "690755", "512425", "622580", "622598", "95555", "468203", "623262", "402658", "623126"]
    prefix_cib = ["438589", "90592", "622909"]
    prefix_ceb = ["620518", "622664", "622668", "622667", "623157", "622670", "623155", "621490", "621492", "620535"]
    prefix_citic = ["622698", "620082", "621770", "622696", "622690", "968809", "433670", "622691", "622999", "621768"]
    prefix_hxb = ["623022", "622633", "621222", "999999", "623021", "622630"]
    prefix_spdb = ["84373", "84390", "87040", "621791", "622518", "621792", "623250", "984303", "87000", "87010"]
    prefix_gdb = ["623259", "623506", "6858009", "9111"]
    prefix_pingan = ["622535", "412962", "412963", "415752", "998800", "622538", "622536", "415753"]
    prefix_egb = ["622384"]
    prefix_czb = ["621019", "622309"]
    prefix_cbhb = ["622884", "621453", "621268"]

    debit_card_types = OrderedDict((
        (u'民生银行',   DebitCard(u'民生银行',     prefix_cmbc, 16)),
        (u'招商银行',    DebitCard(u'招商银行',    prefix_cmb, 16)),
        (u'兴业银行',    DebitCard(u'兴业银行', prefix_cib, 18)),
        (u'光大银行',    DebitCard(u'光大银行',   prefix_ceb, 16)),
        (u'中信银行',    DebitCard(u'中信银行',    prefix_citic, 16)),
        (u'华夏银行',    DebitCard(u'华夏银行',  prefix_hxb, 16)),
        (u'浦发银行',    DebitCard(u'浦发银行', prefix_spdb, 16)),
        (u'广发银行',    DebitCard(u'广发银行', prefix_gdb, 16)),
        (u'平安银行',    DebitCard(u'平安银行',   prefix_pingan, 16)),
        (u'恒丰银行',    DebitCard(u'恒丰银行',   prefix_egb, 16)),
        (u'浙商银行',    DebitCard('浙商银行',   prefix_czb, 19)),
        (u'渤海银行',    DebitCard(u'渤海银行',   prefix_cbhb, 16))
    ))

    # prefix_dic = {"华夏银行": 621222, "招商银行": 690755, "光大银行": 622662, "民生银行": 622615, "中信银行": 433670,
    #           "兴业银行": 622909, "浦发银行": 622516, "广发银行": 623259, "平安银行": 412963, "恒丰银行": 622384,
    #           "浙商银行": 621019, "渤海银行": 621268}

    luhn_lookup = {'0': 0, '1': 2, '2': 4, '3': 6, '4': 8,
                   '5': 1, '6': 3, '7': 5, '8': 7, '9': 9}

    # @classmethod
    # def all_debit_cards(cls):
    #     ret = {}
    #     for key in cls.prefix_dic.keys():
    #         number = cls._bank_card_number(str(cls.prefix_dic[key]))
    #         ret[key] = number
    #         print key+':'+number
    #     return ret

    @classmethod
    def debit_card_provider(cls, card_type=None):
        """ Returns the provider's name of the debit card. """
        if card_type is None:
            card_type = cls.random_element(cls.debit_card_types.keys())
        return cls._debit_card_type(card_type).name

    @classmethod
    def debit_card_number(cls, card_type=None):
        """ Returns a valid debit card number. """
        card = cls._debit_card_type(card_type)
        prefix = cls.random_element(card.prefixes)
        number = cls._generate_number(prefix, card.length)
        return number

    # @classmethod
    # def bank_card_info(cls):
    #     """ Returns a dict that contains bank card info.        """
    #     prefix = cls.random_element(cls.card_prefix)
    #     bank_card_number = cls._bank_card_number()
    #     r = redis.StrictRedis(host='10.12.9.14', port=6379, db=0)
    #     info = r.get(prefix+"CORE_CARD_BIN")
    #     if info is not None:
    #         names = ['bank_name', 'bank_code', 'card_name', 'card_bin', 'card_type']
    #         values = info.decode('utf-8').split('|')
    #         card_info = dict(zip(names, values))
    #         card_info['card_number'] = bank_card_number
    #     else:
    #         print "Redis中没有找到该卡的属性:%s" % prefix
    #         raise Exception
    #     return  card_info

    @classmethod
    def debit_card_expire(cls, start='now', end='+10y', date_format='%m/%y'):
        expire_date = DateTimeProvider.date_time_between(start, end)
        return expire_date.strftime(date_format)

    def debit_card_full(self, card_type=None):
        card = self._debit_card_type(card_type)

        tpl = ('{provider}\n'
               '{owner}\n'
               '{number} {expire_date}\n')

        tpl = tpl.format(provider = card.name,
                         owner = self.generator.parse("{{first_name}} {{last_name}}"),
                         number = self.debit_card_number(card),
                         expire_date = self.debit_card_expire(),
                         )

        return self.generator.parse(tpl)

    @classmethod
    def debit_card_security_code(cls, card_type=None):
        """ Returns a security code string. """
        sec_len = cls._debit_card_type(card_type).security_code_length
        return cls.numerify('#' * sec_len)

    @classmethod
    def _debit_card_type(cls, card_type=None):
        """ Returns a random debit card type instance. """
        if card_type is None:
            card_type = cls.random_element(cls.debit_card_types.keys())
        elif isinstance(card_type, DebitCard):
            return card_type
        return cls.debit_card_types[card_type]

    @classmethod
    def _generate_number(cls, prefix, length):
        """
        'prefix' is the start of the CC number as a string, any number of digits.
        'length' is the length of the CC number to generate. Typically 13 or 16
        """
        number = prefix
        # Generate random char digits
        number += '#' * (length - len(prefix) - 1)
        number = cls.numerify(number)
        reverse = number[::-1]
        # Calculate sum
        tot = 0
        pos = 0
        while pos < length - 1:
            tot += Provider.luhn_lookup[reverse[pos]]
            if pos != (length - 2):
                tot += int(reverse[pos + 1])
            pos += 2
        # Calculate check digit
        check_digit = (10 - (tot % 10)) % 10
        number += str(check_digit)
        return number
