from setuptools import setup, find_packages

setup(
    name='Venkman',
    version='0.5',
    author='Darryl lane',
    author_email='DarrylLane101@gmail.com',
    url='https://github.com/darryllane/venkman',
    packages=['Venkman'],
    include_package_data=True,
    license='LICENSE.txt',
    scripts=['Venkman/venkman'],
    long_description='Service account and Logged in user enumeration. used for hunting priv accounts',
    install_requires=[
    ],
)

