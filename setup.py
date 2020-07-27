from os.path import abspath, dirname, join

from setuptools import setup

CWD = abspath(dirname(__file__))
PACKAGE_NAME='sancaqa'

with open(join(CWD, 'requirements.txt'), encoding="utf-8") as f:
    REQUIREMENTS = f.read().splitlines()

setup(name=PACKAGE_NAME,
      version='0.0.1',
      description='Simplify Automation Test API, App, Web. Built with pytest, singleton pattern, appium, request, selenium',
      url='https://github.com/penguji/sancaQA',
      author='Fachrul Choliluddin',
      author_email='tester.gadungan@gmail.com',
      license='MIT',
      packages=['sancaqa'],
      instal_reqires=REQUIREMENTS,
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'sancaqa = sancaqa.cli:main',
          ],
      })
