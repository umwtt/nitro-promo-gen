import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nitro-promo-gen",
    version="3.0.1",
    author="umwtt",
    author_email="ozkanumtt@gmail.com",
    description="A Nitro Promo Code Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umwtt/nitro-promo-gen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "certifi==2021.10.8",
        "charset-normalizer==2.0.7",
        "idna==3.3",
        "pyperclip==1.8.2",
        "requests==2.26.0",
        "urllib3==1.26.8"
    ],
    entry_points={
        "console_scripts": [
            "nitro-promo-gen=nitro:nitro"
        ]
    }
)