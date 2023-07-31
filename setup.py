from setuptools import setup

import validator

setup(
    name="coar-notify-validator",
    version=validator.__version__,
    description="Utility for validating COAR Notify payloads.",
    packages=[
        "validator",
        "shape_files",
    ],
    include_package_data=True,
    package_data={
        "shape_files": ["shape_files/data/*.ttl"],
    },
    install_requires=[
        "kglab == 0.6.6",
        "rdflib == 6.3.2",
        "pyshacl == 0.23.0",
    ],
    license="MIT",
    url="https://github.com/seanwiseman/coar-notify-validator.git",
    maintainer="Sean Wiseman",
    maintainer_email="seanwiseman2012@gmail.com",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ]
)
