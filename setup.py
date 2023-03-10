from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='sanjumailgenerator3',
    version='0.0.3',
    description='A script to send automated mails.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Sanooj Babu',
    author_email='sanooj.kakkoth@onebillsoftware.com',
    license='MIT',
    classifiers=classifiers,
    keywords='mail',
    packages=find_packages(),
    install_requires=['']
)
