import json
import time
from concurrent.futures import ThreadPoolExecutor

import requests


BASE_URL = "https://jsonplaceholder.typicode.com/photos"
PHOTO_COUNT = 5000
MAX_WORKERS = 50


def fetch_photo(photo_id):
    response = requests.get(f"{BASE_URL}/{photo_id}", timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    start_time = time.time()

    photo_ids = range(1, PHOTO_COUNT + 1)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        photos = list(executor.map(fetch_photo, photo_ids))

    with open("photos.json", "w", encoding="utf-8") as file:
        json.dump(photos, file, ensure_ascii=False, indent=4)

    elapsed_time = time.time() - start_time
    print(f"Total execution time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
