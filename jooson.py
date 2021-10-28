import  json
data='{"name":"harry","add":"pune"}'
print(data)

a1=json.loads(data)
print(a1["name"])

date2={
    "helooo ":"gauresh",
    "Bikes":["ktm","bullet","splander"],
    "pocket":("one rupee coin","pen hain"),
    "isbad":False
}
jsoon=json.dumps(date2)
print(jsoon)




person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)
json1_data = json.loads(person_json)['children']
# Output: {"name": "Bob", "age": 12, "children": null}
print(json1_data)


list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print(list1[0], list2[0])



from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='32419d46f3294a7b8729fdd910392ae0')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()