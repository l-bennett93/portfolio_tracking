import pathlib
import setuptools
HERE = pathlib.Path(__file__).parent.resolve()
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")
setuptools.setup(
    name="portfolio_tracking",
    version="1.0.0",
    description="Stock Portfolio Tracking",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="luke bennett",
    packages=setuptools.find_namespace_packages(include=["portfolio_tracking.*"]),
    python_requires=">=3.5, <4"
)