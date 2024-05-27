import requests
import gzip
import shutil
import os
from tqdm import tqdm

def download_and_decompress(url, output_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    compressed_file_path = output_path + ".gz"

    with open(compressed_file_path, 'wb') as out_file, tqdm(
        desc="Downloading",
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            out_file.write(data)
            bar.update(len(data))

    with gzip.open(compressed_file_path, 'rb') as f_in, open(output_path, 'wb') as f_out, tqdm(
        desc="Decompressing",
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in iter(lambda: f_in.read(1024), b''):
            f_out.write(data)
            bar.update(len(data))

    os.remove(compressed_file_path)

if __name__ == "__main__":
    genome_data_url = "https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.fna.gz"
    output_path = "data/GRCh38_latest_genomic.fna"
    download_and_decompress(genome_data_url, output_path)
