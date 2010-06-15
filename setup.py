from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='eea.rdfmarshaller',
      version=version,
      description="RDF marshaller for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'uuid',
          'surf',
          'surf.rdflib',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
