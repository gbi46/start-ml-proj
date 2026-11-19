"""Create and save reproducible train/test splits for California Housing."""

from pathlib import Path

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split


def split_dataset(test_size=0.2, random_state=42, output_dir="data/splits"):
    """Split the full dataset and save train.csv and test.csv.

    Returns the paths of the two generated CSV files.
    """
    dataset = fetch_california_housing(as_frame=True)
    train, test = train_test_split(
        dataset.frame,
        test_size=test_size,
        random_state=random_state,
        shuffle=True,
    )

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    train_path = output_path / "train.csv"
    test_path = output_path / "test.csv"
    train.to_csv(train_path, index=False)
    test.to_csv(test_path, index=False)
    return train_path, test_path
