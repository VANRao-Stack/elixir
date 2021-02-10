import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elixir",   
    version="0.0.2",
    author="Sanaul Shaheer, V Abhijith Narayan Rao",
    author_email="sanaulshaheer@gmail.com",
    description="A Python package for 1-D blood flow simulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VANRao-Stack/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Computational Biologists',
        'Topic :: Blood Flow Simulator'
    ],
    python_requires='>=3.6',
    install_requires=[
        'tensorflow>=2.4.0',
        'tensorflow_probability>=0.12.0',
        'numpy>=1.19.4',
        'scipy>=1.4.1',
        'plotly'
        ]
)
