# California Housing Data Exploration

This project fetches the California Housing dataset using scikit-learn. It can print a colored data exploration report or create a reproducible train/test split as CSV files.

## Requirements

- Python 3
- Internet access on the first run so scikit-learn can download the dataset
- A terminal at least ~105 characters wide to see the preview table without truncated columns

Python dependencies are pinned in [`requirements.txt`](requirements.txt):

- `scikit-learn` downloads the dataset
- `pandas` holds the data as a DataFrame
- `rich` renders the colored tables in the terminal

## Run

From the project root, run:

```bash
bash run.sh
```

By default, this prints the data exploration report. Pass a mode to `main.py` to choose an action:

```bash
python main.py --describe
python main.py --split
```

`--split` creates `data/splits/train.csv` and `data/splits/test.csv` with an 80/20 split and fixed random seed. You can adjust the split and output location:

```bash
python main.py --split --test-size 0.25 --random-state 7 --output-dir data/my-split
```

The test set should be held aside until model selection and hyperparameter tuning are complete. Use only the training data for those steps, then evaluate the selected model once on the test set.

The script stops on the first error, creates a `.venv` virtual environment if one does not already exist, quietly installs the dependencies (including `rich`), and runs `main.py`.

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

## Output

`main.py` prints the report as a series of sections:

| Section | What it shows |
| --- | --- |
| Preview | The first five rows and the number of rows and columns. The target column is highlighted in yellow. |
| Target | The target column name and its summary statistics (count, mean, std, min, quartiles, max). |
| Features | Every feature column and its data type. |
| Missing values | The number of empty cells (`NaN`/`None`) in each column: green for 0, red otherwise. |
| Correlation with target | The Pearson correlation of each feature with the target, sorted by strength. Positive values are green, negative values are red, and values with \|corr\| >= 0.5 are bold. |
| Leakage check | Any feature with \|corr\| >= 0.95 is flagged in red as possible leakage. Otherwise a green message says there is no obvious leakage. |
| Duplicates | The number of fully duplicated rows: green for 0, red otherwise. |

Both thresholds are constants at the top of `main.py` (`LEAKAGE_CORR_THRESHOLD` and `STRONG_CORR_THRESHOLD`).

### Interpreting the checks

- **Missing values** only counts real empty cells. Missing data encoded as placeholder values such as `0`, `-1`, `999` or `"?"` is not detected; check the summary statistics for suspicious minimums and maximums.
- **Correlation** measures only the linear relationship between a feature and the target, from -1 to 1. A value near 0 means there is no straight-line relationship, not that there is no relationship at all. For example, `Latitude` and `Longitude` correlate weakly with the target on their own but together identify expensive coastal areas.
- **Leakage check** catches only the obvious case where a feature nearly duplicates the target, for example because it was computed from it. It cannot detect leakage through time (features with information from the future) or through the way data is split into train and test sets.

## Dataset

`main.py` uses `sklearn.datasets.fetch_california_housing(as_frame=True)`. Scikit-learn caches the downloaded dataset for subsequent runs.

The dataset comes from the 1990 U.S. census and has 20,640 rows, one per census block group, with no missing values and no duplicate rows.

| Column | Description |
| --- | --- |
| `MedInc` | Median income in the block group, in tens of thousands of dollars |
| `HouseAge` | Median house age in the block group, in years |
| `AveRooms` | Average number of rooms per household |
| `AveBedrms` | Average number of bedrooms per household |
| `Population` | Block group population |
| `AveOccup` | Average number of household members |
| `Latitude` | Block group latitude |
| `Longitude` | Block group longitude |
| `MedHouseVal` | **Target:** median house value, in hundreds of thousands of dollars |

The target is capped: the most expensive houses are recorded as `5.00001` (about $500,000), so their true value is only known to be at least that. Keep this in mind before training a model on it.

## Project structure

```
.
├── main.py           # command-line entry point for exploration or splitting
├── split_data.py     # creates and saves a train/test split
├── description.py    # prints the exploration report
├── run.sh            # creates the virtual environment, installs dependencies, runs main.py
├── requirements.txt  # pinned Python dependencies
└── README.md
```
