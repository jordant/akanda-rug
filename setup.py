from setuptools import setup, find_packages


setup(
    name='Akanda Router Update Generator',
    version='0.1.2',
    description='A service that manages tenant Akanda router instances',
    author='DreamHost',
    author_email='dev-community@dreamhost.com',
    url='http://github.com/dreamhost/akanda-rug',
    license='BSD',
    install_requires=[
        'netaddr>=0.7.5',
        'requests>=0.8.2',
        'python-quantumclient>=2.1'
    ],
    namespace_packages=['akanda'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'akanda-rug-service=akanda.rug.service:main'
        ]
    },
)