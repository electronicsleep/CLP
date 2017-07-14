from setuptools import setup

setup(
    name="clp",
    version='0.1',
    py_modules=['clp'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        clp=clp:main
    ''',
)
