from setuptools import setup, find_packages

setup(
    name='pyudmi',
    version='0.0.3',
    url='https://github.com/arupiot/pyudmi.git',
    author='Paul Harter',
    author_email='paul@glowinthedark.co.uk',
    license="LICENSE",
    description='Helper classes for working with udmi',
    packages=find_packages('src'),
    package_data={'udmi': ['schemata/daq/schemas/udmi/*.json']},
    package_dir={'udmi': 'src/udmi'},
    install_requires=['pytz', 'fastjsonschema']
)