from setuptools import setup


def desc():
    with open("README.md") as f:
        return f.read()


setup(
    name='frasco-geoip',
    version='0.1',
    url='http://github.com/frascoweb/frasco-geoip',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="pygeoip integration for Frasco",
    long_description=desc(),
    py_modules=["frasco_geoip"],
    platforms='any',
    install_requires=[
        'frasco',
        'pygeoip==0.3.1'
    ]
)