from setuptools import find_packages, setup

setup(
    name='python-json-serialization-examples',
    version='0.0.1',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'marshmallow',
        'pytest'
    ],
    tests_require=['pytest'],
    classifiers=[
        'Private :: Do Not Upload'
    ]
)
