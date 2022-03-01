from tempfile import tempdir
import zipfile
from pathlib import Path


class FileUnzip():
    def unzip(self, download_direktorija, extract_direktorija):

        file_location = Path(download_direktorija)
        files = list(file_location.glob("*.zip*"))

        for zip_file in files:
            print(f"file unziped: {zip_file}")
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(extract_direktorija)
  
                
