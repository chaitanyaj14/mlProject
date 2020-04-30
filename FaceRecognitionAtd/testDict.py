# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:22:34 2020

@author: Chaitanya
"""
import xl2dict

myxlobject = xl2dict.XlToDict()
dicto = myxlobject.convert_sheet_to_dict(file_path="userdata.xlsx")

finalDict = {}

for i in range(len(dicto)):
    finalDict.update({i: [dicto[i]['Name'], dicto[i]['SC Code'], dicto[i]['Branch']]})
