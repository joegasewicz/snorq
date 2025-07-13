from setuptools import setup, find_packages

setup(
    name="snorq",
    version="0.1.0",
    description="Async URL sniffer and monitor",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.0",
        "colorlog>=6.7.0",
    ],
    entry_points={
        "console_scripts": [
            "snorq=snorq.main:main",
        ],
    },
    python_requires=">=3.11",
    include_package_data=True,
)
