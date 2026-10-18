# SmartLoyaltySegmentation

> **Archived.** This is a 2018 course/learning project and is no longer maintained.

Customer segmentation for an airline frequent-flyer (loyalty) program using K-Means clustering. The script loads member data from `resources/data.csv`, lets the user pick two attributes in a small Tkinter dialog, normalizes them, chooses the number of clusters with an elbow heuristic over WCSS (inertia) for k = 1..10, and then plots the clusters and prints per-cluster summary statistics (customer share, points share, activity counts).

Smart Airline Loyalty Segmentation Using K-Means Algorithm.

## Tech stack

- Python 3
- pandas, NumPy, SciPy (normalization)
- scikit-learn (K-Means)
- matplotlib (elbow and cluster plots)
- Tkinter (attribute selection dialog and results grid)

## Repository structure

- `main.py` - entry point; runs the full pipeline
- `KMeansIMP.py` - WCSS sweep, elbow selection, final K-Means fit
- `elbow.py` - elbow heuristic that picks the number of clusters
- `normalization.py` - feature normalization
- `utility.py`, `result_extraction.py` - per-cluster statistics
- `plot_results.py` - scatter plot of clusters and centroids
- `UI.py` - Tkinter dialogs and results grid
- `GUI.py` - unused stub window (not imported by `main.py`)
- `resources/data.csv` - semicolon-separated sample member data (99 rows)

## How to run

From the repository root:

```
pip install -r requirements.txt
python main.py
```

Tkinter must be available (it ships with the standard Python installer on Windows and macOS; on Linux it may need the `python3-tk` package). The script shows matplotlib windows during the run; close each one to continue.
