#!/usr/bin/env python
# encoding: utf-8

# jenkins_environment.py
# QHSCodeTools

# Created by Charles on 2017/3/15 上午10:51.
# Copyright © 2017年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

import re

file = open('jenkins_environment.txt', 'r', encoding='utf-8')
arr = []
for line in file:
    arr.append(line[:-1])

new_arr = arr[::2]

for value in new_arr:
    print(value.lower() + " = environsDict['" + value + "']")



