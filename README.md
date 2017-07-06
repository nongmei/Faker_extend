# Faker_extend
扩展Python Faker库，添加client provider，生成客户身份证号、银行卡等信息

# 安装方法
安装redis
`pip install redis`
安装faker
`pip install faker`
将providers文件夹下的内容拷贝到faker所在路径下的providers目录下

# 使用方法
from faker import Faker
fake = Faker('zh_CN')
c = fake.client()
print c

>>>
{
'phone_number': u'15971223764',         #手机号码
'username': u'gang15',                  #网络用户名，字母和数字组合
u'bank_code': u'03030000',              #银行机构代码
'name': u'\u84dd\u6797',                #中文姓名
u'bank_name': u'\u5149\u5927\u94f6\u884c',  #银行名称
u'card_bin': u'623158',                     #卡bin值
'residence': u'\u79c0\u82b3\u5e02\u6df3\u8857B\u5ea7 556608',   #
'company': u'\u98de\u5229\u4fe1\u4f20\u5a92\u6709\u9650\u516c\u53f8',       #中文公司名称
'current_location': (Decimal('-65.4467245'), Decimal('-47.206933')),        #地理位置
'birthdate': '1992-04-08',                                                  #生日
'sex': 'M',                                                                 #性别
u'card_type': u'\u501f\u8bb0\u5361',                                        #银行卡类型
'id_number': '440402196002254930',                                          #身份证号
'job': 'Lawyer',                                                            #工作
'address': u'\u658c\u5e02\u8861\u8defJ\u5ea7 629796',                       #地址
'mail': u'gyi@yahoo.com',                                                   #邮箱
u'card_name': u'\u8054\u540dIC\u5361\u767d\u91d1\u5361',                    #银行卡名称
u'card_number': u'6200850731104341483'                                      #银行卡号
} 
