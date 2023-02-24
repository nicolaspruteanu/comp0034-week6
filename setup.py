# Retained for those who still wish to use this
from setuptools import setup, find_packages

setup(
    name="comp0034-week6",
    packages=["flask_app"],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["flask", "pandas", "openpyxl"],
)
