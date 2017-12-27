from setuptools import setup , find_packages

setup(
    name='webapp-skeleton',
    version='0.1',
    description='WebApp in Flask',
    url='http://github.com/NitigyaS',
    author='NitigySharma',
    author_email='nitigyasharma@hotmail.com',
    license='MIT',
    packages=find_packages(),
    scripts=['run.py'],
    install_requires=[
        'argparse',
        'flask',
        'flask_sqlalchemy',
        'flask_migrate'
    ],
    test_suite='nose.collector',
    tests_require=['nose']
)
