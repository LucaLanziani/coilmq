"""
Simple, lightweight, and easily extensible STOMP message broker.
"""
import os.path
import warnings
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

version = '0.6'

news = os.path.join(os.path.dirname(__file__), 'docs', 'news.txt')
news = open(news).read()
parts = re.split(r'([0-9\.]+)\s*\n\r?-+\n\r?', news)
found_news = ''
for i in range(len(parts)-1):
    if parts[i] == version:
        found_news = parts[i+i]
        break
if not found_news:
    warnings.warn('No news for this version found.')
    
long_description = """
The provided server implementation for CoilMQ uses the Python SocketServer 
libraries; however, CoilMQ is only loosely coupled to this server 
implementation.  It could be used with other socket implementations.

The CoilMQ core classes and bundled storage implementations are built to be
thread-safe.
"""

if found_news:
    title = 'Changes in %s' % version
    long_description += "\n%s\n%s\n" % (title, '-'*len(title))
    long_description += found_news

setup(
    name='CoilMQ',
    version=version,
    description=__doc__,
    long_description=long_description,
    keywords='stomp server broker',
    license='Apache',
    author='Hans Lellelid',
    author_email='hans@xmpl.org',
    url='http://code.google.com/p/coilmq',
    packages=find_packages(exclude=['ez_setup', 'distribute_setup', 'tests', 'tests.*']),
    package_data={'coilmq': ['config/*.cfg*', 'tests/resources/*']},
    zip_safe=False, # We use resource_filename for logging configuration and some unit tests.
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose', 'coverage'],
    install_requires=[
          'distribute',
          'stompclient>=0.2,<0.4',
    ],
    extras_require={
        'daemon': ['python-daemon'],
        'sqlalchemy': ['SQLAlchemy']
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points="""
    [console_scripts]
    coilmq = coilmq.start:main
    """,
)
