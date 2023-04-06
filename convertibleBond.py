import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import csv

 
#集思录爬取可转债信息并筛选

 
def write_csv(data):
    # 1. 创建文件对象
    f = open('可转债.csv', 'w', encoding='utf-8', newline='')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    # 4. 写入csv文件内容
    for dat in data:
        csv_writer.writerow(dat)
    # 5. 关闭文件
    f.close()
 
def Thelogin2():#集思录获取可转债信息
    print("开始登录")
    print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    revise = {
        "胜达转债" : -5, #下修过2次
        "亚泰转债" : -3, #下修过
        "花王转债" : -5, #下修过2次
        "现代转债" : 10, # pb
        "天路转债" : 10, #pb
        "晨丰转债" : 3,  #不停的发不下修公告3
        "奥佳转债" : 2, #pb
        "凌钢转债" : 20, #pb
        "海环转债" : 4,  #pb+不下修公告
        "华源转债" : 1,  #pb
        "京源转债" : 0,
        "合兴转债" : 2, #pb
        "北陆转债" : 0,
        "宏丰转债" : -3, #下修过
        "百达转债" : 0,
        "博世转债" : 0,
        "鸿达转债" : 20, #PB限制下修20，最低73（CCC级）
        "山鹰转债" : 0,
        "皖天转债" : 0,
        "希望转2" : 0,
        "敖东转债" : 0,
        "友发转债" : 0,
        "海亮转债" : 0,
        "岩土转债" : 0,
        "中环转2" : 0,
        "龙大转债" : 0,
        "嘉美转债" : 0,
        "大禹转债" : 0,
        "远东转债" : 0,
        "洪城转债" : 0,
        "永安转债" : 0,
        "濮耐转债" : 0,
        "白电转债" : 0,
        "通22转债" : 0,
        "苏租转债" : 10, #pb
        "中金转债" : 10, #pb
        "现代转债" : 10, #pb
        "苏利转债" : 10, #pb
        "青农转债" : 20, #pb
        "江银转债" : 20, #pb
        "天路转债" : 10, #pb
        "东湖转债" : 20, #pb
        "张行转债" : 20, #pb
        "景兴转债" : 20, #pb
        "双箭转债" : 10, #pb不下修公告，换手率低
        "帝欧转债" : 20, #pb
        "苏农转债" : 20, #pb
        "利群转债" : 5,  #2023-11-03前暂不行使下修权利
        "贵燃转债" : -3, #下修过
        "孚日转债" : -3, #下修过
        "岭南转债" : -5, #下修过
        "无锡转债" : -5, #下修过
        "绿茵转债" : 3,  #不停的发不下修公告
        "鲁泰转债" : 1,  #下修严格且不公告
        "锦鸡转债" : -3, #下修过
        "大秦转债" : 35, #余额太大，换手率太低强赎只要满足转股价值120元的要求！！！PB0.8，无法下修波动非常小，108~112，才4个点，玩毛线
        "文科转债" : 26, #跌倒过80
        "正邦转债" : -5, #下修过
        "广汇转债" : 30, #2020-10-29已满足下修条件，且公司已经发出公告，2023-02-23前暂不行使下修权利！剩余3.71年是刚发行没多久发的公告这么骄傲的转债。虽然没有下修PB限制。剩余规模33.7亿，规模很大，历史最低价约70元左右，往下空间还很大（现在股价比当年最低点还低）	广汇转债
        "吉视转债" : 40, #之前下修过，但是现在下修不能破净剩余时间只有1年多一点了，很难了
        "鹰19转债" : 100,#优先山鹰
        "搜特转债" : -5, #下修过
        "金诚转债" : 0, 
        "九洲转2" : 0,
        "灵康转债" : 0,
        "豪能转债" : 0,
        "惠云转债" : 0,
        "汽模转2" : 0,
        "凯中转债" : -3, #下修过
        "耐普转债" : 1,  #不下修公告
        "朗科转债" : 1,  #不下修
        "泰福转债" : 0,
        "宏辉转债" : 0,  #换手率挺高
        "明电转债" : -3, #下修过
        "东风转债" : 0,
        "汇通转债" : 0,
        "奇精转债" : 4,  #不下修公告
        "正丹转债" : 2,  #不下修公告
        "国光转债" : 2,  #不下修
        "新星转债" : 0,
        "银微转债" : 0,
        "华阳转债" : 7,  #不下修2，波动小5
        "英力转债" : 1,  #不下修
        "永鼎转债" : -3, #下修过
        "城市转债" : 1,  #不下修
        "应急转债" : 1,  #不下修
        "中陆转债" : 1,  #不下修
        "科蓝转债" : 0,
        "永东转2" : 1,  #不下修
        "丰山转债" : 0,
        
              
    }
    
    wait_time = 180
    chrome_options = Options()
    # 这边的账号密码改成自己的账号密码！！！
    account = ''
    password1 = ''
 
    url =f'https://www.jisilu.cn/web/data/cb/list'
 
    # 增加无头（不打开浏览器）
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
 
    # 防止被网站识别（伪装）
    chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])
 
    #打开网页不加载图片
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
        }
    }
    chrome_options.add_experimental_option('prefs', prefs)
 
    browser = webdriver.Chrome(chrome_options = chrome_options)
    browser.get(url)#打开网址
    browser.maximize_window()#窗口最大化
    browser.implicitly_wait(5)
    time.sleep(1)#等待
    #点击登录按钮输入账号密码
    buttons1 = browser.find_elements_by_xpath('//button[@type="button"][1]')
    button1 = buttons1[0]
    browser.execute_script("arguments[0].click();", button1)
    time.sleep(0.5)
    #输入账号密码
    button2 = browser.find_element_by_xpath('//input[@name="user_name"]')
    browser.execute_script("arguments[0].click();", button2)
    button2.send_keys(account)#输入信息
    button3 = browser.find_element_by_xpath('//input[@name="password"]')
    browser.execute_script("arguments[0].click();", button3)
    button3.send_keys(password1)#输入信息
    time.sleep(0.5)
    #勾选同意
    button4 = browser.find_element_by_xpath('//span[@class="agree_text"]')
    browser.execute_script("arguments[0].click();", button4)
    #登录
    buttons2 = browser.find_elements_by_xpath('//a[@class="btn btn-jisilu"]')
    button5 = buttons2[0]
    browser.execute_script("arguments[0].click();", button5)
    browser.implicitly_wait(5)
 
    list_all = []
    list_code = []#可转债代码
    list_name = []#可转债名称
    list_compay = []#公司名称
    list_price = []#现价
    list_premium = []#溢价率
    list_remaininglife = []#剩余年限
    list_yield = []#税前收益率
    list_rating = []#评级
    list_size = []#剩余规模
    list_Turnover = []#换手率
    list_Convertible = []#转股价值
    list_pb = []#pb
    list_change = []#涨跌幅
    list_stock_change = []#正股涨跌幅
    
    #获取所有可转债的溢价率
    #buttonss2 = browser.find_elements_by_xpath('//span[contains(@title,"开始转股")] ')

    #for i in buttonss2:
    #    itext = i.text
    #    list_premium.append(itext)
    #print(list_premium)
    print("登录成功！")
    print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    #获取所有可转债的剩余年限、税前收益率、评级等信息
    buttonss3 = browser.find_elements_by_xpath('//td')
    print("find_elements_by_xpath！")
    print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    # define a dictionary to map index to list
    index_to_list = {
        3: list_code,
        4: list_name,
        5: list_price,
        6: list_change,
        8: list_compay,
        10: list_stock_change,
        11: list_pb,
        13: list_Convertible,
        14: list_premium,
        17: list_rating,
        25: list_remaininglife,
        26: list_size,
        28: list_Turnover,
        29: list_yield
    }
    
    # loop through the buttons and append to the corresponding list
    maxcnt=100000000
    #maxcnt=10
    column=30
    for i, button in enumerate(buttonss3):
        if i >= maxcnt * column:
            break
        index = i % column+1
        if index in index_to_list:
            index_to_list[index].append(button.text)

    print("集思录基础页信息已爬取完毕！")
    print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    
    dict_all = {}
    dict_all["转债代码"]=list_code
    dict_all["转债名称"]=list_name
    dict_all["现价"]=list_price
    dict_all["涨跌幅"]=list_change
    dict_all["公司名称"]=list_compay
    dict_all["正股涨跌"]=list_stock_change
    dict_all["评级"]=list_rating
    dict_all["溢价率"]=list_premium
    dict_all["税前收益"]=list_yield
    dict_all["剩余年限"]=list_remaininglife
    dict_all["剩余规模"]=list_size
    dict_all["转股价值"]=list_Convertible
    dict_all["换手率"]=list_Turnover
    dict_all["pb"]=list_pb
    
    list_columns = ["转债代码","转债名称","公司名称","现价","涨跌幅", "正股涨跌", "评级","溢价率","税前收益","剩余年限","剩余规模","转股价值","换手率", "pb"]
    df_data = pd.DataFrame(dict_all,columns = list_columns)
    
    #去除可交换可转债
    criteria11 = df_data['转债名称'].map(lambda x:'EB'not in x)
    df_data = df_data[criteria11]
    df_data['转债名称'] = df_data['转债名称'].str.strip('!')
    #去除快到期的可转债
    criteria22 = df_data['剩余年限'].map(lambda x:'-'not in x)
    df_data = df_data[criteria22]
    
    #将价格、剩余规模、赎回价和换手率转换为数值类型
    df_data.loc[:,['现价','剩余年限','转股价值','剩余规模']]= df_data.loc[:,['现价','剩余年限','转股价值','剩余规模']].apply(pd.to_numeric)
    
    df_data['溢价率'] = df_data['溢价率'].str.strip('%')
    df_data['溢价率'] = pd.to_numeric(df_data['溢价率'],errors = 'coerce')
    df_data['税前收益'] = df_data['税前收益'].str.strip('%')
    df_data['税前收益'] = pd.to_numeric(df_data['税前收益'],errors = 'coerce')
    df_data['换手率'] = df_data['换手率'].str.strip('%')
    df_data['换手率'] = pd.to_numeric(df_data['换手率'],errors = 'coerce')
    df_data['得分'] = 0

 
    #list1 = df_data.apply(judgee,axis = 1)
    #df_data['type'] = list1
    
    for row in df_data.index:
        price=df_data.loc[row]['现价']
        score=price+max(0, price-120)
        if df_data.loc[row]['剩余规模']>5:
            score += 200
        if df_data.loc[row]['剩余年限']<1:
            score += 200
        elif df_data.loc[row]['剩余年限']<1.5:
            score += 10
        if df_data.loc[row]['转股价值']>125:  #即将强赎
            score += 20
        if df_data.loc[row]['评级'].startswith("A") == False:
            score += 50
        premium = df_data.loc[row]['溢价率']
        premium = price - (price / (1 + premium*0.01))
        score += premium
        if (revise.get(df_data.loc[row]["转债名称"]) != None):
            score += revise[df_data.loc[row]["转债名称"]]
            df_data.loc[row, '修正'] = revise[df_data.loc[row]["转债名称"]]
        df_data.loc[row, '得分'] = score

    df_data=df_data.sort_values('得分')
    df_data = df_data.reset_index(drop=True)
    df_data.index = df_data.index + 1
    
    print("量化计算完成！")
    print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 5000)
    result = open(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+".txt", mode="a+", encoding="utf-8")
    print(df_data, file=result)
    result.close()
    import winsound
    winsound.Beep(1000, 500)

    #write_csv(df_data)
 
    time.sleep(1)#等待
    browser.close()#关闭当前网页
    browser.quit()#完全退出浏览器
    return df_data

    

while True:
    df_data = Thelogin2()





