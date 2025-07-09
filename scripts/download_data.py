import os
import requests
from tqdm import tqdm

def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = url.split('/')[-1]
    filepath = os.path.join(dest_folder, filename)

    # Stream download with progress bar
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 KB

    with open(filepath, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            file.write(data)
            bar.update(len(data))

    print(f"\nDownload completed. File saved to: {filepath}")

if __name__ == "__main__":
    
    dataset_url = "https://drive.google.com/file/d/1HkqgB1aXKcca7OT4rFSS_tF8iVkqL1Pw/view?usp=drive_link"
    download_folder = "data"

    download_file(dataset_url, download_folder)
