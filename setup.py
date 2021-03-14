import io

from setuptools import setup
from setuptools import find_packages

from leasebot import __version__

with io.open('README.md', 'rt', encoding='utf8') as file:
    readme = file.read()

setup(name='leasebot',
      version=__version__,
      description='Artificial intelligence bot ',
      long_description=readme,
      author='test',
      author_email='test',
      url='test',
      license='MIT',
      install_requires=['Click==7.0',
                        'SoundCard==0.2.2',
                        'SoundFile==0.10.2',
                        'keras==2.2.4',
                        'librosa==0.6.3',
                        'numpy==1.14.5',
                        'pyee==5.0.0',
                        'python-osc==1.7.0',
                        'scikit-learn==0.20.3',
                        'scipy==1.2.1',
                        'tensorflow==1.9.0'],
      packages=find_packages(),
      entry_points={
            'console_scripts': {
                'leasebot = leasebot.cli:cli',
            }
      })
