#!/usr/bin/env python
# pylint: disable=C0103


import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    test_runner.verbosity = 2
    failures = test_runner.run_tests(['tests'])
    sys.exit(bool(failures))
