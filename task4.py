# -*- coding: utf-8 -*-

import configparser

outInfo = {"tr": [] }
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
        outInfo["tr"].append(newObj)
        allInfo = allInfo[allInfo.find("/tr")+3:]

config = configparser.ConfigParser()
config.add_section('days')
config.set('days', 'thursday', str(outInfo))

with open('info.ini', 'w', encoding='utf-8') as configfile:
    config.write(configfile)
