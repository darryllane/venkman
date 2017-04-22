from setuptools import setup, find_packages

setup(
    name='Venkman',
    version='1.6.6',
    author='Darryl lane',
    author_email='DarrylLane101@gmail.com',
    url='https://github.com/darryllane/venkman',
    packages=['Venkman'],
    include_package_data=True,
    license='LICENSE.txt',
    description='''
    Service account and logged in user enumeration. Used to hunt for priv accounts''',
    scripts=['Venkman/venkman'],
    install_requires=[
    ],
)

