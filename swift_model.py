#!/usr/bin/env python
# encoding: utf-8

# swift_model.py
# QHSCodeTools

# Created by Charles.Qiu on 2017/2/16 下午4:05.
# Copyright © 2017年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

import re

data = open('swift_model_data.txt', 'r', encoding='utf-8')
arr = []

for line in data:
    arr.append(line)

print('\n' + '*' * 100 + '\n')
print(open('swift_model_data.txt', 'r', encoding='utf-8').read())
print('\n' + '*' * 100 + '\n')

# ---- swift 属性 -----
def formatToProperty(item):
    pattern1 = re.compile('(\w+_?\w+).*?', re.S)
    pattern2 = re.compile('//(\S+)', re.S)
    pattern3 = re.compile('".*?".*?"(.*?)"', re.S)
    str1 = re.findall(pattern1, item)
    str2 = re.findall(pattern2, item)
    str3 = re.findall(pattern3, item)
    if len(str2) > 0:
        comment1 = ""
        for text in str2:
            comment1 = comment1 + text
        comment2 = ""
        if len(str3) > 0:
            for text in str3:
                comment2 = comment2 + text
        str = '/// ' + comment1 + " 例如: " + comment2 + '\n' + 'private(set) var ' + str1[0] + ': String = ""'
    elif len(str3) > 0:
        comment = ""
        for text in str3:
            comment = comment + text
        str = '/// 例如: ' + comment + '\n' + 'private(set) var ' + str1[0] + ': String = ""'
    else:
        str = 'private(set) var ' + str1[0] + ': String = ""'
    return str

arr_property = map(formatToProperty, arr)

for x in arr_property:
    print(x)

print('\n' + '*' * 100 + '\n')

# ---- swift 属性 -----

# ---- swift mapper -----

def formatMapper(x):
    pattern1 = re.compile('(\w+_?\w+).*?', re.S)
    str1 = re.findall(pattern1, x)
    str = 'self.' + str1[0] + ' <- map["' + str1[0] + '"]'
    return str

newArr2 = map(formatMapper, arr)

for item in newArr2:
    print(item)

print('\n' + '*' * 100 + '\n')

# ---- swift mapper -----
