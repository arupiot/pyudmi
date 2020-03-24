from setuptools import setup, find_packages

setup(
    name='pyudmi',
    version='0.0.1',
    url='https://github.com/arupiot/pyudmi.git',
    author='Paul Harter',
    author_email='paul@glowinthedark.co.uk',
    license="LICENSE",
    description='Helper classes for working with udmi',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['pytz', 'fastjsonschema', 'requests'],
)