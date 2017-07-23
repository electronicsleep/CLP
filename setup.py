from setuptools import setup

setup(
    name='clp',
    version='0.1',
    description='Examples for using Python, Fabric and Click',
    author='Chris Robertson',
    url='https://github.com/electronicsleep/CLP',
    py_modules=['clp'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        clp=clp:main
    ''',
)
