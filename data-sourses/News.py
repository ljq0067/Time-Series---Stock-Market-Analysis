# API Exercise with Python
import requests
import json
import csv

company = ['SP500','S&P 500', 'AT&T', 'ATT', 'Ford Motor', 'Apple', 'Microsoft', 'Bank of America', 'Intel', 'Verizon', 'T-Mobile', 'Pfizer', 'Tesla',
           'Google', 'Amazon', 'Uber', 'Costco', 'Alibaba', 'Citi', 'Facebook', 'Meta', 'JPMorgan', 'Twitter', 'Coca-Cola', 'Paypal', 'Goldman Sachs', 'Moderna', 'Netflix', 'Zoom']

for stock in company:
    # use NewsAPI to find news related to stock
    BaseURL1 = ("https://newsapi.org/v2/everything?q=" + ",".join(stock)) + "&apiKey=237d79255be746ca8b2a73cddddac68f"
    URLPost1 = {' API_KEY ': ' 237d79255be746ca8b2a73cddddac68f ',
                ' sortBy ': ' top ',
                ' format ': ' application/json '}
    # print(URLPost1)
    response1 = requests.get(BaseURL1, URLPost1)
    # print(response1)
    jsontxt = response1.json()

    # use json
    t1 = requests.get(BaseURL1, URLPost1)
    json_data1 = json.loads(t1.text)
    json.dumps(json_data1, indent=4)

    filename = stock + '.csv'
    # write in files
    f = open(filename, 'w', newline='', encoding='utf-8')
    writer = csv.writer(f)
    header = [' published_at ', ' author ', 'source_name', 'title ', 'description']
    writer.writerow(header)

    # select needed data
    for series in json_data1["articles"]:
        print(series["publishedAt"], " ", series["author"], " ", series["source"], " ", series["title"], " ", series["description"])
        published_at = series["publishedAt"]
        author = series["author"]
        sourcename = series["source"]["name"]
        title = series["title"]
        description = series["description"]
        row = [published_at, author, sourcename, title, description]
        writer.writerow(row)

    # close the file
    f.close()
