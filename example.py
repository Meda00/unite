# coding: utf-8
import requests
import random
import re
from bs4 import BeautifulSoup
def pachou():
    content = requests.get('https://www.zhihu.com/').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
       print div.text.strip()

def demo_string():
    stra='hello,worlD '
    print stra.capitalize()
    print stra.replace('hello','newcode')
    ##替换
    strb=' \n\rhello newcoder \r\n'
    print 1,strb.lstrip()
    print 2,strb.rstrip()
    strc = 'hello w'
    print 3,strc.startswith('hel')
    print 4,strc.endswith('w')
    print 5, strc.endswith('h')
    print 6,stra+strb+strc
    print 7,len(strc)
    print 8,'-'.join(['a','b','c'])
    print 9,strc.split(' ')
    print 10,strc.find('ello')


def demo_operation():
    print 1, 1+ 2,5/2 ,5*2,5-2
    print 2,True,not True
    print 3,1<2 ,5>2
    print 4,2<<3
    print 5,5|3,5&3,5^2
    x=2
    y=3.3
    print x,y,type(y)
def demo_buildinfunction():
    print 1, max(2,1),min(5,3)
    print 1,len('xxx'),len([1,2,3])
    print 3,abs(-2)
    print 4,range(1,10,3)
    print 5,dir(list)
    x=2
    print 6,eval('x+3')
    print 7,chr(97),ord('a')
    print 8,divmod(5,3)

def demo_controlflow():
    score = 65
    if score>99:
        print 1,'A'
    elif score>60:
        print 2,'B'
    else:
        print 2,'C'

    while score <100:
        print score
        score +=10
    score =65

    for i in range(0,10):
        print 3,i
    for i in range(0, 10,2):
        print 3, i

    for i in range(0, 10,2):
        if i ==0:
             pass #do_specail
        if i<5:
            continue
        print 4,i
        if i == 8:
            break

def demo_list():
    lista=[1,2,3] #vector
    print 1,lista
    listb=['a','b',1.1]
    print 2,listb
    lista.extend(listb)
    print 3,lista
    print 4,len(lista)
    print 5,'a'in listb
    lista = lista+listb
    print 6,lista
    listb.insert(0,'www')
    print 7,listb
    listb.pop(1)
    print 8,listb
    listb.reverse()
    print 9,listb
    print 10,listb[0],listb[1]
    listb.sort()
    print 11, listb
    listb.sort(reverse=True)
    print 12, listb
    print 13,listb*2
    print 14,[0]*14
    tuplea = (1,2,3) #只读
    listaa = [1,2,3]
    listaa.append(4)
    print 15,listaa

def add(a,b):
    return a+b
def sub(a ,b):
    return a-b

def demo_dict():
    dicta={4:16,1:1,2:4,3:9}
    print 1,dicta
    print 2,dicta.keys(),dicta.values()
    print 3,dicta.has_key(1),dicta.has_key('3')
    # for map<int ,int >::iteraor it = x.begin():it !=x.end
    for key,value in dicta.items():
        print 'key_value',key, value
    dictb = {'+': add,'-':sub}
    print 4,dictb['+'](1,2)
    print 5,dictb.get('-')(15,3)
    dictb['*'] = 'x'
    print dictb
    dicta.pop(4)
    print 6,dicta
    del dicta[1]
    print 7,dicta

def demo_set():
    seta =set((1,2,3))
    setb = set((2,3,4))
    setc = set([1,2,3])
    lista= [1,2,3]
    setd = set(lista)
    print 0,setc
    print 00,setd
    print 1,seta
   # print 2, seta + setb  不能加
    seta.add(4)
    print 2,seta
    print 3,seta.intersection(setb)
    print 4,seta & setb
    print 5,seta|setb,seta.union(setb)
    print 6,seta-setb
    seta.add('x')
    print 6,seta
    print 7,len(seta)


#面向对象
class User:
    type = 'USER'

    def __init__(self,name,uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im '+self.name + '  '+str(self.uid)

class Admin(User):
    type = 'ADMIN'

    def __init__(self,name,uid,group):
       User.__init__(self,name,uid)
       self.group = group

    def __repr__(self):
        return 'im'+ self.name +' '+str(self.uid)+ ' '+self.group
class Guest(User):
    def __repr__(self):
        return 'im guest: ' + self.name



def create_user(type):
    if type=='USER':
        return User('u1',1)
    elif type =='ADMIN':
        return Admin('a1',101,'g1')
    else:
       return Guest('gu1',201)
       #raise ValueError('error')

def demo_exception():
    try:
        print 2 / 1
        #print 2 /0
        #if type == 'c':
        raise Exception('Raise Error','newcoder')
    except Exception as e:
        print 'error:',e
    finally :
        print 'clean up'

def demo_random():
    #random.seed(1)  #种子固定死随机
    #x = prex * 1000005 * xxxx
    # prex = x幂等性
    print 1, random.random()#0-1之间的浮点数
    print 2, random.random()*100 #0-100之间的随机数
    print 3, random.randint(0,200)
    print 4, random.choice(range(0,100,10))
    print 5, random.sample(range(0,100),4)
    a = [1,2,3,4,5,6]
    random.shuffle(a) #随机打乱
    print 6,a

'''
##############
            正则表达式
            \d\D\s\S\w\W
            + * ?
            | ^
            ()
            \
            ###############
'''

def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    p2 = re.compile('[\d]')
    p3 = re.compile('[\d]*')
    print p1.findall(str)
    print p2.findall(str)
    print p3.findall(str)
    str1 = 'as@163.com;b@gmail.com;e@163.com;zs@qq.com'
    p4 = re.compile('[\w]+@163\.com')
    print p4.findall(str1)
    p5= re.compile('[\w]+@163|@qq\.com')
    print p5.findall(str1)
    str2='<html><h>title</h><body>xxx</body></html>'
    p6= re.compile('<h>[^<]+</h>')
    print 6,p6.findall(str2)
    p7 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 7,p7.findall(str2)

    str3 = 'xx2016-06-11yy'
    p8 = re.compile('\d\d\d\d-\d\d-\d\d')
    print 8,p8.findall(str3 )
    p9 = re.compile('\d{4}-\d{2}-\d{2}')
    print 9, p9.findall(str3)

if __name__ == "__main__":
    '''
    user1 = User('u1',1)
    print user1
    admin1= Admin('a1',101,'g1')
    print admin1

    print create_user('USERX') 
    '''


    # print 'hello newcode'
    # demo_string()
    #demo_operation()
    #demo_buildinfunction()
    #demo_controlflow()
    #demo_list()
    #demo_dict()
    # demo_set()
    #demo_exception()
    #demo_random()
    demo_re()