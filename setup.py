from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='PyP100_Test',
    version='0.0.10',
    description='A module for controlling the TP-Link Tapo P100 Plugs, P105 Plugs and L1510 Bulbs.',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Toby Johnson',
    author_email='toby.e.m.Johnson@gmail.com',
    keywords=['Tapo', 'Tp-Link', 'P100'],
    url='https://github.com/fishbigger/TapoP100',
    download_url='https://pypi.org/project/PyP100/'
)

install_requires = [
    'pycryptodome==3.10.1',
    'pkcs7==0.1.2',
    'requests==2.24.0',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
