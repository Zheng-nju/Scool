# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:44:46 2020

@author: Flora
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:25:28 2019

@author: Flora
"""
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

import time

from selenium.webdriver.support.ui import Select
import math

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
# chromedriver的绝对路径
driver_path = r'C:\Users\Flora\Anaconda3\Scripts\chromedriver.exe'#（改路径）

# 初始化一个driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)

"""循环1：循环国家中35所学校的地址""" 
#'AllField=Affiliation%3A%28Columbia%29&ContribAffiliationId=10.1145%2Finstitution-60030162',   
US=['AllField=Affiliation%3A%28+Bonn%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60007493','AllField=Affiliation%3A%28Dresden%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60018353','AllField=Affiliation%3A%28Stuttgart%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60015815','AllField=Affiliation%3A%28T%C3%BCbingen%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60017246','AllField=Affiliation%3A%28G%C3%B6ttingen%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60031514','AllField=Affiliation%3A%28Passau%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60014151','AllField=Affiliation%3A%28Free%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60030718','AllField=Affiliation%3A%28Potsdam%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60021763','AllField=AllField%3A%28Ruhr%29+AND+Affiliation%3A%28Bochum%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60005322','AllField=Affiliation%3A%28Hamburg%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60028229','AllField=Affiliation%3A%28Humboldt%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60000762','AllField=Affiliation%3A%28Ulm%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60010586','AllField=Affiliation%3A%28W%C3%BCrzburg%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60012689','AllField=Affiliation%3A%28Bielefeld%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60015595','AllField=Affiliation%3A%28Bremen%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60008293','AllField=Affiliation%3A%28Duisburg-Essen%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60014264','AllField=Affiliation%3A%28Kaiserslautern%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60009941','AllField=Affiliation%3A%28Konstanz%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60025525','AllField=Affiliation%3A%28Hannover%29+AND+Affiliation%3A%28Leibniz%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60004935','AllField=Affiliation%3A%28M%C3%BCnster%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60000401','AllField=Affiliation%3A%28Braunschweig%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60007902','AllField=Affiliation%3A%28Dortmund%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60032991','AllField=Affiliation%3A%28Ilmenau%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60030040','AllField=Affiliation%3A%28Goethe%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60007762','AllField=Affiliation%3A%28Chemnitz%29&startPage=&ContribAffiliationId=10.1145%2Finstitution-60008069']
#UK=['',]
for i in range(0,36):
    """循环2：循环年份"""
    for j in range(2000,2019,5):
        driver.get("https://dl.acm.org/action/doSearch?fillQuickSearch=false&ConceptID=118290&expand=all&AfterYear="+str(j)+"&BeforeYear="+str(j+4)+"&"+US[i]+"&pageSize=50&startPage=&sortBy=Ppub_asc")
        """循环3：循环文献页数"""
        element= driver.find_element_by_class_name('hitsLength').text
        """这里是把数字变成正儿八经的数字"""
        a=element.replace(',','')
        b=int(a)
        c=math.ceil(b/50)
        for k in range(0,c):
# 请求网页
            driver.get("https://dl.acm.org/action/doSearch?fillQuickSearch=false&ConceptID=118290&expand=all&AfterYear="+str(j)+"&BeforeYear="+str(j+4)+"&"+US[i]+"&pageSize=50&startPage="+str(k)+"&sortBy=Ppub_asc")
            time.sleep(1)
            ele=WebDriverWait(driver,15,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,'item-results__checkbox')))
            
            """定位到要悬停的元素,这里是选择那个框框""" 
# element= driver.find_element_by_css_selector('div.item-results__checkbox>span')
            element= driver.find_element_by_class_name('item-results__checkbox')
            driver.execute_script("arguments[0].click();", element)
# 向下翻页至出现所需元素
# ele = element[0]
# driver.execute_script("arguments[0].scrollIntoView();",ele)

# time.sleep(2)

#对定位到的元素执行鼠标悬停操作
            ActionChains(driver).move_to_element(element).perform()
# 点击
            element.click()
            time.sleep(2)
            """这里是点击那个下载的灰色按钮"""
# element= driver.find_element_by_css_selector('a.btn light export-citation>i').click()
            #ele=WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,'icon-export')))
            element= driver.find_element_by_class_name('icon-export')
            element.click()
            time.sleep(4)            

            """这里是下拉框选择endnote格式"""
            #ele=WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,'citation-format')))
            select = Select(driver.find_element_by_id("citation-format"))
            select.select_by_visible_text("EndNote")
            time.sleep(5)

            """这里是点击下载按钮"""
# element= driver.find_element_by_css_selector('a.download__btn>i')
            #ele=WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,'icon-Icon_Download')))
            eles=WebDriverWait(driver,15,0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,'icon-Icon_Download')))
            element=driver.find_element_by_class_name('icon-Icon_Download')            
            element.click()
            time.sleep(2)
            
"""这里是点击关闭页面"""            
driver.close()



