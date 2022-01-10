import requests

def disadvantage_score(cds_code):
    url = "https://api.caschooldashboard.org/LEAs/" + cds_code  +"/7/true"
    response = requests.get(url)
    try:
        data = response.json()
        score = data['disadvantaged']
    except:
        score = 0
    return(score)

def get_school_name(cds_code):
    url = "https://api.caschooldashboard.org/LEAs/" + cds_code  +"/7/true"
    response = requests.get(url)
    try:
        data = response.json()
        school = data['school']
    except:
        school = ""
    return(school)

if __name__ == '__main__':
    print(disadvantage_score('19101990135582'))
