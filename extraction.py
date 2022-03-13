import re
import json

def matchatleastOne(list_of_words_to_be_searched, list_of_queries):
    """returns list of queries if the conatain atleast one of the search term"""
    query_list = []
    for query in list_of_queries:
        query = query[1:-1]
        if re.compile('|'.join(list_of_words_to_be_searched),re.IGNORECASE).search(query):
            #print(query)
            query_list.append(query)
    return query_list

def matchAll(list_of_words_to_be_searched, list_of_queries):
    query_list = []
    for query in list_of_queries:
        query = query[1:-1]
        conatiansAll = False
        for word in list_of_words_to_be_searched:
            if word in query:
                conatiansAll = True
            else:
                conatiansAll = False
                break
        if(conatiansAll):
            print(query)
            query_list.append(i)


def read_write_query(file_name, export_to, list_of_words_to_search_for):
    with open (file_name, "r") as myfile:
        data = myfile.read()
        list_of_queries = re.findall(r'\(.*?\)', data)
        with open(export_to, 'w') as f:
            f.write(json.dumps(matchatleastOne(list_of_words_to_search_for, list_of_queries)))
        
