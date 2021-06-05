import setuptools
import rtop as r

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name=r.APP_NAME,
    version=r.APP_VERSION,
    author=r.APP_AUTHOR,
    license=r.APP_LICENSE,
    description=r.APP_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=r.APP_URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console :: Curses",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: System :: Monitoring"
    ],
    install_requires=[
    ],
    extras_require={
        "dev": [
            "setuptools",
            "wheel",
            "pytest",
            "flake8",
            "twine",
            "sphinx",
            "sphinx_rtd_theme",
        ]
    },
    python_requires='>=3',
    entry_points={
        "console_scripts": [
            f'{r.APP_NAME} = rtop.__main__:main',
        ]
    }
)
