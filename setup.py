from setuptools import setup, find_packages

setup(
    name='Venkman',
<<<<<<< HEAD
    version='1.6.6',
=======
    version='1.6.5',
>>>>>>> 13bf0a5fb52f6aa6a0b604618f4b4961cfe2317a
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

