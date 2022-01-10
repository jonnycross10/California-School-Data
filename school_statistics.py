import requests

def disadvantage_score(cds_code):
    url = "https://api.caschooldashboard.org/LEAs/" + cds_code  +"/7/true"
    response = requests.get(url)
    data = response.json()
    try:
        score = data['disadvantaged']
    except:
        score = 0
    return(score)

def get_school_name(cds_code):
    url = "https://api.caschooldashboard.org/LEAs/" + cds_code  +"/7/true"
    response = requests.get(url)
    data = response.json()
    school = data['school']
    return(school)

if __name__ == '__main__':
    print(disadvantage_score('19101990135582'))
