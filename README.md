# shp2geojson

A Python project for converting [shapefile](https://data.gov.tw/dataset/7441) data to GeoJSON format and processing geographic datasets.

## Overview

This project converts ESRI Shapefiles (e.g. `.shp`, `.dbf`, `.shx`) to GeoJSON. It also processes additional geographic data and metadata files.

This project includes data that has been converted into the GeoJSON format, which users can reference or use for further analysis and application.


## Prerequisites

- Python (see [.python-version](.python-version) for the required version)
- [uv](https://github.com/your-uv-tool-repo) for dependency management (with lock file: [uv.lock](uv.lock))
- Geopandas and its dependencies as specified in [pyproject.toml](pyproject.toml)

## Installation
```bash
uv venv
source .venv/bin/activate
uv sync
```