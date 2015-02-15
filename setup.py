import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'django',
    'pyramid',
    'waitress',
    ]

setup(name='pyramid_django',
      version='0.0',
      description='pyramid_django',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid django',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='pyramid_django',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = pyramid_django:main
      [console_scripts]
      pyramid_django_manage = pyramid_django.scripts.pyramid_django_manage:main
      [pyramid.scaffold]
      pyramid_django = pyramid_django.scaffolds:PyramidDjangoTemplate
      """,
      )
