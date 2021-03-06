# -*- coding: utf-8 -*-

from random import choice
from faker.providers import BaseProvider
from operating_system_dict import os_names
from random import randint


class OperatingSystemProvider(BaseProvider):
    """
    A Provider for operating system related test data

    """
    def os_name(self):
        """
        :return:
        {'Make': 'Acorn Computers', 'Operating_system': 'ARX'},
        """
        operating_system = choice(os_names)
        return operating_system.get('os_name')

    def version(self):
        return f'{randint(0, 10)}.{randint(0, 10)}.{randint(0, 10)}'

