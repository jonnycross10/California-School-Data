from search_results import get_data
import json
import pandas as pd

def generate_cds_codes():
    df = pd.read_csv("./assets/ca_counties.csv")
    #print(df)
    county_names = df['County'].to_list()
    cds_list = []
    for county in county_names:
        print("getting info for: " + county)
        county_data = get_data(county)
        for doc in county_data['value']:
            cds_list.append(doc['document']['cdsCode'])
    return(cds_list)


if __name__ == '__main__':
    print(generate_cds_codes())