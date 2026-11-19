import argparse

from description import describe_dataset
from split_data import split_dataset


def main():
    parser = argparse.ArgumentParser(description="Explore or split California Housing data.")
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument(
        "--describe",
        action="store_true",
        help="print the dataset exploration report (default)",
    )
    actions.add_argument(
        "--split",
        action="store_true",
        help="create and save a reproducible train/test split",
    )
    parser.add_argument("--test-size", type=float, default=0.2, help="test fraction (default: 0.2)")
    parser.add_argument("--random-state", type=int, default=42, help="split seed (default: 42)")
    parser.add_argument(
        "--output-dir", default="data/splits", help="directory for train.csv and test.csv"
    )
    args = parser.parse_args()

    if args.split:
        train_path, test_path = split_dataset(
            test_size=args.test_size,
            random_state=args.random_state,
            output_dir=args.output_dir,
        )
        print(f"Training data: {train_path}")
        print(f"Test data: {test_path}")
    else:
        describe_dataset()


if __name__ == "__main__":
    main()
