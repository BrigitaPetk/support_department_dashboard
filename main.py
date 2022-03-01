import sys
from pathlib import Path
from data_processing.outlook import AttachmentRetriever
from data_processing.unzip import FileUnzip
from data_processing.CSV_Filtration import CsvFiltration
from data_processing.base_filter_by_week import FilterFinalData
from data_processing.base_creation import BaseCreator


if len(sys.argv) < 2:
    print("Please specify base directory!")
    exit()

bazine_direktorija_str = sys.argv[1]
bazine_direktorija = Path(bazine_direktorija_str)
download_direktorija = bazine_direktorija / "download"
extract_direktorija = bazine_direktorija / "extract"
filter_direktorija = bazine_direktorija / "filter"
final_direktorija = bazine_direktorija / "final"
print(str(final_direktorija.absolute()))

download_direktorija.mkdir(parents=True, exist_ok=True)
extract_direktorija.mkdir(parents=True, exist_ok=True)
filter_direktorija.mkdir(parents=True, exist_ok=True)
final_direktorija.mkdir(parents=True, exist_ok=True)

AttachmentRetriever().retrieve(download_direktorija)
print("-------------------------------------attachments saved--------------------------------")
FileUnzip().unzip(download_direktorija, extract_direktorija)
print("-------------------------------------files unziped--------------------------------")
BaseCreator().creator(filter_direktorija)
print("-------------------------------------created data base--------------------------------")
CsvFiltration().firt_filtration(extract_direktorija, filter_direktorija)
print("-------------------------------------first filtration done--------------------------------")
FilterFinalData().final_data(filter_direktorija, final_direktorija)
print("-------------------------------------data analyze done--------------------------------")
