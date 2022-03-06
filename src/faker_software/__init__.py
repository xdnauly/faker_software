# -*- coding: utf-8 -*-

from random import choice
from faker.providers import BaseProvider
from .operating_system_dict import operating_systems
from faker import Faker

class OperatingSystemProvider(BaseProvider):
    """
    A Provider for operating system related test data

    >>> from faker import Faker
    # >>> from faker_software import OperatingSystemProvider
    # >>> fake = Faker()
    # >>> fake.add_provider(OperatingSystemProvider)

    """

    def operating_system_object(self):
        """

        :return:
        {'Make': 'Acorn Computers', 'Operating_system': 'ARX'},
        """
        operating_system = choice(operating_systems)
        return operating_system


fake = Faker('zh-CN')

fake.add_provider()
