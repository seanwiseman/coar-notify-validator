from setuptools import setup

import coar_notify_validator

setup(
    name="coar_notify_validator",
    version=coar_notify_validator.__version__,
    description="Utility for validating COAR Notify payloads.",
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    packages=[
        "coar_notify_validator",
        "coar_notify_validator.shape_files",
    ],
    include_package_data=True,
    install_requires=[
        "kglab == 0.6.6",
        "rdflib == 7.1.1",
        "pyshacl == 0.23.0",
    ],
    license="MIT",
    url="https://github.com/seanwiseman/coar-notify-validator.git",
    maintainer="Sean Wiseman",
    maintainer_email="seanwiseman2012@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ]
)
