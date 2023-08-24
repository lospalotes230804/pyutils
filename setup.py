from setuptools import setup, find_packages

# Library setup file for PyPI (https://pypi.org/)
setup(
    name='pyutils',
    version='0.1.0',
    packages=find_packages(),
    description='Python utilities for common tasks',
    long_description='Python utilities for common tasks' +
        'like string manipulation, file handling, web scraping, etc.',
    author='Oscar Pérez',
    author_email='javalotodo@gmail.com',
    url='https://github.com/tuusuario/pyutils',
    license='MIT',
    python_requires='>=3.8',
    install_requires=[
        'python-dateutil',
    ],
    extras_require=[
        'six',
    ]
)
