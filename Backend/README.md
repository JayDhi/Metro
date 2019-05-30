# 项目介绍
## 环境配置
### 框架依赖
```python
Django==2.2.1
djangorestframework==3.9.4
djangorestframework-simplejwt==4.3.0
mysqlclient==1.4.2.post1
numpy==1.16.4
```
### MySQL版本&引擎
1. 检查```MySQL```版本<br/>
    ![mysql](https://jaydhipic.oss-cn-beijing.aliyuncs.com/Screen%20Shot%202019-05-30%20at%209.45.59%20PM.png)
2. 确保```MySQL```使用```utf-8```编码
   1.  查看MySQL的字符编码
   
   ```sql
   mysql> show variables like "%char%";
   +--------------------------+-----------------------------------------------------------+
   | Variable_name            | Value                                                     |
   +--------------------------+-----------------------------------------------------------+
   | character_set_client     | utf8                                                      |
   | character_set_connection | utf8                                                      |
   | character_set_database   | latin1                                                    |
   | character_set_filesystem | binary                                                    |
   | character_set_results    | utf8                                                      |
   | character_set_server     | utf8                                                      |
   | character_set_system     | utf8                                                      |
   | character_sets_dir       | /usr/local/mysql-5.7.26-macos10.14-x86_64/share/charsets/ |
   +--------------------------+-----------------------------------------------------------+
   ```
   2. 修改对应表项的值<br/>
   ```sql
   set character_set_database='utf8'
   ```
3. 确保```MySQL```引擎为```InnoDB```
    ```sql
    show variables like '%storage_engine%';
    ```
    ![SQLEnginee](https://jaydhipic.oss-cn-beijing.aliyuncs.com/SQLEnginee.png)
## 功能模块
### 用户认证
#### 登录&注册
##### 注册
 * API
     ```
     http://127.0.0.1:8000/User/register/
     ```
 * 数据格式
     ```python
     {"username": "Zenyatta", "password": "sr4400"}
     ```

 * 返回值:
   * ```Token```
     * ```Access Token```
       * 对于需要身份验证的```API```需要在请求头部带上
         * ```PostMan```
            ![postman](https://jaydhipic.oss-cn-beijing.aliyuncs.com/PostMan.png)
         * ```cUrl```
            ```
            curl -H "Authorization: Bearer [Access Token]" [url] (-X POST)
            ```
         * ```httpie```
            ```
            http [url] "Authorization: Bearer [Access Token]"
            ```
     * ```Refresh Token```
       * ```Access Token```的有效时限是五分钟，五分钟后```Access Token```过期，届时若要访问受限```API```需要重新通过```/User/obtain_token/```获取新的```Access Token```; 或者可以选择在当前```Access Token```未过期前带上```Refresh Token```访问```/User/refresh_token/```获取新的```Access Token```，并在加下来的请求中在请求头中以新的```Access Token```代替旧的```Access Token```延续当前的登录状态
   * ```Menu```
     * 适用于当前用户角色权限的可选操作菜单
### 客流量查询
 * API
    ```python
    http://127.0.0.1:8000/Flow/show_flow/
    ```
 * 数据格式
    ```
    {"dates":[1, 2, 3], "stations": [1, 2, 3]}
    dates & stations 两项的键值必须是可迭代的展开列表，可以是单一项，但必须是列表
    例如
    {"dates": [1], "stations": [1]}
    ```

### 站点&路线(待更新)
### 功能菜单(待更新)
### 角色权限管理(待更新)
## 配置单元测试&数据
### Flow 模块
* 数据文件
    ```
    /Backend/data.npy
    ```
* 配置脚本(单元测试配置有问题，所以在DjangoManageShell中调配(Ctrl-C&Ctrl-V))
  1. ```/Backend/```目录下执行```python manage.py shell```
        ![posi](https://jaydhipic.oss-cn-beijing.aliyuncs.com/Screen%20Shot%202019-05-30%20at%2010.45.40%20PM.png)

  2. 复制如下脚本
        ```python
        # 以下是依赖项
        from App.Flow.models import get_flow_model()
        import numpy as np
        import pickle
        # 以下是数组转换函数
        def trans(inlist):
            return dict((k_1, dict((k_2, dict((k_3, v_3) for k_3, v_3 in zip(['in', 'out'], v_2))) for k_2, v_2 in zip(range(1, len(v_1)+1), v_1))) for k_1, v_1 in zip(range(1, len(inlist)+1), inlist))
        def retrive_one_station(i, Dic):
            return {k_1: v_1[i] for k_1, v_1 in Dic.items()} 
        def regroup(flatDic):
            return {i+1: {j: flatDic[i*144+j] for j in range(1, 145)} for i in range(19)}    
        # 以下是文件读取, np数组的去归一化
        nparray = np.loads('data.npy')
        intlist = [[[int(i*3000) for i in j] for j in k] for k in nparray.tolist()]
        Dic = trans(intlist)
        # 以下是将Dic中的(2376, 81, 2)字典重排为(81, 144, 2)字典, 并存到中转变量dbCache中
        dbCache = {}
        for i in range(1, 82):
        dbCache[i] = regroup(retrive_one_station(i, Dic))
        # dbCache的格式应该是{station:{date: {in & out}}}
        for i in range(1, 82):
        flow = get_flow_model().objects.create(id=i)
        for j in range(1, 20):
            pkled = pickle.dumps(dbCache[i][j])
            setattr(flow, 'date_%s' % j, pkled)
        flow.save()
        ```