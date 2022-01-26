# from __future__ import print_function
# import time
# import douyin_open/Oauth2UserToken
# from douyin_open/Oauth2UserToken.rest import ApiException
# from pprint import pprint
#
# # create an instance of the API class
# api_instance = douyin_open/Oauth2UserToken.OauthCodeApi()
# client_key = 'client_key_example' # str | 应用唯一标识
# response_type = 'code' # str | 设置为'code'这个字符串即可
# scope = 'scope_example' # str | 应用授权作用域,多个授权作用域以英文逗号（,）分隔
# redirect_uri = 'redirect_uri_example' # str | 授权成功后的回调地址，必须以http/https开头。域名必须对应申请应用时填写的域名，如不清楚请联系应用申请人。
# state = 'state_example' # str | 用于保持请求和回调的状态 (optional)
#
# try:
#     # 获取授权码(code)
#     api_instance.platform_oauth_connect_get(client_key, response_type, scope, redirect_uri, state=state)
# except ApiException as e:
#     print("Exception when calling OauthCodeApi->platform_oauth_connect_get: %s\n" % e)