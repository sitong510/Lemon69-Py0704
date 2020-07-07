import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")
from Exercise.R_W_case import read_data
from Exercise.http_request import http_request
from Exercise.R_W_case import write_data
Token=None
def run(file_name,sheet_name,c1,c2):   #c1代表测试用例执行的实际结果，c2代表Pass或Fail
    global Token  #声明函数外的Token和函数内的Token是同一个值
    all_data=read_data(file_name,sheet_name)
    print("所有的测试数据：",all_data)
    for test_data in all_data:
        ip="http://120.78.128.25:8766"
        response = http_request(ip + test_data[4], eval(test_data[5]), token= Token, method=test_data[3])
        if 'login' in test_data[4]:  #登录用例
            Token="Bearer " + response['data']['token_info']['token']
        print("最后的结果值：",response)

        #测试结果写回Excel
        write_data(file_name,sheet_name,test_data[0]+1,c1,str(response))  #调用函数
        #判断期望值与实际值是否相等
        actual={'code':response['code'],'msg':response['msg']}
        if eval(test_data[6])==actual:
            print("测试通过")
            write_data(file_name,sheet_name,test_data[0]+1,c2,'Pass')
        else:
            print("测试未通过")
            write_data(file_name,sheet_name,test_data[0]+1,c2,'Fail')
run('Mycase.xlsx','recharge',8,9)
