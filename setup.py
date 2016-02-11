from setuptools import setup, find_packages

setup(name='datashell',
    description='Because namespaces are a honking great idea, but loading a gazillion packages to take a quick peek at some data is not.',
    long_description=open('README.rst').read(),
    author='Stijn Debrouwere',
    author_email='stijn@debrouwere.org',
    url='https://github.com/debrouwere/datashell/',
    download_url='http://www.github.com/debrouwere/datashell/tarball/master',
    version='0.4.4',
    license='ISC',
    packages=find_packages(),
    keywords='data analytics statistics',
    scripts=[
        'bin/datashell',
        'bin/datashell-qt',
        'bin/datashell-jupyter',
        'bin/datashell-install',
    ],
    include_package_data=True,
    install_requires=[
        'ipython',
        'numpy',
        'sympy',
        'scipy',
        'pandas',
        'statsmodels',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        ],
    )
