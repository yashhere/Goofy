"""
A tool to automatically generate .gitignore file for your project
"""
from setuptools import find_packages, setup

dependencies = ['click']

setup(

)
setup(
    name='pooh',
    version='0.1.0',
    url='https://github.com/yash2696/Pooh',
    license='MIT',
    author='Yash Agarwal',
    author_email='yashagarwaljpr@gmail.com',
    description='A tool to automatically generate .gitignore file for your project',
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'pooh = pooh.cli:main',
        ],
    },
    py_modules=['pooh'],
)
