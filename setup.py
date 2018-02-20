from setuptools import setup, find_packages


runtime = set([
    "pelican",
    "markdown",
    "flask",
    "gunicorn",
    "jupyter",
    "fabric"
    "pycrypto",
])

develop = set([
    "ipython",
    "pytest",
    "flake8",
])

if __name__ == "__main__":
    setup(
        name="insights-core-docs",
        version="0.0.1",
        packages=find_packages(),
        install_requires=list(runtime),
        extras_require={
            "develop": list(runtime | develop),
            "optional": ["python-cjson"],
        },
        include_package_data=True
    )
