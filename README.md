This is a repo for my small learning projects/tasks

1. Baby Names Analysis - https://github.com/DataSamuraii/Learning/tree/master/google-python-exercises/babynames

---
# Baby Names Analysis

This script provides an analysis of popular baby names from HTML files containing ranked lists of names.

## Overview

Given an HTML file named `baby<year>.html`, the script extracts a list of baby names along with their ranks for that particular year. The list begins with the year, followed by names and their ranks in alphabetical order.

## Prerequisites

- Python 3.x
- The `re` module from Python's standard library (for regular expressions)

## Usage

### Command-line Interface

You can use the script in the following ways:

1. **Print Names to Console**:
   ```bash
   python babynames.py baby1990.html
   ```

2. **Write Names to a Summary File**:
   ```bash
   python babynames.py --summaryfile baby1990.html
   ```
   This command creates a new file named `baby1990.html.summary` containing the extracted names.

3. **Process Multiple Files**:
   ```bash
   python babynames.py baby1990.html baby1991.html
   ```

### Script Functions

- `extract_names(filename)`: Given a filename, this function returns a list of names and their ranks extracted from the HTML file.
  
## Output Format

The output, either printed to the console or written to a summary file, is a list that begins with the year, followed by names and their ranks in alphabetical order.

```
1990
Aaliyah 91
Aaron 57
Abagail 895
...
```

## Contributing

If you wish to contribute to this script, please submit a pull request on GitHub.

---
