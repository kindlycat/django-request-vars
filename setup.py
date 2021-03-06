import setuptools

from request_vars import __version__


def readme():
    with open('README.rst') as f:
        return f.read()


setuptools.setup(
    name='django-request-vars',
    version=__version__,
    description='Stores current request, user and your defined data in thread '
    'local variable.',
    long_description=readme(),
    keywords=[
        'django',
        'thread',
        'variable',
        'request',
        'user',
        'cache',
        'middleware',
    ],
    author='Grigory Mishchenko',
    author_email='grishkokot@gmail.com',
    url='https://github.com/kindlycat/django-request-vars/',
    packages=setuptools.find_packages(exclude=('tests*',)),
    include_package_data=True,
    install_requires=['Django>=1.11'],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'License :: OSI Approved :: BSD License',
    ],
)
