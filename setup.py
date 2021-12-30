from setuptools import setup

setup(
    name='fsa',
    version='0.1.0',
    description='Python package designed to work with Finite-state machine',
    author='Mikhail Eremeev',
    author_email='meremeev@sfedu.ru',
    url='https://github.com/tediore-wf/fsa',
    packages=['fsa'],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': ['fsa=fsa.cli.main:main'],
    },
    install_requires=['PyYAML == 6.0'],
    platforms=['any'],
)
