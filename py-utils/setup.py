from setuptools import setup
import pathlib

import pkg_resources
import setuptools

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]
setup(
    name='py_utils',
    version='0.0.1',
    python_requires=">3.6.0",
    packages=['py_utils',"py_utils/mapreduce","py_utils/math","py_utils/file","py_utils/excel"],
    url='',
    license='',
    author='i',
    author_email='',
    description='',
    install_requires=install_requires
)
