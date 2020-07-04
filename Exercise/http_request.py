import requests
def http_request(url,data,token=None,method='post'):
    header={'X-Lemonban-Media-Type': 'lemonban.v2',
            'Authorization': token}
    if method=='get':
        result=requests.get(url,json=data,headers=header)
    else:
        result=requests.post(url,json=data,headers=header)
    return result.json()
if __name__ == '__main__':
    reg_url='http://120.78.128.25:8766/futureloan/member/register'
    reg_data={'mobile_phone':15523469707,'pwd':'123456789'}
    login_url='http://120.78.128.25:8766/futureloan/member/login'
    login_data={'mobile_phone':15523469707,'pwd':'123456789'}
    response=http_request(login_url,login_data)   #登录返回的json结果
    token=response['data']['token_info']['token']
    rec_url = 'http://120.78.128.25:8766/futureloan/member/recharge'
    rec_data = {'member_id': 199182, 'amount': '17'}
    wit_url = 'http://120.78.128.25:8766/futureloan/member/withdraw'
    wit_data = {'member_id': 199182, 'amount': '7'}
    print(http_request(rec_url,rec_data,"Bearer "+ token))