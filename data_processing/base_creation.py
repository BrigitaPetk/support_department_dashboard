import pandas as pd
from pathlib import Path


class BaseCreator():
    def creator(self, filter_direktorija, final_direktorija):

        filter_files = list(filter_direktorija.glob("*.csv*"))
        
        if not filter_files:
            print("folder is empty")

            empty_data_base = {'TecReq#': [], 'Year':[],'Month':[], 'Week':[], 'Created+3mod':[], 'First Lock+3mod':[], 'FirstResponse+3mod':[], 'Close Time+3mod':[], 
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

            empty_data_base = {'Year':[], 'Month':[], 'Week': [],'request number': [],'request number in LT': [], 
                'request number in AT':[] , 'request number in CH':[] ,
                'request number in DE':[] , 'request number in IN':[] ,
                'IMP request number': [], 'SMART request number':[], 'STRAT request number': [],
                'EMPTY request number': [], 'LT request number in DE':[],
                'LT request number in CH':[], 'LT request number in AT':[], 'LT CTS': [],
                'knowledge level empty': [],  'knowledge level 1-2': [], 'knowledge level 3-4': [],
                'STRAT solution time': [], 'IMP solution time': [], 'SMART solution time': [],
                'EMPTY solution time': [], 'Intake': [] }
            df = pd.DataFrame(empty_data_base)
            df.to_csv(f'{final_direktorija}/base_by_week.csv', sep=',', index=False)
            print("final data base was created")
        else: 
            print("not empty folder")

    def creator_GB(self, filter_direktorija_GB, final_direktorija_GB):

        filter_files = list(filter_direktorija_GB.glob("*.csv*"))
        
        if not filter_files:
            print("folder is empty")

            empty_data_base = {'TecReq#': [], 'Year':[],'Month':[], 'Week':[], 'Created+3mod':[], 'First Lock+3mod':[], 'FirstResponse+3mod':[], 'Close Time+3mod':[], 
                        'First Response - Created':[], 'First Lock - Created':[], 'Queue':[], 'Owner Country Code':[], 'State':[], 'Number of Articles':[], 
                        'Needed knowledge level':[], 'Case CV':[]}
            df = pd.DataFrame(empty_data_base)
            df.to_csv(f'{filter_direktorija_GB}/base_GB.csv', sep=';', index=False)
            print("base was created")
        else: 
            print("not empty folder")

        final_files = list(final_direktorija_GB.glob("*.csv*"))

        if not final_files:
            print("folder is empty")

            empty_data_base = {'Year':[], 'Month':[], 'Week': [],'request number': [],'request number in LT': [], 
                'request number in GB':[] , 'request number in IE':[], 'request number in IN':[] ,
                'IMP request number': [], 'SMART request number':[], 'STRAT request number': [],
                'EMPTY request number': [], 'LT request number in GB':[],
                'LT request number in IE':[],  'LT CTS': [],
                'knowledge level empty': [],  'knowledge level 1-2': [], 'knowledge level 3-4': [],
                'STRAT solution time': [], 'IMP solution time': [], 'SMART solution time': [],
                'EMPTY solution time': [], 'Intake': [] }
            df = pd.DataFrame(empty_data_base)
            df.to_csv(f'{final_direktorija_GB}/base_by_week.csv', sep=',', index=False)
            print("final data base was created")
        else: 
            print("not empty folder")
                   