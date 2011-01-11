import os
from distutils.core import setup
from distutils.sysconfig import get_python_lib
import media_nommer

long_description = open('README.rst').read()


TWISTED_PLUGIN_PATH = os.path.join(get_python_lib(), 'twisted', 'plugins')
NOMMER_PLUGIN_PATH = os.path.join('media_nommer', 'twisted', 'plugins')
data_files = [
    (
        TWISTED_PLUGIN_PATH,
        [os.path.join(NOMMER_PLUGIN_PATH, 'feederd.py')]
    ),
    (
        TWISTED_PLUGIN_PATH,
        [os.path.join(NOMMER_PLUGIN_PATH, 'ec2nommerd.py')]
    ),
    #(
    #    TWISTED_PLUGIN_PATH,
    #    [os.path.join(NOMMER_PLUGIN_PATH, 'scavengerd.py')]
    #),
]

setup(
    name='media-nommer',
    version=media_nommer.VERSION,
    description='A Python-based media encoding system, using Amazon AWS as its backbone.',
    long_description=long_description,
    author='DUO Interactive, LLC',
    author_email='gtaylor@duointeractive.com',
    license='BSD License',
    url='http://duointeractive.github.com/media-nommer/',
    platforms=["any"],
    requires=['boto', 'twisted', 'txrestapi'],
    provides=['media_nommer'],
    packages=[
        'media_nommer',
        'media_nommer.client', 'media_nommer.conf',
        'media_nommer.core', 'media_nommer.core.job_state_backends',
        'media_nommer.core.nommers', 'media_nommer.core.nommers.ec2_ffmpeg',
        'media_nommer.core.storage_backends',
        'media_nommer.ec2nommerd', 'media_nommer.ec2nommerd.web',
        'media_nommer.feederd', 'media_nommer.feederd.web',
        'media_nommer.scavengerd', 'media_nommer.scavengerd.web',
        'media_nommer.utils'
    ],
    data_files=data_files,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Topic :: Multimedia :: Video :: Conversion',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
