import urllib2, csv, sys

def get( token, companyNumber, country ):
    urlRequest = 'https://plus.dnb.com/v1/match/cleanseMatch?registrationNumber='+ companyNumber +'&countryISOAlpha2Code=' + country

    requestHeaders = {
        "Authorization": "Bearer " + token
    }

    request = urllib2.Request(urlRequest, headers=requestHeaders)

    try:
        result = urllib2.urlopen(request)
        print(companyNumber + ' OK')
    except urllib2.HTTPError, e:
        print(companyNumber + ' FAIL Code: ' + str(e.code))

if (__name__ == "__main__"):
    token = sys.argv[1]
    filePath = sys.argv[2]
    with open(filePath) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            get(token, row[0], row[1])

