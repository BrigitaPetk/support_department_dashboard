from isort import file
import pandas as pd
from pathlib import Path


class BaseCreator():
    def creator(self, filter_direktorija):

        files = list(filter_direktorija.glob("*.csv*"))
        

        if not files:
            print("folder is empty")

            empty_data_base = {'TecReq#': [], 'Year':[], 'Week':[], 'Created+3mod':[], 'First Lock+3mod':[], 'FirstResponse+3mod':[], 'Close Time+3mod':[], 
                        'First Response - Created':[], 'First Lock - Created':[], 'Queue':[], 'Owner Country Code':[], 'State':[], 'Number of Articles':[], 
                        'Needed knowledge level':[], 'Case CV':[]}
            df = pd.DataFrame(empty_data_base)
            df.to_csv(f'{filter_direktorija}/base.csv', sep=';', index=False)
            print("base was created")
        else: 
            print("not empty folder")


                   