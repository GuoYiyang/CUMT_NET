from tkinter import *
from tkinter import ttk
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"'
)

def login():
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url='http://10.2.5.251/')
    xuehao = driver.find_element_by_xpath(
        '//*[@id="edit_body"]/div[2]/div/form/input[2]')
    xuehao.send_keys(e1.get())
    mima = driver.find_element_by_xpath(
        '//*[@id="edit_body"]/div[2]/div/form/input[3]')
    mima.send_keys(e2.get())
    if select_net == 0:
        yuyingshang = driver.find_element_by_xpath(
            '//*[@id="edit_body"]/div[2]/div/select/option[2]')
        yuyingshang.click()
    elif select_net == 1:
        yuyingshang = driver.find_element_by_xpath(
            '//*[@id="edit_body"]/div[2]/div/select/option[3]')
        yuyingshang.click()
    elif select_net == 2:
        yuyingshang = driver.find_element_by_xpath(
            '//*[@id="edit_body"]/div[2]/div/select/option[4]')
        yuyingshang.click()
    elif select_net == 3:
        yuyingshang = driver.find_element_by_xpath(
            '//*[@id="edit_body"]/div[2]/div/select/option[5]')
        yuyingshang.click()
    denglu = driver.find_element_by_xpath(
        '//*[@id="edit_body"]/div[2]/div/form/input[1]')
    denglu.click()

def logout():
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url='http://10.2.5.251/')
    zhuxiao = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div/form/input')
    zhuxiao.click()
    queren = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/input[1]')
    queren.click()

def handler(event):
    current = combobox.current()
    select_net = current


root = Tk()
root.title('CUMT_NET')
Label(root,text="账号:").grid(row=0,column=0,padx=10,pady=5)
Label(root,text="密码:").grid(row=1,column=0,padx=10,pady=5)
Label(root,text="运营商:").grid(row=2,column=0,padx=10,pady=5)

e1 = Entry(root)
e2 = Entry(root,show="*")
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)

select_net = 0
values=['校园网','中国移动','中国联通','中国电信']
combobox = ttk.Combobox(root, values=values)
combobox.bind('<<ComboboxSelected>>', handler)
combobox.grid(row=2,column=1,padx=10,pady=5)

Button(root,text="登录",command=login).grid(row=3,column=0,sticky="w",padx=10,pady=5)
Button(root,text="注销",command=logout).grid(row=3,column=1,sticky="e",padx=10,pady=5)

mainloop()