try:
    from setuptools import setup
except ImprtError:
    from distutils.core import setup

config = {
    'description' = 'House walkthrough',
    'author' = 'abhi',
    'url' = 'URL to get it at',
    'download_url' = 'Were to download it',
    'author_email' = 'abhi@mailbox.org',
    'version' = '0.1',
    'install_requires' = ['nose'],
    'packages' = ['walk'],
    'scripts' = [],
    'name' = 'walk'
}

setup(**config)
