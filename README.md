# California Housing Data Exploration

This project fetches the California Housing dataset using scikit-learn, loads it as a pandas DataFrame, and prints the first five rows and the dataset dimensions.

## Requirements

- Python 3
- Internet access on the first run so scikit-learn can download the dataset

Python dependencies are pinned in [`requirements.txt`](requirements.txt).

## Run

From the project root, run:

```bash
bash run.sh
```

The script creates a `.venv` virtual environment if one does not already exist, installs the dependencies, and runs `main.py`. The output includes a preview of the data and its number of rows and columns.

You can also run the program manually after activating the environment:

```bash
source .venv/bin/activate
python main.py
```

On Windows PowerShell, set up and run it with:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

## Dataset

`main.py` uses `sklearn.datasets.fetch_california_housing(as_frame=True)`. The fetched frame contains the dataset features and the `MedHouseVal` target. Scikit-learn caches the downloaded dataset for subsequent runs.
