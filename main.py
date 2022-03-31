import sys
from pathlib import Path
import logging
from data_processing.outlook_local import AttachmentRetriever
# from data_processing.outlook_server import AttachmentRetrieverServer
from data_processing.unzip import FileUnzip
# from data_processing.CSV_Filtration import CsvFiltration
from data_processing.CSV_Filtration import CsvFiltration
from data_processing.base_filter_by_week import FilterFinalData
from data_processing_GB.base_filter_by_week import FilterFinalData_GB
from data_processing.base_creation import BaseCreator
# from data_processing.delete_old_files import DeleteFiles
# from data_processing.delete_old_data import DataDelete
from data_processing.base_filter_by_month import CsvFiltrationMonths

logging.basicConfig(filename='stages.log' , level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

if len(sys.argv) < 2:
    print("Please specify base directory!")
    exit()

bazine_direktorija_str = sys.argv[1]
bazine_direktorija = Path(bazine_direktorija_str)
download_direktorija = bazine_direktorija / "download"
extract_direktorija = bazine_direktorija / "extract"
filter_direktorija = bazine_direktorija / "filter"
final_direktorija = bazine_direktorija / "final"
filter_direktorija_GB = bazine_direktorija / "filter_GB"
final_direktorija_GB = bazine_direktorija / "final_GB"
print(str(final_direktorija.absolute()))

download_direktorija.mkdir(parents=True, exist_ok=True)
extract_direktorija.mkdir(parents=True, exist_ok=True)
filter_direktorija.mkdir(parents=True, exist_ok=True)
final_direktorija.mkdir(parents=True, exist_ok=True)
filter_direktorija_GB.mkdir(parents=True, exist_ok=True)
final_direktorija_GB.mkdir(parents=True, exist_ok=True)

AttachmentRetriever().retrieve(download_direktorija)
print("-------------------------------------attachments saved--------------------------------")
logging.info(f"1. attacment saved")
# AttachmentRetrieverServer().retrieve_server(download_direktorija)
# print("-------------------------------------attachments saved--------------------------------")
# logging.info(f"1. attacment from server saved")
FileUnzip().unzip(download_direktorija, extract_direktorija)
print("-------------------------------------files unziped--------------------------------")
logging.info(f"2. files unziped")
BaseCreator().creator(filter_direktorija, final_direktorija, filter_direktorija_GB, final_direktorija_GB)
print("-------------------------------------created data base--------------------------------")
logging.info(f"3. base.csv and base_GB.csv was created or exists")
CsvFiltration().first_filtration_GB(extract_direktorija, filter_direktorija_GB)
CsvFiltration().first_filtration(extract_direktorija, filter_direktorija)
print("-------------------------------------first filtration done--------------------------------")
logging.info(f"4. csv files filtrated to base.csv and base_GB.csv")
FilterFinalData().final_data(filter_direktorija, final_direktorija)
FilterFinalData_GB().final_data(filter_direktorija_GB, final_direktorija_GB)
print("-------------------------------------data analyze done--------------------------------")
logging.info(f"5. data filtrated by week")
CsvFiltrationMonths().filtration_month(filter_direktorija, final_direktorija, filter_direktorija_GB, final_direktorija_GB)
print("-------------------------------------base by month--------------------------------")
logging.info(f"6. data filtrated by month")
# DeleteFiles().delete(download_direktorija, extract_direktorija)
# print("-------------------------------------old files deleted--------------------------------")
# logging.info(f"7. old files delyted")
# DataDelete().delete_old_data(filter_direktorija, filter_direktorija_GB)
# print("-------------------------------------old data data--------------------------------")
# logging.info(f"8. old data delyted")