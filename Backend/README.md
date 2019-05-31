# 更新内容
[**戳我传送**](#whats_new)
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
## 本地运行
1. 在```settings.py```中配置数据库连接
   ![settings](https://jaydhipic.oss-cn-beijing.aliyuncs.com/settings.png)
2. 在```/Backend/```下执行
    ```python
    python manage.py makemigrations
    python maange.py migrate
    ```
3. 执行如下命令以测试各项```API```
   ```python
   python manage.py runserver
   ```
## ```API```列表
### ```User/```
 * ```POST: register/```注册
   * 数据格式
     ```
     {"username": "username", "password": "password"}
     ```
 * ```POST: obtain_token/```令牌获取
   * 数据格式
     ```
     {"username": "username", "password": "password"}
     ```
 * ```GET: admin_user/```管理用户(需要Access Token&管理员权限)
   * [在请求头中带上```Access Token```](#jump)
   * 设置管理员账号
     ```python
     python manage.py createsuperuser
     ```
### ```Flow/```
 * ```GET: show_flow/```获取某日期(范围内)某(些)站点的客流量
   * [数据格式](#flow_query)
     ```
     {"dates": [date_1, date_2], "stations": [s_1, s_2]}
     ```
### <span id="whats_new">```Station/```</span>
 * ```GET: get_station```获取某(些)站点的信息
   * 数据格式
     * 无```json```请求, 返回所有站点的信息<br/>
        ![response_all_station](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/reponse_get_station_without_json.png)<br/>
     * 获取选中站点的信息
        ```python
        {"stations": [1, 2, 3]}
        # station键值必须是列表
        {"stations": [1]}
        ```

        ![request_some_stations](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/request_get_menu_with_json.png)<br/>
        ![response_some_stations](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/response_get_station_with_json.png)<br/>
 * ```POST: edit_station```编辑站点信息
   * 数据格式
     * 创建新站点
        ```python
        {"station_info": {"station_name": "Station1"},
        # 下面这项可以省略, 省略的时候默认创建一个不属于任何线路的站点
         "relationship": {"route_id": 1, "seq": 2}
        }
        ```

        ![1](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/reponse_before_add_station.png)<br/>
        ![request_add_station](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/request_add_station.png)<br/>
        ![response_add_station](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/reponse_after_add_station.png)<br/>
     * 编辑现有站点信息
        ```python
        {"station_info": {"station_name": "Station1"},
         "relationship": {"route_id": 1, "seq": 3}
        }
        ```
        需要注意的是如果```relationship```中的```route_id```不存在, 或者是```route_id X seq```的组合存在的话, 会返回报错信息
         * 例如:<br/>
            ![2](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/dumpliacte.png)<br/>
         * 正确请求<br/>
            ![1](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/request_edit_exist_station.png)<br/>
            ![3](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/response_after_edit_exist_station.png)<br/>
         * 错误请求<br/>
           * 存在站点<br/>
            ![1](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/dumpl.png)<br/>
           * 试图覆盖<br/>
            ![2](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/request_dupliacte_seq.png)<br/>
            ![3](https://jaydhipic.oss-cn-beijing.aliyuncs.com/5_31/reponse_dump.png)<br/>

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
       * <span id="jump">对于需要身份验证的```API```需要在请求头部带上</span>
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
       * ```Access Token```的有效时限是五分钟，五分钟后```Access Token```过期，届时若要访问受限```API```需要重新通过```/User/obtain_token/```获取新的```Access Token```; 或者可以选择在当前```Access Token```未过期前带上```Refresh Token```访问```/User/refresh_token/```获取新的```Access Token```，并在加下来的请求中以新的```Access Token```代替请求头中旧的```Access Token```延续当前的登录状态
   * ```Menu```
     * 适用于当前用户角色权限的可选操作菜单
        ![example](https://jaydhipic.oss-cn-beijing.aliyuncs.com/Metro_register.png)

### 客流量查询
 * API
    ```python
    http://127.0.0.1:8000/Flow/show_flow/
    ```
 * <span id="flow_query">数据格式</span>
    ```python
    {"dates":[1, 2, 3], "stations": [1, 2, 3]}
    # dates & stations 两项的键值必须是可迭代的展开列表，可以是单一项，但必须是列表
    # 例如
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
    ![posi](https://jaydhipic.oss-cn-beijing.aliyuncs.com/Screen%20Shot%202019-05-30%20at%2010.45.40%20PM.png)

* 配置脚本(单元测试配置有问题，所以在DjangoManageShell中调配(```Ctrl-C```&```Ctrl-V```))
  1. ```/Backend/```目录下执行```python manage.py shell```
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
# 开发笔记
* 基于角色的权限管理
  * 重构用户模型, 增添用户属性
    ```python
    class Account(AbstractUser):
        CATEGORY_CHOICE = (
            (),
            ()
        )
        category = models.()
    ```
  * 自定义permission_classes
    * 参考```rest_framework.permissions.IsAuthenticated```
        ```python
        class IsAuthenticated(BasePermission):
            """
            Allows access only to authenticated users.
            """

            def has_permission(self, request, view):
                return bool(request.user and request.user.is_authenticated)
        ```
    1. ~~**思路一**~~
        * 重写```has_permission()```在函数内完成权限的验证
            >[**Django-REST Framework Object Level Permissions and User Level Permissions**](https://micropyramid.com/blog/django-rest-user-level-permissions-and-object-level-permissions/)
            ```python
                class IsAuthenticated(BasePermission):
                    def has_permission(self, request, view):
                        return bool(request.user and 
                                request.user.is_authenticated and 
                                request.user.category == 1)
            ```
            * 缺陷: ```request.user```是一个```AnonymousUser```,没有```category```属性
                >[**Django JWT authentication - user is anonymous in middleware**](https://stackoverflow.com/questions/50793212/django-jwt-authentication-user-is-anonymous-in-middleware) 
            
            * 可能的解决方案: 自定义中间件```middleware```,在```django-rest-frame```的中间件拦截```HttpRequest```,并对``user``进行转换前保留对应属性<br/>

                >[**A Django Rest Framework Jwt middleware to support request.user**](http://blog.sadafnoor.me/blog/a-django-rest-framework-jwt-middleware-to-support-request-user/)

                >[**How add Authenticate Middleware JWT django?**](https://stackoverflow.com/questions/45266728/how-add-authenticate-middleware-jwt-django)
        
    2. ~~**思路二**~~
        * 在```JWT```的```Payload```中添加所需的用户属性, 在用户发起请求验证```token```的时候解析```token```完成验证, 从```request.META```中取出```HTTP_AUTHORIZATION```并且反序列化
        1. 修改```response_payload_handler```
            * 对于```django-restframework-jwt```:
               1. 参考```rest_framework_jwt.utils.jwt_reponse_payload_handler()```自定义```new_jwt_response_payload_handler()```:
                    ```python
                    def jwt_response_payload_handler(token, user=None, request=None):
                        return {
                            'token': token,
                            'username': user.username,
                            'user_id' : user.id,
                            'email' : user.email
                        }
                    ``` 
                2. 在```settings.py```中修改对应的处理函数
                    ```python
                        'JWT_RESPONSE_PAYLOAD_HANDLER':
                        'accounts.utils.jwt_response_payload_handler',
                    ```
                    >[**Getting user id returned with JWT
Ask Question**](https://stackoverflow.com/questions/54575716/getting-user-id-returned-with-jwt)
                    >[**Store more than default information in django-rest-framework-jwt**](https://stackoverflow.com/questions/35239401/store-more-than-default-information-in-django-rest-framework-jwt)
            * 对于```rest_framework_simplejwt```:
                1. 继承```TokenObtainPairSerializer```,并添加属性:
                    ```python
                    class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
                        def validate(self, attrs):
                            data = super().validate(attrs)
                            refresh = self.get_token(self.user)
                            data['refresh'] = str(refresh)
                            data['access'] = str(refresh.access_token)

                            # Add extra responses here
                            data['username'] = self.user.username
                        return data


                    class MyTokenObtainPairView(TokenObtainPairView):
                        serializer_class = MyTokenObtainPairSerializer

                    ```
                2. 在```urls.py```中修改对应选项:
                    ```python
                    from Account.utils import MyTokenObtainPairView

                    urlpatterns = [
                        path('admin/', admin.site.urls),
                        path('obtain/', MyTokenObtainPairView.as_view()),
                    ]
                    ```
        * 缺陷: 修改的只是```response_payload```, 而不是```payload```, 相关属性在生成```token```的时候已经被编码
        2. 修改```payload_handler```
            * 对于```rest_framework_jwt```:
                1. 参考```rest_framework_jwt.utils.jwt_payload_handler```实现自己的```jwt_payload_handler```但即便是复制原始代码, 修改```JWT_PAYLOAD_HANDLER```后会出现能取得```token```, 但在后续验证的过程中报错的情况:
                    ```
                    "GET /images/all/ HTTP/1.1" 401 58"
                    "detail": "Authentication credentials were not provided."
                    ```
                    >[**Django Rest Framework : Authentication credentials were not provided**](https://stackoverflow.com/questions/53510881/django-rest-framework-authentication-credentials-were-not-provided)

                    >[**How can i make django-rest-framework-jwt return token on registration?**](https://stackoverflow.com/questions/31147430/how-can-i-make-django-rest-framework-jwt-return-token-on-registration)
        3. 修改```JWTMiddleWare```
            ```python
            import jwt
            import traceback

            from django.utils.functional import SimpleLazyObject
            from django.utils.deprecation import MiddlewareMixin
            from django.contrib.auth.models import AnonymousUser, User
            from django.conf import LazySettings
            from django.contrib.auth.middleware import get_user

            settings = LazySettings()


            class JWTAuthenticationMiddleware(MiddlewareMixin):
                def process_request(self, request):
                    request.user = SimpleLazyObject(lambda: self.__class__.get_jwt_user(request))

                @staticmethod
                def get_jwt_user(request):

                    user_jwt = get_user(request)
                    if user_jwt.is_authenticated():
                        return user_jwt
                # token = request.META.get('HTTP_AUTHORIZATION', None)
                    token = request.META.get('AUTHORIZATION', None)

                    user_jwt = AnonymousUser()
                    if token is not None:
                        try:
                            user_jwt = jwt.decode(
                                        token,
                                        settings.WP_JWT_TOKEN,
                                        )
                            user_jwt = User.objects.get(
                                id=user_jwt['data']['user']['id']
                            )
                        except Exception as e: # NoQA
                            traceback.print_exc()
                        return user_jwt
            ```

    3. **思路三**
        > [**Django Permission进阶使用**](https://segmentfault.com/a/1190000007124746)
        1. 在每个对象上添加不同的权限
            在```DjangoShell```中
            ```python
            from django.contrib.auth.models import Group, Permission
            from django.contrib.contenttypes.models import ContentType
 
            content_type = ContentType.objects.get(app_label='school', model='Discussion')
            permission = Permission.objects.create(codename='can_publish',
                                                name='Can Publish Discussions',
                                                content_type=content_type)

            ```
        2. 对用户进行分组
            在```Django```后台进行分组权限操作的时候会报错```(Django==2.0.2)```
            ```no such table: main.auth_permission__old```
            >[no such table: main.auth_user__old](https://www.baidu.com/s?wd=no+such+table:+main.auth_permission__old&tn=84053098_3_dg&ie=utf-8)
        3. 对不同分组进行授权
        4. 在```permission_classes```的```has_permission```中进行验证
            ```python
            class IsCat0(BaseException):
                def has_permission(self, request, view):
                    return request.user.has_perm('auth.group.can_add_userq')
            ```