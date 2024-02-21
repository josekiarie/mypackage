from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example pthon package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/josekiarie/mypackage',
    author='Jose Kiarie',
    author_email='idealelectronicsken@gmail.com'
)