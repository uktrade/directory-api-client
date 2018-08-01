"""
Export Directory API client
"""
import ast
import re
from setuptools import setup, find_packages


def get_version():
    pattern = re.compile(r'__version__\s+=\s+(.*)')

    with open('directory_api_client/version.py', 'rb') as src:
        return str(ast.literal_eval(
            pattern.search(src.read().decode('utf-8')).group(1)
        ))


setup(
    name='directory_api_client',
    version=get_version(),
    url='https://github.com/uktrade/directory-api-client',
    license='MIT',
    author='Department for International Trade',
    description='Python client for Directory API.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=[
        'django>=1.9,<2.0a1',
        'requests>=2.18.4,<3.0.0',
        'directory_client_core<5.0.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
