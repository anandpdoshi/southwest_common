from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='southwest_common',
    version=version,
    description='Common code for Southwest ERPNext',
    author='Anand Doshi',
    author_email='anand@frappe.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
