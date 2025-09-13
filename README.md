# Ubuntu Image Fetcher

Ubuntu Image Fetcher is a simple Python tool for downloading images from the web. Users can enter the URL of an image, and the program fetches and saves it into a local directory.

---

## Features

- Fetch images from any valid URL.
- Automatically creates a folder (`Fetched_Images`) to store downloaded images.
- Verifies that the provided URL points to an actual image.
- Automatically generates a filename if one is not provided in the URL.
- Handles invalid URLs and connection errors gracefully.

---

## Prerequisites

- Python 3.x installed
- `requests` library

You can install the required library with:

```bash
pip install requests
```
