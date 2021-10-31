# -*- coding: utf-8 -*-
import re

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