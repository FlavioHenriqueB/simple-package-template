from setuptools import setup, find_packages

with open("README.md", "r") as f:
    Bank_App_v3 = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Bank_App_v3",
    version="3.0.0",
    author="Flavio_Brito",
    author_email="flaviobrito.edf@gmail.com",
    description="My short description",
    long_description=Bank_App_v3,
    long_description_content_type="text/markdown",
    url="https://github.com/FlavioHenriqueB/BankaApp_Study.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)