from pip.req import parse_requirements
from setuptools import setup

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt",session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='py_utils',
    version='0.0.1',
    python_requires=">3.6.0",
    packages=['py_utils',"py_utils/mapreduce","py_utils/deployer","py_utils/math","py_utils/file","py_utils/excel"],
    url='',
    license='',
    author='i',
    author_email='',
    description='',
    install_requires=reqs
)
