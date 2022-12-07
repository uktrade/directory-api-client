from setuptools import find_packages, setup

setup(
    name='directory_api_client',
    version='26.1.1',
    url='https://github.com/uktrade/directory-api-client',
    license='MIT',
    author='Department for International Trade',
    description='Python client for Directory API.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'django>=2.2.10,<4.0.0',
        'requests>=2.22.0,<3.0.0',
        'directory_client_core>=6.1.0,<8.0.0',
    ],
    extras_require={
        'test': [
            'codecov==2.1.7',
            'pytest-cov==2.8.1',
            'pytest==5.3.5',
            'requests_mock==1.7.0',
            'setuptools>=45.2.0,<50.0.0',
            'twine>=3.1.1,<4.0.0',
            'wheel>=0.34.2,<1.0.0',
            'black==22.10.0',
            'blacken-docs==1.6.0',
            'isort==5.6.4',
            'flake8==5.0.4',
            'pre-commit-hooks==3.3.0',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
