import socket

def liandui(s,m,n):
    a=list(set(s))
    a.sort()
    L=list(s)
    if len(a)==m:#牌的种类
        b=0
        for x in a:
            if L.count(x)==n:#牌的数目
                b+=1
        if b==m:
            if (ord(a[-1])-ord(a[0]))==(m-1):
                return (m,n)

def sandaiyi(s,m):
    L=[]
    a=list(set(s))
    b=0
    for x in a:
        if s.count(x)==m:#牌的数目
            b+=1
            L.append(x)
    L.sort()
    if len(L)>=1:
        if len(a)>1 and b==(len(a)-b) and ord(L[-1])-ord(L[0])==(b-1):
            return m*10+1

def sandaier(s,m):
    L=[]
    a=list(set(s))
    b=c=0
    for x in a:
        if s.count(x)==m:
            b+=1
            L.append(x)
    L.sort()
    for x in a:
        if s.count(x)==2:
            c+=1
    if len(L)>=1:
        if len(s)>1 and ord(L[-1])-ord(L[0])==(b-1):
            if b==c:
                return m*10+2
            elif len(s)-b*4==b*2:
                return m*10+2

def zhadan(chupai):
    if len(set(chupai))*4==len(chupai):
        return 99


def shunzi(s):
    a=list(set(s))
    a.sort()
    if len(a)==len(s) and (ord(a[-1])-ord(a[0]))==(len(a)-1):
        return 666

def one_b(chupai,data):
    if chupai>data.split()[1][:-2]:
        return 888

def sandaiyi_b(chupai,data,g):
    for x in chupai:
        if chupai.count(x)==g:
            for y in data.split()[1][:-2]:
                if data.split()[1][:-2].count(y)==g:
                    if x>y:
                        return 888

def guize_b(chupai,data):
    if len(chupai)==1:#一
        return one_b(chupai,data)
    elif len(chupai)==2:#一对
        if liandui(chupai,1,2)==(1,2):#一对
            return one_b(chupai,data)
    elif len(chupai)==3:#三个
        if liandui(chupai,1,3)==(1,3):#三个
            return one_b(chupai,data)
    elif len(chupai)==4:
        if sandaiyi(chupai,3)==31:
            return sandaiyi_b(chupai,data,3)
    elif len(chupai)==5:
        if sandaier(chupai,3)==32:
            return sandaiyi_b(chupai,data,3)
        elif sandaiyi(chupai,4)==41:
            return sandaiyi_b(chupai,data,4)
        elif shunzi(chupai)==666:
            return one_b(chupai,data) 
    elif len(chupai)==6:
        if liandui(chupai,3,2)==(3,2):#一对#3连对
            return one_b(chupai,data)
        elif liandui(chupai,2,3)==(2,3):#三
            return one_b(chupai,data)
        elif sandaier(chupai,4)==42:
            return sandaiyi_b(chupai,data,4)
        elif shunzi(chupai)==666:
            return one_b(chupai,data)
    elif len(chupai)==7:
        if shunzi(chupai)==666:
            return one_b(chupai,data) 
    elif len(chupai)==8:
        if liandui(chupai,4,2)==(4,2):#一对#4连对
            return one_b(chupai,data)
        elif sandaiyi(chupai,3)==31:
            return sandaiyi_b(chupai,data,3)
        elif liandui(chupai,2,4)==(2,4):
            return one_b(chupai,data)
        elif shunzi(chupai)==666: 
            return one_b(chupai,data)
        elif sandaier(chupai,4)==42:
            return sandaiyi_b(chupai,data)
    elif len(chupai)==9:
        if liandui(chupai,3,3)==(3,3):#三个
            return one_b(chupai,data)
        elif shunzi(chupai)==666: 
            return one_b(chupai,data)
    elif len(chupai)==10:
        if liandui(chupai,5,2)==(5,2):#一对#连对
            return one_b(chupai,data)
        elif sandaier(chupai,3)==32:
            return sandaiyi_b(chupai,data,3)
        elif sandaiyi(chupai,4)==41:
            return sandaiyi_b(chupai,data,4)
        elif shunzi(chupai)==666:
            return one_b(chupai,data)
    elif len(chupai)==11:
        if shunzi(chupai)==666:
            return one_b(chupai,data) 
    elif len(chupai)==12:
        if liandui(chupai,6,2)==(6,2):#一对#连对
            return one_b(chupai,data)
        elif liandui(chupai,4,3)==(4,3):#三个
            return one_b(chupai,data)
        elif sandaiyi(chupai,3)==31:
            return sandaiyi_b(chupai,data,3)
        elif sandaier(chupai,4)==42:#两个4带一
            return sandaiyi_b(chupai,data,4)
        elif shunzi(chupai)==666:
            return one_b(chupai,data)
    elif len(chupai)==13:
        if shunzi(chupai)==666:
            return one_b(chupai,data) 
    elif len(chupai)==14:
        if liandui(chupai,7,2)==(7,2):#一对#连对 
            return one_b(chupai,data)
    elif len(chupai)==15:
        if sandaier(chupai,3)==32:
            return sandaiyi_b(chupai,data,3)
        elif sandaiyi(chupai,4)==41:
            return sandaiyi_b(chupai,data,4)
        elif liandui(chupai,5,3)==(5,3):
            return one_b(chupai,data)
    elif len(chupai)==16:
        if liandui(chupai,8,2)==(8,2):#一对#连对
            return one_b(chupai,data)
        elif sandaiyi(chupai,3)==31:
            return sandaiyi_b(chupai,data,3)
    elif len(chupai)==18:
        if liandui(chupai,9,2)==(9,2):#一对#连对
            return one_b(chupai,data)
        elif sandaier(chupai,4)==42:
            return sandaiyi_b(chupai,data,4)
        elif liandui(chupai,6,3)==(6,3):
            return one_b(chupai,data)
    elif len(chupai)==20:
        if liandui(chupai,10,2)==(10,2):#一对#连对
            return one_b(chupai,data)
        elif sandaiyi(chupai,3)==31:
            return sandaiyi_b(chupai,data,3)
        elif sandaier(chupai,3)==32:
            return sandaiyi_b(chupai,data,3)
        elif sandaiyi(chupai,4)==41:
            return sandaiyi_b(chupai,data,4)
    else:
        print('输入有误请重新输入')



def guize(chupai):
    if len(chupai)==1:#一
        return '10'
    elif len(chupai)==2:#一对
        if liandui(chupai,1,2)==(1,2):#一对
            return '11'
        elif chupai=='op' or chupai=='po':
            return '95'
        else:
            return '0'
    elif len(chupai)==3:#三个
        if liandui(chupai,1,3)==(1,3):#三个
            return '12'
        else:
            return '0'
    elif len(chupai)==4:
        if sandaiyi(chupai,3)==31:
            return '13'
        elif zhadan(chupai)==99:
            return '94'
        else:
            return '0'
    elif len(chupai)==5:
        if sandaier(chupai,3)==32:
            return '15'
        elif sandaiyi(chupai,4)==41:
            return '16'
        elif shunzi(chupai)==666:
            return '17'
        else:
            return '0' 
    elif len(chupai)==6:
        if liandui(chupai,3,2)==(3,2):#一对#3连对
            return '18'
        elif liandui(chupai,2,3)==(2,3):#三
            return '19'
        elif sandaier(chupai,4)==42:
            return '20'
        elif shunzi(chupai)==666:
            return '21'
        else:
            return '0'
    elif len(chupai)==7:
        if shunzi(chupai)==666:
            return '22'
        else:
            return '0' 
    elif len(chupai)==8:
        if liandui(chupai,4,2)==(4,2):#一对#4连对
            return '23'
        elif sandaiyi(chupai,3)==31:
            return '24'
        elif shunzi(chupai)==666: 
            return '26'
        elif sandaier(chupai,4)==42:
            return '27'
        elif zhadan(chupai)==99:
            return '96'
        else:
            return '0'
    elif len(chupai)==9:
        if liandui(chupai,3,3)==(3,3):#三个
            return '28'
        elif shunzi(chupai)==666: 
            return '29'
        else:
            return '0'
    elif len(chupai)==10:
        if liandui(chupai,5,2)==(5,2):#一对#连对
            return '30'
        elif sandaier(chupai,3)==32:
            return '31'
        elif sandaiyi(chupai,4)==41:
            return '32'
        elif shunzi(chupai)==666:
            return '33'
        else:
            return '0'
    elif len(chupai)==11:
        if shunzi(chupai)==666:
            return '34'
        else:
            return '0' 
    elif len(chupai)==12:
        if liandui(chupai,6,2)==(6,2):#一对#连对
            return '35'
        elif sandaiyi(chupai,3)==31:
            return '37'
        elif sandaier(chupai,4)==42:
            return '38'
        elif shunzi(chupai)==666:
            return '40'
        elif zhadan(chupai)==99:
            return '97'
        else:
            return '0'
    elif len(chupai)==13:
        if shunzi(chupai)==666:
            return '42'
        else:
            return '0'
    elif len(chupai)==14:
        if liandui(chupai,7,2)==(7,2):#一对#连对 
            return '43'
        else:
            return '0'
    elif len(chupai)==15:
        if sandaier(chupai,3)==32:
            return '44'
        elif sandaiyi(chupai,4)==41:
            return '45'
        elif liandui(chupai,5,3)==(5,3):
            return '46'
        else:
            return '0'
    elif len(chupai)==16:
        if liandui(chupai,8,2)==(8,2):#一对#连对
            return '47'
        elif sandaiyi(chupai,3)==31:
            return '48'
        elif zhadan(chupai)==99:
            return '98'
        else:
            return '0'
    elif len(chupai)==18:
        if liandui(chupai,9,2)==(9,2):#一对#连对
            return '50'
        elif sandaier(chupai,4)==42:
            return '51'
        elif liandui(chupai,6,3)==(6,3):
            return '52'
        else:
            return '0'
    elif len(chupai)==20:
        if liandui(chupai,10,2)==(10,2):#一对#连对
            return '53'
        elif sandaiyi(chupai,3)==31:
            return '54'
        elif sandaier(chupai,3)==32:
            return '55'
        elif sandaiyi(chupai,4)==41:
            return '56'
        elif liandui(chupai,5,4)==(5,4): 
            return '57'
        elif zhadan(chupai)==99:
            return '99'
        else:
            return '0'
    else:
        return '0' 


def yanpai(chupai,shoupai):
    for x in chupai:
        if x not in shoupai or chupai.count(x)>shoupai.count(x):
            return
    else:
        return 7777

def jieshou(a,lishi,shoupai1,b):
    global data
    data=a.recv(1024).decode()
    if data=='1win' or data=='1lose':
        print(data[1:])
        while True:  
            ccccc=input('请输入0继续,1退出')
            if ccccc!='0' and ccccc!='1':
                continue
            else:
                break
        if ccccc=='0':
            main()
        else:
            exit()
    else:
        lishi.insert(0,data)
        print()
        print(data.split()[2],pipei(zhuanbian(data.split()[1][:-2])),data.split()[0][1:])
        print()
        print(b,pipei(shoupai1))

def user_input():
    while True: 
        x = input('请输入0继续,1退出')
        if x in ["0","1"]:
            return x
        

def jiesou(a,lishi,shoupai1,b):
    global data
    data=a.recv(1024).decode()
    if data=='1win' or data=='1lose':
        print(data[1:])
        while True:  
            ccccc=input('请输入0继续,1退出')
            if ccccc!='0' and ccccc!='1':
                continue
            else:
                break
        if ccccc=='0':
            main()
        else:
            exit()
    else:
        lishi.insert(0,data)
        print()
        print(data.split()[2],pipei(zhuanbian(data.split()[1][:-2])),data.split()[0][1:])
        print()
        print(b,pipei(shoupai1))
        return 'break'

def pipei(liebiao):#把列表加进去出来图像  a1和a不匹配
    color = ['\u2660 ','\u2663 ','\u2665 ','\u2666 ']
    number=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    pokers = [c+' '+n for c in color for n in number]+['小鬼','大王','不要']
    L,L1,L2=[],[],[]
    v=''
    b=1
    for y in range(4):
        for x in range(97,110):
            v=chr(x)+str(b)
            L.append(v)
            b+=1
            if b == 5:
                b=1
            v=''
    for x in range(ord('o'),ord('p')+1):
        L.append(chr(x))
    L.append('z')
    zidian=dict(zip(L,pokers))
    for x in liebiao:
        L2.append(zidian[x])
    return L2


def zhuanma(liebiao1):#把输入数据转换为系统数据字符串
    try:
        L,L1=['3','4','5','6','7','8','9','10','j','q','k','a','2','w','W','z'],[]
        f=''
        f10=''
        for x in range(97,110):
            L1.append(chr(x))
        for x in range(111,113):
            L1.append(chr(x))
        L1.append('z')
        a=dict(zip(L,L1))
        for x in liebiao1:
            if x=='1':
                f10+='1'
                continue
            if x=='0' and f10=='1':
                f+=a['10']
                f10=''
                continue
            if f10=='1' and x!='0':
                return '出牌规则错误'
            f+=a[x]
            f10=''
        return f
    except KeyError:
        return '出牌规则错误'
def zhuanma1(liebiao):#获取系统所需列表字符类型,获取展示手牌源码
    L=[]
    for x in liebiao:
        L.append(x[0])
    return L

def peidui(s,s1,c):#获取转发字符
    zifu=''
    for x in c:
        if x=='z':
            return 'z'
        zifu+=str(s1[s.index(x)])
        s1.remove(s1[s.index(x)])
        s.remove(x)
    return zifu

def zhuanbian(a):#把接受过来的字符串转变成可以匹配的列表
    L=[]
    f=''
    for x in a:
        if x == 'p' or x == 'o' or x == 'z':
            L.append(x)
        else:
            f+=x
            if len(f)==2:
                L.append(f)
                f='' 
    return L

def main():
    global data                    
    lishi=[]
    a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    a.connect(('176.130.2.154',10010))
    a.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    while True:
        b=input('按0准备')
        if b!='0':
            continue
        else:
            break
    a.send(b.encode())
    n=2 
    data=b'1'
    while True: 
        if data.decode()=='农夫' or n=='1' :
            break
        data=a.recv(1024)
        if data.decode()=='农夫':
            print(data.decode())
            break
        else:
            shoupai,shoupai1,sanzhang=[],[],[]
        if data.decode()[0]=='[':
            for x in eval(data.decode()):
                shoupai1.append(x)
            for x in zhuanma1(eval(data.decode())):
                shoupai.append(x)
            print(pipei(eval(data.decode())))#手牌
        while True:
            data=a.recv(1024)
            if data.decode()=='请选地主':
                print(data.decode())
                while True:
                    n=input("输入0放弃，输入1确定")
                    if n not in ["0","1"]:
                        continue
                    else:
                        break 
                a.send(n.encode())
                if n=='1':
                    data=a.recv(1024)
                    sanzhang.append(pipei(eval(data.decode())))
                    # print(pipei(eval(data.decode())))
                    for x in eval(data.decode()):
                        shoupai1.append(x)
                    for x in zhuanma1(eval(data.decode())):
                        shoupai.append(x)
                    break
                elif n=='0':
                    break   
            elif data.decode()=='农夫':
                print(data.decode())
                break

    shoupai.sort()
    shoupai1.sort()
    print(sanzhang)
    print(pipei(shoupai1))
    while True:
        if len(shoupai)==20:
            shenfen='地主'
            chupai=input('请出牌')
            chupai=zhuanma(chupai)
            if yanpai(chupai,shoupai)==7777:
                if type(guize(chupai))==str and guize(chupai)!='0':
                    chupai1=peidui(shoupai,shoupai1,chupai)
                    a.send((str(len(shoupai))+' '+chupai1+guize(chupai)+' '+shenfen).encode())
                    jieshou(a,lishi,shoupai1,shenfen)
                    break
                else:
                    continue
        else:
            shenfen='农夫'
            jieshou(a,lishi,shoupai1,shenfen)
            break

    while True:
        if data[0]=='0':
            for x in lishi:
                if x.split()[1][:-2]=='z':
                    pass
                else:
                    data=x
                    print(data.split()[2],pipei(zhuanbian(data.split()[1][:-2])),data.split()[0][1:])
                    print()
                    print(b,pipei(shoupai1))
                    break
            if lishi[0].split()[1][:-2]=='z' and lishi[1].split()[1][:-2]=='z':
                while True:
                    chupai=input('请出牌')
                    chupai=zhuanma(chupai)
                    if yanpai(chupai,shoupai)==7777:
                        chupai1=peidui(shoupai,shoupai1,chupai)
                        a.send((str(len(shoupai))+' '+chupai1+guize(chupai)+' '+shenfen).encode())
                        if jiesou(a,lishi,shoupai1,shenfen)=='break':
                            break
            else:            
                while True:
                    print(data)
                    chupai=input('请出牌')
                    chupai=zhuanma(chupai)
                    if yanpai(chupai,shoupai)==7777:
                        if guize(chupai)==data.split()[1][-2:] and guize_b(chupai,data)==888:
                            chupai1=peidui(shoupai,shoupai1,chupai)
                            a.send((str(len(shoupai))+' '+chupai1+guize(chupai)+' '+shenfen).encode())
                            if jiesou(a,lishi,shoupai1,shenfen)=='break':
                                break 
                        elif guize(chupai)>'90' and guize(chupai)>=data.split()[1][-2:]:
                            if guize(chupai)==data.split()[1][-2:]:
                                if max(chupai)>max(data.split()[1][:-2]):
                                    chupai1=peidui(shoupai,shoupai1,chupai)
                                    a.send((str(len(shoupai))+' '+chupai1+guize(chupai)+' '+shenfen).encode()) 
                                    if jiesou(a,lishi,shoupai1,shenfen)=='break':
                                        break
                            else:
                                chupai1=peidui(shoupai,shoupai1,chupai)
                                # quchu(chupai,shoupai)
                                a.send((str(len(shoupai))+' '+chupai1+guize(chupai)+' '+shenfen).encode())
                                if jiesou(a,lishi,shoupai1,shenfen)=='break':
                                    break         
                    elif chupai=='z':
                        a.send((str(len(shoupai))+' '+chupai+guize(chupai)+' '+shenfen).encode())
                        if jiesou(a,lishi,shoupai1,shenfen)=='break':
                            break

        elif data[0]=='1':
            jieshou(a,lishi,shoupai1,shenfen)    

main()          








