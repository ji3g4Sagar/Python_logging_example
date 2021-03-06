#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging

"""使用logger客製化log的相關資訊"""


logger = logging.getLogger('sagar_log') #利用getLogger方法實體化一個logging物件
logger.setLevel(logging.DEBUG) #設定log的等級

"""
Log的層級, 由上而下遞增優先權

debug
info
warn
error
critical
"""
handler = logging.FileHandler('Script.log', 'a') #利用handler建立處理器,這邊使用fileHndler寫檔案
handler.setLevel(logging.DEBUG) #設定寫檔時,那些等級的log會被輸出

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s') #利用Formtter 設定輸出格式

handler.setFormatter(formatter) #將formtter這個實體物件塞給handler

logger.addHandler(handler) #最後在將handler塞給logger


logger.info('info message!!')
logger.error('error message!!')


"""
logging.debug('debug message!!')

logging.warning('warn message!!')
logging.error('error message!!')
logging.critical('critical message!!')

"""