# -*- coding: utf-8 -*-
 
import time
import json
import xmltodict
import re

def task0():
    days = {"days": {"thursday": {"tr": []} }}
    with open('info.xml', mode='r', encoding='utf-8') as f:
        allInfo = f.read()
        while "tr" in allInfo:
            newObj = {
                    "time": {
                        "hours": "",
                        "weeks": ""
                    },
                    "room": {
                        "aud": "",
                        "address": ""
                    },
                    "lesson": {
                        "title": "",
                        "teacher": ""
                    },
                    "lesson-format": ""
                }
            newObj["time"]["hours"] = allInfo[allInfo.find("<hours>")+7:allInfo.find("</hours>")]
            newObj["time"]["weeks"] = allInfo[allInfo.find("<weeks>")+7:allInfo.find("</weeks>")]
            newObj["room"]["aud"] = allInfo[allInfo.find("<aud>")+5:allInfo.find("</aud>")]
            newObj["room"]["address"] = allInfo[allInfo.find("<address>")+9:allInfo.find("</address>")]
            newObj["lesson"]["title"] = allInfo[allInfo.find("<title>")+7:allInfo.find("</title>")]
            newObj["lesson"]["teacher"] = allInfo[allInfo.find("<teacher>")+9:allInfo.find("</teacher>")]
            newObj["lesson-format"] = allInfo[allInfo.find("<lesson-format>")+15:allInfo.find("</lesson-format>")]
            days["days"]["thursday"]["tr"].append(newObj)
            allInfo = allInfo[allInfo.find("/tr")+3:]

    outInfo = str(days)
    outInfo = outInfo.replace('\'', '\"')
    with open('info.json', mode='w', encoding='utf-8') as f:   
        f.write(outInfo)

def task1():
    file = open('info.xml', mode='r', encoding='utf-8')
    info = file.read()
    file.close()
    inInfo = xmltodict.parse(info)
    outInfo = json.dumps(inInfo, ensure_ascii=False)


    with open('info.json', mode='w', encoding='utf-8') as f:   
        f.write(outInfo)

def task2():
    days = {"days": {"thursday": {"tr": []} }}
    with open('info.xml', mode='r', encoding='utf-8') as f:
        allInfo = f.read()
        while "tr" in allInfo:
            newObj = {
                    "time": {
                        "hours": "",
                        "weeks": ""
                    },
                    "room": {
                        "aud": "",
                        "address": ""
                    },
                    "lesson": {
                        "title": "",
                        "teacher": ""
                    },
                    "lesson-format": ""
                }
            newObj["time"]["hours"] = re.search(r'<hours>(.*)</hours>', allInfo).group(1)
            newObj["time"]["weeks"] = re.search(r'<weeks>(.*)</weeks>', allInfo).group(1)
            newObj["room"]["aud"] = re.search(r'<aud>(.*)</aud>', allInfo).group(1)
            newObj["room"]["address"] = re.search(r'<address>(.*)</address>', allInfo).group(1)
            newObj["lesson"]["title"] = re.search(r'<title>(.*)</title>', allInfo).group(1)
            newObj["lesson"]["teacher"] = re.search(r'<teacher>(.*)</teacher>', allInfo).group(1)
            newObj["lesson-format"] = re.search(r'<lesson-format>(.*)</lesson-format>', allInfo).group(1)
            days["days"]["thursday"]["tr"].append(newObj)
            allInfo = allInfo[allInfo.find("/tr")+3:]

    outInfo = str(days)
    outInfo = outInfo.replace('\'', '\"')
    with open('info.json', mode='w', encoding='utf-8') as f:   
        f.write(outInfo)

startTime = time.time()
for i in range(10):
    task0()
print('обязательное задание', time.time() - startTime)

startTime = time.time()
for i in range(10):
    task1()
print('доп задание 1', time.time() - startTime)

startTime = time.time()
for i in range(10):
    task2()
print('доп задание 2', time.time() - startTime)