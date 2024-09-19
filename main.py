# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name, there="there"):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {there}')  # Press Ctrl+F8 to toggle the breakpoint.

# Get data by using API,help me to get the data by using get method.
# Get data by from this url: https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=LTMV&lang=en&rformat=csv

import os
import requests
import pandas as pd
from io import StringIO

def get_weather_data(data_type, lang, rformat, save_dir):
    url = f"https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType={data_type}&lang={lang}&rformat={rformat}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        df = pd.read_csv(StringIO(data))
        print(df)
        # Create the directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)

        # Define the file path
        file_path = os.path.join(save_dir, f"{data_type}_{lang}_{rformat}.csv")

        # Save the DataFrame to a CSV file
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

if __name__ == "__main__":
    data_type = "LTMV"
    lang = "en"
    rformat = "csv"
    save_dir = r"G:\Other computers\My PC\PolyU_PhD\Thesis\Data"
    get_weather_data(data_type, lang, rformat, save_dir)





# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
