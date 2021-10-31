# -*- coding: utf-8 -*-

import json
import xmltodict

file = open('info.xml', mode='r', encoding='utf-8')
info = file.read()
file.close()
inInfo = xmltodict.parse(info)
outInfo = json.dumps(inInfo, ensure_ascii=False)


with open('info.json', mode='w', encoding='utf-8') as f:   
    f.write(outInfo)