from setuptools import setup, find_packages
import os

version = '0.2.1'

setup(name='collective.wysiwyg_biografy',
      version=version,
      description="The Plone user's biografy using the WYSIWYG editor",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        ],
      keywords='plone biografy wysiwyg editor',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://plone.org/products/collective.wysiwyg_biografy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone>4.0b1',
          'plone.app.users',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
