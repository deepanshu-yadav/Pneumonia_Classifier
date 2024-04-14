# script for downloading the data
import os
import requests
import zipfile

from tqdm import tqdm

if __name__ == "__main""":
    # create a data folder
    data_folder = "./data"
    os.mkdir(data_folder)

    # download the data
    url = "https://data.mendeley.com/public-files/datasets/rscbjbr9sj/files/f12eaf6d-6023-432f-acc9-80c9d7393433/file_downloaded"

    zip_folder = os.path.join(data_folder, "ChestXRay2017.zip")

    r = requests.get(url, stream=True)

    # size in bytes
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024

    print("Downloading ...")
    with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
        with open(zip_folder, "wb") as file:
            for data in r.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
    print("Done.")

    with zipfile.ZipFile(zip_folder, "r") as zip_ref:
        zip_ref.extractall(data_folder)
