try:
    from setuptools import setup
except ImprtError:
    from distutils.core import setup

config = {
    'description' = 'Exercise 47',
    'author' = 'abhi',
    'author_email' = 'abhi@mailbox.org',
    'version' = '0.1',
    'install_requires' = ['nose'],
    'packages' = ['ex47'],
    'scripts' = [],
    'name' = 'exercise47'
}

setup(**config)
