import pandas as pd
from pathlib import Path
import os


class BaseCreator():
    def creator(self, filter_direktorija, final_direktorija, filter_direktorija_GB, final_direktorija_GB):

        def base_creator(location, name):
            filter_files = list(location.glob("*.csv*"))
            if not filter_files:
                empty_data_base = {'TecReq#': [], 'Year':[],'Month':[], 'Week':[], 'Created+3mod':[], 'First Lock+3mod':[], 'FirstResponse+3mod':[], 'Close Time+3mod':[], 
                            'First Response - Created':[], 'First Lock - Created':[], 'Queue':[], 'Owner Country Code':[], 'State':[], 'Number of Articles':[], 
                            'Needed knowledge level':[], 'Case CV':[]}
                df = pd.DataFrame(empty_data_base)
                df.to_csv(f'{location}/{name}.csv', sep=';', index=False)
                print("base was created")
            else: 
                print("not empty folder")


        def filtration_by_week_creator(location, name):
            final_files = list(location.glob("*.csv*"))
            if not final_files:
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
                df.to_csv(f'{location}/{name}.csv', sep=',', index=False)
                print("final data base was created")
            else: 
                print("not empty folder")

        def filtration_by_week_creator_GB(location, name):
            final_files = list(location.glob("*.csv*"))
            if not final_files:
                empty_data_base = {'Year':[], 'Month':[], 'Week': [],'request number': [],'request number in LT': [], 
                    'request number in GB':[] , 'request number in IE':[], 'request number in IN':[] ,
                    'IMP request number': [], 'SMART request number':[], 'STRAT request number': [],
                    'EMPTY request number': [], 'LT request number in GB':[],
                    'LT request number in IE':[],  'LT CTS': [],
                    'knowledge level empty': [],  'knowledge level 1-2': [], 'knowledge level 3-4': [],
                    'STRAT solution time': [], 'IMP solution time': [], 'SMART solution time': [],
                    'EMPTY solution time': [], 'Intake': [] }
                df = pd.DataFrame(empty_data_base)
                df.to_csv(f'{final_direktorija_GB}/{name}.csv', sep=',', index=False)
                print("final data base was created")
            else: 
                print("not empty folder")

        def base_by_month_creator(location, name):
            filter_files = list(location.glob("*.csv*"))
            file_names = [Path(file).name for file in filter_files]
            for file_name in file_names:
                if file_name != f"{name}.csv":
                    data = {'Month':[], 'Request number': [], 'Request number LT': []}
                    df = pd.DataFrame(data)
                    df.to_csv(f'{location}/{name}.csv', sep=',', index=False)
                    print("base by month was created")
                else: 
                    print("month file already exists")



        base_creator(filter_direktorija, 'base')
        base_creator(filter_direktorija_GB, 'base_GB')
        filtration_by_week_creator(final_direktorija, 'base_by_week')
        filtration_by_week_creator_GB(final_direktorija_GB, 'base_by_week')
        base_by_month_creator(final_direktorija, "base_by_month")
        base_by_month_creator(final_direktorija_GB, "base_by_month_GB")
            