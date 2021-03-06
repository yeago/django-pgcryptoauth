from setuptools import setup, find_packages
import os

import pgcryptoauth


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

setup(
    name='django-pgcryptoauth',
    version=pgcryptoauth.__version__,
    description='Django hasher for pgcrypto encoded passwords.',
    long_description=README,
    url='https://github.com/tomatohater/django-pgcryptoauth',
    author='Drew Engelson',
    author_email='drew@engelson.net',
    license='BSD',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data={},
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
