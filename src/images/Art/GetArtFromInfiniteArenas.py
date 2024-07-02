import os
import requests
from bs4 import BeautifulSoup


# Function to download PNG files from a given URL and save them to a specified directory
def download_png_files(url, save_dir, exclude_patterns=[]):
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the links that end with .png, excluding specified patterns
    png_links = [
        link.get("href")
        for link in soup.find_all("a")
        if link.get("href").endswith(".png")
        and not any(
            link.get("href").endswith(pattern) for pattern in exclude_patterns
        )
    ]

    # Create the save directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Download each PNG file
    for link in png_links:
        file_name = os.path.join(save_dir, os.path.basename(link))
        file_url = short_url + link
        print(f"Downloading {file_url}...")

        # Send a GET request to the file URL
        file_response = requests.get(file_url)
        file_response.raise_for_status()

        # Save the file
        with open(file_name, "wb") as file:
            file.write(file_response.content)
        print(f"Saved {file_name}")

    print(f"All PNG files have been downloaded from {url}.")


# URL and directory for pilots
pilots_url = "https://infinitearenas.com/xw2/images/artwork/pilots/"
pilots_save_dir = "pilots"
pilots_exclude_patterns = [
    "-delta7baethersprite.png",
    "Copy.png",
    "rebel-fang.png",
]

# URL and directory for upgrades
upgrades_url = "https://infinitearenas.com/xw2/images/artwork/upgrades/"
upgrades_save_dir = "upgrades"
upgrades_exclude_patterns = ["b6bladewingprototype1.png", "doublecrew.png"]

short_url = "https://infinitearenas.com"
# Download PNG files from pilots directory
download_png_files(pilots_url, pilots_save_dir, pilots_exclude_patterns)

# Download PNG files from upgrades directory
download_png_files(upgrades_url, upgrades_save_dir, upgrades_exclude_patterns)
