import os

from setuptools import find_packages, setup

CURRENT_WORKING_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURRENT_WORKING_DIRECTORY, 'README.md')) as fp:
    README = fp.read()

setup(
    name='django-admin-autocomplete-list-filter',
    version='0.1.1',
    description='Ajax autocomplete list filter for Django admin',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/demiroren-teknoloji/django-admin-autocomplete-list-filter',
    author='Demirören Teknoloji Django Team',
    author_email='account@demirorenteknoloji.com',
    license='MIT',
    python_requires='>=3.0',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    include_package_data=True,
)
