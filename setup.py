import setuptools
import pathlib

component_name = "streamlit_geolocation"

# See https://docs.streamlit.io/library/components/publish
# rm -rf dist/;python3 setup.py sdist bdist_wheel;twine upload dist/*
setuptools.setup(
    name=component_name,
    version="0.0.7",
    description="A custom Streamlit component to get the users location via js navigator.geolocation.",
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    author='Patrick Steffanic',
    author_email='steffaniccodes@gmail.com',
    url='https://github.com/steffanic/streamlit-geolocation',
    install_requires=["streamlit>=1.0.0"],
    keywords=['Python', 'Streamlit', 'JavaScript'],
    python_requires=">=3.8",
)