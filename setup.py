from setuptools import setup

setup(
    name='overfitted-io-client',
    version='0.1.0',    
    description='A client for the API hosted at overfitted.io',
    url='https://github.com/overfitted-io/python-api-client',
    author='Dan Sporici',
    author_email='dan@overfitted.io',
    license='BSD 2-clause',
    packages=['overfitted_io_client'],
    install_requires=['requests'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)