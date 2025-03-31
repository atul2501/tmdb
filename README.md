# Movie Data Extraction from TMDB API

## Overview
This script fetches popular movie data from The Movie Database (TMDB) API. It iterates through 500 pages of popular movies and extracts key details such as title, overview, popularity, vote count, original language, vote average, and release date.

## Requirements
Ensure you have the following installed:
- Python 3.x
- `requests` library
- `pandas` library

You can install the required libraries using:
```bash
pip install requests pandas
```

## Usage
1. Obtain an API key from [TMDB](https://www.themoviedb.org/).
2. Replace `api_key` in the script with your actual TMDB API key.
3. Run the script:
   ```bash
   python script.py
   ```

## Code Explanation
- The script loops through pages 1 to 500 of TMDB's popular movies.
- It makes a GET request to the TMDB API for each page.
- Extracts and stores movie attributes such as:
  - Title
  - Overview
  - Popularity
  - Vote count
  - Original language
  - Vote average
  - Release date
- The extracted data is stored in a pandas DataFrame (`final`).
- The script uses `pd.concat()` to append new data frames efficiently.

## Notes
- The script assumes that the API key is valid.
- Exceeding the API rate limit may result in temporary blocks; handle it with sleep intervals if needed.
- Modify the script to save the final dataset to a CSV file:
  ```python
  final.to_csv('movies_data.csv', index=False)
  ```

## Disclaimer
This script is intended for educational and non-commercial use. Ensure compliance with TMDB API terms of use.
