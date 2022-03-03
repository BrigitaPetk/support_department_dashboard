import os.path, time
from pathlib import Path
import datetime
import os

class DeleteFiles():
    def delete(self, download_direktorija, extract_direktorija):
        file_location1 = download_direktorija
        file_location2 = extract_direktorija
        zip_files = list(file_location1.glob("*.zip*"))
        csv_files = list(file_location2.glob("*.csv*"))

        folders = [zip_files, csv_files]

        today = datetime.date.today()
        time_delta = today - datetime.timedelta(days=19)

        for files in folders:
            for file in files:
                t = os.path.getmtime(file)
                formated = datetime.datetime.fromtimestamp(t)
                if formated.date()  > time_delta:
                    print(f"{file} file is new")
                else:
                    print(f"{file}file will be deleted")
                    os.remove(file)

    
    

    
    