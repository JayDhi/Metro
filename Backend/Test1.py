import django.apps
django.apps.apps.get_models()

from django.contrib.contentypes.models import ContentType
for ct in ContentType.objects.all():
    m = ct.model_class()
    print("%s.%s\t%d" % (m.__module__, m.__name__, m._defautl_manager.count()))

from User.models import __create_user_model, get_user_db, exe_sql, get_diy_user_model

userModel = get_diy_user_model().objects.create(id=24, name="zhangsan", age=18)
userModel._meta.db_table

from User.serializers import XSerializer
from User.models import __create_user_model, get_user_db, exe_sql, get_diy_user_model
sets = XSerializer(get_diy_user_model(), many=True)


sql = ['CREATE TABLE %s (id int(11) NOT NULL']
for i in range(1,10):
    sql.append('data_%s int(11)'%i)
sql.append('PRIMARY KEY(id));')
create_sql = ",".join(sql)

ds = dict((k1, dict((k_2, dict((k_3, v_3) for k_3, v_3 in ()))for k_2, v_2 in ()))for k_1, v_1 in ())
ds = dict(k_1, (k_2, dict((dict((k_3, v_3) for k_3, v_3 in zip(['in', 'out'], v2))) for k_2, v_2 in zip(range(len(v1)+1), v1)) for k_1, v_1 in zip(range(len(test)+1), test))

a = [[['a', 'b', 'c'], ['d', 'e', 'f']],]
Dict = dict((k_1, dict((k_2, dict((k_3, v_3) for k_3, v_3 in zip(['in', 'out'], v_2))) for k_2, v_2 in zip(range(len(v_1)+1), v_1))) for k_1, v_1 in zip(range(len(test)+1), test))
dic(() for k_3, v_3 in zip(range(len(v_3)+1), v_3))

# +++++++++++++
from App.Flow.models import __create_flow_model, get_flow_db, exe_sql, get_flow_model
flowmodel = get_flow_model().objects.create(id=1)

select column_name as ColumnName,data_type as DataType,character_maximum_length as Length from information_schema.columns where table_name ='flow'




test = [[[i[0]*3000, i[1]*3000] for i in j] for j in array]

Ds = {}
for d3, c3 in zip(test, range(1, len(test)+1)):
     item3 = {}
     for d2, c2 in zip(d3, range(1, len(d3)+1)):
             item2 = {}
             for d1, c1 in zip(d2, ['in', 'out']):
                     item2[c1]=d1
             item3[c2] = item2
     Ds[c3] = item3
ds = dict(() for k_1, v_1 in zip(range(len(tets)+1)))

ds = dict((dict(k_2, dict(k_1, v_1) for k_1, v_1 in zip(['in', 'out'], )) for ()) for (range(len(test)+1),))
ds = dict(k_3, (dict(k_2, dict(k_1, v_1)
    for k_1, v_1 in zip(['in', 'out'], v_2))
    for k_2, v_2 in zip(range(len(v_3)+1), v_3))
    for k_3, v_3 in zip(range(len(test)+1), test))
ds = dict(())

ds = dict((k1, dict((k_2, dict((k_3, v_3) for k_3, v_3 in ()))for k_2, v_2 in ()))for k_1, v_1 in ())

###########从NPY数组中提取  
Dic = dict((k_1, dict((k_2, dict((k_3, v_3) for k_3, v_3 in zip(['in', 'out'], v_2))) for k_2, v_2 in zip(range(1, len(v_1)+1), v_1))) for k_1, v_1 in zip(range(1, len(intlist)+1), intlist))
##############3
ds = dict(k_3, (dict(k_2, dict(k_1, v_1) for k_1, v_1 in zip(['in', 'out'], v_2)) for k_2, v_2 in zip(range(len(v_3)+1), v_3)) for k_3, v_3 in zip(range(len(test)+1), test))

target = dict((, dict((k, v) for k, v in () if v[])) for in ())

{k_1: {k_2: dict([(k, v_1[0][k]) for k in v_1[0]) for k_2 in range(len(v_1)+1)} for k_1, v_1 in zip(range(len(ds)+1), ds)}
{k_1: {k_2: {k_3: v_1 for } for k_2 in range(len(v_1)+1)} for k_1, v_1 in zip(range(len(ds)+1), ds)}

dict([(k, a[k]) for k in a])

{k_1: {k_2: dict([k, v_1[1][k]] for k in v_1[1]) for k_2 in range(90)} for k_1, v_1 in zip(range(len(ds)+1), ds)}



{k_1: {2: dict([(k_3, v_1[2][k_3]) for k_3 in v_1[2]]} for k_1, v_1 in zip(range(len(dict)), dict[k_1])}


### 提取某站点的所有数据########
{k_1: {1: dict([(k_3, v_1[1][k_3]) for k_3 in v_1[1]])} for k_1, v_1 in Dic.items()}
{k_1: {2: v_1[2]} for k_1, v_1 in Dic.items()}
{k_1: {i: v_1[i]} for k_1, v_1 in Dic.items()}
{k_1: v_1[1] for k_1, v_1 in Dic.items()} ######<------------
########################
{k_1: v_1[1] for k_1, v_1 in ds.items()}

def f(i, dic):
    return {k_1: {i: v_1[i]} for k_1, v_1 in dic.items()}

def g(i, dic):
    return {k_1: v_1[i] for k_1, v_1 in dic.items()}

[[k, v_1[2][k]] for k in v_1[2] for k_1, v_1 in zip(range(len(d)),d(k_1))]

dict = {
1: {
    2:{
        'in':2,
        'out':3
    },
    3:{
        'in':4,
        'out':5,
    },
},
2:{
    2:{
        'in':2,
        'out':3,
    },
    3:{
        'in':3,
        'out':4,
    }
}
}

dic = {1: {2:{'in':2,'out':3},3:{'in':4,'out':5,},},2:{2:{'in':2,'out':3,},3:{'in':3,'out':4,}}}

baseList = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def changeBase(n,b):
    x,y = divmod(n,b)
    if x>0:
        return changeBase(x,b) + baseList[y]
    else:             
        return baseList[y]

def changeToTenBase(s,b):
    sL = list(s)
    sL.reverse()
        
    for x in xrange(len(sL)):
        result = result + baseList.index(sL[x])*(b**x)
    return result


# 从时间轴上抽取某一站点的数据
for t in ds:
    tl = {}
    for als in t:
        als = {}

{k: v[1] for k, v in zip(range(len(ds)+1), ds.values())}
 zip([v for v in range(1, len(ds)/144+1)])

# 对提取到的1-2376重拍,拍成三层嵌套的字典
{k: {k_1: v_1 for k_1, v_1 in zip([i for i in range(1, 145)]*19, newDic.values())} for k in [l for l in range(1, 19) for m in range(144)]}

{k : pickle.dumps(v) for k, v in zip(a, a.items())}

{k: {} for k, v in zip(range(1, len(station1)+1), station1.items()) }

Dic = dict((k_1, dict((k_2, dict((k_3, v_3) for k_3, v_3 in zip(['in', 'out'], v_2))) for k_2, v_2 in zip(range(1, len(v_1)+1), v_1))) for k_1, v_1 in zip(range(1, len(test)+1), test))

### 1.重新编号
# {k//4 : v for k, v in zip([i for i in range(1, 145)]*19, newDic.values())}
{j: {k : v for v in newDic.values()} for j in range(1, 19)} #!! 每层都会从头迭代newDic
###

nparray = np.load('file')

intlist = [[[int(i*3000) for i in j] for j in k] for k in nparray.tolist()]


def trans(inlist):
    return dict((k_1, dict((k_2, dict((k_3, v_3) for k_3, v_3 in zip(['in', 'out'], v_2))) for k_2, v_2 in zip(range(1, len(v_1)+1), v_1))) for k_1, v_1 in zip(range(1, len(inlist)+1), inlist))

def regroup(flatDic):
    return {i+1: {j: flatDic[i*144+j] for j in range(1, 145)} for i in range(19)}


def retrive_one_station(i, Dic):
    return {k_1: v_1[i] for k_1, v_1 in Dic.items()} 


File = {}
for i in range(1, 82):
    File[i] = regroup(retrive_one_station(i, Dic))

regroup(retrive_one_station(1, Dic))

for i in range(1, 82):
    flow = get_flow_model().objects.create(id=i)
    for j in range(1, 20):
        pkled = pickle.dumps(File[i][j])
        setattr(flow, 'date_%s' % j, pkled)
    flow.save()

for i in range(2, 83):
    flow = get_flow_model().objects.get(id=i)
    flow.id=i-1
    flow.save()
from App.Flow.models import __create_flow_model, get_flow_db, exe_sql, get_flow_model
from App.Flow.models import get_flow_model

# 测试 EditRoute EditStation   
from App.Combination.models import RouteXStation
from App.Station.models import Station
from App.Station.serializers import EditStation

s = EditStation(data={"station_name":"test 5"})

from App.Route.serializers import EditRoute
sz = EditRoute(data={"route_name": "Test1"}, context={"s1":{"station_id":1, "seq":1}, "s2":{"station_id":2, "seq": 2}, "s3":{"station_id":3, "seq":3}})


from App.Combination.models import RouteXStation
from App.Route.models import Route
from App.Route.serializers import EditRoute
r = Route.objects.get(route_name="Test1")
sz = EditRoute(r, context={"s1":{"station_id":1, "seq": 4}, "s2":{"station_id":2, "seq":3}}, data={"route_name":"Test1"})