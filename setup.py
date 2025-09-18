from setuptools import setup, find_packages

setup(
    name="hubspot-connector",
    version="0.0.0",
    author="dan ish",
    author_email="dan@gmail.com",
    description="A utility class to interact with Hubspot using OAuth 2.0 credentials.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["hub_spot"],
    python_requires=">=3.10",
    install_requires=[
        "requests"
    ],
)