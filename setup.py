from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vega',
    version='0.1.0',
    author='jinland',
    author_email='jinland67@gmail.com',
    description='A collection of libraries needed to use python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jinland67/vega-lib.git',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.10',
    install_requires=[
        'PyMySQL >= 1.0.2',
        'sshtunnel >= 0.4.0',
        'pytz >= 2021.3',
        'python-dateutil >= 2.8.2',
        'psutil >= 5.8.0',
        'slack-sdk >= 3.11.2',
        'beautifulsoup4 >= 4.10.0',
        'selenium >= 4.0.0'
    ],
    package_data={"vega-lib": ["*.txt"]},
    include_package_data=True,
)