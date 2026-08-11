from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Licence :: OSI Approved :: MIT Licence',
    'Programming Language :: Python :: 3'
]


setup(
    name="CelMut",
    version="1.0",
    description="This is a library for operating on cells",
    long_description=open("README.txt").read() + "\n\n" + open("CHANGELOG.txt").read(),
    url="",
    author="Neonge",
    author_email="neonge1674@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords="gnk",
    packages=find_packages(),
    requires=['']
)