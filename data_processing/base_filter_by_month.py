import pandas as pd
from pathlib import Path


class CsvFiltrationMonths():
    def filtration_month(self, filter_direktorija, final_direktorija, filter_direktorija_GB, final_direktorija_GB):

        def months(from_location,in_location, base_name, data_name):
            base = pd.read_csv(f'{from_location}/{base_name}.csv', delimiter=';', engine='python').set_index('TecReq#')
            month_name =["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            month_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            request_number = []
            total_LT =[]

            for number in month_number:
                request = base.loc[base['Month'] == number]
                rows, columns = request.shape
                request_number.append(rows)

                df_lt = request.loc[request['Owner Country Code'] == 'LT']
                rows_lt, columns = df_lt.shape
                total_LT.append(rows_lt)

            data = {'Month':month_name, 'Request number': request_number, 'Request number LT': total_LT}
            month_data = pd.DataFrame(data)
            month_data.to_csv(f"{in_location}/{data_name}.csv", sep=',', index=False)
        
        months(filter_direktorija, final_direktorija, 'base','base_by_month')
        months(filter_direktorija_GB, final_direktorija_GB, 'base_GB','base_by_month_GB')
