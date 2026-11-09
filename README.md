# Start ML Project

This repository currently contains the Python environment setup for the project. No application entry point or training script is included yet.

## Requirements

- Python 3. Install a version compatible with the packages in `requirements.txt`.
- Bash, to run the provided setup script.

## Setup

From the project root, run:

```bash
bash run.sh
```

This creates a virtual environment in `.venv`, activates it for the script, and installs the pinned dependencies from `requirements.txt`.

To activate the environment in your current terminal after setup:

```bash
source .venv/bin/activate
```

On Windows, create and activate the environment with the platform-specific commands instead:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Running the project

There is currently no application or model script to run. Once one is added, its launch command can be documented here.

## Dependencies

The project dependencies are listed and version-pinned in [`requirements.txt`](requirements.txt). To install or update them manually inside the active environment, run:

```bash
python -m pip install -r requirements.txt
```
