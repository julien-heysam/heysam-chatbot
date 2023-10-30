from setuptools import find_packages, setup

setup(
    name="src",
    version="0.1.0",
    description="Sam joins sales calls & Slack channels, providing AEs instant and contextual responses to product questions, eliminating delays, and the need for a dedicated SE on every call",
    author="HeySam",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license="MIT",
)
