# coding=utf-8

from pymongo import MongoClient
from bson.objectid import ObjectId

# 连接
collection = MongoClient('localhost', 27017)

# 选择数据库
db = collection['HFBigDataTest']

study = db["study"]
# db['allY.xls'].find() 表查询数据
for i in study.find():
    # study.insert_one(i)
    print(i)

"""
remove 删除集合中的文档 用法:
    study.remove()
    study.remove({"_id": "5a3793b11b77fd0c44bc92c4"})
"""
study.remove({"_id": "5a3793b11b77fd0c44bc92c4"})
"""
find_one 查询一条数据 find_one({'name':'user2'}) 查询条件
"""
# study.find_one()


"""
更新： update() 函数
update(criteria, objNew, upsert, mult)
    criteria: 需要被更新的条件表达式
    objNew: 更新表达式
    upsert: 如目标记录不存在，是否插入新文档。
    multi: 是否更新多个文档。
"""
print(study.find_one({'_id': ObjectId("5a3793b11b77fd0c44bc9357")}))
study.update({'_id': "5a3793b11b77fd0c44bc9357"}, {'$set': {'基础设施投资': 'test'}},
             multi=True)
"""
数据库的查询
基本上是用find()函数进行查询，
判断：
$lt 小于 {'age': {'$lt': 20}}
$gt 大于 {'age': {'$gt': 20}}
$lte小于等于{'age': {'$lte': 20}}
$gte大于等于{'age': {'$gte': 20}}
$ne 不等于{'age': {'$ne': 20}}
$in 在范围内 {'age': {'$in': [20,30]}}
$nin 不在范围内 {'age': {'$nin': [20, 30]}}
还可以用正则来匹配： 
    例如查询名字以M开头的学生数据： study.find({'name': {'$regex'： '^M.*'}})
    
$regex匹配正则{'name': {'$regex': '^M.*'}}name以M开头
$exists属性是否存在{'name': {'$exists': True}}name属性存在
$type类型判断{'age': {'$type': 'int'}}age的类型为int
$mod数字模操作{'age': {'$mod': [5, 0]}}年龄模5余0
$text文本查询{'$text': {'$search': 'Mike'}}text类型的属性中包含Mike字符串
$where高级条件查询{'$where': 'obj.fans_count == obj.follows_count'}自身粉丝数等于关注数
"""

"""
对查询出来的数据进行统计 study.find().count()
排序：
    study.find().sort('name' pymongo.ASCENDING).skip(2).limit() 
    排序完然后进行偏移然后再限制输出的个数
"""

study.find({"age": {'$lt': 15}})
study.find({'name': "user8"})


"""
由于mongodb不支持表连接，所以文档中采取 JSON 这种层级结构存储多层数据，
我们可以直接用嵌入(Embed)代替传统关系型数据库的关联引用(Reference)。
(1)# 条件表达式中的多级路径须用引号,以 "." 分割
    u = db.集合名.find_one({"im.qq":12345678})
    # 查询结果如：{"_id" : ObjectId("4c479885089df9b53474170a"), "name" : "user1", 
    "im" : {"msn" : "user1@hotmail.com", "qq" : 12345678}}

    print u['im']['msn']   #表打印出： user1@hotmail.com

(2)# 多级路径的更新
    db.集合名.update({"im.qq":12345678}, {'$set':{"im.qq":12345}})

(3)for u in db.users.find({'data':"abc"}): print u
  # 显示如： { "_id" : ObjectId("4c47a481b48cde79c6780df5"), "name" : "user8", 
  "data" : [ { "a" : 1, "b" : 10 }, 3, "abc" ] }

"""