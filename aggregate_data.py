from search_results import get_data
from school_statistics import disadvantage_score, get_school_name
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

def generate_disadvantaged_scores(cds_list):
    score_dct = {}
    for cds_code in cds_list:
        print(cds_code)
        school_name = get_school_name(cds_code)
        print(school_name)
        score_dct[school_name] = disadvantage_score(cds_code)
        print(str(score_dct[school_name])+"\n")
    return score_dct
    
    

if __name__ == '__main__':
    # print(generate_cds_codes())
    #TODO check for duplicates
    codes = generate_cds_codes()
    #TODO add more logging
    print(generate_disadvantaged_scores(codes))