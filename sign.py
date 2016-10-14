"""
# make verify sign string whit key
# author:mr.glt
# e-mail:mr.glt@ghostasm.com
# test:
test = {'qwe':'2','fds':'1','zxc':'3','iuy':{'c':'123','ee':[1,2,3],'ttt':{'ppp':'asdasd'},'ddd':{'fff':123123,'a':321321,'b':{'ooo':{'yyy':123123}}}}}
print make_verify_str(test,"IM_A_KEY")

result:
fds=1&iuy={"c":"123","ddd":{"a":321321,"b":{"ooo":{"yyy":123123}},"fff":123123},"ee":[1,2,3],"ttt":{"ppp":"asdasd"}}&qwe=2&zxc=3&key=IM_A_KEY
"""

def make_verify_str(obj,v_key='',_type = 0):
    if _type==0:
        data = ''
        keys = sorted(obj.keys())   # 字典序排列
        for key in keys:
            if type(obj[key]) is dict:
                data += str(key)+'='
                data += make_verify_str(obj[key],'',1)
                data += '&'
            elif type(obj[key]) is list:
                data += str(key)+'='
                data += make_verify_str(obj[key],'',2)
                data += '&'
            else:
                data += str(key)+'='
                data += str(obj[key])
                data+= '&'
        return data+'key='+v_key
    elif _type==1:
        data = '{'
        keys = sorted(obj.keys())   # 字典序排列
        i=0
        for key in keys:
            if type(obj[key]) is dict:  # 字典
                data += '"'+str(key)+'":'
                data += make_verify_str(obj[key],'',1)
            elif type(obj[key]) is list:    # 列表
                data += '"'+str(key)+'":'
                data += make_verify_str(obj[key],'',2)
            elif type(obj[key]) is str:     # 字符串
                data += '"'+key+'":"'+str(obj[key])+'"'
            else:
                data += '"'+key+'":'+str(obj[key])
            i+=1
            if i < len(keys):
                data+=','
        data += '}'
        return data
    elif _type == 2:
        data = '['
        keys = sorted(obj)             # 字典序排列
        i=0
        for key in keys:
            if type(key) is dict:      # 字典
                data += make_verify_str(key,'',1)
            elif type(key) is list:    # 列表
                data += make_verify_str(key,'',2)
            elif type(key) is str:     # 字符串
                data +='"'+str(key)+'"'
            else:
                data +=str(key)
            i+=1
            if i < len(keys):
                data+=','
        data += ']'
        return data