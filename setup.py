from setuptools import setup, find_packages

setup(
    name='info_gempa_cli',
    version='0.1',
    author='Faishal Risfandi',
    description='Informasi gempa',
    author_email='risfandi@dlutrix.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'request',
        'tabulate',
        'wheel'
    ],
    entry_points='''
        [console_scripts]
        igempa=main:main
    ''',
)

