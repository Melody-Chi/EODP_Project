# League of Legends KDA Analysis

This project provides a comprehensive data processing pipeline to analyze the KDA (Kills-Deaths-Assists) ratio from League of Legends Challenger matches. Our aim is to determine factors that can help players achieve a higher KDA and, consequently, a higher win rate.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data Processing Steps](#data-processing-steps)
5. [Results](#results)
6. [Limitations](#limitations)
7. [Future Work](#future-work)
8. [Contributors](#contributors)

## Introduction

League of Legends (LoL) is a popular online multiplayer game. A higher KDA often correlates with better gameplay. By examining datasets from the NA, EUW, and KR servers, we're hoping to identify trends that contribute to a player's KDA.

## Installation

**Prerequisites:** 
- Python 3.x
- Libraries: pandas, numpy, matplotlib, seaborn, etc.

```bash
git clone https://github.com/Melody-Chi/EODP_Project1.git
cd League-of-Legends-Matches-Analysing
```

## Usage

```python
python kda_analysis.py --server NA
```

## Data Processing Steps

1. **Data Cleaning:** Removal of missing values from the dataset.
2. **Merging Datasets:** Combining datasets from multiple servers (EU, KR, NA) for comprehensive analysis.
3. **Outlier Removal:** Removal of unusual KDA values (greater than 8).
4. **Data Filtering:** Selecting matches between certain levels for consistent analysis.
5. **Visualization:** Box plots, bar charts, confusion matrices, histograms, etc., to better understand the data.

## Results

Our preliminary findings show significant relationships between KDA and certain in-game variables like damage to buildings, turret kills, gold earned, and more. Detailed results can be found in the `results` directory.

## Limitations

1. The dataset focuses only on challenger matches, which might not represent the entire player base.
2. The dataset lacks some potentially useful data like match outcomes and match duration.
3. The categorization of roles is not specific enough for nuanced analysis.

## Future Work

We plan to incorporate Master matches data and refine our data processing steps for more accurate analysis.

## Contributors

- Liang
- Jino
- Melody
- William

---
