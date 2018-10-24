from setuptools import setup, find_packages

deps = [
        'python-hglib'
        ]

setup(name='trybisect',
      version='0.1',
      description ="""Regression finder using Mozilla try server""",
      author="Bebe",
      author_email="bebe@mozilla.ro",
      url='http://github.com/',
      license='MPL 1.1/GPL 2.0/LGPL 2.1',
      packages=find_packages(exclude=['legacy']),
      entry_points={  # Optional
          'console_scripts': [
              'try_bisect=trybisect.run:main',
          ],
      },
      install_requires = deps,
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent'
                  ]
      )
