#
## 前端
### 地图绘制
~~TWaver~~
JTopo
* 端点、连线绘制
## 后端
![Backend](https://jaydhipic.oss-cn-beijing.aliyuncs.com/IMG_6449.jpg)
### json 文件''包围会报错，要换成""

### 自定义用户模型
```
(DjangoTest) ➜  DjangoTest python manage.py makemigrations
SystemCheckError: System check identified some issues:
ERRORS:
Account.Account.groups: (fields.E304) Reverse accessor for 'Account.groups' clashes with reverse accessor for 'User.groups'.
HINT: Add or change a related_name argument to the definition for 'Account.groups' or 'User.groups'.
Account.Account.user_permissions: (fields.E304) Reverse accessor for 'Account.user_permissions' clashes with reverse accessor for 'User.user_permissions'.
HINT: Add or change a related_name argument to the definition for 'Account.user_permissions' or 'User.user_permissions'.
auth.User.groups: (fields.E304) Reverse accessor for 'User.groups' clashes with reverse accessor for 'Account.groups'.
HINT: Add or change a related_name argument to the definition for 'User.groups' or 'Account.groups'.
auth.User.user_permissions: (fields.E304) Reverse accessor for 'User.user_permissions' clashes with reverse accessor for 'Account.user_permissions'.
HINT: Add or change a related_name argument to the definition for 'User.user_permissions' or 'Account.user_permissions'.
```
> [link](https://blog.51cto.com/xiaoo/1883535?source=drt)
```
AUTH_USER_MODEL must be of the form 'app_label.model_name'
```

### 自定义Http返回字典时返回的对象错误 
```shell
Internal Server Error: /register/
Traceback (most recent call last):
  File "/Users/james/.virtualenvs/DjangoTest/lib/python3.7/site-packages/django/core/handlers/exception.py", line 35, in inner
    response = get_response(request)
  File "/Users/james/.virtualenvs/DjangoTest/lib/python3.7/site-packages/django/utils/deprecation.py", line 97, in __call__
    response = self.process_response(request, response)
  File "/Users/james/.virtualenvs/DjangoTest/lib/python3.7/site-packages/django/middleware/common.py", line 113, in process_response
    if response.status_code == 404:
AttributeError: 'dict' object has no attribute 'status_code'
```
### 新建线路的同时添加站点
需要序列器内创建嵌套序列器

### SerilalizerMethodField结合JWT
```
curl   -X POST   -H "Content-Type: application/json"   -d '{"username": "JayDhi", "password": "DJayGoo"}'   http://localhost:8000/api/auth/token/obtain/
```

```
http http://127.0.0.1:8000/api/test/ "Authorization: Bearer [accesskey]"
```
#### 认证&权限
* ~~login_required~~
* 在基于函数的视图模式下@api_view与@permission_classes的组合
  ```python
  @api_view(['POST'])
  @permission_classes((IsAuthenticated,))
  ```

* Toke理解
  * Token应对的是这样一种情景:浏览器打开了2个标签页:```Tab A--> www.A.com```, ```Tab B-->WWW.B.com```, 用户在A完成了登录的操作, 而B是一个钓鱼网站, 假设B上的非法脚本
    ~~成功地读取到了用户的账号密码信息, 并且通过~~试图伪造请求的方式伪装成用户在A网站上执行操作, 而A网站对于登录的用户签发Token, 此时, 虽然B向A后台发送的请求与用户本人
    在A向A后台发送的请求一模一样, 但是由于A发送的请求带有Token, 因此B发送的虚假请求会被拦截
  * Token解决的问题不是账号在后台、前端，传输过程中的安全问题，这三个环节的数据安全有相应的模块保证, 而是在多标签页的情况下, 保证用户请求是由真正的标签页发送的
* 刷新Token
  * 刷新```token```以获得新的```token```的作用在于，持续保持活跃用户登录状态。比如通过用户密码获得的```token```有效时间为1小时，那么也就意味着1小时后此```token```失效，用户必须得重新登录，这对于活跃用户来说其实是多余的。如果这个用户在这1小时内都在浏览网站，我们不应该让用户重新登录，就是在```token```没有失效之前调用刷新接口为用户获得新的token。
* ```Token```与```UserSerializer```的组合
* ```Token get_user()```
* 注册时返回T```oken```, 自定义序列器, ```Pylint```报错
  ```
  No value for argument 'self' in function callpylint(no-value-for-parameter)
  ```
  代码如下:
  ```python
  class RegisterationSerializer(serializers.ModelSerializer):
    def create(self, **data):
        instance = user_model.objects.create(**data)
        token = get_token(instance=instance)
        return {instance, token}
    class Meta:
        model = user_model
        fields = ('username', 'password', )
  ```
    * ~~在serializer内返回token~~
      * ```python
        class AccountSerializer(serializers.ModelSerializer):
            token = serializers.SerializerMethodField()
            def create(self, data):
        # return user_model.objects.create_user(**data)
        instance = Account.objects.create(username=data["username"], password=data["password"])
        # instance.set_password(data['password'])
        # instance.save()
        token = get_token(instance)
        content = {
            "account": instance,
            "token": token,
        }
        return data"""
        class Meta:
            model = Account
            fields = ('username', )
        ```
        在POST的时候, SerializerMethodField()激活的get_xx(self, obj)中的obj是一个OrderedDict
    * 写两个view, 注册用的views会返回token
* ~~permission_classes实现各种权限~~
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

基于Group, User, Permission, Action的进阶使用

Permission <--> Action
通过Permission直接获取Action, 从而生成Menu, 而非通过Role中转, 需要自定义Permission/Group类
### asldkf