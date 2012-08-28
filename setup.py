from setuptools import find_packages
from setuptools import setup
import os


long_description = (
    open(os.path.join("collective", "behavior", "price", "docs", "README.rst")).read() + "\n" +
    open(os.path.join("collective", "behavior", "price", "docs", "HISTORY.rst")).read() + "\n" +
    open(os.path.join("collective", "behavior", "price", "docs", "CONTRIBUTORS.rst")).read())


setup(
    name='collective.behavior.price',
    version='0.1',
    description="Behavior to make content pricing.",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@gmail.com',
    url='https://github.com/collective/collective.behavior.price/',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.behavior'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone>=4.2',
        'five.grok',
        'hexagonit.testing',
        'plone.behavior',
        'plone.directives.form',
        'py-moneyed',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
