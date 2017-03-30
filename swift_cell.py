#!/usr/bin/env python
# encoding: utf-8

# swift_cell.py
# QHSCodeTools

# Created by Charles.Qiu on 2017/2/28 下午3:44.
# Copyright © 2017年 Charles.Qiu. All rights reserved.
# HomePage: https://github.com/CharlesQiu
# Email: qhs@outlook.com

datas = [
    ('label', 'FeedbackTime'),
    ('label', 'Feedback'),
    ('label', 'ReplyTime'),
    ('label', 'Reply'),
    # ('label', ''),
    # ('label', ''),
]

for data in datas:
    if data[0] == 'label':
        print('private let lbl' + data[1] + ' = UILabel()')

print(' ')

for data in datas:
    if data[0] == 'label':
        print('lbl' + data[1] + '.text = newValue?.str' + data[1])
        print('lbl' + data[1] + '.textColor = newValue?.color' + data[1])
        print('lbl' + data[1] + '.font = newValue?.font' + data[1])
    print(' ')

for data in datas:
    if data[0] == 'label':
        print('contentView.addSubview(lbl' + data[1] + ')')

print(' ')

for data in datas:
    if data[0] == 'label':
        print('lbl' + data[1] + '.snp.makeConstraints { (make) in')
        print('\n}\n')

        # lblLandlord.snp.makeConstraints { (make) in
        #     make.leading.equalTo(contentView).offset(HGYSize.marginLeading_15)
        #     make.top.equalTo(contentView).offset(HGYSize.marginTop_15)
        # }


        # contentView.addSubview(lblLandlord)
        # contentView.addSubview(lblOrderSn)
        # contentView.addSubview(lblOrderTime)

# private let lblLandlord = UILabel()

# lblLandlord.text = newValue?.strLandlord
# lblLandlord.textColor = newValue?.colorLandlord
# lblLandlord.font = newValue?.fontLandlord
#
# lblOrderSn.text = newValue?.strNumber
# lblOrderSn.textColor = newValue?.colorNumber
# lblOrderSn.font = newValue?.fontNumber
#
# lblOrderTime.text = newValue?.strTime
# lblOrderTime.textColor = newValue?.colorTime
# lblOrderTime.font = newValue?.fontTime


