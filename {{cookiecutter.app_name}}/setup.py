from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.readlines()

if __name__ == '__main__':
    setup(
        name="app",
        version="0.0.0",
        packages=find_packages(),
        install_requires=requirements,
        author="{{cookiecutter.author}}",
        author_email="{{cookiecutter.author_email}}",
    )

