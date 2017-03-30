#!/usr/bin/env python
# encoding: utf-8

# swift_maidian.py
# QHSCodeTools

# Created by Charles.Qiu on 2017/2/16 下午4:29.
# Copyright © 2017年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

import re

file = open('swift_maidian_data.txt', 'r', encoding='utf-8')
arr = []
for line in file:
    arr.append(line)

print('\n' + '*' * 100 + '\n')
print(open('swift_maidian_data.txt', 'r', encoding='utf-8').read())
print('\n' + '*' * 100 + '\n')

def formatToStructContent(x):
    pattern1 = re.compile(r'(\w+).*?', re.S)
    pattern2 = re.compile(u'[\\u4e00-\\u9fa5]+\w+', re.S)
    str1 = re.findall(pattern1, x)
    str2 = re.findall(pattern2, x)

    if len(str2) > 0:
        str = '/// ' + str2[0] + '\nstatic let ' + str1[0] + ' = "' + str1[0] + '"'
    else:
        str = '@"' + str1[0] + '": @"' + str1[0] + '"'
    return str

newArr = map(formatToStructContent, arr)

for item in newArr:
    if item != None:
        print(item)

print('\n' + '*' * 100 + '\n')

def formatToEventCode(x):
    pattern1 = re.compile(r'(\w+).*?', re.S)
    pattern2 = re.compile(u'[\\u4e00-\\u9fa5]+\w+', re.S)
    str1 = re.findall(pattern1, x)
    str2 = re.findall(pattern2, x)

    if len(str2) > 0:
        str = '/// ' + str2[0] + '\n' + 'MobClick.event(HGYEvent.' + str1[0] + ')'
    else:
        str = '@"' + str1[0] + '": @"' + str1[0] + '"'
    return str

newArr = map(formatToEventCode, arr)

for item in newArr:
    if item != None:
        print(item)

print('\n' + '*' * 100 + '\n')
