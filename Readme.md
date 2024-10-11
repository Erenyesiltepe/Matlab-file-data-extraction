# Data Processing Script

This script is designed to load and process experimental and recall data from MATLAB files, converting them into pandas DataFrames for further analysis. It is particularly useful for researchers and data analysts working with biomotion data.

## Requirements

Ensure you have the following packages installed:

- `scipy`
- `pandas`

You can install these packages using pip:

```sh
pip install -r requirements.txt
```

The folder structure where the script should run has to be as follows:

```
ParentFolder
|-p1|
|   |-experimentRecall_data
|   |-experimentData
|-p2|
|   |-experimentRecall_data
|   |-experimentData
```

Then you may change folder_name variable with your ParentFolder name then run: 
```bash
    python test.py
```