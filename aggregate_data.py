from search_results import get_data
import json
import pandas as pd

def generate_cds_codes():
    df = pd.read_csv("./assets/ca_counties.csv")
    #print(df)
    county_data = get_data("Placer")
    cds_list = []
    for doc in county_data['value']:
        cds_list.append(doc['document']['cdsCode'])
    return(cds_list)


if __name__ == '__main__':
    generate_cds_codes()