from setuptools import setup, find_packages

setup(
    name="star_orbit",
    version="0.1-beta",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "orbit = star_orbit.main:main"
        ]
    },
    install_requires=[],
)