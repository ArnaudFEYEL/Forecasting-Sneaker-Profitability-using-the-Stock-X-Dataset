import importlib
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

packages = [
    "platform",
    "pathlib",
    "matplotlib",
    "numpy",
    "pandas",
    "plotly",
    "seaborn",
    "sklearn",
    "requests",
    "scipy"
]

for package in packages:
    try:
        importlib.import_module(package)
        print(f"{package} is installed.")
    except ImportError:
        print(f"{package} is not installed. Installing...")
        install_package(package)
