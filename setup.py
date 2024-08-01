from os import path
from setuptools import setup

# read the contents of your description file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

test_deps = ["python-dotenv==0.20.0", "pytest==7.1.3"]
extras = {"test": test_deps}

setup(
    name="heyoo",
    version="0.1.3",
    description="Opensource Python wrapper to WhatsApp Cloud API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Neurotech-HQ/heyoo",
    download_url="https://github.com/Neurotech-HQ/heyoo/archive/refs/tags/v0.1.3.tar.gz",
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["heyoo"],
    install_requires=["httpx>=0.27.0", "requests-toolbelt>=0.9.1", "colorama", "typing;python_version<'3.5'"],
    tests_require=test_deps,
    extras_require=extras,
    keywords=[
        "heyoo",
        "heyoo-libary",
        "WhatsApp Cloud API Wrapper",
        "PyWhatsApp",
        "WhatsApp API in Python",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
