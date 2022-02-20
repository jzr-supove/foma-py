import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="foma",
    version="1.0.0",
    author="Mans Hulden",
    author_email="mans.hulden@gmail.com",
    maintainer="Jasur Yusupov",
    maintainer_email="jasuryusupov14@gmail.com",
    description="Python bindings for Foma",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/GooDeeJaY/foma-py",
    project_urls={
        "Bug Tracker": "https://github.com/GooDeeJaY/foma-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)