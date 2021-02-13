import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

settings = __import__('django_package_template')
setup(
    name=settings.__package_name__,
    version=settings.__version__,
    packages=find_packages(),
    include_package_data=True,
    license=settings.__license__,
    description=settings.__description__,
    long_description=README,
    long_description_content_type='text/markdown',
    url=settings.__github_url__,
    author=settings.__author__,
    author_email=settings.__author_email__,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
    ]
)
