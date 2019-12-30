import sqlite3
from tkinter import *
from tkinter import ttk
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'
)



#登录
def login():
    c.execute('update user set id=?, pass=?',(str(e1.get()),str(e2.get())))
    c.execute('select * from user')
    row = c.fetchone()
    select_net = row[2]
    print(select_net)
    print(str(e1.get()))
    print(str(e2.get()))
    print('正在登陆！')
    conn.commit()


    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url='http://10.2.5.251/')
    xuehao = driver.find_element_by_xpath(
        '//*[@id="edit_body"]/div[2]/div/form/input[2]')
    xuehao.send_keys(e1.get())
    time.sleep(1)
    mima = driver.find_element_by_xpath(
        '//*[@id="edit_body"]/div[2]/div/form/input[3]')
    time.sleep(1)
    mima.send_keys(e2.get())
    if select_net == 0:
        yuyingshang = driver.find_element_by_xpath(
            '//*[@id="edit_body"]/div[2]/div/select/option[2]')
        time.sleep(1)
        yuyingshang.click()
    elif select_net == 1:
        yuyingshang = driver.find_element_by_xpath(
            '//*[@id="edit_body"]/div[2]/div/select/option[3]')
        time.sleep(1)
        yuyingshang.click()
    elif select_net == 2:
        yuyingshang = driver.find_element_by_xpath(
            '//*[@id="edit_body"]/div[2]/div/select/option[4]')
        time.sleep(1)
        yuyingshang.click()
    elif select_net == 3:
        yuyingshang = driver.find_element_by_xpath(
            '//*[@id="edit_body"]/div[2]/div/select/option[5]')
        time.sleep(1)
        yuyingshang.click()
    denglu = driver.find_element_by_xpath(
        '//*[@id="edit_body"]/div[2]/div/form/input[1]')
    time.sleep(1)
    denglu.click()


#注销
def logout():
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url='http://10.2.5.251/')
    zhuxiao = driver.find_element_by_xpath(
        '//*[@id="edit_body"]/div[2]/div/form/input')
    zhuxiao.click()
    queren = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/form/input[1]')
    queren.click()


def handler(event):
    current = combobox.current()
    select_net = current
    c.execute('update user set net = ?',(select_net,))
    conn.commit()
    


#图形界面
root = Tk()
root.title('CUMT_NET')
#标签
Label(root, text="账号:").grid(row=0, column=0, padx=10, pady=5)
Label(root, text="密码:").grid(row=1, column=0, padx=10, pady=5)
Label(root, text="运营商:").grid(row=2, column=0, padx=10, pady=5)
#输入
conn = sqlite3.connect('cumt_net.db')
c = conn.cursor()
c.execute('select * from user')
row = c.fetchone()
if row :
    default_xuehao = StringVar(value=row[0])
    default_mima = StringVar(value=row[1])
    select_net = row[2]
else:
    default_xuehao = StringVar(value="")
    default_mima = StringVar(value="")
    select_net = 0
e1 = Entry(root, textvariable=default_xuehao)
e2 = Entry(root, textvariable=default_mima)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
#选择框
values = ['校园网', '中国移动', '中国联通', '中国电信']
combobox = ttk.Combobox(root, values=values)
combobox.current(int(select_net))
combobox.bind('<<ComboboxSelected>>', handler)
combobox.grid(row=2, column=1, padx=10, pady=5)


#按钮
Button(root, text="登录", command=login).grid(row=3,
                                            column=0,
                                            sticky="w",
                                            padx=10,
                                            pady=5)
Button(root, text="注销", command=logout).grid(row=3,
                                             column=1,
                                             sticky="e",
                                             padx=10,
                                             pady=5)

mainloop()
c.close()
conn.close()
if __name__ == "__main__":
    pass
