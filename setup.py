import setuptools

setuptools.setup(
    name='smart-folder',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/smart-folder']
)
