from setuptools import setup, find_packages

setup(
    name="snorq",
    version="0.2.2",
    description="Async URL sniffer and monitor",
    author="Joe Gasewicz",
    author_email="contact@josef.digital",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.0",
        "colorlog>=6.7.0",
        "aiosmtplib>=4.0.1",
        "marshmallow>=4.0.0",
        "click>=8.2.1"
    ],
    entry_points={
        "console_scripts": [
            "snorq=snorq.main:main",
        ],
    },
    python_requires=">=3.11",
    include_package_data=True,
)
