from isort import file
import pandas as pd
from pathlib import Path


class BaseCreator():
    def creator(self, filter_direktorija, final_direktorija):

        filter_files = list(filter_direktorija.glob("*.csv*"))
        
        if not filter_files:
            print("folder is empty")

            empty_data_base = {'TecReq#': [], 'Year':[], 'Week':[], 'Created+3mod':[], 'First Lock+3mod':[], 'FirstResponse+3mod':[], 'Close Time+3mod':[], 
                        'First Response - Created':[], 'First Lock - Created':[], 'Queue':[], 'Owner Country Code':[], 'State':[], 'Number of Articles':[], 
                        'Needed knowledge level':[], 'Case CV':[]}
            df = pd.DataFrame(empty_data_base)
            df.to_csv(f'{filter_direktorija}/base.csv', sep=';', index=False)
            print("base was created")
        else: 
            print("not empty folder")

        final_files = list(final_direktorija.glob("*.csv*"))

        if not final_files:
            print("folder is empty")

            empty_data_base = {'Year':[], 'Week': [],'request number': [],'request number in LT': [], 
                'request number in AT':[] , 'request number in CH':[] ,
                'request number in DE':[] , 'request number in IN':[] ,
                'IMP request number': [], 'SMART request number':[], 'STRAT request number': [],
                'EMPTY request number': [], 'LT request number in DE':[],
                'LT request number in CH':[], 'LT request number in AT':[], 'LT CTS': [],
                'knowledge level empty': [],  'knowledge level 1': [], 
                'knowledge level 2': [], 'knowledge level 3': [], 'knowledge level 4': [],
                'STRAT solution time': [], 'IMP solution time': [], 'SMART solution time': [],
                'EMPTY solution time': [], 'Intake': [] }
            df = pd.DataFrame(empty_data_base)
            df.to_csv(f'{final_direktorija}/base_by_week.csv', sep=';', index=False)
            print("final data base was created")
        else: 
            print("not empty folder")

                   