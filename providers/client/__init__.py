# coding=utf-8

from .. import BaseProvider
from faker.generator import random
import itertools


class Provider(BaseProvider):
    """
    This provider is a collection of functions to generate personal profiles and identities.

    """

    def simple_client(self, sex=None):
        """
        Generates a basic profile with personal informations
        """
        SEX = ["F", "M"]
        if sex not in SEX:
            sex = self.random_element(SEX)
        if sex == 'F':
            name = self.generator.name_female()
        elif sex == 'M':
            name = self.generator.name_male()
        return {
            "username": self.generator.user_name(),
            "name": name,
            "sex": sex,
            "address": self.generator.address(),
            "mail": self.generator.free_email(),

            #"password":self.generator.password()
            "birthdate": self.generator.date(),

        }

    def client(self, fields=None, sex=None):
        """
        Generates a complete profile.
        If "fields" is not empty, only the fields in the list will be returned
        """
        if fields is None:
            fields = []

        d = {
            "custId": self.cust_id(),
            "job": self.generator.job(),
            "company": self.generator.company(),
            "residence": self.generator.address(),
            # "current_location": (self.generator.latitude(), self.generator.longitude()),
            "phone_number": self.generator.phone_number(),
            # "card_number": self.generator.bank_card_info()
        }

        d = dict(d, **self.generator.simple_profile(sex))
        # d = dict(d, **self.generator.bank_card_info())
        d['bank_name'] = self.generator.debit_card_provider()
        d['card_number'] = self.generator.debit_card_number(d['bank_name'])
        id_number = self.generator.id_number(d['sex'])
        d['id_number'] = id_number
        #field selection
        if len(fields) > 0:
            d = dict((k, v) for (k, v) in d.items() if k in fields)

        return d

    def cust_id(self):
        id = int(random.uniform(1000000, 9999999))
        return str(id)