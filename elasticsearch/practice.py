from elasticsearch import Elasticsearch
from datetime import datetime
import pytz

es = Elasticsearch()

es.indices.create(index='index-name', ignore=400)  # 设置一个index  忽略400错误

# es.indices.delete(index='test-index', ignore=[400, 404])  # 删除一个index 忽略400
# 404错误

# es.cluster.health(wait_for_status='yellow', request_timeout=1)
#
# es.search(index='test_index', filter_path=['hits.hits._*'])
body = {"name": 'lucy', 'sex': 'female', 'age': 10}
luck = {"name": 'luck', 'sex': 'female', 'age': 10}
tom = {"name": 'tom', 'sex': 'female', 'age': 11}


es.index(index='index-name', doc_type='typeName', body=body, id="idValue")

es.create(index='index-name', doc_type='typeName', body=luck, id='luck')
es.create(index='index-name', doc_type='typeName', body=tom, id='tom')
time = datetime.utcnow().replace(tzinfo=pytz.utc)

# es.update(index='index-name', doc_type='typeName', id='idValue',
#           body={"doc": {"age": 13}, "script": {}})

print(es.get(index='index-name', doc_type='typeName', id="idValue"))
print(es.get(index='index-name', doc_type='typeName', id='luck'))


query_all = {'query': {"match_all": {}}}
query_jack = {"query": {"term": {"name": "tom"}}}
query_range = {"query": {"range": {"age": {'gt': 11}}}}

all_doc = es.search(index='index-name', doc_type='typeName', body=query_all)
print(all_doc)


es.delete(index='index-name', doc_type='typeName', id='luck')
es.delete(index='index-name', doc_type='typeName', id='idValue')
