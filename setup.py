from setuptools import setup, find_packages

version = '1.1.3'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='ip6words',
      version=version,
      author="Lucas Estienne",
      author_email="lucas@estienne.sh",
      url="https://github.com/lstn/ip6words",
      description="Converts IPv6 addresses to and from a user friendly format using words.",
      packages=find_packages(),
      package_data={ 
          'ip6w': ['LICENSE', 'README.md', 'requirements.txt'],
          'ip6w.src': ['ip6w/src/words.dill']
      },
      include_package_data=True,
      install_requires=requirements,
      entry_points={
          'console_scripts': [
              'ip6words = ip6w.src.__main__:main'
          ]
      },
)